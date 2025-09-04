

# Smart Learning Circle

A Django-based web application for creating and managing learning circles, where educators can host sessions and students can join.

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- User authentication with role-based system (Student/Educator)
- Learning circle creation and management
- Chat functionality within learning circles
- Payment processing between students and educators
- Responsive web interface

## Technology Stack
- **Backend**: Django 5.2.5
- **Database**: MySQL 
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Railway
- **Authentication**: Django's built-in authentication system
- **Static Files**: Whitenoise

## Prerequisites
- Python 3.13+
- MySQL (for development) or PostgreSQL (for production)
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd smart-learning-circle

markdown



Create a virtual environment:
```
python -m venv .venv_smart_learning_circle
source .venv_smart_learning_circle/bin/activate  # On Windows: .venv_smart_learning_circle\Scripts\activate
```

bash


Install dependencies:
```
pip install -r requirements.txt
```
bash


Configuration
1. Create a .env file in the project root with the following variables:
```
DEBUG=True
DJANGO_SECRET_KEY=your-secret-key-here
MYSQL_DATABASE=smart_learning
MYSQL_USER=your-mysql-username
MYSQL_PASSWORD=your-mysql-password
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
```

2. Generate a secure Django secret key:
```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

```


Database Setup  
1. Make sure your MySQL server is running
2. Create the database:
```
CREATE DATABASE smart_learning  
CHARACTER SET utf8mb4 COLLATE   
utf8mb4_unicode_ci;
```
3. Run migrations:
```
python manage.py migrate

```
4. Create a superuser (optional):
```
python manage.py createsuperuser
```

Running the Application
Activate the virtual environment:

source .venv_smart_learning_circle/bin/activate

bash


Start the development server:

python manage.py runserver

bash


Visit http://127.0.0.1:8000 in your browser

Deployment
This project is configured for deployment on Railway:

Create a Railway account at https://railway.app/

Install the Railway CLI:

npm install -g @railway/cli
railway login

bash


Initialize the Railway project:

railway init

bash


Add a PostgreSQL database service in the Railway dashboard

Set environment variables in Railway:

railway variables set DJANGO_SECRET_KEY="your-secure-secret-key"
railway variables set DEBUG=False
railway variables set ALLOWED_HOSTS="your-project-production.up.railway.app"

bash


Deploy the application:

railway up

bash


Run migrations after deployment:

railway shell
python manage.py migrate
python manage.py collectstatic --noinput

bash


Project Structure
smart-learning-circle/
├── core/                    # Main application
│   ├── models.py           # Data models
│   ├── views.py            # View functions
│   ├── forms.py            # Forms
│   └── ...
├── smart_learning_circle/   # Project settings
│   ├── settings.py         # Configuration
│   ├── urls.py            # URL routing
│   └── ...
├── templates/              # HTML templates
├── static/                 # Static files
├── requirements.txt        # Python dependencies
├── Procfile               # Deployment configuration
└── manage.py              # Django management script

txt


Contributing
Fork the repository
Create a feature branch
Commit your changes
Push to the branch
Create a pull request
