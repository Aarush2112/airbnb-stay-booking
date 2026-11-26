from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=180)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Stay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=160, unique=True)),
                ('location', models.CharField(max_length=150)),
                ('category', models.CharField(choices=[
                    ('cabins', 'Cabins'),
                    ('beachfront', 'Beachfront'),
                    ('city', 'City Lofts'),
                    ('countryside', 'Countryside'),
                    ('desert', 'Desert'),
                    ('tiny-homes', 'Tiny Homes'),
                    ('treehouses', 'Treehouses'),
                    ('chalets', 'Chalets'),
                ], max_length=40)),
                ('price_per_night', models.PositiveIntegerField()),
                ('rating', models.DecimalField(decimal_places=2, default=4.85, max_digits=3)),
                ('review_count', models.PositiveIntegerField(default=24)),
                ('max_guests', models.PositiveSmallIntegerField(default=4)),
                ('bedrooms', models.PositiveSmallIntegerField(default=2)),
                ('bathrooms', models.PositiveSmallIntegerField(default=1)),
                ('host_name', models.CharField(max_length=80)),
                ('host_badge', models.CharField(default='Superhost', max_length=40)),
                ('image_filename', models.CharField(max_length=120)),
                ('summary', models.CharField(max_length=240)),
                ('description', models.TextField()),
                ('amenities', models.CharField(help_text='Comma-separated list of amenities', max_length=400)),
                ('is_featured', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-is_featured', 'title'],
            },
        ),
        migrations.CreateModel(
            name='BookingInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=120)),
                ('guest_email', models.EmailField(max_length=254)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('guests', models.PositiveSmallIntegerField(default=2)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('stay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquiries', to='website.stay')),
            ],
            options={
                'verbose_name_plural': 'Booking inquiries',
                'ordering': ['-created_at'],
            },
        ),
    ]
