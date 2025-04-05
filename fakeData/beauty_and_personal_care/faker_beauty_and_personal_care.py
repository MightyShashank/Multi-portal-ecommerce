import json
import random
import uuid
from fakeData.electronics.faker_electronics import Faker

fake = Faker()
Faker.seed(42)

categories = {
    "beauty": [
        "skincare", "haircare", "makeup", "fragrances", "grooming-kits",
        "bath-body", "hair-styling", "manicure-pedicure", "shavers-trimmers", "sunscreen"
    ]
}

product_data = {
    "skincare": [
        ("HydraGlow Moisturizer", "GlowSkin", "SK-#####"),
        ("Vitamin C Serum", "DermaCare", "DC-#####"),
        ("Aloe Vera Gel", "Nature's Touch", "NT-#####"),
        ("Anti-Aging Night Cream", "Youthful Glow", "YG-#####"),
        ("Hyaluronic Acid Toner", "PureSkin", "PS-#####")
    ],
    "haircare": [
        ("Keratin Repair Shampoo", "HairEssence", "HE-#####"),
        ("Coconut Nourish Conditioner", "Herbal Luxe", "HL-#####"),
        ("Argan Oil Hair Serum", "SilkTress", "ST-#####"),
        ("Dandruff Control Shampoo", "Scalp Guard", "SG-#####"),
        ("Deep Conditioning Hair Mask", "ReviveLocks", "RL-#####")
    ],
    "makeup": [
        ("Long-Lasting Matte Lipstick", "GlamBeauty", "GB-#####"),
        ("Waterproof Eyeliner", "EyeDefine", "ED-#####"),
        ("HD Foundation", "FlawlessSkin", "FS-#####"),
        ("Velvet Touch Blush", "CheekGlow", "CG-#####"),
        ("Smoky Eyeshadow Palette", "BoldBeauty", "BB-#####")
    ],
    "fragrances": [
        ("Eau de Parfum - Midnight Mist", "LuxuryScents", "LS-#####"),
        ("Citrus Breeze Cologne", "FreshAura", "FA-#####"),
        ("Musk & Oud Perfume", "EliteAroma", "EA-#####"),
        ("Rose Vanilla Body Spray", "BlossomScent", "BS-#####"),
        ("Woody Amber Eau de Toilette", "ScentCraft", "SC-#####")
    ],
    "grooming-kits": [
        ("Men's Premium Grooming Kit", "GentlemanCare", "GC-#####"),
        ("Women's Self-Care Set", "GlowEssentials", "GE-#####"),
        ("Beard Grooming Combo", "BeardCraft", "BC-#####"),
        ("Facial Care Kit", "SmoothSkin", "SS-#####"),
        ("Travel Grooming Essentials", "OnTheGo", "OTG-#####")
    ],
    "bath-body": [
        ("Lavender Shower Gel", "AromaBath", "AB-#####"),
        ("Exfoliating Body Scrub", "SilkySkin", "SK-#####"),
        ("Moisturizing Body Lotion", "HydraGlow", "HG-#####"),
        ("Eucalyptus Bath Salts", "ZenSpa", "ZS-#####"),
        ("Aloe Vera Body Wash", "FreshCare", "FC-#####")
    ],
    "hair-styling": [
        ("Volumizing Hair Mousse", "StyleMax", "SM-#####"),
        ("Strong Hold Hair Gel", "FlexHold", "FH-#####"),
        ("Heat Protectant Spray", "ShieldHair", "SH-#####"),
        ("Smoothing Hair Cream", "SilkShine", "SS-#####"),
        ("Texturizing Hair Wax", "UrbanStyle", "US-#####")
    ],
    "manicure-pedicure": [
        ("Gel Nail Polish Set", "NailArtPro", "NAP-#####"),
        ("Cuticle Care Oil", "PureNails", "PN-#####"),
        ("Nail Strengthening Serum", "StrongTips", "ST-#####"),
        ("Foot Repair Cream", "SoftFeet", "SF-#####"),
        ("Complete Manicure Kit", "PerfectNails", "PN-#####")
    ],
    "shavers-trimmers": [
        ("Electric Beard Trimmer", "TrimTech", "TT-#####"),
        ("Rechargeable Hair Clipper", "ProGroom", "PG-#####"),
        ("Precision Eyebrow Shaper", "BrowPerfect", "BP-#####"),
        ("Body Hair Grooming Kit", "SmoothEdge", "SE-#####"),
        ("5-Blade Wet & Dry Shaver", "UltraShave", "US-#####")
    ],
    "sunscreen": [
        ("SPF 50+ Water-Resistant Sunscreen", "SunShield", "SS-#####"),
        ("Tinted Sunscreen with SPF 30", "GlowProtect", "GP-#####"),
        ("Matte Finish Sunblock", "UVGuard", "UVG-#####"),
        ("Aloe-Infused After-Sun Lotion", "CoolCare", "CC-#####"),
        ("Mineral Sunscreen for Sensitive Skin", "DermaSun", "DS-#####")
    ]
}

descriptions = {
    "skincare": [
        "A deeply hydrating moisturizer enriched with natural extracts to keep your skin soft and supple all day long.",
        "A powerful vitamin C serum that brightens your skin tone, reduces dark spots, and enhances your natural glow.",
        "A refreshing aloe vera gel that soothes and nourishes dry, irritated skin, leaving it cool and hydrated.",
        "An anti-aging night cream infused with retinol and peptides to reduce fine lines and boost collagen production.",
        "A lightweight hyaluronic acid toner that locks in moisture and revitalizes your skin’s natural radiance.",
        "A detoxifying charcoal face mask that clears pores, absorbs excess oil, and fights acne breakouts.",
        "A gentle exfoliating face scrub with natural fruit enzymes to remove dead skin cells and promote smoother skin.",
        "A soothing green tea face mist that refreshes and hydrates your skin instantly.",
        "A SPF 50+ sunblock that shields your skin from harmful UV rays while keeping it lightweight and non-greasy.",
        "A nourishing shea butter lip balm that keeps your lips hydrated and protected from harsh weather."
    ],
    "haircare": [
        "A keratin-infused shampoo designed to repair damaged hair and restore its natural shine and strength.",
        "A nourishing conditioner with coconut oil and shea butter to detangle and deeply hydrate dry, frizzy hair.",
        "An argan oil hair serum that smooths split ends, tames flyaways, and adds a silky finish to any hairstyle.",
        "A scalp-revitalizing shampoo that eliminates dandruff and provides long-lasting relief from itchiness and flaking.",
        "A deep conditioning hair mask that repairs, strengthens, and protects hair from heat and environmental damage.",
        "A biotin-rich hair growth tonic that strengthens roots and promotes thicker, healthier hair.",
        "A sulfate-free color-protect shampoo that extends the vibrancy of dyed hair while preventing damage.",
        "A lightweight leave-in conditioner that hydrates, detangles, and protects hair throughout the day.",
        "A caffeine-infused scalp serum that energizes hair follicles and reduces hair fall.",
        "A volumizing dry shampoo that absorbs excess oil and instantly refreshes your hair without washing."
    ],
    "makeup": [
        "A long-lasting matte lipstick with rich pigmentation that stays vibrant and smudge-free for hours.",
        "A waterproof eyeliner that glides on smoothly, delivering intense color and a sharp, defined look.",
        "A high-coverage HD foundation that provides a flawless, airbrushed finish with a lightweight feel.",
        "A soft, blendable blush that adds a natural flush of color to your cheeks for a fresh, radiant look.",
        "A versatile eyeshadow palette with highly pigmented shades for creating bold and glamorous eye looks.",
        "A silky-smooth makeup primer that blurs pores and extends the wear of your foundation.",
        "A creamy concealer that covers blemishes, dark circles, and redness without creasing.",
        "A volumizing mascara that enhances lash length, curl, and definition for a dramatic eye effect.",
        "A setting spray that locks in makeup for all-day wear while providing a dewy or matte finish.",
        "A color-changing lip gloss that reacts to your skin’s pH for a custom shade."
    ],
    "fragrances": [
        "A luxurious eau de parfum with a captivating blend of floral, woody, and musky notes for a timeless appeal.",
        "A fresh citrus cologne that energizes your senses with zesty lemon, bergamot, and orange peel aromas.",
        "A rich musk and oud perfume that exudes sophistication and lingers on the skin for long-lasting wear.",
        "A delicate rose vanilla body spray that offers a sweet, romantic fragrance perfect for everyday use.",
        "A bold and charismatic woody amber eau de toilette that leaves a lasting impression wherever you go.",
        "A soft lavender and sandalwood mist that provides a calming and stress-relieving scent.",
        "A fresh ocean breeze fragrance that embodies the essence of summer and adventure.",
        "A spicy cinnamon and patchouli blend that delivers an exotic and mysterious allure.",
        "A gourmand perfume featuring notes of caramel, chocolate, and vanilla for a sweet indulgence.",
        "A floral jasmine and lily fragrance that is fresh, feminine, and beautifully delicate."
    ],
    "grooming-kits": [
        "A premium men’s grooming kit featuring a razor, beard oil, trimmer, and aftershave for a polished look.",
        "A women’s self-care set with skincare essentials, a jade roller, and a nourishing face mask for relaxation.",
        "A complete beard grooming combo with precision trimmers, beard balm, and a boar-bristle brush.",
        "A professional facial care kit containing a cleansing brush, serum, and hydrating sheet masks.",
        "A compact travel grooming essentials kit with mini-sized products for effortless on-the-go grooming.",
        "A multi-purpose shaving and grooming set with ergonomic razor, shaving cream, and pre-shave oil.",
        "A nail care and pedicure set with stainless steel tools for salon-like results at home.",
        "A body grooming kit with precision attachments for shaving and trimming different areas with ease.",
        "A deluxe bath and spa set with essential oils, body butter, and exfoliating scrubs for a relaxing experience.",
        "An electric hair removal kit with different attachments for a smooth and pain-free experience."
    ],
    "bath-body": [
        "A soothing lavender shower gel enriched with essential oils to refresh and relax your senses.",
        "An exfoliating body scrub that removes dead skin cells, revealing smooth, radiant skin underneath.",
        "A deeply moisturizing body lotion infused with shea butter and vitamin E for long-lasting hydration.",
        "A luxurious eucalyptus bath salt blend designed to detoxify and soothe tired muscles after a long day.",
        "A gentle aloe vera body wash that cleanses and nourishes the skin while maintaining its natural moisture.",
        "A foaming bath soak with chamomile and honey to provide a spa-like relaxation experience.",
        "A body butter with cocoa and almond oil that deeply hydrates and softens dry, flaky skin.",
        "A cooling menthol-infused foot soak that relieves soreness and refreshes tired feet.",
        "A fresh cucumber and mint body spray that keeps you feeling revitalized all day long.",
        "A 3-in-1 body wash, shampoo, and conditioner combo for a quick and effective cleansing routine."
    ],
    "hair-styling": [
        "A volumizing hair mousse that adds body and lift for a fuller, more voluminous hairstyle.",
        "A strong-hold hair gel that keeps your style in place all day without stiffness or flaking.",
        "A heat protectant spray that shields hair from heat damage while enhancing shine and smoothness.",
        "A smoothing hair cream that tames frizz and provides a sleek, polished finish for any hairstyle.",
        "A texturizing hair wax that adds definition and a matte finish for a trendy, effortlessly cool look.",
        "A curl-enhancing cream that defines curls and reduces frizz for a natural, bouncy style.",
        "A salt spray for effortless beach waves with a lightweight, touchable texture.",
        "A fast-drying hairspray that provides long-lasting hold without stickiness.",
        "A root-lifting spray that boosts volume at the scalp for fuller-looking hair.",
        "A shine-boosting serum that adds a silky, polished finish to any hairstyle."
    ],
    "manicure-pedicure": [
        "A vibrant gel nail polish set with long-lasting, chip-resistant shades for a flawless manicure.",
        "A nourishing cuticle care oil that strengthens nails and promotes healthy growth.",
        "A nail strengthening serum that repairs brittle nails and prevents splitting and breakage.",
        "A hydrating foot repair cream that softens rough, dry feet for a smooth, baby-soft feel.",
        "A complete manicure kit with professional tools for shaping, buffing, and perfecting your nails.",
        "A long-wearing top coat that adds shine and extends the life of your manicure.",
        "A foot scrub infused with peppermint and tea tree oil to refresh and exfoliate feet.",
        "A fast-drying nail polish remover that removes color without drying out nails.",
        "A dip powder nail system for long-lasting, salon-quality nails at home.",
        "A nail art stamping kit for creating unique, intricate designs effortlessly."
    ],
    "shavers-trimmers": [
        "A precision electric shaver with ultra-sharp blades for a smooth, close shave with minimal irritation.",
        "A high-performance beard trimmer with multiple length settings for a customized grooming experience.",
        "A waterproof electric razor designed for both wet and dry shaving, ensuring versatility and comfort.",
        "A cordless body groomer with advanced skin protection technology for safe and effortless trimming.",
        "A professional-grade hair clipper with self-sharpening blades and a powerful motor for barbershop-quality results.",
        "A compact travel-friendly trimmer with USB charging and an ergonomic design for on-the-go grooming.",
        "An advanced multi-grooming kit with attachments for beard, nose, ear, and body hair trimming.",
        "A hypoallergenic foil shaver with dual cutting elements for a close shave without skin irritation.",
        "A fast-charging beard and mustache trimmer with a long-lasting battery for extended use.",
        "A 5-in-1 grooming tool featuring a precision trimmer, shaver, detailer, and body groomer in one."
    ],
    "sunscreen": [
        "A lightweight SPF 50+ sunscreen that provides broad-spectrum protection without leaving a greasy residue.",
        "A water-resistant mineral sunscreen infused with zinc oxide for sensitive skin and long-lasting defense.",
        "A tinted sunscreen that offers sun protection while evening out skin tone for a natural, radiant look.",
        "An oil-free sunscreen gel with quick absorption, ideal for oily and acne-prone skin types.",
        "A daily moisturizing sunscreen with aloe vera and vitamin E to nourish and protect your skin.",
        "A sweat-resistant sports sunscreen that stays effective even during intense physical activity.",
        "A reef-safe sunscreen lotion formulated without harmful chemicals to protect both skin and marine life.",
        "A dual-action sunscreen and primer that preps your skin for makeup while shielding it from UV rays.",
        "A high-SPF sunscreen mist that offers easy, mess-free application for full-body sun protection.",
        "A hydrating after-sun lotion with aloe and cucumber to soothe sun-exposed skin and reduce redness."
    ]
}

features = {
    "skincare": {
        "Ingredients": ["Hyaluronic acid", "Vitamin C", "Retinol", "Niacinamide", "Salicylic acid"],
        "Skin Type": ["Oily", "Dry", "Combination", "Sensitive", "Normal"],
        "Texture": ["Gel", "Cream", "Serum", "Lotion", "Foam"],
        "Benefits": ["Hydration", "Anti-aging", "Brightening", "Acne control", "UV protection"],
        "Application": ["Daily use", "Night treatment", "Spot treatment", "Exfoliation", "Mask"]
    },
    
    "haircare": {
        "Hair Type": ["Straight", "Curly", "Wavy", "Coily", "Damaged"],
        "Key Ingredients": ["Argan oil", "Keratin", "Biotin", "Tea tree oil", "Coconut oil"],
        "Shampoo Benefits": ["Volumizing", "Moisturizing", "Dandruff control", "Hair fall reduction", "Color protection"],
        "Conditioner Benefits": ["Deep conditioning", "Frizz control", "Shine enhancement", "Heat protection", "Detangling"],
        "Treatment Types": ["Hair masks", "Serums", "Scalp treatments", "Leave-in conditioners", "Hair oils"]
    },

    "makeup": {
        "Product Type": ["Foundation", "Concealer", "Blush", "Eyeshadow", "Lipstick"],
        "Finish": ["Matte", "Dewy", "Satin", "Glowy", "Sheer"],
        "Coverage": ["Full", "Medium", "Light", "Buildable", "Tinted"],
        "Skin Type": ["Oily", "Dry", "Combination", "Sensitive", "Normal"],
        "Longevity": ["Long-wearing", "Waterproof", "Transfer-proof", "Sweat-resistant", "Smudge-proof"],
        "Formulation": ["Liquid", "Powder", "Cream", "Stick", "Gel"]
    },

    "fragrances": {
        "Fragrance Type": ["Eau de Parfum", "Eau de Toilette", "Eau de Cologne", "Body Mist", "Perfume Oil"],
        "Notes": ["Floral", "Woody", "Citrus", "Spicy", "Musky"],
        "Longevity": ["Long-lasting", "Moderate", "Light", "Daywear", "Nightwear"],
        "Occasion": ["Casual", "Formal", "Romantic", "Sporty", "Luxury"],
        "Bottle Size": ["30ml", "50ml", "75ml", "100ml", "150ml"]
    },

    "grooming-kits": {
        "Kit Includes": ["Trimmer", "Razor", "Shaving cream", "Aftershave", "Scissors"],
        "Usage": ["Beard grooming", "Hair trimming", "Body grooming", "Shaving", "Multi-purpose"],
        "Blade Material": ["Stainless steel", "Titanium-coated", "Ceramic", "Self-sharpening"],
        "Power Source": ["Cordless", "Rechargeable", "Battery-operated", "USB charging", "Plug-in"],
        "Accessories": ["Adjustable combs", "Cleaning brush", "Travel pouch", "Precision trimmer", "Lubricating oil"]
    },

    "bath-body": {
        "Product Type": ["Body wash", "Shower gel", "Bath salts", "Body scrub", "Body butter"],
        "Skin Benefits": ["Moisturizing", "Exfoliating", "Soothing", "Brightening", "Refreshing"],
        "Key Ingredients": ["Shea butter", "Aloe vera", "Essential oils", "Coconut milk", "Eucalyptus"],
        "Texture": ["Creamy", "Gel-based", "Foamy", "Scrub", "Oil-based"],
        "Scent Options": ["Floral", "Citrus", "Woody", "Fruity", "Unscented"]
    },

    "hair-styling": {
        "Styling Tools": ["Hair dryer", "Straightener", "Curling iron", "Hot brush", "Crimper"],
        "Heat Settings": ["Low", "Medium", "High", "Adjustable", "Cool shot"],
        "Coating": ["Ceramic", "Tourmaline", "Titanium", "Ionic", "Infrared"],
        "Hair Types": ["Fine", "Thick", "Curly", "Straight", "Frizzy"],
        "Additional Features": ["Auto shut-off", "Fast heating", "Dual voltage", "Wireless", "Salon-grade"]
    },

    "manicure-pedicure": {
        "Kit Includes": ["Nail clippers", "Cuticle pusher", "Nail file", "Buffing block", "Cuticle oil"],
        "Nail Polish Type": ["Gel", "Matte", "Glossy", "Quick-dry", "Peel-off"],
        "Nail Length": ["Short", "Medium", "Long", "Acrylic extensions", "Natural"],
        "Special Features": ["Chip-resistant", "Fast-drying", "Vegan", "Nail strengthening", "Long-lasting"],
        "Professional Use": ["Salon-grade tools", "Home use", "UV curing required", "Manicure & pedicure combo", "Portable kit"]
    },

    "shavers-trimmers": {
        "Blade Type": ["Foil", "Rotary", "Hybrid", "Double-edge", "Self-sharpening"],
        "Power Source": ["Battery-powered", "Cordless", "Rechargeable", "USB charging", "Wired"],
        "Wet & Dry Use": ["Shower-safe", "Dry shave only", "Foam-compatible", "Waterproof", "Rinseable"],
        "Attachments": ["Precision trimmer", "Adjustable comb", "Beard shaping tool", "Ear & nose trimmer", "Detail trimmer"],
        "Motor Type": ["High-speed", "Low-noise", "Turbo mode", "Dual-cut technology", "Linear motor"]
    },

    "sunscreen": {
        "SPF Level": ["SPF 15", "SPF 30", "SPF 50", "SPF 60", "SPF 100"],
        "Skin Type": ["Oily", "Dry", "Sensitive", "Combination", "Normal"],
        "Formulation": ["Cream", "Gel", "Spray", "Tinted", "Stick"],
        "Water Resistance": ["Not water-resistant", "Water-resistant (40 min)", "Very water-resistant (80 min)", "Sweat-proof", "Long-lasting"],
        "Key Ingredients": ["Zinc oxide", "Titanium dioxide", "Aloe vera", "Vitamin E", "Green tea extract"]
    }
}


sellers = [{
    "seller_id": str(uuid.uuid4()),
    "store_name": fake.company(),
    "location": fake.city()
} for _ in range(10)]


def generate_fake_product(category, subcategory):
    name, brand, model_pattern = random.choice(product_data[subcategory])
    seller = random.choice(sellers)
    model_number = fake.bothify(text=model_pattern)

    stock = random.randint(0, 100)
    status = "Out of Stock" if stock == 0 else "In Stock"

    # Descriptions: Pick a random number of descriptions from the subcategory in descriptions
    product_descriptions = descriptions.get(subcategory, [])
    selected_descriptions = random.sample(product_descriptions, k=random.randint(1, len(product_descriptions)))

   # Get features for the selected subcategory
    product_features = features.get(subcategory, {})
    selected_features = {}

    # Iterate through each feature category and pick one random feature from the list
    for feature_category, feature_list in product_features.items():
        selected_features[feature_category] = random.choice(feature_list)  # Pick one feature randomly
        
    return {
        "id": str(uuid.uuid4()),
        "name": name,
        "description": " ".join(selected_descriptions),  # Join all selected descriptions
        "brand": brand,
        "model_number": model_number,
        "category": category,
        "sub-category": subcategory,
        "identifiers": {
            "sku": fake.bothify(text="SKU-#####"),
            "upc": fake.ean(length=13),
            "ean": fake.ean(length=8),
            "isbn": None
        },
        "price": {
            "amount": round(random.uniform(50, 3000), 2),
            "currency": "USD"
        },
        "availability": {
            "stock": stock,
            "status": status,
            "restock_date": fake.date_time_this_year().isoformat() if stock == 0 else None
        },
        "rating": {
            "average": round(random.uniform(1, 5), 1),
            "number_of_reviews": random.randint(0, 5000)
        },
        "dimensions": {
            "height_cm": round(random.uniform(5, 50), 2),
            "width_cm": round(random.uniform(5, 50), 2),
            "depth_cm": round(random.uniform(1, 20), 2),
            "weight_kg": round(random.uniform(0.1, 5), 2)
        },
        "colors": random.sample(["Black", "White", "Silver", "Blue", "Red", "Gold"], k=3),
        "features": selected_features,  # Directly use the selected features
        "images": [{"url": fake.image_url(), "alt_text": name + " product image"} for _ in range(3)],
        "seller": seller
    }

##########################

dataset = []
for category, subcategories in categories.items():
    for subcategory in subcategories:
        dataset.extend([generate_fake_product(category, subcategory) for _ in range(50)])  # 50 products per subcategory

with open("fake_products_beauty_and_personal_care.json", "w") as f:
    json.dump(dataset, f, indent=4)

print("Fake product dataset with 500 products generated successfully!")
