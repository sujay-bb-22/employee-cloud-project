# Cloud Deployment of an Employee Management System Using Python and Flask

## Project Description

This is a simple beginner-friendly Cloud Computing academic project. It shows how a small web-based Employee Management System can be built with Python, Flask, HTML, CSS, and SQLite, then prepared for deployment to a public cloud hosting platform.

The application supports basic employee record management for a small organization.

## Features

- Add a new employee
- View all employees
- Edit employee information
- Delete an employee with browser confirmation
- Automatic SQLite database creation
- Success messages after important operations
- Simple professional interface suitable for a college project

## Technology Stack

- Python 3
- Flask
- HTML5
- CSS3
- SQLite
- Gunicorn for cloud deployment

## Project Structure

```text
employee-cloud-project/
|
|-- app.py
|-- requirements.txt
|-- Procfile
|-- README.md
|-- employees.db
|
|-- templates/
|   |-- index.html
|   |-- add.html
|   `-- edit.html
|
`-- static/
    `-- style.css
```

## Installation Instructions

Open Windows PowerShell in the project folder and run the following commands.

```powershell
cd employee-cloud-project
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks virtual environment activation, run this command once in the same PowerShell window and then try activation again:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## How to Run Locally

After installing dependencies, start the Flask application:

```powershell
python app.py
```

Open this URL in a browser:

```text
http://127.0.0.1:5000
```

## Required Commands

Create a virtual environment:

```powershell
python -m venv venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the application:

```powershell
python app.py
```

Stop the application:

```powershell
Ctrl+C
```

## Cloud Deployment Overview

This project is prepared for deployment from a GitHub repository to a free cloud hosting platform that supports Python web apps.

Basic deployment steps:

1. Create a GitHub repository.
2. Upload or push this project folder to the repository.
3. Create a new web service on the cloud hosting platform.
4. Connect the GitHub repository.
5. Set the build command to:

```text
pip install -r requirements.txt
```

6. Set the start command to:

```text
gunicorn app:app
```

The included `Procfile` also contains the Gunicorn start command:

```text
web: gunicorn app:app
```

## Application Screenshots

Add screenshots here after running the project locally.

- Home page screenshot: `screenshots/home-page.png`
- Add employee page screenshot: `screenshots/add-employee-page.png`
- Edit employee page screenshot: `screenshots/edit-employee-page.png`

## Notes About SQLite on Cloud Platforms

SQLite is good for a simple academic demo because it is easy to understand and does not require a separate database server.

On many cloud hosting platforms, SQLite data may not be permanent if the server restarts or redeploys. For a real production system, use a managed database such as PostgreSQL. For this beginner project, SQLite is acceptable because the goal is to demonstrate cloud deployment of a simple Flask application.

cd C:\Users\sujay\Documents\Codex\2026-08-23\files-pasted-by-the-user-project\employee-cloud-project
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
