# 🏗️ SitePulse — Intelligent Data Capture & 3D Digital Twin Platform

SitePulse connects real-world infrastructure project progress with planned construction schedules. It features an interactive 3D digital twin, photo-based site assessment, schedule intelligence (Gantt tracking), AI delay detection, and automated manager email dispatching.

---

## 🌟 Key Features

- **🌐 3D Digital Twin (Three.js):** Walk the site virtually. Interactive 3D building models reflect live zone progress, schedule deviation, and risk status.
- **📸 Photo-Based Site Assessment:** Upload blueprint drawings and site photographs to run automated visual comparison analysis against baseline schedule activities.
- **⚡ Reactive Live Mode:** Submitting a site assessment dynamically updates every section across the platform in real time (Command Center KPIs, 3D Digital Twin heights & colors, Gantt chart, AI Delay detection, and Alerts).
- **📊 Schedule Intelligence (Gantt Chart):** Compare planned vs. actual progress stage by stage (`ACT-001` through `ACT-022`).
- **🤖 AI Delay Detection & Recommendations:** Identifies bottlenecks early, estimates schedule impact (+X days), and ranks corrective action items.
- **📧 Manager Email Dispatch System:** Dispatches action plans directly to the Project Manager's email address with optional SMTP credentials.
- **🗄️ PostgreSQL Database Schema:** Includes full relational schema (`SIH26122_schema_postgres.sql`) and sample data (`SIH26122_postgres_full.sql`).

---

## 🚀 Quick Start (Local Setup)

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/sitepulse-platform.git
cd sitepulse-platform
```

### 2. Start the Server
```bash
npm start
# OR
node server.cjs
```

### 3. Open in Browser
Navigate to **[http://localhost:8080](http://localhost:8080)** in your browser.

---

## 📂 Project Structure

```
site-overview/
├── index.html                    # Single-Page Application (SPA) frontend
├── server.cjs                    # Node.js backend server (Static file serving + API endpoints)
├── server.py                     # Alternative Python HTTP/SMTP backend server
├── package.json                  # Node.js project configuration
├── README.md                     # Project documentation
├── SIH26122_schema_postgres.sql  # PostgreSQL database schema
├── SIH26122_postgres_full.sql    # Full PostgreSQL database seed data
├── sample_blueprint.jpg          # Sample architectural blueprint image for testing
└── sample_site_photo.jpg         # Sample active construction site photo for testing
```

---

## 🛠️ API Endpoints

- `POST /api/send-email`: Dispatches recommendation action plan to project manager email address.
- `POST /api/assessments`: Saves site photo assessment report to database.

---

## 📄 License
MIT License
