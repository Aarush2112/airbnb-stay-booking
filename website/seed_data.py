from django.db.utils import OperationalError
from .models import Stay

INITIAL_STAYS = [
    {
        'title': 'Pinecone Ridge A-Frame Cabin',
        'slug': 'pinecone-ridge-a-frame-cabin',
        'location': 'Manali, Himachal Pradesh',
        'category': 'cabins',
        'price_per_night': 145,
        'rating': '4.94',
        'review_count': 68,
        'max_guests': 4,
        'bedrooms': 2,
        'bathrooms': 1,
        'host_name': 'Aarav Mehta',
        'host_badge': 'Superhost',
        'image_filename': 'stay_cabin.png',
        'summary': 'Timber A-frame tucked inside cedar woods with a panoramic mountain deck.',
        'description': (
            'Wake up to misty pine valleys and floor-to-ceiling windows in this handcrafted A-frame cabin. '
            'Features a wood-burning fireplace, dedicated workspace, fast Wi-Fi, and a private cedar deck '
            'ideal for stargazing after mountain hikes.'
        ),
        'amenities': 'Mountain view, Fireplace, High-speed Wi-Fi, Full kitchen, Free parking, Private deck',
        'is_featured': True,
    },
    {
        'title': 'Sunlit Terracotta Coastal Villa',
        'slug': 'sunlit-terracotta-coastal-villa',
        'location': 'North Goa, India',
        'category': 'beachfront',
        'price_per_night': 210,
        'rating': '4.91',
        'review_count': 52,
        'max_guests': 6,
        'bedrooms': 3,
        'bathrooms': 3,
        'host_name': 'Maya Fernandes',
        'host_badge': 'Superhost',
        'image_filename': 'stay_beach.png',
        'summary': 'Breezy whitewashed villa steps from the Arabian Sea with an open terrace.',
        'description': (
            'Designed for slow coastal mornings, this sunlit villa pairs arched verandahs with direct beach access. '
            'Enjoy a shaded courtyard dining area, outdoor rain shower, and chef-ready kitchen.'
        ),
        'amenities': 'Beachfront access, Air conditioning, Outdoor shower, Wi-Fi, Courtyard dining, Washer',
        'is_featured': True,
    },
    {
        'title': 'Skyline Brick & Glass City Loft',
        'slug': 'skyline-brick-glass-city-loft',
        'location': 'Bandra West, Mumbai',
        'category': 'city',
        'price_per_night': 130,
        'rating': '4.88',
        'review_count': 91,
        'max_guests': 3,
        'bedrooms': 1,
        'bathrooms': 1,
        'host_name': 'Kabir Kapoor',
        'host_badge': 'Guest Favorite',
        'image_filename': 'stay_loft.png',
        'summary': 'Industrial-chic loft with double-height windows and walkable cafe culture.',
        'description': (
            'Flooded with natural light through steel-framed windows, this quiet urban loft sits minutes from '
            'artisan bakeries, galleries, and seaside promenades. Includes ergonomic desk setup and espresso bar.'
        ),
        'amenities': 'City skyline view, Dedicated workspace, Espresso machine, Smart TV, Elevator, Self check-in',
        'is_featured': True,
    },
    {
        'title': 'Meadowbrook Stone Cottage',
        'slug': 'meadowbrook-stone-cottage',
        'location': 'Coorg, Karnataka',
        'category': 'countryside',
        'price_per_night': 115,
        'rating': '4.96',
        'review_count': 44,
        'max_guests': 4,
        'bedrooms': 2,
        'bathrooms': 2,
        'host_name': 'Nandini Rao',
        'host_badge': 'Superhost',
        'image_filename': 'stay_countryside.png',
        'summary': 'Restored stone cottage surrounded by rolling coffee estates and mist.',
        'description': (
            'Set on four acres of private coffee and spice trails, Meadowbrook offers fresh estate-brewed coffee '
            'each morning, warm timber interiors, and quiet reading nooks overlooking green hills.'
        ),
        'amenities': 'Estate trails, Complimentary breakfast, Fireplace, Wi-Fi, Free parking, Garden patio',
        'is_featured': True,
    },
    {
        'title': 'Red Rock Adobe Desert Retreat',
        'slug': 'red-rock-adobe-desert-retreat',
        'location': 'Jaisalmer, Rajasthan',
        'category': 'desert',
        'price_per_night': 165,
        'rating': '4.89',
        'review_count': 37,
        'max_guests': 4,
        'bedrooms': 2,
        'bathrooms': 2,
        'host_name': 'Vikram Rathore',
        'host_badge': 'Superhost',
        'image_filename': 'stay_desert.png',
        'summary': 'Sun-baked sandstone retreat with rooftop stargazing lounge.',
        'description': (
            'Built with traditional cooling thick-wall architecture, this tranquil desert home opens onto golden '
            'dunes and crisp night skies. Unwind on the rooftop charpoy terrace at sunset.'
        ),
        'amenities': 'Desert horizon view, Rooftop lounge, Air conditioning, Local breakfast, Wi-Fi, Fire pit',
        'is_featured': True,
    },
    {
        'title': 'Mirror Lake Glass Tiny Home',
        'slug': 'mirror-lake-glass-tiny-home',
        'location': 'Nainital, Uttarakhand',
        'category': 'tiny-homes',
        'price_per_night': 95,
        'rating': '4.92',
        'review_count': 61,
        'max_guests': 2,
        'bedrooms': 1,
        'bathrooms': 1,
        'host_name': 'Rhea Sharma',
        'host_badge': 'Guest Favorite',
        'image_filename': 'stay_tinyhome.png',
        'summary': 'Minimalist lakeside tiny house with a private wooden dock.',
        'description': (
            'Designed for couples and solo writers, this compact glass-front tiny home sits right at the water edge. '
            'Launch a kayak from the private dock or brew tea while watching the lake mist lift.'
        ),
        'amenities': 'Lakefront dock, Kayaks included, Heating, Compact kitchen, Wi-Fi, Self check-in',
        'is_featured': True,
    },
    {
        'title': 'Emerald Canopy Treehouse',
        'slug': 'emerald-canopy-treehouse',
        'location': 'Wayanad, Kerala',
        'category': 'treehouses',
        'price_per_night': 155,
        'rating': '4.95',
        'review_count': 39,
        'max_guests': 2,
        'bedrooms': 1,
        'bathrooms': 1,
        'host_name': 'Devika Nair',
        'host_badge': 'Superhost',
        'image_filename': 'stay_treehouse.png',
        'summary': 'Elevated bamboo-and-teak sanctuary nestled in tropical rainforest.',
        'description': (
            'Perched twenty feet above the forest floor, Emerald Canopy surrounds you with birdsong and swaying '
            'banyan branches. Features a wraparound balcony and locally sourced organic breakfast.'
        ),
        'amenities': 'Rainforest canopy view, Wraparound balcony, Organic breakfast, Wi-Fi, Eco-friendly bath',
        'is_featured': False,
    },
    {
        'title': 'Aurora Ridge Nordic Chalet',
        'slug': 'aurora-ridge-nordic-chalet',
        'location': 'Gulmarg, Jammu & Kashmir',
        'category': 'chalets',
        'price_per_night': 240,
        'rating': '4.97',
        'review_count': 29,
        'max_guests': 6,
        'bedrooms': 3,
        'bathrooms': 2,
        'host_name': 'Zoya Mir',
        'host_badge': 'Superhost',
        'image_filename': 'stay_chalet.png',
        'summary': 'Ski-in alpine chalet with heated floors and cedar sauna.',
        'description': (
            'Step directly onto powdery slopes from this warm Nordic-inspired chalet. After a day outdoors, '
            'relax in the private cedar sauna or gather around the central stone hearth.'
        ),
        'amenities': 'Ski-in access, Cedar sauna, Heated floors, Fireplace, Full kitchen, Mountain view',
        'is_featured': False,
    },
]


def ensure_stays_seeded():
    """Populate initial stays on first run if database tables exist and are empty."""
    try:
        if Stay.objects.exists():
            return
        for item in INITIAL_STAYS:
            Stay.objects.get_or_create(slug=item['slug'], defaults=item)
    except OperationalError:
        # Database migrations have not been applied yet.
        return
