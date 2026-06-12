# A&A Global News Platform

**Developed, Founded, and Owned by Shivam Kumar.**

This is the official repository for **A&A Global** (Axis & Atom Global), a premium digital news publication platform built, owned, and maintained exclusively by **Shivam Kumar**. All rights, including code, design, features, database schemas, and branding, are reserved under a proprietary license.

## 🚀 Tech Stack

This website is built with a robust, modern technology stack designed for scalability and security:

### Backend
- **Python 3.10+**: Core programming language.
- **Flask Framework**: Lightweight and flexible WSGI web application framework.
- **SQLite & SQLAlchemy (ORM)**: Database architecture for fast, reliable data storage.
- **Flask-Migrate (Alembic)**: Database schema migration tracking.
- **Waitress**: Production-ready WSGI server.

### Frontend
- **HTML5 & CSS3**: Custom, responsive layout with a dark/light minimalist aesthetic.
- **Bootstrap 5.3.3**: Grid system and responsive UI components.
- **Jinja2**: Server-side HTML templating for dynamic rendering.

### Security & Optimization
- **Flask-Login**: Secure session management and authentication for administrators.
- **Flask-WTF & WTForms**: Form validation and automatic CSRF (Cross-Site Request Forgery) protection.
- **Bcrypt**: Robust password hashing.
- **Flask-Limiter**: IP-based rate limiting to prevent brute-force and DDoS attacks.
- **Flask-Caching**: View and data caching to handle high traffic loads efficiently.
- **HTTP Security Headers**: Custom headers implemented (`X-Content-Type-Options`, `X-Frame-Options: SAMEORIGIN`, `X-XSS-Protection`, `Strict-Transport-Security`, `Referrer-Policy`) to block clickjacking, XSS, and MIME-sniffing.

## 🌟 Features

- **Admin Dashboard**: Comprehensive CMS to manage articles, categories, comments, and site advertisements.
- **Dynamic Breaking News Ticker**: Customizable top-bar scrolling ticker directly manageable from the admin panel (via the `is_breaking` toggle).
- **SEO Optimized**: Fully integrated with OpenGraph, Twitter Cards, dynamic meta descriptions, and structured sitemaps.
- **Google AdSense Ready**: Pre-configured ad slots (Header, Sidebar, In-Article, Footer) with asynchronous loading tags embedded in the `<head>`.
- **Professional Legal Pages**: Out-of-the-box legally sound Privacy Policy, Terms of Service, and Copyright DMCA Disclaimers protecting the Founder (Shivam Kumar) and the platform's intellectual property.



## 🛠️ Local Development & Running

1. **Activate the Virtual Environment**:
   ```bash
   .\venv\Scripts\activate
   ```

2. **Install Dependencies** (if needed):
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Migrations** (if you change models):
   ```bash
   flask db migrate -m "Description"
   flask db upgrade
   ```

4. **Run the Development Server**:
   ```bash
   python run.py
   ```
   *The site will be available at http://127.0.0.1:5000*

## 📦 Deployment to GitHub

This folder is completely ready to be uploaded to a GitHub repository:

1. Open your terminal in this directory.
2. Initialize git: `git init`
3. Add all files: `git add .` (Note: `instance/` and `venv/` are ignored via `.gitignore` to keep secrets safe).
4. Commit: `git commit -m "Initial commit"`
5. Link to your repository: `git remote add origin <YOUR_GITHUB_REPO_URL>`
6. Push: `git push -u origin main`


