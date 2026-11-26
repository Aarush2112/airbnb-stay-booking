# StayVista — Vacation Rental & Stays Web Application (Airbnb-Inspired)

- **Student Name:** [Student Name]
- **Roll Number:** [Roll Number]
- **Section:** [Section]

## 1. Project Objective
Build a multi-page Django web application using template inheritance (`base.html`), named URL routing (`{% url %}`), views, SQLite database models with migrations, static assets (CSS, JavaScript, and local PNG images), server-side form validation, and Django's built-in authentication system.

## 2. Website Theme & Reference
- **Theme:** Vacation rentals & unique stays marketplace (**StayVista**), inspired by Airbnb's clean card grid, category filter strip, pill search bar, coral-rose (`#FF385C`) accent palette, and sticky booking card layout.
- **Original Assets:** All branding, copy, SVG logo, and property illustrations are original local assets stored under `website/static/website/images/`.

## 3. Features and Page Descriptions
| Page | URL | Description |
| :--- | :--- | :--- |
| **Home** | `/` | Hero search bar, horizontal category strip, 6 featured stays, and host/support callout. |
| **Explore Stays** | `/stays/` | Filterable catalog of all 8 stays by category (`?category=...`) and destination keyword (`?q=...`). |
| **Stay Detail** | `/stays/<slug>/` | Full property details, host badge, amenities grid, live nightly price estimator, and validated Booking Inquiry POST form. |
| **About & Contact** | `/about/` | Platform overview, security highlights, and validated Contact Support POST form. |
| **Log In** | `/login/` | Authenticates users by username or email using `django.contrib.auth.authenticate()` and `login()`. |
| **Sign Up** | `/signup/` | Registers new users with server-side validation, password confirmation matching, and PBKDF2 password hashing via `User.objects.create_user()`. |
| **Log Out** | `/logout/` | Ends the active user session and redirects to Home. |

## 4. Navigation Flow
- **Home (`/`)** &rarr; Search bar or category pills &rarr; **Explore Stays (`/stays/`)**
- **Home (`/`)** or **Explore Stays (`/stays/`)** &rarr; Click any property card &rarr; **Stay Detail (`/stays/<slug>/`)**
- **Header & Footer (all pages)** &rarr; `Home`, `Explore Stays`, `About & Contact`, `Log in`, `Sign up` (or `Log out` when signed in)
- **Log In (`/login/`)** &harr; **Sign Up (`/signup/`)** &rarr; Direct links between both auth pages and back to **Home (`/`)**

## 5. Technologies Used
- **Backend:** Python 3.11+, Django (`>=4.2,<6.0`), SQLite3
- **Frontend:** HTML5, CSS3 (responsive grid & flexbox), Vanilla JavaScript
- **Authentication:** `django.contrib.auth` (PBKDF2 password hashing, CSRF protection)

## 6. Django Project Structure
```text
stayvista_project/
├── manage.py
├── requirements.txt
├── README.md
├── stayvista_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── website/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── seed_data.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    ├── static/
    │   └── website/
    │       ├── css/style.css
    │       ├── js/main.js
    │       └── images/
    │           ├── hero_banner.png
    │           └── stay_*.png (8 listing images)
    └── templates/
        └── website/
            ├── base.html
            ├── home.html
            ├── stays.html
            ├── stay_detail.html
            ├── about.html
            ├── login.html
            └── signup.html
```

## 7. How to Run the Project
1. **Extract the archive** and open a terminal inside `stayvista_project/`.
2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS / Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```
   *(Note: The 8 sample stays automatically seed into SQLite on the first visit to `/` or `/stays/`.)*
5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
6. **Open in browser:** Visit `http://127.0.0.1:8000/`.

## 8. Screenshots
- `[Add screenshot of Home page (/)]`
- `[Add screenshot of Explore Stays page (/stays/)]`
- `[Add screenshot of Stay Detail page (/stays/pinecone-ridge-a-frame-cabin/)]`
- `[Add screenshot of About & Contact page (/about/)]`
- `[Add screenshot of Login (/login/) and Sign Up (/signup/) pages]`

## 9. Known Limitations / Future Improvements
- **Local Development Secret Key:** `settings.py` reads `DJANGO_SECRET_KEY` from the environment with a local development fallback; set a strong environment secret and `DJANGO_DEBUG=False` before any public deployment.
- **Booking Inquiries:** Reservation requests are validated and saved to `BookingInquiry` in SQLite without live payment processing.
- **Future Enhancements:** User trip dashboard, host property submission form, and interactive map view.
