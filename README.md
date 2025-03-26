# 🍽 Foody API Backend

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Mustafa-Vienna/foodie-back)](https://github.com/Mustafa-Vienna/foodie-back/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Mustafa-Vienna/foodie-back)](https://github.com/Mustafa-Vienna/foodie-back/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Mustafa-Vienna/foodie-back)](https://github.com/Mustafa-Vienna/foodie-back)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Mustafa-Vienna&repo=foodie-back&layout=compact)


## Project Overview

Foodie API is a backend for a community platform where food lovers can share and discover delicious recipes. Built with Django Rest Framework, it provides a robust backend for social interactions around food content.

### 🌐 Related Projects

#### 🧠 Backend API (Django Rest Framework + JWT)
- 🔗 GitHub: [Mustafa-Vienna/foodie-back](https://github.com/Mustafa-Vienna/foodie-back)
- 🚀 Live: [https://foodieback-0e50528a3736.herokuapp.com/](https://foodieback-0e50528a3736.herokuapp.com/)

#### 💻 Frontend Application (React)
- 🔗 GitHub: [Mustafa-Vienna/foodie](https://github.com/Mustafa-Vienna/foodie)
- 🚀 Live: [https://foodiefront-bacd5250c6d8.herokuapp.com/](https://foodiefront-bacd5250c6d8.herokuapp.com/)


## 📁 Project Structure

```
FOODIE-BACK/
│
├── manage.py
├── requirements.txt
├── README.md
├── Procfile
├── runtime.txt
├── db.sqlite3
│
├── foodie_api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── settings.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   └── wsgi.py
│
├── comments/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
│
├── followers/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
│
├── likes/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
│
├── posts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── fit_post_content.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
│
├── profiles/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
│
├── media/
│   └── images/
│       ├── tiika_burger_75fade9.webp
│       └── milk_burger.webp
│
└── .gitignore
```

## 🗂 Project Modules

* 🧠 Main Config: `foodie_api/`
  - Core project configuration
  - API settings and main URLs
  - Permissions and serializers

* 🍽 Posts: `posts/`
  - Create, read, update, delete food posts
  - Content management
  - Post-related utilities

* ❤️ Likes: `likes/`
  - Like functionality
  - User interaction tracking

* 💬 Comments: `comments/`
  - Comment system
  - User discussions

* 👥 Followers: `followers/`
  - User follow/unfollow mechanics
  - Social connection management

* 👤 Profiles: `profiles/`
  - User profile management
  - Profile-related operations

## 🚀 Features

### ✅ Current Features

- 🔐 JWT-based user authentication
- 👤 User profile management (with avatar & bio)
- 🍽 Create, update, delete food posts
- 🖼 Image upload via Cloudinary
- ❤️ Like system for posts
- 💬 Comment system under posts
- 👥 Follow/unfollow users
- 🔎 Filtering and pagination
- 📦 Modular, RESTful API design

### 🔜 Upcoming Features

- 🔔 Real-time notifications (WebSockets)
- 💌 Direct messaging between users
- 🌟 Recipe bookmarking or save-for-later
- 🧠 Smart content recommendations

---

## 🔧 Technologies Used

### 🖥 Backend

- Django 5.1.5
- Django Rest Framework 3.15.2
- PostgreSQL (via dj-database-url)
- Cloudinary (media storage)
- WhiteNoise (static file serving)

### 🔐 Authentication

- Simple JWT 5.4.0
- Django AllAuth
- Dj-Rest-Auth

### 🧰 Additional Libraries

- `django-cors-headers`
- `django-filter`
- `gunicorn` (WSGI server for deployment)
- `pillow` (image handling)

---

## 🛠 Prerequisites

Make sure you have the following installed:

- Python 3.9+
- `pip`
- `virtualenv` (recommended for isolated environments)

---

## ⚡️ Quick Start

### 📥 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Mustafa-Vienna/foodie-back.git
cd foodie-back
```

2. **Create a virtual environment**
  ```bash
  python -m venv venv
  source venv/bin/activate 

  # On Windows use 
  `venv\Scripts\activate`
  ```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
  - Create an `env.py` file with:
```python
import os
os.environ['SECRET_KEY'] = 'your-secret-key'
os.environ['DATABASE_URL'] = 'your-database-url'
os.environ['CLOUDINARY_URL'] = 'your-cloudinary-url'
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Start the development server**
```bash
python manage.py runserver
```

## 🔐 Environment Configuration

These environment variables must be set (either in `env.py` for local use or in your hosting config for deployment):

| Variable                | Description                                 |
|-------------------------|---------------------------------------------|
| `SECRET_KEY`            | Django secret key                           |
| `DATABASE_URL`          | PostgreSQL connection string                |
| `CLOUDINARY_URL`        | Full Cloudinary media URL                   |
| `CLOUDINARY_CLOUD_NAME` | Your Cloudinary cloud name                  |
| `CLOUDINARY_API_KEY`    | Your Cloudinary API key                     |
| `CLOUDINARY_API_SECRET` | Your Cloudinary API secret                  |
| `DEV`                   | Set to `1` for local development            |
| `ALLOWED_HOSTS`         | Comma-separated list of allowed domains     |

