from django.contrib import admin
from .models import BookingInquiry, ContactMessage, Stay


@admin.register(Stay)
class StayAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'category', 'price_per_night', 'rating', 'is_featured')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'location', 'host_name')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(BookingInquiry)
class BookingInquiryAdmin(admin.ModelAdmin):
    list_display = ('stay', 'guest_name', 'guest_email', 'check_in', 'check_out', 'guests', 'created_at')
    list_filter = ('check_in',)
    search_fields = ('guest_name', 'guest_email', 'stay__title')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at')
    search_fields = ('name', 'email', 'subject')
