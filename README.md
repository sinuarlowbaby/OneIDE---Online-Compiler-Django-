<div align="center">

# 📝 OneIDE - Online Compiler & Coding Community Platform

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)

<p align="center">
  <strong>Compile. Collaborate. Connect.</strong><br>
  A comprehensive web application designed to facilitate coding, learning, and group collaboration.
</p>

[Report Bug](https://github.com/your-username/your-repo-name/issues) · [Request Feature](https://github.com/your-username/your-repo-name/issues)

</div>

---

## 📖 Overview

This platform provides a robust **online compiler** for multiple languages, a community hub for sharing and discussing code, and administrative tools for managing users and content. It bridges the gap between learning to code and collaborating in a team environment.

---
### ✨ Features

#### 🔐 User Authentication & Management

  * **Secure Login & Registration:** User accounts with secure password handling.
  * **Role-Based Access:** Distinct roles for 'User' and 'Admin' with tailored dashboards and permissions.
  * **Forgot Password:** Password recovery via email using SMTP.
  * **Profile Management:** Users can manage their personal details and profile picture.
  * **User Blocking/Unblocking:** Admins can manage user access by blocking or unblocking accounts.

#### 💻 Online Compiler & Coding Tools

  * **Multi-Language Support:** Integrated compilers for **Python**, **Java**, **C**, and **C++**.
  * **Real-time Compilation:** Execute code directly within the browser.
  * **Code Saving:** Save code snippets with topic, language, and date for future reference.
  * **Code History:** View a history of executed and saved code.
  * **Edit Saved Code:** Modify and update previously saved code snippets.

#### 🤝 Community & Collaboration

  * **Code Sharing:**
      * **Individual Sharing:** Share code directly with other users.
      * **Group Sharing:** Share code within created groups with 'Static' (read-only) or 'Editable' permissions.
  * **Group Management:**
      * Create and manage user groups with names, descriptions, and icons.
      * Add or remove members and assign roles (e.g., Admin, User).
      * Delete groups or specific group content.
  * **Feedback & Complaints:**
      * Users can send feedback and ratings.
      * Users can lodge complaints, and admins can view and reply to them.
  * **Example Programs:** Access a library of sample programs categorized by language and topic for learning.

#### 🛠️ Admin Dashboard

  * **User Management:** View all users, manage their status (block/unblock), and view individual profiles.
  * **Content Moderation:** View all shared code, complaints, and feedback.
  * **Sample Program Management:** Add, edit, and manage the library of example programs.
  * **Complaint Resolution:** Reply to user complaints directly from the dashboard.

### 🛠️ Tech Stack

  * **Backend Framework:** Django (Python)
  * **Database:** SQLite (Default Django DB) / MySQL (Compatible)
  * **Frontend:** HTML, CSS, JavaScript, Bootstrap (Jinja2 Templating)
  * **Authentication:** Django Auth System
  * **Email Services:** Python `smtplib` for email notifications

### 🚀 Getting Started

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Install Dependencies:**
    Ensure Python is installed, then run:

    ```bash
    pip install django
    ```

3.  **Database Migration:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Create Superuser (Admin):**

    ```bash
    python manage.py createsuperuser
    ```

5.  **Run the Server:**

    ```bash
    python manage.py runserver
    ```

6.  **Access the Application:**
    Open your browser and navigate to `http://127.0.0.1:8000/`.


## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend** | ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat-square&logo=bootstrap&logoColor=white) ![JS](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) |
| **Database** | ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white) (Production compatible with MySQL) |
| **Services** | SMTP (Email Notifications) |

---    

### 📂 Project Structure

```
app/
├── migrations/       # Database migrations
├── static/           # Static files (CSS, JS, Images)
├── templates/        # HTML Templates
│   ├── admin/        # Admin-specific templates
│   ├── user/         # User-specific templates
│   ├── login.html
│   ├── registration.html
│   └── ...
├── admin.py          # Django Admin configuration
├── apps.py           # App configuration
├── models.py         # Database models
├── tests.py          # Tests
├── urls.py           # URL routing
└── views.py          # View functions (Business logic)
```

### 🤝 Contributing

Contributions are welcome\! Please follow these steps:

1.  **Fork** the repository.
2.  Create a **Feature Branch**.
3.  **Commit** your changes.
4.  **Push** to the branch.
5.  Open a **Pull Request**.

### 📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).