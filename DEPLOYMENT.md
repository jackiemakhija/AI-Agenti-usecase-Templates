# Deployment Guide

This guide explains how to deploy the Data Steward Council to production environments.

## ⚠️ Important Note

This application is currently a **demonstration/proof-of-concept**. Before deploying to production, consider the following enhancements:

## Production Readiness Checklist

### Security
- [ ] Replace SQLite with PostgreSQL or similar
- [ ] Implement proper authentication (OAuth2, JWT)
- [ ] Add rate limiting to API endpoints
- [ ] Enable HTTPS/TLS encryption
- [ ] Implement API key rotation
- [ ] Add input sanitization and validation
- [ ] Set up security headers (CORS, CSP, etc.)
- [ ] Implement audit logging
- [ ] Add secrets management (AWS Secrets Manager, Azure Key Vault)

### Scalability
- [ ] Replace synchronous consensus engine with async
- [ ] Implement task queue (Celery, RabbitMQ)
- [ ] Add caching layer (Redis)
- [ ] Set up load balancing
- [ ] Implement horizontal scaling
- [ ] Add database connection pooling
- [ ] Optimize database queries
- [ ] Implement CDN for frontend assets

### Reliability
- [ ] Add comprehensive error handling
- [ ] Implement retry logic for API calls
- [ ] Set up health checks and monitoring
- [ ] Add logging and observability (ELK, Datadog)
- [ ] Implement circuit breakers
- [ ] Add backup and disaster recovery
- [ ] Set up alerting (PagerDuty, Opsgenie)

### Performance
- [ ] Optimize database indexes
- [ ] Implement query caching
- [ ] Add response compression
- [ ] Optimize frontend bundle size
- [ ] Implement lazy loading
- [ ] Add service worker for offline support

## Deployment Options

### Option 1: Docker Deployment (Recommended)

#### Create Dockerfile for Backend

```dockerfile
# backend/Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Create Dockerfile for Frontend

```dockerfile
# frontend/Dockerfile
FROM node:18-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

#### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - DATABASE_URL=postgresql://user:pass@db:5432/steward
    depends_on:
      - db
    volumes:
      - ./backend/data:/app/data

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=steward
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

#### Deploy with Docker Compose

```bash
# Set environment variables
export OPENAI_API_KEY=your-key-here

# Build and start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Option 2: AWS Deployment

#### Architecture
```
Internet → CloudFront (CDN)
              ↓
         S3 (Frontend Static Files)
              ↓
         ALB (Load Balancer)
              ↓
         ECS/Fargate (Backend Containers)
              ↓
         RDS PostgreSQL (Database)
              ↓
         ElastiCache Redis (Caching)
```

#### Steps

1. **Frontend (S3 + CloudFront)**
```bash
# Build frontend
cd frontend
npm run build

# Upload to S3
aws s3 sync dist/ s3://your-bucket-name/

# Create CloudFront distribution
aws cloudfront create-distribution \
  --origin-domain-name your-bucket-name.s3.amazonaws.com
```

2. **Backend (ECS Fargate)**
```bash
# Build and push Docker image
docker build -t steward-backend ./backend
docker tag steward-backend:latest your-ecr-repo/steward-backend:latest
docker push your-ecr-repo/steward-backend:latest

# Create ECS task definition and service
aws ecs create-service \
  --cluster your-cluster \
  --service-name steward-backend \
  --task-definition steward-backend:1 \
  --desired-count 2
```

3. **Database (RDS)**
```bash
# Create PostgreSQL instance
aws rds create-db-instance \
  --db-instance-identifier steward-db \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --master-username admin \
  --master-user-password your-password
```

### Option 3: Azure Deployment

#### Architecture
```
Internet → Azure Front Door
              ↓
         Azure Static Web Apps (Frontend)
              ↓
         Azure App Service (Backend)
              ↓
         Azure Database for PostgreSQL
              ↓
         Azure Cache for Redis
```

#### Steps

1. **Frontend (Static Web Apps)**
```bash
# Install Azure CLI
az login

# Create static web app
az staticwebapp create \
  --name steward-frontend \
  --resource-group your-rg \
  --source https://github.com/your-repo \
  --location "East US" \
  --branch main \
  --app-location "/frontend" \
  --output-location "dist"
```

2. **Backend (App Service)**
```bash
# Create App Service plan
az appservice plan create \
  --name steward-plan \
  --resource-group your-rg \
  --sku B1 \
  --is-linux

# Create web app
az webapp create \
  --name steward-backend \
  --resource-group your-rg \
  --plan steward-plan \
  --runtime "PYTHON:3.10"

# Deploy code
az webapp up \
  --name steward-backend \
  --resource-group your-rg
```

3. **Database (Azure Database for PostgreSQL)**
```bash
# Create PostgreSQL server
az postgres server create \
  --name steward-db \
  --resource-group your-rg \
  --location eastus \
  --admin-user admin \
  --admin-password your-password \
  --sku-name B_Gen5_1
```

### Option 4: Google Cloud Platform

#### Architecture
```
Internet → Cloud CDN
              ↓
         Cloud Storage (Frontend)
              ↓
         Cloud Run (Backend)
              ↓
         Cloud SQL PostgreSQL
              ↓
         Memorystore Redis
```

#### Steps

1. **Frontend (Cloud Storage + CDN)**
```bash
# Build frontend
cd frontend
npm run build

# Create bucket and upload
gsutil mb gs://your-bucket-name
gsutil -m cp -r dist/* gs://your-bucket-name/

# Make bucket public
gsutil iam ch allUsers:objectViewer gs://your-bucket-name
```

2. **Backend (Cloud Run)**
```bash
# Build and push container
gcloud builds submit --tag gcr.io/your-project/steward-backend

# Deploy to Cloud Run
gcloud run deploy steward-backend \
  --image gcr.io/your-project/steward-backend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

3. **Database (Cloud SQL)**
```bash
# Create PostgreSQL instance
gcloud sql instances create steward-db \
  --database-version=POSTGRES_14 \
  --tier=db-f1-micro \
  --region=us-central1
```

## Environment Variables

### Production Environment Variables

```bash
# Backend (.env.production)
OPENAI_API_KEY=your-production-key
OPENAI_MODEL=gpt-4o-mini
DATABASE_URL=postgresql://user:pass@host:5432/db
REDIS_URL=redis://host:6379/0
SECRET_KEY=your-secret-key
ALLOWED_ORIGINS=https://yourdomain.com
DEBUG=False
LOG_LEVEL=INFO
```

### Frontend Environment Variables

```bash
# Frontend (.env.production)
VITE_API_URL=https://api.yourdomain.com
VITE_WS_URL=wss://api.yourdomain.com/ws
```

## Database Migration

### Migrate from SQLite to PostgreSQL

```python
# migration_script.py
import sqlite3
import psycopg2
from psycopg2.extras import execute_values

# Connect to SQLite
sqlite_conn = sqlite3.connect('data_steward.db')
sqlite_cursor = sqlite_conn.cursor()

# Connect to PostgreSQL
pg_conn = psycopg2.connect(
    host='your-host',
    database='steward',
    user='user',
    password='pass'
)
pg_cursor = pg_conn.cursor()

# Migrate each table
tables = ['datasets', 'policies', 'pii_classifications', ...]

for table in tables:
    # Read from SQLite
    sqlite_cursor.execute(f"SELECT * FROM {table}")
    rows = sqlite_cursor.fetchall()
    
    # Write to PostgreSQL
    if rows:
        columns = [desc[0] for desc in sqlite_cursor.description]
        query = f"INSERT INTO {table} ({','.join(columns)}) VALUES %s"
        execute_values(pg_cursor, query, rows)

pg_conn.commit()
```

## Monitoring & Logging

### Application Monitoring

```python
# Add to main.py
from prometheus_client import Counter, Histogram
import logging

# Metrics
debate_counter = Counter('debates_total', 'Total debates started')
debate_duration = Histogram('debate_duration_seconds', 'Debate duration')

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### Health Checks

```python
# Add to routes.py
@router.get("/health/live")
def liveness():
    return {"status": "alive"}

@router.get("/health/ready")
def readiness(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"status": "ready"}
    except:
        raise HTTPException(status_code=503, detail="Not ready")
```

## Backup Strategy

### Database Backups

```bash
# Automated daily backups
0 2 * * * pg_dump -h host -U user steward > backup_$(date +\%Y\%m\%d).sql

# Backup to S3
aws s3 cp backup_$(date +\%Y\%m\%d).sql s3://your-backup-bucket/
```

### Application State Backups

```bash
# Backup uploaded files
aws s3 sync /app/data s3://your-backup-bucket/data/

# Backup configuration
aws s3 cp .env s3://your-backup-bucket/config/
```

## Cost Optimization

### OpenAI API Costs
- Use `gpt-4o-mini` instead of `gpt-4` (10x cheaper)
- Implement caching for repeated queries
- Set max_tokens limits
- Monitor usage with OpenAI dashboard

### Infrastructure Costs
- Use auto-scaling to match demand
- Implement spot instances where possible
- Use reserved instances for predictable workloads
- Optimize database instance sizes
- Implement CDN caching

## Support & Maintenance

### Regular Tasks
- [ ] Monitor error logs daily
- [ ] Review API usage weekly
- [ ] Update dependencies monthly
- [ ] Review security patches
- [ ] Backup verification
- [ ] Performance optimization
- [ ] Cost analysis

### Incident Response
1. Monitor alerts
2. Investigate issues
3. Apply fixes
4. Document incidents
5. Post-mortem analysis
6. Implement preventive measures

---

**Note**: This is a starting point. Customize based on your specific requirements, scale, and compliance needs.

