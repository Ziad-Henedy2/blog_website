# 📝 Blog Website

A full-featured blog web application built with **Django** — allowing users to register, log in, create posts, and browse content in a clean, responsive interface.

---

## 🚀 Features

- 🔐 **User Authentication** — Register, login, and logout functionality via the `accounts` app
- 📄 **Blog Posts** — Create, view, and manage blog posts through the `plogapp`
- 🧭 **Routing & Config** — Clean URL routing managed by the `plog` project configuration
- 🎨 **Responsive UI** — Custom CSS styling with HTML templates for a seamless experience
- 🗄️ **Django ORM** — Database management using Django's built-in ORM

---

## 🛠️ Tech Stack

| Layer       | Technology          |
|-------------|---------------------|
| Backend     | Python, Django      |
| Frontend    | HTML5, CSS3         |
| Database    | SQLite (default)    |
| Auth        | Django Auth System  |

---

## 📁 Project Structure

```
blog_website/
├── accounts/          # User registration, login & logout
├── plog/              # Project settings, main URLs, WSGI/ASGI config
├── plogapp/           # Core blog app — models, views, URLs, forms
├── static/
│   └── css/           # Custom stylesheets
├── templates/         # HTML templates (base layout + per-app templates)
├── manage.py          # Django management entry point
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

5. **Create a superuser** *(optional — for admin access)*
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

---

## 🔑 Usage

- **Register** a new account or **log in** with existing credentials
- Browse the blog homepage to view all published posts
- Authenticated users can **create and manage** their own blog posts
- Admin users can manage all content via `/admin`

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

1. Fork the project
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

