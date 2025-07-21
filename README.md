# Secure-Blog

Secure-Blog is a web application designed to provide a secure platform for blogging and user account management. As its name implies, SECURE BLOG features robust security practices—including role-based access control—to ensure user data safety and appropriate permissions management.

## Features

- User authentication and registration system
- **Role-based access control** (RBAC) for users (e.g., admin, editor, author, regular user)
- Secure user account management
- Blog post creation, editing, and deletion
- SQLite database backend for data storage
- Modular app structure for scalability

## Technologies Used

- Python
- Django 
- SQLite (database: `db.sqlite3`)
- HTML

## Project Structure

```
accounts/         # Handles user account features
core/             # Core app functionality (details in code)
secureblog/       # Main project configuration
manage.py         # Django management script
db.sqlite3        # SQLite database file
Project SECUREBLOG.docx # Project documentation (see contents for details)
a.txt             # Additional text resource
```

## Getting Started

1. **Clone the repository:**
   ```
   git clone https://github.com/A22051694/Secure-Blog.git
   cd Secure-Blog
   ```

2. **Install dependencies:**
   Ensure you have Python and Django installed:
   ```
   pip install django
   ```

3. **Run database migrations:**
   ```
   python manage.py migrate
   ```

4. **Start the development server:**
   ```
   python manage.py runserver
   ```

5. **Access the app:**
   Open your browser and go to `http://127.0.0.1:8000/`

## Documentation

- See `Project SECUREBLOG.docx` for detailed project documentation and requirements.

## License

This project currently does not specify a license.

## Author

- [A22051694](https://github.com/A22051694)

---
