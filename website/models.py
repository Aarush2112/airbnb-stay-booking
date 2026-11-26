from django.db import models


class Stay(models.Model):
    CATEGORY_CHOICES = [
        ('cabins', 'Cabins'),
        ('beachfront', 'Beachfront'),
        ('city', 'City Lofts'),
        ('countryside', 'Countryside'),
        ('desert', 'Desert'),
        ('tiny-homes', 'Tiny Homes'),
        ('treehouses', 'Treehouses'),
        ('chalets', 'Chalets'),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True)
    location = models.CharField(max_length=150)
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES)
    price_per_night = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=4.85)
    review_count = models.PositiveIntegerField(default=24)
    max_guests = models.PositiveSmallIntegerField(default=4)
    bedrooms = models.PositiveSmallIntegerField(default=2)
    bathrooms = models.PositiveSmallIntegerField(default=1)
    host_name = models.CharField(max_length=80)
    host_badge = models.CharField(max_length=40, default='Superhost')
    image_filename = models.CharField(max_length=120)
    summary = models.CharField(max_length=240)
    description = models.TextField()
    amenities = models.CharField(
        max_length=400,
        help_text='Comma-separated list of amenities',
    )
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', 'title']

    def __str__(self):
        return f'{self.title} ({self.location})'

    def amenity_list(self):
        return [item.strip() for item in self.amenities.split(',') if item.strip()]


class BookingInquiry(models.Model):
    stay = models.ForeignKey(Stay, on_delete=models.CASCADE, related_name='inquiries')
    guest_name = models.CharField(max_length=120)
    guest_email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveSmallIntegerField(default=2)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Booking inquiries'

    def __str__(self):
        return f'{self.guest_name} -> {self.stay.title} ({self.check_in} to {self.check_out})'


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.subject} ({self.email})'
