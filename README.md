# Django REST API Setup Guide

## 🛠️ Prerequisites
- Python 3.8+
- MySQL Server 5.7+
- virtualenv (`pip install virtualenv`)

## 🚀 Initial Setup

### 1. Create Virtual Environment
```
virtualenv -p python3 env
```

### Activate it:
```
source env/bin/activate  # Linux/Mac
.\env\Scripts\activate   # Windows
```

### 2. Install Dependencies
```
python install -r requirements.txt
```

### 3. Create an .env file in the root folder.
DJANGO_MySQL_API/.env (with the following structure).
```
# Database settings
DB_ENGINE=django.db.backends.mysql
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_NAME=django_api
DB_PASSWORD=your_password
```

### 4. Database Migrations
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Start Project
```
python manage.py runserver
```

### 📡 API Endpoints
Method	Endpoint	Description
```
GET	/api/companies/	List all companies
GET	/api/companies/<id>/	Get specific company
POST	/api/companies/	Create new company
PUT	/api/companies/update/<id>/	Update company
DELETE	/api/companies/delete/<id>/	Delete company
```
