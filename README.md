<div align="center">

# 📝 **OneIDE**
### 🌐 Online Compiler & Coding Community Platform

<img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
<img src="https://img.shields.io/badge/Maintained-Yes-brightgreen?style=for-the-badge">

<br/>

### ⚡ *Compile. Collaborate. Connect.*

A powerful **online compiler + coding community platform** with real-time execution, group collaboration, and admin control.

[🐞 Report Bug](https://github.com/your-username/your-repo-name/issues) • [✨ Request Feature](https://github.com/your-username/your-repo-name/issues)

</div>

---

## 📖 Overview

**OneIDE** is a full-stack web application that offers:
- A **multi-language online compiler**
- A **coding community for sharing programs**
- **Group collaboration** with permissions
- A complete **admin dashboard** for moderation  

It bridges the gap between **learning to code** and **collaborative software development**.

---

## ✨ Features

### 🔐 User Authentication & Management
- ✅ Secure Login & Registration  
- ✅ Role-Based Access (Admin / User)  
- ✅ Forgot Password via Email (SMTP)  
- ✅ Profile Management with Image Upload  
- ✅ Admin Blocking & Unblocking of Users  

---

### 💻 Online Compiler & Coding Tools
- 🌍 Supports **Python, Java, C, C++**
- ⚡ Real-time Code Execution
- 💾 Save Programs with Topic, Language & Date
- 🕒 View Code Execution History
- ✏️ Edit & Update Saved Programs

---

### 🤝 Community & Collaboration
- 🔄 **Code Sharing**
  - Individual Sharing
  - Group Sharing (Static / Editable)
- 👥 **Group Management**
  - Create Groups with Icons
  - Add/Remove Members
  - Assign Roles (Admin, User)
- ⭐ Feedback & Rating System
- 📢 Complaint System with Admin Replies
- 📚 Library of Example Programs

---

### 🛠️ Admin Dashboard
- 👤 View & Manage Users
- 🚫 Block / Unblock Accounts
- 🧾 Monitor Shared Code
- 📬 Handle Complaints & Feedback
- 📖 Manage Example Programs

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| **Backend** | Django, Python |
| **Frontend** | HTML, CSS, JavaScript, Bootstrap |
| **Database** | MySQL |
| **Auth** | Django Auth System |
| **Email** | SMTP (`smtplib`) |

---

## 🚀 Getting Started

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Install Dependencies
bash
Copy code
pip install django
3️⃣ Run Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
4️⃣ Create Admin
bash
Copy code
python manage.py createsuperuser
5️⃣ Start Server
bash
Copy code
python manage.py runserver
6️⃣ Open in Browser
cpp
Copy code
http://127.0.0.1:8000/
🗄️ Database Setup
✅ Option 1: Import SQL Dump
sql
Copy code
CREATE DATABASE oneide;
bash
Copy code
mysql -u your_username -p oneide < oneide_dump.sql
✅ Option 2: Fresh Django Setup
bash
Copy code
python manage.py makemigrations
python manage.py migrate
🧩 ER Relationship (Simplified)
pgsql
Copy code
LOGIN ||--|| USER : credentials
USER  ||--o{ CODE : saves
USER  ||--o{ GROUP : creates
GROUP ||--|{ MEMBER : contains
USER  ||--|{ MEMBER : joins
USER  ||--o{ FEEDBACK : writes
USER  ||--o{ SHARE_P2P : sends
GROUP ||--o{ SHARE_GROUP : receives
📂 Project Structure
pgsql
Copy code
app/
├── migrations/
├── static/
├── templates/
│   ├── admin/
│   ├── user/
│   ├── login.html
│   ├── registration.html
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── urls.py
└── views.py
🤝 Contributing
Fork the Repository

Create a Feature Branch

Commit Your Changes

Push to Your Branch

Open a Pull Request

📄 License
This project is licensed under the MIT License ✅
Free to use for educational and commercial purposes.

<div align="center">
💙 If you like this project, don't forget to ⭐ the repo!
</div> ```