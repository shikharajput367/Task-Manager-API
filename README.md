**Task Management Application**

**Overview**

The Task Management Application is a simple web-based task management system built with Django. It allows users to manage tasks through a user-friendly interface and includes Google Login integration for secure authentication. The app is structured with an n-tier architecture and includes an admin panel for managing Google OAuth keys and inviting new users.


**Features**

**User Features:**

1. Google Login: Secure authentication using Google OAuth.
2. Task Management: Perform CRUD (Create, Read, Update, Delete) operations on tasks.
3. Simple UI: Clean and easy-to-use interface for task management.
   
**Admin Features:**

1. Manage Google OAuth credentials.
2. Invite new users via email with unique registration links.
3. View, add, and manage tasks.
   
**Tech Stack**

1. Backend: Django 5.1.3
2. Frontend: Django Templates, css, html
3. Authentication: Google OAuth2
4. Database: SQLite (default for development)

**Installation**

**Clone the Repository:**

git clone https://github.com/your-username/task-management-app.git
cd task-management-app

**Set Up Virtual Environment:**

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

**Install Dependencies:**

pip install -r requirements.txt

**Run Migrations:**

python manage.py makemigrations
python manage.py migrate

**Set Up Google OAuth:**

Create a new project on the Google Cloud Console.
Enable the Google OAuth2 API.
Generate client credentials (Client ID, Client Secret, Redirect URI) and store them in the admin panel under "Google OAuth Credentials."

**Run the Development Server:**

python manage.py runserver

**Access the Application:**

Admin Panel: http://127.0.0.1:8000/admin/
Task Management App: http://127.0.0.1:8000/
