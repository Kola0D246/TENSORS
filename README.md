# 🧠 Smart Classroom and Timetable Scheduler

---

## 📌 Overview

This project aims to automate and optimize the timetable scheduling process in higher education institutions using AI and constraint satisfaction algorithms. It minimizes clashes, balances faculty workload, and maximizes classroom utilization — aligning with NEP 2020’s multidisciplinary framework.

---

## 🎯 Problem Statement

- Limited classrooms and overlapping schedules  
- Faculty constraints and uneven workload  
- Complex elective and multidisciplinary structures  
- Static timetables that ignore real-time changes  
- Manual, error-prone scheduling using spreadsheets  

---

## 💡 Proposed Solution

A **web-based platform** that:

- Collects institutional data (faculty, classrooms, subjects, student groups)  
- Generates optimized, conflict-free timetables using AI  
- Dynamically adjusts schedules based on real-time changes (faculty leave, room unavailability)  
- Provides role-based dashboards and approval workflows  

---

## 🧭 Key Features

- 🔐 Role-based Authentication (Admin, HOD, Faculty, Student)  
- 🧩 Dynamic AI-based Scheduling (Google OR-Tools / OptaPlanner)  
- 🏫 Multi-department & Multi-shift support  
- 📊 Analytics Dashboard (faculty workload, classroom utilization)  
- 🔄 Real-time timetable updates & conflict resolution  
- 📥 Export options (PDF/Excel) + Website embedding  
- 📅 Policy-compliant scheduling (AICTE norms, NEP 2020 ready)

---

## 🏗️ System Architecture

**Core Modules:**

1. Authentication & Role Management  
2. Data Management (Courses, Faculty, Students, Infra)  
3. Scheduling Engine (CSP / Genetic Algorithm)  
4. Approval Workflow  
5. Visualization & Analytics  
6. Notifications and Reports  

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | React.js, Tailwind CSS / Material UI, FullCalendar.js |
| **Backend** | Django / FastAPI (Python) or Node.js (Express) |
| **Database** | PostgreSQL / MySQL |
| **Scheduling Engine** | Google OR-Tools, OptaPlanner, Rule-based Logic |
| **APIs** | RESTful / GraphQL |
| **Hosting** | AWS / GCP / Azure |
| **Version Control** | Git + GitHub |

## 🧰 Installation & Setup

```bash
# Clone repository
git clone https://github.com/<your-repo>/smart-scheduler.git

# Navigate to project folder
cd smart-scheduler

# Backend setup
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

## AI / Optimization Workflow

1. Base Generation: Constraint Satisfaction (Google OR-Tools)
2. Incremental Updates: OptaPlanner for localized changes
3. Minor Adjustments: Rule-based swapping system

## 📜 License

You are allowed to view or fork the repo, but not permitted to use, copy, modify, or distribute this software in your own projects