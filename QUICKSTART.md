# Quick Start Guide

Get the Data Steward Council demo running in 5 minutes!

## Prerequisites Check

Before starting, ensure you have:

- ✅ Python 3.10+ installed: `python --version`
- ✅ Node.js 18+ installed: `node --version`
- ✅ OpenAI API key from https://platform.openai.com/api-keys

## Step-by-Step Setup

### 1. Backend Setup (2 minutes)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env  # Windows
# cp .env.example .env  # Mac/Linux

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-your-key-here
```

### 2. Initialize Database & Generate Data (1 minute)

```bash
# Still in backend directory
python scripts/init_database.py
python scripts/generate_synthetic_data.py
```

You should see:
```
✅ Generated customer_data: 1000 records, 15 columns
✅ Generated employee_records: 500 records, 15 columns
✅ Generated patient_data: 750 records, 18 columns
✅ Generated transaction_history: 2000 records, 12 columns
```

### 3. Start Backend Server (30 seconds)

```bash
# Still in backend directory
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
✅ Database initialized
```

Keep this terminal open!

### 4. Frontend Setup (1 minute)

Open a NEW terminal:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

### 5. Start Frontend Dashboard (30 seconds)

```bash
# Still in frontend directory
npm run dev
```

You should see:
```
  VITE v5.0.11  ready in 500 ms

  ➜  Local:   http://localhost:5173/
```

## 🎉 You're Ready!

Open your browser to: **http://localhost:5173**

## First Demo Run

1. **Go to "Live Council Debate" tab** (should be open by default)
2. **Select a dataset** from the dropdown (try "customer_data")
3. **Click "Start Debate"** button
4. **Watch the magic happen!** 🎭

You'll see:
- ✨ Agents lighting up as they become active
- 💬 Real-time debate messages streaming
- 🎯 Issues transitioning from "Contested" → "Under Review" → "Agreed"
- ✅ Final consensus and approved policy

## Explore Other Tabs

- **Policy Management**: View approved policies with side-by-side comparisons
- **Datasets**: Browse datasets, PII classifications, and lineage
- **Analytics**: See agent performance metrics and charts
- **Settings**: Configure API settings and read help guide

## Troubleshooting

### Backend won't start
```bash
# Check Python version
python --version  # Should be 3.10+

# Verify OpenAI API key in .env
cat backend/.env  # Mac/Linux
type backend\.env  # Windows

# Reinstall dependencies
pip install -r backend/requirements.txt --force-reinstall
```

### Frontend won't start
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json  # Mac/Linux
# rmdir /s node_modules & del package-lock.json  # Windows
npm install
```

### Agents not responding
- ✅ Check OpenAI API key is valid
- ✅ Verify you have API credits: https://platform.openai.com/usage
- ✅ Check backend terminal for error messages
- ✅ Try using `gpt-4o-mini` model (cheaper and faster)

### WebSocket connection issues
- ✅ Ensure backend is running on port 8000
- ✅ Check browser console for errors (F12)
- ✅ Try refreshing the page

## Cost Estimate

Using `gpt-4o-mini` (recommended):
- **Per debate**: ~$0.05 - $0.10
- **10 demos**: ~$0.50 - $1.00
- **Free tier**: $5 credit for new OpenAI accounts

## Next Steps

1. ✅ Run debates on different datasets
2. ✅ Compare policies in Policy Management tab
3. ✅ Check Analytics for performance metrics
4. ✅ Read the full README.md for detailed documentation
5. ✅ Explore agent_flows.md for technical diagrams

## Support

If you encounter issues:
1. Check the logs in both terminal windows
2. Review the README.md troubleshooting section
3. Ensure all prerequisites are met
4. Verify .env configuration

---

**Enjoy exploring the Data Steward Council! 🚀**

