# Cloud Deployment of an Employee Management System Using Python and Flask

A simple web-based Employee Management System built with Python and Flask. The application allows users to manage employee records through a clean interface and demonstrates how a Flask application can be deployed to a cloud hosting platform.

## Live Demo

**Application:** https://employee-cloud-project.onrender.com

**GitHub Repository:** https://github.com/sujay-bb-22/employee-cloud-project

## Features

* Add new employees
* View all employee records
* Edit existing employee information
* Delete employees with confirmation
* Automatic SQLite database initialization
* Success messages for important operations
* Clean and responsive user interface
* Cloud deployment using Render

## Technology Stack

* Python 3
* Flask
* HTML5
* CSS3
* SQLite
* Gunicorn
* GitHub
* Render

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

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sujay-bb-22/employee-cloud-project.git
```

### 2. Move into the Project Directory

```bash
cd employee-cloud-project
```

### 3. Create a Virtual Environment

```powershell
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the virtual environment again.

### 5. Install Dependencies

```powershell
pip install -r requirements.txt
```

## Running the Application

Start the Flask application:

```powershell
python app.py
```

Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

To stop the application:

```text
Ctrl+C
```

## Usage

The application supports the following operations:

### Add Employee

Add a new employee by providing:

* Name
* Email
* Department
* Position

### View Employees

The home page displays all employee records in a table.

### Edit Employee

Update the details of an existing employee.

### Delete Employee

Remove an employee record after confirming the deletion.

## Cloud Deployment

The application is deployed as a web service on Render.

### Deployment Configuration

**Build Command**

```text
pip install -r requirements.txt
```

**Start Command**

```text
gunicorn app:app
```

The project also includes a `Procfile` with the following configuration:

```text
web: gunicorn app:app
```

### Deployment Flow

```text
Local Development
       |
       v
GitHub Repository
       |
       v
Render Web Service
       |
       v
Live Application
```

## Cloud Deployment Model

The application uses a public cloud deployment model.

The source code is hosted on GitHub and connected to Render, which builds and deploys the application as a publicly accessible web service.

## Application Architecture

```text
+------------------+
|   User Browser   |
+------------------+
          |
          v
+------------------+
|  Render Cloud    |
|   Web Service    |
+------------------+
          |
          v
+------------------+
| Gunicorn Server  |
+------------------+
          |
          v
+------------------+
| Flask Application|
+------------------+
          |
          v
+------------------+
| SQLite Database  |
+------------------+
```

## Database

The application uses SQLite to store employee records.

Each employee record contains:

* ID
* Name
* Email
* Department
* Position

The database is initialized automatically when the application runs.

## Project Links

* **Live Application:** https://employee-cloud-project.onrender.com
* **GitHub Repository:** https://github.com/sujay-bb-22/employee-cloud-project

## Notes

SQLite is used to keep the application lightweight and simple. On cloud platforms with ephemeral storage, database changes may not persist after redeployment or certain service restarts.

For a production deployment, a managed database such as PostgreSQL would be a better choice.
