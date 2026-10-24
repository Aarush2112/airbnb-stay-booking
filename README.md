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
| Pillow | Image handling |
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
git clone <repository-url>
cd <repository-folder>
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

- [x] Initialized Django project
- [x] Created `accounts`, `listings`, and `bookings` apps
- [x] Set up the Python virtual environment
- [x] Installed project dependencies
- [x] Created templates and static directories
- [x] Generated `requirements.txt`

### Upcoming

- [ ] Configure Django settings and URL routing
- [ ] Implement database models
- [ ] Develop property listing pages
- [ ] Implement user authentication
- [ ] Develop booking functionality
- [ ] Integrate frontend and backend
- [ ] Test and finalize the application