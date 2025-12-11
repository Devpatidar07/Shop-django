---

README.md

Django Project – Installation & Setup Guide

This repository contains a Django 3.1 project with PostgreSQL support, AWS S3 integration, and essential utilities. Follow the steps below to set up the project on your local machine.


---

1. System Requirements

Python 3.8+

pip

Git

Virtualenv (optional)

PostgreSQL (only if not using SQLite)

VS Code (recommended)



---

2. Clone the Repository

git clone https://github.com/<username>/<repo>.git
cd <repo>


---

3. Create & Activate Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

macOS / Linux

python3 -m venv venv
source venv/bin/activate


---

4. Install Requirements

pip install --upgrade pip
pip install -r requirements.txt

requirements.txt

asgiref==3.2.10
boto3==1.17.36
botocore==1.20.36
certifi==2020.12.5
chardet==4.0.0
Django==3.1
django-admin-honeypot==1.1.0
django-admin-thumbnails==0.2.5
django-session-timeout==0.1.0
django-storages==1.11.1
idna==2.10
jmespath==0.10.0
Pillow==7.2.0
psycopg2-binary==2.8.6
python-dateutil==2.8.1
python-decouple==3.4
pytz==2020.1
requests==2.25.1
s3transfer==0.3.6
six==1.15.0
sqlparse==0.3.1
urllib3==1.26.3


---

5. Create .env File

Create a file named .env in the project root:

SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# If using PostgreSQL
DB_NAME=your_db_name
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# AWS S3 (only if used)
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
AWS_S3_REGION_NAME=

Do not upload .env to GitHub.


---

6. Database Setup

SQLite (Default)

No setup needed.

PostgreSQL

Create database:

CREATE DATABASE your_db_name;


---

7. Apply Migrations

python manage.py makemigrations
python manage.py migrate


---

8. Create Superuser

python manage.py createsuperuser


---

9. Collect Static Files (For Production)

python manage.py collectstatic --noinput


---

10. Run Development Server

python manage.py runserver

Visit:
http://127.0.0.1:8000/


---

11. Common Errors & Fixes

ModuleNotFoundError

Activate virtual environment:

venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

psycopg2 Error

Ensure PostgreSQL is installed or use included psycopg2-binary.

SECRET_KEY Missing

Add SECRET_KEY in .env.

ALLOWED_HOSTS Error

Use:

ALLOWED_HOSTS=127.0.0.1,localhost


---

12. Useful Git Commands

git status
git add .
git commit -m "Update"
git push origin main


---

13. Project Structure

project/
│
├── app1/
├── app2/
├── templates/
├── static/
├── media/
├── requirements.txt
├── manage.py
└── .env


---

14. Setup Complete

Your Django project is ready.
