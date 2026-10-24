# Airbnb Stay Booking System

A web-based accommodation booking platform inspired by Airbnb, built using **Django and Python**.

The project aims to provide a simple and user-friendly platform for exploring properties, viewing accommodation details, and booking stays.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Django | Web framework |
| HTML, CSS, JavaScript | Frontend development |
| Django Templates | Dynamic page rendering |
| SQLite | Database |
| Git & GitHub | Version control |

## Project Structure

```text
airbnb_clone/
│
├── config/                 # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/               # User authentication
├── listings/               # Property listings
├── bookings/               # Stay reservations
│
├── templates/
│   ├── accounts/
│   ├── listings/
│   └── bookings/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                  # Uploaded images
├── venv/                   # Virtual environment (not tracked)
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <https://github.com/Aarush2112/airbnb-stay-booking>
cd <airbnb_clone>
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate the virtual environment:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

*Note: The project currently contains the initial Django structure. Application configuration and feature development are pending.*

## Planned Features

- User registration and authentication
- Property listings with images, descriptions, and prices
- Property search by location
- Detailed property pages
- Check-in and check-out date selection
- Stay booking and availability validation
- Booking history and management
- Responsive user interface
- Django admin panel

## Team Overview

| S. No. | Team Member | GitHub Profile |
|---|---|---|
| 1 | Aarush Gupta | [@Aarush2112](https://github.com/Aarush2112) |
| 2 | Sneha Gangwar | [@snehard06](https://github.com/snehard06) |
| 3 | Alok Rawat | [@alokr25012-lab](https://github.com/alokr25012-lab) |
| 4 | Tanvi | [@tanvia25087-prog](https://github.com/tanvia25087-prog) |
| 5 | Member 5 | [@username](https://github.com/username) |

## Development Progress

### Completed

- [x] Initialized Django project (`config`)
- [x] Created Django applications (`accounts`, `listings`, `bookings`)
- [x] Set up Python virtual environment
- [x] Installed Django and generated `requirements.txt`
- [x] Created templates, static, and media directories
- [x] Configured `settings.py` with installed apps and template/static directories
- [x] Configured main URL routing in `config/urls.py`
- [x] Created individual URL configurations for all three apps
- [x] Created a temporary homepage in `listings/views.py`
- [x] Successfully passed Django system checks using `python manage.py check`

### Upcoming

- [ ] Initialize SQLite database using `python manage.py migrate`
- [ ] Verify the homepage using `python manage.py runserver`
- [ ] Set up individual Git branches for team members
- [ ] Implement database models for properties and bookings
- [ ] Develop property listings and property detail pages
- [ ] Implement user registration, login, and logout
- [ ] Implement booking functionality and availability validation
- [ ] Develop responsive frontend templates and styling
- [ ] Integrate all modules
- [ ] Perform final testing and debugging