# 🚀 Service Monitoring API

A production-ready backend system that monitors external and internal services, tracks uptime, and provides real-time observability using automated health checks and performance metrics.

---

## 📌 Overview

**Service Monitoring API** is a backend-focused project designed to simulate a real-world observability system:

* Monitors external and internal APIs automatically
* Collects and stores performance metrics over time
* Detects service failures using resilient logic
* Provides aggregated system health insights
* Runs in a containerized environment using Docker

This project demonstrates **real-world backend engineering**, including background processing, system monitoring, fault detection, and data aggregation.

---

## 🧠 Key Features

### 🔹 Service Monitoring

* Register services (external APIs or internal projects)
* Configurable health check intervals
* Supports multiple services simultaneously

---

### 🔹 Automated Health Checks

* Background scheduler using APScheduler
* Periodic service checks (status + response time)
* Timeout and error handling

---

### 🔹 Metrics Collection

* Stores response time and status for each check
* Tracks historical performance data
* Enables time-based analysis (last 24h uptime)

---

### 🔹 Intelligent Status Detection

* Avoids false positives using failure thresholds
* Marks services as DOWN only after consecutive failures
* Reflects real-world fault tolerance strategies

---

### 🔹 Observability Endpoints

* Aggregated system status (`/status`)
* Historical metrics per service (`/metrics/{service_id}`)
* Real-time system health insights

---

### 🔹 Production Setup

* Fully Dockerized environment
* Environment-based configuration
* Modular and scalable architecture

---

## 🏗️ Architecture

```
app/
├── api/ # FastAPI routes (services, metrics, status)
├── core/ # Database & config
├── db/ # Database setup, SQLAlchemy models
├── schemas/ # Pydantic schemas
├── services/ # Business logic (monitoring, status)
├── workers/ # Background scheduler (APScheduler)
└── main.py # Application entry point
```

---

## ⚙️ Tech Stack

* **FastAPI** – high-performance web framework  
* **PostgreSQL** – relational database  
* **SQLAlchemy** – ORM  
* **APScheduler** – background job scheduling  
* **Docker** – containerization  

---

## 🔌 API Endpoints

### Services

```
POST /services
GET /services
```

* Register and manage monitored services

---

### Metrics

```
GET /metrics/{service_id}
```

* Retrieve historical monitoring data for a service

---

### Status

```
GET /status
```

* Get aggregated system health:
  * Current status (UP/DOWN)
  * Average response time
  * Uptime percentage (last 24h)

---

## 🐳 Running Locally

### 1. Clone the repository

```
git clone https://github.com/flobell/service-monitoring-api.git
cd service-monitoring-api
```

### 2. Configure environment variables

```
cp .env.example .env
```

### 3. Run with Docker

```
docker-compose up --build
```

---

### 3. Run manually

```
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

---

## 🌐 Deployment

The API is deployed on Render: Not Available
<!-- 
```
https://your-api-url.onrender.com
``` -->

## 🎯 What This Project Demonstrates

This project highlights:

* Background job processing in backend systems
* Real-time service monitoring and observability
* Fault-tolerant system design (failure thresholds)
* Time-series data collection and aggregation
* RESTful API design with FastAPI
* Docker-based development environment

---

## 🚀 Future Improvements

* Per-service scheduling intervals  
* Alerting system (Slack / Email / Webhooks)  
* Advanced query optimization (aggregations & indexing)  
* Caching layer (Redis)  
* Authentication & multi-tenant support  
* Dashboard (UI for visualization)  

---

## 👨‍💻 Author

**Pedro Flores**  
Backend Developer (Python | FastAPI | PostgreSQL)

---

## ⭐ Why This Matters

This is not just another CRUD API.

It is a **production-style observability system** that reflects how real platforms:

* monitor services continuously  
* detect failures intelligently  
* analyze performance over time  
* provide actionable system insights  

---

👉 This project is part of my backend engineering portfolio focused on building production-ready systems.