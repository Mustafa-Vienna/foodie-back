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

## 🧠 Foodie API Backend Features

This Django REST Framework-powered backend delivers a robust and modular API for the Foodie platform, complete with image handling, authentication, and social interactions.

---

### 🔐 JWT-Based Authentication

- Secure login and token management with **SimpleJWT**
- Returns custom payload with user details (ID, username, profile image)
- Integrated into login/signup flow

📸 *Proof:*  
![Admin Login](../foodie-back/documentation/backend_validation/admin_login.png)

---

### 👤 User Profile Management

- Profiles are automatically created on user registration
- Users can edit their name, bio, and avatar
- Avatar images are handled via **Cloudinary**
- Dynamic counts for:
  - Posts
  - Followers
  - Following

📸 *Proof:*  
![Profile Detail](../foodie-back/documentation/backend_validation/user_profile.png)

---

### 🍽 Create, Update & Delete Food Posts

- Authenticated users can:
  - Create rich posts with title, intro, steps, ingredients, and images
  - Update or delete only their own posts
- Validations for fields like tags, category, and image

📸 *Proof:*  
![Post Management](../foodie-back/documentation/backend_validation/posts_management.png)

---

### 🖼 Image Upload via Cloudinary

- Profile and post images stored using **Cloudinary**
- Fallback to a default image when none is uploaded
- Fully integrated into serializers for real-time rendering

---

### ❤️ Like System for Posts

- Users can like/unlike any post
- Total likes and like status (`liked` / `not liked`) are calculated per user
- Tooltip feedback and frontend counter sync

📸 *Proof:*  
![Comments](../foodie-back/documentation/backend_validation/Likes_system.png)

---

### 💬 Comment System Under Posts

- Comment creation, listing, and user linking
- Shows author info and avatar
- Only comment owners can delete or update their comments

📸 *Proof:*  
![Comments](../foodie-back/documentation/backend_validation/Comment_system.png)

---

### 👥 Follow/Unfollow Users

- Authenticated users can follow or unfollow others
- Profile detail view shows:
  - Follow status
  - Followers and following counts
- Prevents duplicate follows

📸 *Proof:*  
![Comments](../foodie-back/documentation/backend_validation/Followes_system.png)

---

### 🔎 Filtering, Search & Pagination

- Full filtering and ordering for posts:
  - `likes_count`, `comments_count`, `created_at`, etc.
- Filter by tag or category using DjangoFilterBackend
- Paginated results for efficient browsing

📸 *Proof:*  
![Search & Filters](../foodie-back/documentation/backend_validation/Search_Filter_system.png)  
![Tags System](../foodie-back/documentation/backend_validation/Posts_Tags_system.png)

---

### 📦 Modular & RESTful API Design

- Organized by app: `profiles`, `posts`, `comments`, `likes`, `followers`
- RESTful views and URL patterns for clean endpoint usage
- Token-protected POST, PATCH, DELETE actions

---

### 🚫 Error Handling Example

- Example: Attempting to access a non-existent profile

📸 *Proof:*  
![404 Profile Not Found](../foodie-back/documentation/backend_validation/non_exist_profile.png)


### 🔜 Upcoming Features

The following features are in the pipeline and will be implemented in future versions of the Foodie API. These enhancements aim to improve user engagement, content interaction, and personalization across the platform.

---

#### 🔁 Like & Reply to Comments
- Allow users to like individual comments for better feedback visibility.
- Introduce **comment replies** to enable threaded discussions.
- Build hierarchical structure using parent-child relationships.

🧪 *Planned Test Cases:*
- Verify comment reply creation by authenticated users.
- Ensure reply nesting is limited to one level deep (for clarity).
- Test like toggling on comments and reply consistency in API.

---

#### 📝 Add New Post from Profile Page
- Allow users to create posts directly from their profile page.
- Reduces navigation friction and promotes more posting activity.
- Improves UX by placing creation entry points where users are most active.

🧪 *Planned Test Cases:*
- Ensure form visibility only for profile owners.
- Validate post creation and redirection back to profile on success.

---

#### 🌟 Popular Profiles
- A new endpoint to list **top profiles** based on:
  - Follower count
  - Post count
  - Engagement (likes, comments)

🧪 *Planned Test Cases:*
- Rank profiles correctly based on dynamic follower/post metrics.
- Ensure endpoint is paginated and filterable.

---

#### 🔔 Real-Time Notifications (WebSockets)
- Notify users in real-time about:
  - New followers
  - Likes
  - Comments or replies
- Built with Django Channels + Redis backend

🧪 *Planned Test Cases:*
- Validate event broadcasting on `like`, `comment`, or `follow`.
- Test fallback to polling for unsupported clients.

---

#### 💌 Direct Messaging (DM)
- Private chat between users.
- Supports:
  - New message notifications
  - Chat list with latest activity
  - Real-time updates via WebSockets

🧪 *Planned Test Cases:*
- Ensure only involved users can view or send messages.
- Rate-limit message sending to prevent spam.

---

#### 📌 Save for Later / Bookmark Recipes
- Users can bookmark recipes and view a "Saved Posts" section.
- Helps users build personal collections for future cooking inspiration.

🧪 *Planned Test Cases:*
- Prevent duplicate bookmarks per user.
- Validate saved/un-saved toggle in both frontend and API.

---

#### 🧠 Smart Content Recommendations
- Recommend posts based on:
  - Tags
  - Categories
  - Previously liked or commented content
- Powered by simple rule-based logic at first (can later move to ML-based)

🧪 *Planned Test Cases:*
- Ensure recommendations exclude the user’s own posts.
- Validate fallback to trending posts if data is insufficient.

---

### 🧩 Followers System – Coming Soon!

The `followers` app is already in place, with models and serializers prepared.  
Due to time constraints during the current milestone, it was not integrated into the frontend. However, it will be completed in the next version and linked with the notifications and profile feed system.

🧪 *Planned Test Cases:*
- Follow/unfollow toggle and state validation
- Prevent self-following
- Count accuracy on profile detail

---

> 📅 All features are structured with test-driven development in mind, and will include proper unit tests and integration tests using Django REST Framework and `pytest` as needed.


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

