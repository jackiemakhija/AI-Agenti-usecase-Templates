# Data Steward Council - Policy-by-Consensus System

## 🎯 Overview

An intelligent multi-agent system where AI agents collaborate to establish data governance policies through consensus. Built with Microsoft AutoGen and OpenAI, this demo showcases how autonomous agents can work together to identify PII, track data lineage, and create comprehensive data governance policies.

## 🏗️ Architecture

### Agent Roles

1. **Policy Author Agent** 📝
   - Proposes initial data governance policies
   - Analyzes datasets and suggests retention rules
   - Creates PII masking recommendations

2. **Classifier Agent** 🔍
   - Identifies and tags PII in datasets
   - Categorizes data sensitivity levels
   - Validates data classification standards

3. **Lineage Tracer Agent** 🔗
   - Tracks data lineage and dependencies
   - Maps data flow across systems
   - Identifies downstream impacts of policy changes

4. **Negotiator Agent** ⚖️
   - Reconciles conflicts between agents
   - Facilitates consensus building
   - Finalizes and publishes approved policies

### Technology Stack

**Backend:**
- Python 3.10+
- Microsoft AutoGen (pyautogen)
- OpenAI API (GPT-4)
- FastAPI for REST API
- SQLite for data storage (easy setup, no external dependencies)

**Frontend:**
- React 18 with Vite
- TypeScript
- Tailwind CSS for styling
- Framer Motion for animations
- Recharts for visualizations
- WebSocket for real-time updates

## 📋 Prerequisites

1. **Python 3.10 or higher**
   - Download: https://www.python.org/downloads/

2. **Node.js 18+ and npm**
   - Download: https://nodejs.org/

3. **OpenAI API Key**
   - Sign up: https://platform.openai.com/signup
   - Get API key: https://platform.openai.com/api-keys
   - Free tier: $5 credit for new accounts
   - Estimated cost for demo: < $1

## 🚀 Installation Guide

### Step 1: Clone and Setup Backend

```bash
# Navigate to project directory
cd c:\MyCode

# Create Python virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
# source venv/bin/activate

# Install Python dependencies
pip install -r backend/requirements.txt
```

### Step 2: Configure Environment Variables

Create a `.env` file in the `backend` directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
DATABASE_URL=sqlite:///./data_steward.db
```

### Step 3: Initialize Database and Synthetic Data

```bash
cd backend
python scripts/init_database.py
python scripts/generate_synthetic_data.py
```

### Step 4: Setup Frontend

```bash
cd frontend
npm install
```

## 🎮 Running the Demo

### Start Backend Server

```bash
cd backend
python main.py
```

Backend will run on: `http://localhost:8000`

### Start Frontend Dashboard

```bash
cd frontend
npm run dev
```

Frontend will run on: `http://localhost:5173`

## 🎨 Dashboard Features

### 1. Live Council Debate Tab
- Real-time agent discussion visualization
- Agent avatars with activity indicators
- Issue cards showing debate status
- Animated transitions: Contested → Under Review → Agreed

### 2. Policy Management Tab
- Side-by-side diff viewer
- Policy version comparison
- PII tag highlights
- Retention rule changes
- Masking policy updates

### 3. Datasets Tab
- Browse available datasets
- Trigger new policy debates
- View PII classifications
- Data lineage visualization

### 4. Analytics Tab
- Agent activity metrics
- Policy approval timeline
- Consensus progress charts
- Debate statistics

### 5. Settings Tab
- OpenAI API configuration
- Agent behavior tuning
- Notification preferences
- Help guide and documentation

## 📊 Demo Scenarios

### Scenario 1: Customer Data Governance
- Dataset: `customer_data.csv` (1000 records)
- Contains: Names, emails, SSNs, addresses, phone numbers
- Watch agents debate PII masking and retention policies

### Scenario 2: Employee Records
- Dataset: `employee_records.csv` (500 records)
- Contains: Employee IDs, salaries, performance reviews
- Observe lineage tracing and access control policies

### Scenario 3: Healthcare Data
- Dataset: `patient_data.csv` (750 records)
- Contains: Medical records, diagnoses, prescriptions
- See HIPAA compliance policy creation

## 🔄 Agent Workflow (SPAR Framework)

### Complete End-to-End Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         USER INITIATES DEBATE                            │
│                    (Selects Dataset → Clicks Start)                     │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    ROUND 1: SENSE PHASE (Analysis)                       │
├─────────────────────────────────────────────────────────────────────────┤
│  🔍 CLASSIFIER AGENT                                                     │
│  ├─ Scans dataset columns and sample data                               │
│  ├─ Applies regex patterns for PII detection                            │
│  ├─ Identifies: SSN, Email, Phone, Names, Addresses, etc.               │
│  └─ Outputs: PII Classifications with confidence scores                 │
│                                                                          │
│  🔗 LINEAGE TRACER AGENT                                                 │
│  ├─ Maps source and target systems                                      │
│  ├─ Traces data transformation logic                                    │
│  ├─ Builds dependency chains                                            │
│  └─ Outputs: Lineage records with impact scores                         │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    ROUND 2: PLAN PHASE (Proposal)                        │
├─────────────────────────────────────────────────────────────────────────┤
│  📝 POLICY AUTHOR AGENT                                                  │
│  ├─ Receives PII classifications from Classifier                        │
│  ├─ Considers lineage impact from Lineage Tracer                        │
│  ├─ Designs comprehensive governance policy:                            │
│  │  ├─ Retention period (based on data type)                            │
│  │  ├─ Masking rules (per PII sensitivity)                              │
│  │  ├─ Access controls (read/write/delete)                              │
│  │  └─ Compliance tags (GDPR, HIPAA, CCPA, etc.)                        │
│  └─ Outputs: Initial Policy Proposal                                    │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    ROUND 3: ACT PHASE (Validation)                       │
├─────────────────────────────────────────────────────────────────────────┤
│  🔍 CLASSIFIER VALIDATES POLICY                                          │
│  ├─ Checks if all critical PII has masking rules                        │
│  ├─ Verifies compliance tags match data types                           │
│  ├─ Raises objections if protection is insufficient                     │
│  └─ Outputs: Validation result + Issues + Suggestions                   │
│                                                                          │
│  🔗 LINEAGE TRACER ASSESSES IMPACT                                       │
│  ├─ Evaluates policy impact on downstream systems                       │
│  ├─ Identifies high-impact dependencies                                 │
│  ├─ Issues warnings for critical systems                                │
│  └─ Outputs: Impact assessment + Warnings + Suggestions                 │
│                                                                          │
│  ⚖️ NEGOTIATOR IDENTIFIES CONFLICTS                                      │
│  ├─ Collects all issues from agents                                     │
│  ├─ Categorizes by severity (Critical/High/Medium/Low)                  │
│  ├─ Creates issue cards for dashboard                                   │
│  └─ Outputs: Conflict list with priorities                              │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                  ROUND 4: REFLECT PHASE (Negotiation)                    │
├─────────────────────────────────────────────────────────────────────────┤
│  ⚖️ NEGOTIATOR PROPOSES RESOLUTIONS                                      │
│  ├─ For critical issues: Apply strictest protection                     │
│  ├─ For medium issues: Find balanced compromise                         │
│  ├─ For low issues: Suggest minor adjustments                           │
│  └─ Outputs: Resolution proposals for each conflict                     │
│                                                                          │
│  📝 POLICY AUTHOR REVISES POLICY                                         │
│  ├─ Applies approved resolutions                                        │
│  ├─ Updates masking rules, retention, compliance tags                   │
│  ├─ Incorporates feedback from all agents                               │
│  └─ Outputs: Revised Policy (Version 2)                                 │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    ROUND 5: CONSENSUS VOTE                               │
├─────────────────────────────────────────────────────────────────────────┤
│  Each agent casts a vote on the final policy:                           │
│                                                                          │
│  📝 Policy Author:     ✅ APPROVE                                        │
│  🔍 Classifier:        ✅ APPROVE                                        │
│  🔗 Lineage Tracer:    ✅ APPROVE                                        │
│                                                                          │
│  ⚖️ NEGOTIATOR CALCULATES CONSENSUS                                      │
│  ├─ Counts approvals: 3 out of 3 agents                                 │
│  ├─ Consensus Score: 100% (≥ 75% threshold required)                    │
│  ├─ Status: ✅ CONSENSUS REACHED                                         │
│  └─ Finalizes policy with metadata                                      │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      POLICY PUBLISHED & SAVED                            │
├─────────────────────────────────────────────────────────────────────────┤
│  ✅ Final Policy Status: APPROVED                                        │
│  📊 Saved to Database:                                                   │
│     ├─ Policy document with all rules                                   │
│     ├─ PII classifications                                              │
│     ├─ Lineage records                                                  │
│     ├─ Debate transcript (all messages)                                 │
│     ├─ Issues and resolutions                                           │
│     └─ Consensus metadata                                               │
│                                                                          │
│  📱 Dashboard Updated:                                                   │
│     ├─ Live debate stream shows completion                              │
│     ├─ Issue cards transition to "Agreed"                               │
│     ├─ Policy appears in Policy Management tab                          │
│     └─ Analytics updated with new metrics                               │
└─────────────────────────────────────────────────────────────────────────┘
```

### SPAR Framework Breakdown

#### Sense Phase
- **Classifier Agent**: Perceives dataset structure, identifies PII patterns
- **Lineage Tracer Agent**: Maps data relationships and dependencies
- **Policy Author Agent**: Analyzes dataset context and business requirements

#### Plan Phase
- **Policy Author Agent**: Designs governance rules and retention policies
- **Classifier Agent**: Plans PII protection strategies
- **Lineage Tracer Agent**: Strategizes impact mitigation
- **Negotiator Agent**: Creates consensus-building approach

#### Act Phase
- **All Agents**: Execute their specialized tasks
- **Policy Author**: Drafts and revises policies
- **Classifier**: Tags PII and validates protection
- **Lineage Tracer**: Documents dependencies
- **Negotiator**: Mediates conflicts and facilitates votes

#### Reflect Phase
- **All Agents**: Evaluate policy effectiveness
- **Negotiator**: Incorporates feedback and calculates consensus
- **System**: Publishes final approved policy

## 📁 Project Structure

```
data-steward-council/
├── backend/
│   ├── agents/
│   │   ├── policy_author.py
│   │   ├── classifier.py
│   │   ├── lineage_tracer.py
│   │   └── negotiator.py
│   ├── core/
│   │   ├── consensus_engine.py
│   │   └── debate_manager.py
│   ├── api/
│   │   └── routes.py
│   ├── database/
│   │   ├── models.py
│   │   └── schemas.py
│   ├── scripts/
│   │   ├── init_database.py
│   │   └── generate_synthetic_data.py
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.tsx
│   ├── package.json
│   └── vite.config.ts
├── docs/
│   ├── agent_flows.md
│   └── architecture.md
└── README.md
```

## 🔐 Security & Privacy

- All synthetic data is randomly generated
- No real PII is used in the demo
- OpenAI API calls are logged for transparency
- Local SQLite database for data isolation

## 🐛 Troubleshooting

### Backend won't start
- Verify Python version: `python --version`
- Check OpenAI API key in `.env`
- Ensure virtual environment is activated

### Frontend build errors
- Clear node_modules: `rm -rf node_modules && npm install`
- Check Node version: `node --version`

### Agents not responding
- Verify OpenAI API key is valid
- Check API quota: https://platform.openai.com/usage
- Review backend logs for errors

## 📚 Additional Resources

- [Microsoft AutoGen Documentation](https://microsoft.github.io/autogen/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [SPAR Framework Guide](https://github.com/microsoft/autogen/blob/main/notebook/agentchat_planning.ipynb)

## 🎯 Success Metrics

✅ All agents communicate and reach consensus
✅ Real-time debate visualization works smoothly
✅ Policy diffs are clearly displayed
✅ Multiple datasets can be processed
✅ No errors during normal operation
✅ Professional, engaging UI with dark theme

## 📚 Documentation

This project includes comprehensive documentation:

- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute setup guide for first-time users
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Complete project overview and features
- **[TESTING_CHECKLIST.md](TESTING_CHECKLIST.md)** - Comprehensive QA testing guide
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Production deployment guide (Docker, AWS, Azure, GCP)
- **[IMPLEMENTATION_COMPLETE.md](IMPLEMENTATION_COMPLETE.md)** - Implementation status and walkthrough
- **[docs/agent_flows.md](docs/agent_flows.md)** - Detailed Mermaid flow diagrams for all agents
- **[docs/architecture.md](docs/architecture.md)** - System architecture deep-dive

### Quick Links

- **Getting Started**: See [QUICKSTART.md](QUICKSTART.md)
- **Understanding the System**: See [docs/architecture.md](docs/architecture.md)
- **Testing**: See [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md)
- **Deployment**: See [DEPLOYMENT.md](DEPLOYMENT.md)

## 📝 License

MIT License - Free for educational and commercial use

## 🤝 Contributing

This is a demo application. Feel free to extend and customize for your needs!

---

**Built with ❤️ using Microsoft AutoGen and OpenAI**

