# 🚀 VPlace - A College Placement Portal

Welcome to **VPlace**, a comprehensive web application built on Django designed to streamline the student placement lifecycle. The application assists students in building profiles, practicing aptitude/programming quizzes, tracking upcoming events, matching with job requirements, and receiving automated WhatsApp notifications for suitable roles.

---

## ✨ Features

### 👤 Profile & Portfolio Builder
*   **Comprehensive Profiles**: Manage student details, roles, "About Me" sections, skills, education history, and projects.
*   **Experience & Achievements**: Dynamic addition and tracking of past work experience and student achievements.
*   **Dynamic Resume Generation**: Export profile details directly into a clean, professionally formatted PDF using `ReportLab`.

### 💼 Smart Job Matching & Alerts
*   **Intelligent Recommendations**: Automatic job matching based on profile skills, roles, and open job requirements.
*   **WhatsApp Notifications**: Integrated with the **Twilio API** to instantly notify students via WhatsApp when a new job matches their skillset.

### 📅 Event Calendar
*   **Placement Tracking**: Stay updated with recruitment drives, webinars, and mock interview events.

### 📝 Preparation & Quizzes
*   **Aptitude & Programming Practice**: Quizzes covering essential topics, split into clear categories:
    *   **Aptitude**: Profit and Loss, Percentage, Permutation & Combination, Table Charts, Pie Charts, Bar Graphs.
    *   **Programming**: C++, Java, Python.
*   **Score Tracking**: Automatic submission grading with scoreboards to monitor progress over time.

---

## 🛠️ Technology Stack

*   **Backend Framework**: Django 5.1.1 & Django REST Framework (DRF)
*   **Database**: SQLite (Default development database)
*   **API Integrations**: Twilio (WhatsApp API)
*   **Document Generation**: ReportLab (PDF Generation), Python-docx
*   **Styling**: HTML5, Vanilla CSS

---

## 📂 Project Structure

```text
placement_portal/
│
├── Readme.md                   # Project documentation
└── backend/                    # Root Django project
    ├── backend/                # Project configuration (settings, URLs, etc.)
    │   ├── settings.py
    │   └── urls.py
    ├── credentials/            # App managing Authentication, Profile, Jobs, and Quizzes
    │   ├── models.py           # Database Schemas (Profile, Job, Quiz, Submission, etc.)
    │   ├── views.py            # Business logic (Matching, PDF Resume, Session management)
    │   ├── urls.py             # Route endpoints
    │   ├── serializers.py      # Serializers for DRF
    │   └── utils.py            # Helper modules
    ├── myapp/                  # Secondary app for templates and static assets
    ├── media/                  # User uploads (Profile photos, Company logos)
    ├── static/                 # CSS/JS assets
    ├── manage.py               # Django CLI tool
    └── db.sqlite3              # Database file
```

---

## ⚙️ Setup & Installation

Follow these steps to run the Placement Portal locally:

### 1. Prerequisites
Ensure you have Python (version 3.10 or higher) installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/Roshanbits/finalyearproject.git
cd placement_portal/backend
```

### 3. Set Up a Virtual Environment (Recommended)
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
.\venv\Scripts\activate

# Activate virtual environment (macOS/Linux)
source venv/bin/activate
```

### 4. Install Dependencies
Install all the required python packages:
```bash
pip install django djangorestframework twilio reportlab python-docx docx2pdf
```

### 5. Database Migrations
Apply database migrations to set up your SQLite schemas:
```bash
python manage.py migrate
```

### 6. Create a Superuser
Create an administrator account to access the Django Admin Portal:
```bash
python manage.py createsuperuser
```

### 7. Run the Server
Launch the local development server:
```bash
python manage.py runserver
```
Visit the application in your browser at `http://127.0.0.1:8000/`.

---

## ⚙️ Integrations & Configurations

### 📱 Twilio (WhatsApp Integration)
The application utilizes Twilio to send automated job match alerts. Update your credentials in `backend/backend/settings.py`:
```python
TWILIO_ACCOUNT_SID = 'your_account_sid_here'
TWILIO_AUTH_TOKEN = 'your_auth_token_here'
TWILIO_WHATSAPP_FROM = 'whatsapp:+14155238886' # Twilio sandbox number
```

### 📁 Media Files Upload
To support profile pictures and company logos, media files are stored under the `/media/` path. Ensure your settings reference the correct folders:
*   `MEDIA_URL = '/media/'`
*   `MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`
