# Ecommerce Product Catalog

A simple Django-based product catalog with an `accounts` app for registration/login and a `catalog` app for managing categories and products.

**Quick Overview**
- Root (`/`) shows the registration page (`accounts.register`).
- Login page: `/accounts/login/`
- Catalog home: `/catalog/`
- Admin: `/admin/`

**Prerequisites**
- Python 3.8+ (use the virtual environment provided or create your own)
- (Optional) A virtual environment in `env/` is present in this workspace.

**Setup (Windows PowerShell)**
```powershell
# Activate virtual environment (if using the included env)
env\Scripts\Activate.ps1

# Install dependencies (if you have a requirements.txt)
pip install -r requirements.txt
# OR at minimum install Django and Pillow if not present
pip install django pillow

# Apply migrations
python manage.py migrate

# Create a superuser for admin
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Open the site at `http://127.0.0.1:8000/` — the register page should appear first. After registration you'll be redirected to the login page.

**Notes**
- Post-login redirect currently sends users to the named URL `home` (the catalog home). If you want a different behavior, update `accounts/views.py` (`login_view`) to change `next_page` or use `LOGIN_REDIRECT_URL` in `Ecommerce_Catalog/settings.py`.
- Static files are served from `static/` and media files from `media/` during development (`DEBUG = True`).

**Project Structure (important files/dirs)**
- `accounts/` — registration, login, profile
- `catalog/` — product and category views, templates
- `Ecommerce_Catalog/` — project settings and URL conf
- `db.sqlite3` — SQLite database (development)

If you want, I can also generate a `requirements.txt`, add a development Makefile/PowerShell script for common tasks, or update the post-login redirect behavior. Which would you like next?