# Testing Checklist for Data Steward Council

This document provides a comprehensive testing checklist to verify all features work correctly.

## Pre-Testing Setup

### Environment Verification
- [ ] Python 3.10+ installed: `python --version`
- [ ] Node.js 18+ installed: `node --version`
- [ ] OpenAI API key configured in `backend/.env`
- [ ] Virtual environment created and activated
- [ ] All Python dependencies installed: `pip list`
- [ ] All Node dependencies installed: `npm list` (in frontend/)

### Database & Data
- [ ] Database initialized: `backend/data_steward.db` exists
- [ ] Synthetic data generated: 4 CSV files in `backend/data/`
  - [ ] customer_data.csv (1000 records)
  - [ ] employee_records.csv (500 records)
  - [ ] patient_data.csv (750 records)
  - [ ] transaction_history.csv (2000 records)

### Services Running
- [ ] Backend server running on http://localhost:8000
- [ ] Frontend dashboard running on http://localhost:5173
- [ ] No errors in backend terminal
- [ ] No errors in frontend terminal

## Backend API Testing

### Health Checks
- [ ] GET http://localhost:8000/ returns welcome message
- [ ] GET http://localhost:8000/health returns `{"status": "healthy"}`
- [ ] GET http://localhost:8000/docs shows Swagger UI

### Dataset Endpoints
- [ ] GET /api/datasets returns 4 datasets
- [ ] GET /api/datasets/1 returns customer_data details
- [ ] GET /api/datasets/1/sample returns sample data with columns

### Policy Endpoints
- [ ] GET /api/policies returns empty list initially
- [ ] After debate: GET /api/policies returns created policy
- [ ] GET /api/policies/{id} returns specific policy

### PII & Lineage Endpoints
- [ ] After debate: GET /api/pii-classifications/1 returns PII data
- [ ] After debate: GET /api/lineage/1 returns lineage records

### Dashboard Stats
- [ ] GET /api/dashboard/stats returns statistics
- [ ] total_datasets = 4
- [ ] total_policies increases after debates

### WebSocket
- [ ] WebSocket connection to ws://localhost:8000/ws succeeds
- [ ] Messages stream during debate
- [ ] Connection stays alive with heartbeat

## Frontend UI Testing

### Navigation & Layout
- [ ] Dashboard loads without errors
- [ ] Header displays "Data Steward Council"
- [ ] All 5 tabs are visible and clickable
- [ ] Footer shows version and status indicator
- [ ] Dark theme applied correctly

### Live Council Debate Tab

#### Initial State
- [ ] Tab loads with empty state
- [ ] Dataset dropdown shows 4 datasets
- [ ] "Start Debate" button is disabled when no dataset selected
- [ ] 4 agent avatars displayed (not active)
- [ ] Debate stream shows placeholder message
- [ ] Issues panel shows "No issues detected"

#### During Debate
- [ ] Select "customer_data" from dropdown
- [ ] Click "Start Debate" button
- [ ] Button changes to "Debating..." and is disabled
- [ ] Agent avatars light up as they become active
- [ ] Green pulse indicator appears on active agents
- [ ] Messages stream in real-time
- [ ] Round counter updates (1/5, 2/5, etc.)
- [ ] Issue cards appear in issues panel
- [ ] Issue status transitions: Contested → Under Review → Agreed
- [ ] Auto-scroll works in message stream

#### After Debate
- [ ] Final consensus message appears
- [ ] All issues show "Agreed" status
- [ ] Issue summary shows correct counts
- [ ] "Start Debate" button re-enabled
- [ ] Can start new debate with different dataset

### Policy Management Tab

#### Policy List
- [ ] Policies appear after debates
- [ ] Each policy shows dataset name
- [ ] Status badge displays correctly (Approved/Under Review/Draft)
- [ ] Creation date formatted properly
- [ ] Consensus score bar displays
- [ ] Clicking policy selects it

#### Policy Details
- [ ] Selected policy shows full details
- [ ] Title and description displayed
- [ ] Retention period shown in days
- [ ] Compliance tags displayed as badges
- [ ] Masking rules table populated
- [ ] Access controls grid shows read/write/delete roles
- [ ] "Approved By" section shows agent names

### Datasets Tab

#### Dataset Grid
- [ ] All 4 datasets displayed as cards
- [ ] Each card shows name and row count
- [ ] Clicking dataset selects it
- [ ] Selected dataset highlighted

#### PII Classifications
- [ ] PII fields listed for selected dataset
- [ ] Each field shows column name, type, sensitivity
- [ ] Sensitivity badges color-coded (Critical/High/Medium/Low)
- [ ] Confidence percentage displayed

#### Data Lineage
- [ ] Lineage paths displayed
- [ ] Source → Target systems shown
- [ ] Transformation logic visible
- [ ] Impact score displayed

### Analytics Tab

#### Stats Cards
- [ ] Total Datasets card shows 4
- [ ] Total Policies card updates after debates
- [ ] Agent Activities card shows activity count
- [ ] PII Fields Protected card shows total

#### Charts
- [ ] Consensus Score Trend chart renders
- [ ] Policy Status Distribution pie chart renders
- [ ] Charts are interactive (hover tooltips work)

#### Agent Performance
- [ ] 4 agent performance cards displayed
- [ ] Each shows task count and success rate
- [ ] Data updates after debates

### Settings Tab

#### Configuration
- [ ] OpenAI API key input field present
- [ ] Model dropdown shows options
- [ ] Max Debate Rounds input works
- [ ] Consensus Threshold input works
- [ ] Save button present

#### Help Guide
- [ ] Getting Started steps listed
- [ ] Agent Roles explained
- [ ] SPAR Framework described
- [ ] Resource links clickable
- [ ] Tips section visible

## Agent Behavior Testing

### Policy Author Agent
- [ ] Proposes policy in Round 2
- [ ] Policy includes retention_days
- [ ] Policy includes masking_rules
- [ ] Policy includes access_controls
- [ ] Policy includes compliance_tags
- [ ] Revises policy based on feedback in Round 4
- [ ] Votes in Round 5

### Classifier Agent
- [ ] Identifies PII in Round 1
- [ ] Detects email addresses
- [ ] Detects phone numbers
- [ ] Detects SSN
- [ ] Detects names
- [ ] Detects addresses
- [ ] Assigns correct sensitivity levels
- [ ] Validates policy in Round 3
- [ ] Raises objections if PII unprotected
- [ ] Votes in Round 5

### Lineage Tracer Agent
- [ ] Maps lineage in Round 1
- [ ] Identifies source systems
- [ ] Identifies target systems
- [ ] Calculates impact scores
- [ ] Assesses policy impact in Round 3
- [ ] Issues warnings for high-impact changes
- [ ] Votes in Round 5

### Negotiator Agent
- [ ] Monitors discussion throughout
- [ ] Identifies conflicts in Round 3
- [ ] Categorizes issues by severity
- [ ] Proposes resolutions in Round 4
- [ ] Calculates consensus in Round 5
- [ ] Finalizes policy
- [ ] Generates debate summary

## Consensus Mechanism Testing

### Conflict Resolution
- [ ] Critical issues get strictest protection
- [ ] Medium issues get balanced compromise
- [ ] Low issues get minor adjustments
- [ ] All conflicts resolved before final vote

### Voting Process
- [ ] All agents cast votes
- [ ] Votes counted correctly
- [ ] Consensus score calculated (votes/total)
- [ ] 75% threshold enforced
- [ ] Policy approved if ≥75%
- [ ] Policy under_review if <75%

### Policy Finalization
- [ ] Resolutions applied to policy
- [ ] Consensus metadata added
- [ ] Status set correctly
- [ ] Approved_by_agents list populated
- [ ] Policy saved to database

## Data Persistence Testing

### Database Writes
- [ ] Datasets saved correctly
- [ ] Policies saved with all fields
- [ ] PII classifications saved
- [ ] Lineage records saved
- [ ] Debate sessions saved
- [ ] Debate messages saved
- [ ] Issues saved with status
- [ ] Agent activities logged

### Data Retrieval
- [ ] Datasets load on page refresh
- [ ] Policies persist across sessions
- [ ] PII data retrievable
- [ ] Lineage data retrievable
- [ ] Debate history accessible

## Error Handling Testing

### Invalid Inputs
- [ ] Starting debate without dataset shows error
- [ ] Invalid API requests return proper errors
- [ ] Missing .env shows clear error message

### Network Issues
- [ ] Backend offline shows connection error
- [ ] WebSocket disconnect handled gracefully
- [ ] API timeout handled properly

### Edge Cases
- [ ] Empty dataset handled
- [ ] No PII detected handled
- [ ] No lineage found handled
- [ ] Consensus failure handled

## Performance Testing

### Response Times
- [ ] Dataset list loads < 1 second
- [ ] Policy list loads < 1 second
- [ ] Debate completes in 30-60 seconds
- [ ] UI remains responsive during debate

### Resource Usage
- [ ] Backend memory usage reasonable
- [ ] Frontend memory usage reasonable
- [ ] No memory leaks after multiple debates
- [ ] Database file size reasonable

## Cross-Browser Testing

### Chrome
- [ ] All features work
- [ ] UI renders correctly
- [ ] WebSocket connects

### Firefox
- [ ] All features work
- [ ] UI renders correctly
- [ ] WebSocket connects

### Edge
- [ ] All features work
- [ ] UI renders correctly
- [ ] WebSocket connects

## Accessibility Testing

### Keyboard Navigation
- [ ] Tab key navigates through elements
- [ ] Enter key activates buttons
- [ ] Escape key closes modals (if any)

### Screen Reader
- [ ] Semantic HTML used
- [ ] ARIA labels present where needed
- [ ] Alt text on images

### Visual
- [ ] Sufficient color contrast
- [ ] Text readable at different sizes
- [ ] Focus indicators visible

## Documentation Testing

### README.md
- [ ] All setup steps work
- [ ] Prerequisites listed correctly
- [ ] Installation commands accurate
- [ ] Troubleshooting section helpful

### QUICKSTART.md
- [ ] 5-minute setup achievable
- [ ] Commands copy-paste correctly
- [ ] Screenshots/diagrams clear

### Code Documentation
- [ ] Python docstrings present
- [ ] TypeScript types defined
- [ ] Comments explain complex logic

## Final Verification

### Complete User Journey
1. [ ] Fresh install from scratch
2. [ ] Follow QUICKSTART.md exactly
3. [ ] Run first debate successfully
4. [ ] Explore all tabs
5. [ ] Run second debate with different dataset
6. [ ] Verify data persists
7. [ ] Check analytics updated
8. [ ] Review policy details
9. [ ] No errors encountered

### Production Readiness
- [ ] No console errors in browser
- [ ] No warnings in terminal
- [ ] All dependencies up to date
- [ ] Security best practices followed
- [ ] Code is well-organized
- [ ] Documentation is comprehensive

## Test Results Summary

**Date Tested**: _______________  
**Tester**: _______________  
**Environment**: _______________

**Total Tests**: _____ / _____  
**Passed**: _____  
**Failed**: _____  
**Blocked**: _____

**Critical Issues Found**: _____  
**Minor Issues Found**: _____

**Overall Status**: ⬜ PASS  ⬜ FAIL  ⬜ NEEDS WORK

**Notes**:
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

