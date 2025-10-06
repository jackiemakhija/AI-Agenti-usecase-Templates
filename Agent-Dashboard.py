import asyncio
import os
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient
from openai import AsyncOpenAI

openaiClient = AsyncOpenAI(
    base_url = "https://models.github.ai/inference",
    api_key = os.environ["GITHUB_TOKEN"],
)

DASHBOARD_AGENT_INSTRUCTIONS = """
Act as a dashboard assistant. Summarize key metrics for multiple stocks (e.g., NVDA, AAPL, MSFT).
Return JSON with current price, % change, and notable news for each.
"""

USER_INPUTS = [
    "Show dashboard summary for NVDA, AAPL, MSFT"
]

async def main():
    async with ChatAgent(
        chat_client=OpenAIChatClient(
            async_client=openaiClient,
            ai_model_id="deepseek/DeepSeek-R1"
        ),
        instructions=DASHBOARD_AGENT_INSTRUCTIONS,
        tools=None,
    ) as agent:
        thread = agent.get_new_thread()
        for user_input in USER_INPUTS:
            print(f"\n# User: '{user_input}'")
            async for chunk in agent.run_stream([user_input], thread=thread):
                if chunk.text:
                    print(chunk.text, end="")
            print("")

if __name__ == "__main__":
    asyncio.run(main())
