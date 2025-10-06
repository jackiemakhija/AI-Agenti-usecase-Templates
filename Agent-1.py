"""Build Agent using Microsoft Agent Framework in Python
# Run this python script
> pip install agent-framework
> python <this-script-path>.py
"""

import asyncio
import os

from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient
from openai import AsyncOpenAI

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
openaiClient = AsyncOpenAI(
    base_url = "https://models.github.ai/inference",
    api_key = os.environ["GITHUB_TOKEN"],
)

AGENT_NAME = "ai-agent"
AGENT_INSTRUCTIONS = "Act as an expert financial analyst to monitor and summarize daily stock performance.  \nFocus specifically on the stock specified by the user, providing clear insights for informed decision-making.\n\n# Guidelines\n- Check real-time price data and historical trends for NVDA\n- Compare performance against relevant market indices (e.g., NASDAQ, S&P 500)\n- Highlight significant price movements (+/- 2% daily change)\n- Identify notable news/events impacting the stock\n- Present technical indicators (RSI, moving averages)\n- Use layman-friendly explanations for financial metrics\n\n# Output Format\nReturn XML-formatted analysis with this structure:\n<daily_summary date=\"10/03/2025\">\n  <stock symbol=\"NVDA\">\n    <price_data>\n      <current>[Current price]</current>\n      <change_percent>[Daily % change]</change_percent>\n      <high_low>\n        <day_high>[Daily high]</day_high>\n        <day_low>[Daily low]</day_low>\n      </high_low>\n    </price_data>\n    <analysis>\n      <market_comparison>[Comparison to indices]</market_comparison>\n      <key_driver>[Main price movement factor]</key_driver>\n      <technical_analysis>[RSI/Moving average status]</technical_analysis>\n    </analysis>\n  </stock>\n</daily_summary>\n\n# Notes\n- Verify data from at least 2 reliable sources\n- Always include timestamps for price data\n- Flag any unusual trading volume patterns"

# User inputs for the conversation
USER_INPUTS = [
    "tell me the scope of NVDA trend",
]


async def main() -> None:
    async with (
        ChatAgent(
            chat_client=OpenAIChatClient(
                async_client=openaiClient,
                ai_model_id="deepseek/DeepSeek-R1"
            ),
            instructions=AGENT_INSTRUCTIONS,
            tools=None,
        ) as agent
    ):
        # Create a new thread that will be reused
        thread = agent.get_new_thread()

        # Process user messages
        for user_input in USER_INPUTS:
            print(f"\n# User: '{user_input}'")
            async for chunk in agent.run_stream([user_input], thread=thread):
                if chunk.text:
                    print(chunk.text, end="")
                elif (
                    # log tool calls if any
                    chunk.raw_representation
                    and chunk.raw_representation.raw_representation
                    and hasattr(chunk.raw_representation.raw_representation, "choices")
                    and chunk.raw_representation.raw_representation.choices is not None
                    and len(chunk.raw_representation.raw_representation.choices) > 0
                    and hasattr(chunk.raw_representation.raw_representation.choices[0], "delta")
                    and hasattr(chunk.raw_representation.raw_representation.choices[0].delta, "tool_calls")
                    and chunk.raw_representation.raw_representation.choices[0].delta.tool_calls is not None
                    and len(chunk.raw_representation.raw_representation.choices[0].delta.tool_calls) > 0
                ):
                    toolCalls = list(filter(lambda call: call.function.name != None, chunk.raw_representation.raw_representation.choices[0].delta.tool_calls))
                    if len(toolCalls) > 0:
                        print("")
                        print("Tool calls:", list(map(lambda call: call.function.name, toolCalls)))
            print("")
        
        print("\n--- All tasks completed successfully ---")

    # Give additional time for all async cleanup to complete
    await asyncio.sleep(1.0)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("Program finished.")
