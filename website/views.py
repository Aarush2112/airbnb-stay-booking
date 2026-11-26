from datetime import date
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import BookingInquiry, ContactMessage, Stay
from .seed_data import ensure_stays_seeded


CATEGORY_META = [
    ('all', 'All Stays'),
    ('cabins', 'Cabins'),
    ('beachfront', 'Beachfront'),
    ('city', 'City Lofts'),
    ('countryside', 'Countryside'),
    ('desert', 'Desert'),
    ('tiny-homes', 'Tiny Homes'),
    ('treehouses', 'Treehouses'),
    ('chalets', 'Chalets'),
]


def home(request):
    ensure_stays_seeded()
    featured_stays = Stay.objects.filter(is_featured=True)[:6]
    return render(request, 'website/home.html', {
        'featured_stays': featured_stays,
        'categories': CATEGORY_META,
    })


def stays(request):
    ensure_stays_seeded()
    active_category = request.GET.get('category', 'all').strip()
    query = request.GET.get('q', '').strip()

    queryset = Stay.objects.all()
    if active_category and active_category != 'all':
        queryset = queryset.filter(category=active_category)
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)
            | Q(location__icontains=query)
            | Q(summary__icontains=query)
            | Q(category__icontains=query)
        )

    return render(request, 'website/stays.html', {
        'stays': queryset,
        'categories': CATEGORY_META,
        'active_category': active_category,
        'query': query,
    })


def stay_detail(request, slug):
    ensure_stays_seeded()
    stay = get_object_or_404(Stay, slug=slug)
    related_stays = Stay.objects.exclude(pk=stay.pk)[:3]

    form_data = {
        'guest_name': request.user.get_full_name() or request.user.username if request.user.is_authenticated else '',
        'guest_email': request.user.email if request.user.is_authenticated else '',
        'check_in': '',
        'check_out': '',
        'guests': '2',
        'notes': '',
    }

    if request.method == 'POST':
        form_data = {
            'guest_name': request.POST.get('guest_name', '').strip(),
            'guest_email': request.POST.get('guest_email', '').strip(),
            'check_in': request.POST.get('check_in', '').strip(),
            'check_out': request.POST.get('check_out', '').strip(),
            'guests': request.POST.get('guests', '1').strip(),
            'notes': request.POST.get('notes', '').strip(),
        }

        errors = []
        if not form_data['guest_name']:
            errors.append('Please enter your full name.')
        if not form_data['guest_email']:
            errors.append('Please enter a valid email address.')
        else:
            try:
                validate_email(form_data['guest_email'])
            except ValidationError:
                errors.append('Please enter a valid email address.')

        check_in_date = None
        check_out_date = None
        try:
            check_in_date = date.fromisoformat(form_data['check_in'])
            check_out_date = date.fromisoformat(form_data['check_out'])
            if check_out_date <= check_in_date:
                errors.append('Check-out date must be after check-in date.')
        except ValueError:
            errors.append('Please provide valid check-in and check-out dates.')

        try:
            guest_count = int(form_data['guests'])
            if guest_count < 1 or guest_count > stay.max_guests:
                errors.append(f'Guests must be between 1 and {stay.max_guests}.')
        except ValueError:
            guest_count = 1
            errors.append('Please enter a valid number of guests.')

        if errors:
            for err in errors:
                messages.error(request, err)
        else:
            nights = (check_out_date - check_in_date).days
            total_estimate = nights * stay.price_per_night
            BookingInquiry.objects.create(
                stay=stay,
                guest_name=form_data['guest_name'],
                guest_email=form_data['guest_email'],
                check_in=check_in_date,
                check_out=check_out_date,
                guests=guest_count,
                notes=form_data['notes'],
            )
            messages.success(
                request,
                f'Reservation request sent to {stay.host_name} for {nights} night(s) '
                f'(estimated ${total_estimate}).',
            )
            return redirect('website:stay_detail', slug=stay.slug)

    return render(request, 'website/stay_detail.html', {
        'stay': stay,
        'related_stays': related_stays,
        'form_data': form_data,
    })


def about(request):
    form_data = {'name': '', 'email': '', 'subject': '', 'message': ''}

    if request.method == 'POST':
        form_data = {
            'name': request.POST.get('name', '').strip(),
            'email': request.POST.get('email', '').strip(),
            'subject': request.POST.get('subject', '').strip(),
            'message': request.POST.get('message', '').strip(),
        }

        errors = []
        if not form_data['name']:
            errors.append('Name is required.')
        if not form_data['email']:
            errors.append('Email is required.')
        else:
            try:
                validate_email(form_data['email'])
            except ValidationError:
                errors.append('Please enter a valid email address.')
        if not form_data['subject']:
            errors.append('Subject is required.')
        if not form_data['message']:
            errors.append('Please enter your message.')

        if errors:
            for err in errors:
                messages.error(request, err)
        else:
            ContactMessage.objects.create(**form_data)
            messages.success(request, 'Thank you! Your message has been received by the StayVista support team.')
            return redirect('website:about')

    return render(request, 'website/about.html', {'form_data': form_data})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('website:home')

    identifier = ''
    if request.method == 'POST':
        identifier = request.POST.get('identifier', '').strip()
        password = request.POST.get('password', '')

        if not identifier or not password:
            messages.error(request, 'Please enter both your username/email and password.')
        else:
            username_to_auth = identifier
            if '@' in identifier:
                matched_user = User.objects.filter(email__iexact=identifier).first()
                if matched_user:
                    username_to_auth = matched_user.username

            user = authenticate(request, username=username_to_auth, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                next_url = request.GET.get('next')
                if next_url and next_url.startswith('/'):
                    return redirect(next_url)
                return redirect('website:home')
            messages.error(request, 'Invalid username/email or password. Please try again.')

    return render(request, 'website/login.html', {'identifier': identifier})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('website:home')

    form_data = {'full_name': '', 'username': '', 'email': ''}

    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        form_data = {'full_name': full_name, 'username': username, 'email': email}
        errors = []

        if not full_name:
            errors.append('Full name is required.')
        if not username:
            errors.append('Username is required.')
        elif User.objects.filter(username__iexact=username).exists():
            errors.append('That username is already taken.')

        if not email:
            errors.append('Email address is required.')
        else:
            try:
                validate_email(email)
                if User.objects.filter(email__iexact=email).exists():
                    errors.append('An account with this email already exists.')
            except ValidationError:
                errors.append('Please enter a valid email address.')

        if not password or len(password) < 8:
            errors.append('Password must be at least 8 characters long.')
        elif password != confirm_password:
            errors.append('Password and Confirm Password do not match.')

        if errors:
            for err in errors:
                messages.error(request, err)
        else:
            name_parts = full_name.split(None, 1)
            first_name = name_parts[0]
            last_name = name_parts[1] if len(name_parts) > 1 else ''
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            login(request, user)
            messages.success(request, f'Account created! Welcome to StayVista, {first_name}.')
            return redirect('website:home')

    return render(request, 'website/signup.html', {'form_data': form_data})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'You have been logged out.')
    else:
        logout(request)
        messages.info(request, 'You have been logged out.')
    return redirect('website:home')
