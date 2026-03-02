# Blog Website

A full-featured blog web application built with **Django** — allowing users to register, log in, create, update, and delete blog posts in a clean, responsive interface.

---

## Features

- **User Authentication** — Register, login, and logout via the `accounts` app
- **Full CRUD for Posts** — Create, read, update, and delete blog posts
- **Home Feed** — Browse all published blog posts on the homepage
- **Post Detail View** — Read individual posts on a dedicated page
- **Delete Confirmation** — Safe post deletion with a confirmation step
- **SQLite Database** — Lightweight local database, ready out of the box

---

## 🛠️ Tech Stack

| Layer       | Technology              |
|-------------|-------------------------|
| Backend     | Python 3, Django        |
| Frontend    | HTML5, CSS3 (base.css)  |
| Database    | SQLite3                 |
| Auth        | Django Auth System      |
| Server      | WSGI / ASGI (Django)    |

---

## Project Structure

```
blog_website/
│
├── accounts/                   # User authentication app
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── plog/                       # Project configuration
│   ├── settings.py
│   ├── urls.py                 # Root URL dispatcher
│   ├── asgi.py
│   └── wsgi.py
│
├── plogapp/                    # Core blog application
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py               # Post model
│   ├── urls.py
│   ├── views.py                # CRUD views
│   └── tests.py
│
├── static/
│   └── css/
│       └── base.css            # Global stylesheet
│
├── templates/                  # Django HTML templates
│   ├── registration/
│   │   ├── login.html
│   │   └── signup.html
│   ├── base.html               # Shared base layout
│   ├── home.html               # Blog feed
│   ├── post_detail.html        # Single post view
│   ├── new_post.html           # Create post form
│   ├── post_update.html        # Edit post form
│   └── delete_post.html        # Delete confirmation
│
├── manage.py                   # Django CLI entry point
└── .gitignore
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ziad-Henedy2/blog_website.git
   cd blog_website
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** *(optional — for admin panel access)*
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open in your browser**
   ```
   http://127.0.0.1:8000/
   ```

---

##  Usage

| Action            | URL                  |
|-------------------|----------------------|
| Home / Post Feed  | `/`                  |
| Sign Up           | `/accounts/signup/`  |
| Log In            | `/accounts/login/`   |
| Log Out           | `/accounts/logout/`  |
| New Post          | `post/new/`              |
| Post Detail       | `/post/<id>/`        |
| Edit Post         | `/post/<id>/update/` |
| Delete Post       | `/post/<id>/delete/` |
| Admin Panel       | `/admin/`            |

---

## Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

1. Fork the project
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request
