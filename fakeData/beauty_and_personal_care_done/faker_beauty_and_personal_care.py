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
        ("HydraGlow Moisturizer", "GlowSkin", "SK-00001"),
        ("Vitamin C Serum", "DermaCare", "DC-00002"),
        ("Aloe Vera Gel", "Nature's Touch", "NT-00003"),
        ("Anti-Aging Night Cream", "Youthful Glow", "YG-00004"),
        ("Hyaluronic Acid Toner", "PureSkin", "PS-00005"),
        ("Tea Tree Foaming Face Wash", "GreenBotanica", "GB-00006"),
        ("Retinol 1% Serum", "DermaCare", "DC-00007"),
        ("Oil-Free Daily Moisturizer", "SkinFix", "SF-00008"),
        ("Rosewater Facial Mist", "Blossom & Dew", "BD-00009"),
        ("SPF 50 Sunscreen Gel", "SunDefend", "SD-00010"),
        ("Collagen Boosting Cream", "Youthful Glow", "YG-00011"),
        ("Niacinamide 10% Serum", "GlowSkin", "SK-00012"),
        ("Brightening Face Mask", "DermaLite", "DL-00013"),
        ("Deep Clean Clay Mask", "Nature's Touch", "NT-00014"),
        ("Micellar Cleansing Water", "AquaGlow", "AG-00015"),
        ("Charcoal Detox Scrub", "UrbanSkin", "US-00016"),
        ("Hydrating Night Mask", "MoonEssence", "ME-00017"),
        ("Salicylic Acid Cleanser", "DermaCare", "DC-00018"),
        ("Green Tea Toner", "LeafyCare", "LC-00019"),
        ("Under Eye Gel", "GlowSkin", "SK-00020"),
        ("Squalane Moisturizer", "PureSkin", "PS-00021"),
        ("Caffeine Eye Cream", "Awake Beauty", "AB-00022"),
        ("Exfoliating Face Pads", "DailyPeel", "DP-00023"),
        ("AHA BHA Peeling Solution", "SkinLab", "SL-00024"),
        ("Barrier Repair Cream", "DermaRestore", "DR-00025"),
        ("Ceramide Face Lotion", "HydraEssence", "HE-00026"),
        ("Rice Water Bright Foam", "Oriental Glow", "OG-00027"),
        ("Vitamin E Night Oil", "Nature's Touch", "NT-00028"),
        ("Botanical Day Cream", "FloraSkin", "FS-00029"),
        ("Matte Finish Moisturizer", "UrbanSkin", "US-00030"),
        ("Peptide Infused Cream", "GlowSkin", "SK-00031"),
        ("Anti-Pollution Gel", "SkinFix", "SF-00032"),
        ("Chamomile Soothing Toner", "HerbalMist", "HM-00033"),
        ("Hydrating Gel Cleanser", "DermaCare", "DC-00034"),
        ("Licorice Root Brightening Serum", "GlowAlchemy", "GA-00035"),
        ("Vitamin B5 Hydration Booster", "PureSkin", "PS-00036"),
        ("Shea Butter Hand Cream", "Nature's Touch", "NT-00037"),
        ("Rosehip Oil", "Botaniq", "BQ-00038"),
        ("Daily Facial Sunscreen SPF 30", "SunDefend", "SD-00039"),
        ("Lavender Night Balm", "MoonEssence", "ME-00040"),
        ("Probiotic Face Cream", "SkinSymmetry", "SS-00041"),
        ("Hemp Seed Facial Oil", "EarthKind", "EK-00042"),
        ("Multivitamin Skin Elixir", "VitaDerm", "VD-00043"),
        ("Deep Hydration Sleeping Pack", "HydraGlow", "HG-00044"),
        ("Oatmeal Soothing Cream", "GentleSkin", "GS-00045"),
        ("Pore Minimizing Serum", "GlowSkin", "SK-00046"),
        ("Blue Light Shield Cream", "UrbanSkin", "US-00047"),
        ("Watermelon Gel Moisturizer", "FreshFruit", "FF-00048"),
        ("Cica Recovery Cream", "SkinRepair", "SR-00049"),
        ("Enzyme Peeling Mask", "FruitFusion", "FF-00050")
    ],
        "haircare": [
        ("Keratin Repair Shampoo", "HairEssence", "HE-00001"),
        ("Coconut Nourish Conditioner", "Herbal Luxe", "HL-00002"),
        ("Argan Oil Hair Serum", "SilkTress", "ST-00003"),
        ("Dandruff Control Shampoo", "Scalp Guard", "SG-00004"),
        ("Deep Conditioning Hair Mask", "ReviveLocks", "RL-00005"),
        ("Biotin Boost Shampoo", "HairEssence", "HE-00006"),
        ("Tea Tree Scalp Treatment", "Herbal Luxe", "HL-00007"),
        ("Keratin Infused Conditioner", "SilkTress", "ST-00008"),
        ("Clarifying Apple Cider Rinse", "Scalp Guard", "SG-00009"),
        ("Protein Repair Hair Mask", "ReviveLocks", "RL-00010"),
        ("Volumizing Dry Shampoo", "AirBounce", "AB-00011"),
        ("Anti-Frizz Hair Cream", "TameTress", "TT-00012"),
        ("Leave-In Hair Detangler", "SilkTress", "ST-00013"),
        ("Caffeine Scalp Energizer", "RootRevive", "RR-00014"),
        ("Color Protect Shampoo", "HairEssence", "HE-00015"),
        ("Avocado Deep Repair Mask", "Herbal Luxe", "HL-00016"),
        ("Argan Curl Enhancer", "SilkTress", "ST-00017"),
        ("Dandruff Defense Conditioner", "Scalp Guard", "SG-00018"),
        ("Rosemary Hair Growth Oil", "ReviveLocks", "RL-00019"),
        ("Shine & Gloss Hair Spray", "GlamTress", "GT-00020"),
        ("Heat Protectant Mist", "TameTress", "TT-00021"),
        ("Keratin Smoothing Serum", "SilkTress", "ST-00022"),
        ("Thickening Shampoo", "HairEssence", "HE-00023"),
        ("Silk Protein Conditioner", "Herbal Luxe", "HL-00024"),
        ("Amla Strengthening Oil", "NatureLocks", "NL-00025"),
        ("Split End Repair Cream", "TameTress", "TT-00026"),
        ("Moisture Retention Hair Butter", "ReviveLocks", "RL-00027"),
        ("Chamomile Blonde Brightener", "GoldenStrand", "GS-00028"),
        ("Peppermint Cooling Conditioner", "Herbal Luxe", "HL-00029"),
        ("Volumizing Root Lifter", "AirBounce", "AB-00030"),
        ("Detoxifying Charcoal Shampoo", "Scalp Guard", "SG-00031"),
        ("Hydrating Aloe Conditioner", "HairEssence", "HE-00032"),
        ("Silk Therapy Leave-In Spray", "SilkTress", "ST-00033"),
        ("Hair Growth Stimulating Serum", "RootRevive", "RR-00034"),
        ("UV Protect Hair Mist", "TameTress", "TT-00035"),
        ("Reparative Overnight Hair Mask", "ReviveLocks", "RL-00036"),
        ("Bamboo Shine Shampoo", "Herbal Luxe", "HL-00037"),
        ("Curl Defining Cream", "SilkTress", "ST-00038"),
        ("Oat Milk Sensitive Scalp Shampoo", "Scalp Guard", "SG-00039"),
        ("Coconut Milk Hydration Mask", "HairEssence", "HE-00040"),
        ("Green Tea Revitalizing Conditioner", "Herbal Luxe", "HL-00041"),
        ("Silicone-Free Smoothening Cream", "SilkTress", "ST-00042"),
        ("Onion Black Seed Oil", "NatureLocks", "NL-00043"),
        ("Lustrous Locks Shine Oil", "ReviveLocks", "RL-00044"),
        ("Honey Repair Hair Mask", "GoldenStrand", "GS-00045"),
        ("Keratin Soothe Leave-In", "HairEssence", "HE-00046"),
        ("Rice Water Strength Tonic", "RootRevive", "RR-00047"),
        ("Apple Stem Cell Scalp Serum", "Scalp Guard", "SG-00048"),
        ("Biotin Collagen Hair Spray", "TameTress", "TT-00049"),
        ("Avocado Curl Revival Cream", "SilkTress", "ST-00050")
    ],
        "makeup": [
        ("Long-Lasting Matte Lipstick", "GlamBeauty", "GB-#####"),
        ("Waterproof Eyeliner", "EyeDefine", "ED-#####"),
        ("HD Foundation", "FlawlessSkin", "FS-#####"),
        ("Velvet Touch Blush", "CheekGlow", "CG-#####"),
        ("Smoky Eyeshadow Palette", "BoldBeauty", "BB-#####"),
        
        ("Liquid Matte Lipstick", "LuxeLips", "LL-#####"),
        ("Volumizing Mascara", "LashUp", "LU-#####"),
        ("Cream Concealer", "CoverPro", "CP-#####"),
        ("Translucent Setting Powder", "GlowSet", "GS-#####"),
        ("Natural Glow Highlighter", "ShinePop", "SP-#####"),

        ("BB Cream SPF 30", "DewDrop", "DD-#####"),
        ("Contour & Highlight Duo", "Sculptique", "SQ-#####"),
        ("Peach Tone Blush", "BlushBloom", "BBM-#####"),
        ("Eyebrow Definer Pencil", "BrowCraft", "BC-#####"),
        ("Lip & Cheek Tint", "ColorCharm", "CC-#####"),

        ("Matte Compact Powder", "VelvetMatte", "VM-#####"),
        ("Gel Eyeliner Pot", "EyeInk", "EI-#####"),
        ("Tinted Lip Balm", "MoistLips", "ML-#####"),
        ("Makeup Fixing Spray", "StayGlam", "SGM-#####"),
        ("Color Correcting Palette", "ToneFix", "TF-#####"),

        ("Liquid Highlighter Drops", "GlowUp", "GU-#####"),
        ("Pressed Powder Foundation", "TrueFinish", "TFN-#####"),
        ("Cream Blush Stick", "BloomRush", "BR-#####"),
        ("Eyeshadow Crayon Set", "PopPigment", "PP-#####"),
        ("Lash Curling Mascara", "CurlaLash", "CL-#####"),

        ("Lip Crayon Matte", "KissInk", "KI-#####"),
        ("Illuminating Primer", "PrimeRadiance", "PR-#####"),
        ("Sheer Lip Gloss", "GlossyPop", "GP-#####"),
        ("Dual Finish Foundation", "BaseBlend", "BBL-#####"),
        ("Kajal Stick", "DarkEyes", "DE-#####"),

        ("Makeup Remover Balm", "MeltAway", "MA-#####"),
        ("Shimmer Eyeshadow Quad", "GleamBox", "GBX-#####"),
        ("Matte Bronzer", "SunContour", "SC-#####"),
        ("Full Coverage Concealer", "HideIt", "HI-#####"),
        ("Velvet Matte Lip Cream", "SoftLuxe", "SLX-#####"),

        ("Lash Volumizer Primer", "LashBoost", "LB-#####"),
        ("Glow Setting Mist", "FreshMist", "FM-#####"),
        ("Cushion Foundation", "AirSkin", "AS-#####"),
        ("Tinted Brow Gel", "ArchFix", "AF-#####"),
        ("Pore Blurring Primer", "BlurFix", "BF-#####"),

        ("Glitter Liquid Eyeshadow", "ShinyEyes", "SE-#####"),
        ("Nude Lipstick Kit", "BareLuxe", "BLX-#####"),
        ("Matte Makeup Stick", "MatteQuick", "MQ-#####"),
        ("Glossy Lip Plumper", "PlumpMe", "PM-#####"),
        ("Ultra Black Mascara", "InkLash", "IL-#####"),

        ("Multi-Use Concealer Pen", "ConcealPro", "CNP-#####"),
        ("Velvet Matte Lip Kit", "GlamKit", "GK-#####"),
        ("Holographic Highlighter", "HoloShine", "HS-#####"),
        ("Mousse Blush", "SoftBloom", "SB-#####"),
        ("Liquid Contour Wand", "ContourEase", "CE-#####")
    ],
        "fragrances": [
        ("Eau de Parfum - Midnight Mist", "LuxuryScents", "LS-00001"),
        ("Citrus Breeze Cologne", "FreshAura", "FA-00002"),
        ("Musk & Oud Perfume", "EliteAroma", "EA-00003"),
        ("Rose Vanilla Body Spray", "BlossomScent", "BS-00004"),
        ("Woody Amber Eau de Toilette", "ScentCraft", "SC-00005"),
        
        ("Ocean Drift Eau de Cologne", "AquaVibe", "AV-00006"),
        ("Floral Essence Perfume", "PetalBloom", "PB-00007"),
        ("Vanilla Musk Body Mist", "SoftWhiff", "SW-00008"),
        ("Cedarwood Forest Cologne", "NatureNote", "NN-00009"),
        ("Sweet Orchid Eau de Parfum", "GlamScent", "GS-00010"),
        
        ("Crisp Linen Spray", "FreshAura", "FA-00011"),
        ("Night Bloom Perfume", "LuxuryScents", "LS-00012"),
        ("Amber Noir Cologne", "EliteAroma", "EA-00013"),
        ("Coconut Breeze Mist", "BlossomScent", "BS-00014"),
        ("Bergamot Citrus Eau de Toilette", "ScentCraft", "SC-00015"),
        
        ("Spiced Vanilla Cologne", "WarmWhiff", "WW-00016"),
        ("Iris & Sandalwood Perfume", "EliteAroma", "EA-00017"),
        ("Rainforest Mist Body Spray", "BlossomScent", "BS-00018"),
        ("Lavender Meadow Eau de Parfum", "LuxuryScents", "LS-00019"),
        ("Sunset Amber Cologne", "FreshAura", "FA-00020"),
        
        ("Velvet Rose Mist", "PetalBloom", "PB-00021"),
        ("Fresh Cotton Eau de Toilette", "ScentCraft", "SC-00022"),
        ("Mandarin Spice Perfume", "EliteAroma", "EA-00023"),
        ("Ocean Breeze Body Mist", "AquaVibe", "AV-00024"),
        ("Herbal Musk Cologne", "NatureNote", "NN-00025"),
        
        ("Pomegranate Glow Eau de Parfum", "GlowScents", "GS-00026"),
        ("Night Oud Intense Cologne", "LuxuryScents", "LS-00027"),
        ("Cucumber Mint Spray", "FreshAura", "FA-00028"),
        ("Saffron Wood Perfume", "EliteAroma", "EA-00029"),
        ("Wildflower Bliss Mist", "BlossomScent", "BS-00030"),
        
        ("Tropical Rain Cologne", "AquaVibe", "AV-00031"),
        ("Lily Petal Eau de Parfum", "PetalBloom", "PB-00032"),
        ("Warm Cashmere Body Spray", "SoftWhiff", "SW-00033"),
        ("Amber & Patchouli Cologne", "ScentCraft", "SC-00034"),
        ("Berry Citrus Eau de Toilette", "FreshAura", "FA-00035"),
        
        ("Magnolia Musk Perfume", "LuxuryScents", "LS-00036"),
        ("Alpine Woods Cologne", "NatureNote", "NN-00037"),
        ("Rose Noir Body Mist", "GlamScent", "GS-00038"),
        ("Lemongrass Zest Spray", "FreshAura", "FA-00039"),
        ("Cherry Blossom Eau de Parfum", "BlossomScent", "BS-00040"),
        
        ("Cinnamon Spice Cologne", "WarmWhiff", "WW-00041"),
        ("Jasmine Dream Perfume", "PetalBloom", "PB-00042"),
        ("Citrus Rain Mist", "AquaVibe", "AV-00043"),
        ("Fresh Bamboo Cologne", "NatureNote", "NN-00044"),
        ("Sage & Sea Salt Eau de Toilette", "ScentCraft", "SC-00045"),
        
        ("Golden Oud Perfume", "EliteAroma", "EA-00046"),
        ("Vanilla Orchid Mist", "SoftWhiff", "SW-00047"),
        ("Midnight Bloom Body Spray", "LuxuryScents", "LS-00048"),
        ("Pear Blossom Cologne", "FreshAura", "FA-00049"),
        ("Tobacco & Leather Perfume", "ScentCraft", "SC-00050")
    ],
        "grooming-kits": [
        ("Men's Premium Grooming Kit", "Bevel", "BV-00001"),
        ("Women's Self-Care Set", "The Body Shop", "TBS-00002"),
        ("Beard Grooming Combo", "Honest Amish", "HA-00003"),
        ("Facial Care Kit", "Neutrogena", "NG-00004"),
        ("Travel Grooming Essentials", "Philips", "PH-00005"),

        ("Luxury Beard Kit", "Mountaineer Brand", "MB-00006"),
        ("Complete Shaving Set", "The Art of Shaving", "AS-00007"),
        ("Sensitive Skin Grooming Kit", "Cetaphil", "CT-00008"),
        ("Men's Hair & Beard Pack", "SheaMoisture", "SM-00009"),
        ("Unisex Grooming Box", "Burt's Bees", "BB-00010"),

        ("Men's Skincare & Beard Kit", "L’Oréal Men Expert", "LE-00011"),
        ("Basic Beard Kit", "Cremo", "CR-00012"),
        ("Women's Glow-Up Kit", "Olay", "OL-00013"),
        ("Men's Fresh Face Set", "Nivea Men", "NV-00014"),
        ("Beard Trimmer & Oil Combo", "Braun", "BR-00015"),

        ("On-the-Go Care Set", "Harry's", "HY-00016"),
        ("Hair & Skin Wellness Box", "Kiehl’s", "KH-00017"),
        ("Sensitive Face Pack", "Aveeno", "AV-00018"),
        ("Shaving and Aftershave Kit", "Gillette", "GL-00019"),
        ("Deluxe Beauty Kit", "Clinique", "CL-00020"),

        ("Total Body Grooming Set", "Wahl", "WH-00021"),
        ("Nourishing Beard Pack", "Viking Revolution", "VR-00022"),
        ("Full Body Care Set", "Dove", "DV-00023"),
        ("Glow & Hydrate Kit", "Himalaya", "HM-00024"),
        ("Face, Hair, Beard Box", "Man Arden", "MA-00025"),

        ("Deep Clean Skincare Kit", "Innisfree", "IN-00026"),
        ("Professional Beard Set", "Bossman", "BM-00027"),
        ("Complete Women's Grooming Set", "WOW Skin Science", "WS-00028"),
        ("Men's Care & Trim Kit", "Remington", "RM-00029"),
        ("Radiant Skin Beauty Pack", "Forest Essentials", "FE-00030"),

        ("Hydration Facial Kit", "Plum", "PL-00031"),
        ("Trim & Shave Essentials", "Panasonic", "PN-00032"),
        ("Glow Boost Kit", "Lakme", "LK-00033"),
        ("Beard Balm & Brush Set", "ZEUS", "ZU-00034"),
        ("Shea Nourish Kit", "BodyHerbals", "BH-00035"),

        ("Face & Beard Combo", "UrbanGabru", "UG-00036"),
        ("Hydrating Skincare Kit", "WOW for Men", "WM-00037"),
        ("Professional Grooming Set", "Nova", "NV-00038"),
        ("Deluxe Trimming Set", "Syska", "SK-00039"),
        ("Men’s Charcoal Kit", "The Man Company", "MC-00040"),

        ("Botanical Beard Pack", "Beardo", "BD-00041"),
        ("Nourish & Restore Grooming Kit", "Mamaearth", "ME-00042"),
        ("Essential Grooming Combo", "Bombay Shaving Company", "BSC-00043"),
        ("Shaving & Skincare Kit", "Gillette Labs", "GL-00044"),
        ("Sensitive Grooming Box", "Simple", "SP-00045"),

        ("Oil Control Face Kit", "Everyuth", "EY-00046"),
        ("Soothing Aftercare Set", "Pond’s", "PD-00047"),
        ("Unisex Skin Kit", "Minimalist", "MN-00048"),
        ("Men’s Facial Trio", "Ustraa", "US-00049"),
        ("Classic Care Gift Set", "Nivea", "NV-00050")
    ],
        "bath-body": [
        ("Lavender Shower Gel", "The Body Shop", "TBS-00001"),
        ("Exfoliating Body Scrub", "St. Ives", "SI-00002"),
        ("Moisturizing Body Lotion", "Vaseline", "VA-00003"),
        ("Eucalyptus Bath Salts", "Dr Teal's", "DT-00004"),
        ("Aloe Vera Body Wash", "Nivea", "NV-00005"),

        ("Shea Butter Body Cream", "Palmer's", "PA-00006"),
        ("Coconut Milk Shower Gel", "OGX", "OG-00007"),
        ("Soothing Oat Body Wash", "Aveeno", "AV-00008"),
        ("Ultra Healing Body Lotion", "Jergens", "JG-00009"),
        ("Peppermint Foot Soak", "Bath & Body Works", "BBW-00010"),

        ("Moisture Therapy Lotion", "Avon", "AVN-00011"),
        ("Rose Water Body Mist", "Forest Essentials", "FE-00012"),
        ("Brightening Body Lotion", "Olay", "OL-00013"),
        ("Hydrating Body Balm", "Neutrogena", "NG-00014"),
        ("Cucumber & Mint Body Wash", "Biotique", "BQ-00015"),

        ("Charcoal Detox Body Scrub", "WOW Skin Science", "WOW-00016"),
        ("Goat Milk Soap Bar", "Dionis", "DN-00017"),
        ("Citrus Energy Body Wash", "Himalaya", "HM-00018"),
        ("Almond Oil Body Butter", "Kama Ayurveda", "KA-00019"),
        ("Chamomile Calming Bath Gel", "Aroma Magic", "AM-00020"),

        ("Silkening Shower Oil", "L’Occitane", "LO-00021"),
        ("Turmeric & Sandal Body Cleanser", "Patanjali", "PT-00022"),
        ("Yogurt Skin Smoothing Lotion", "Nivea", "NV-00023"),
        ("Vanilla Bean Body Scrub", "Tree Hut", "TH-00024"),
        ("Lavender Salt Soak", "Herbivore", "HB-00025"),

        ("Refreshing Shower Gel", "Fiama", "FM-00026"),
        ("Body Milk Lotion", "Sebamed", "SB-00027"),
        ("Cooling Body Mist", "Victoria’s Secret", "VS-00028"),
        ("Tea Tree Oil Body Wash", "The Body Shop", "TBS-00029"),
        ("Moringa Softening Body Butter", "The Body Shop", "TBS-00030"),

        ("Whipped Shea Butter Cream", "SheaMoisture", "SM-00031"),
        ("Cocoa Butter Body Lotion", "Palmer's", "PA-00032"),
        ("Mint Eucalyptus Shower Bomb", "Earth Therapeutics", "ET-00033"),
        ("Bath Fizzies Gift Pack", "Soulflower", "SF-00034"),
        ("Ocean Breeze Shower Gel", "Dove", "DV-00035"),

        ("Lemon Verbena Body Cleanser", "C.O. Bigelow", "COB-00036"),
        ("Body Polish Sugar Scrub", "Tree Hut", "TH-00037"),
        ("Herbal Rose Bath Powder", "Khadi Natural", "KN-00038"),
        ("Soothing Milk Bath", "Lush", "LSH-00039"),
        ("Orange Zest Body Mist", "Nykaa", "NY-00040"),

        ("Moisture Lock Body Oil", "Bio-Oil", "BO-00041"),
        ("Green Tea Body Wash", "Plum", "PL-00042"),
        ("Hydra Boost Gel Lotion", "Neutrogena", "NG-00043"),
        ("Coconut & Vanilla Body Lotion", "Love Beauty and Planet", "LBP-00044"),
        ("Dead Sea Mud Soap", "Ahava", "AH-00045"),

        ("Almond & Honey Body Lotion", "Dove", "DV-00046"),
        ("Rice Water Shower Gel", "Innisfree", "IN-00047"),
        ("Cocoa Almond Body Butter", "Fabindia", "FI-00048"),
        ("Musk Scented Bath Soap", "Yardley London", "YL-00049"),
        ("Mint & Green Clay Body Scrub", "Bare Body Essentials", "BBE-00050")
    ],
        "hair-styling": [
        ("Volumizing Mousse", "TRESemmé", "TS-00001"),
        ("Extra Hold Hair Gel", "Garnier Fructis", "GF-00002"),
        ("Thermal Creations Heat Tamer", "TRESemmé", "TS-00003"),
        ("Frizz Ease Secret Weapon Finishing Cream", "John Frieda", "JF-00004"),
        ("Messy Look Hair Wax", "Gatsby", "GB-00005"),

        ("Volume Injection Mousse", "Redken", "RK-00006"),
        ("Curl Enhancing Smoothie", "SheaMoisture", "SM-00007"),
        ("Got2b Glued Styling Spiking Glue", "Schwarzkopf", "SK-00008"),
        ("Sculpting Gel", "Biolage", "BL-00009"),
        ("Reworkable Hair Clay", "American Crew", "AC-00010"),

        ("Perfect Setting Spray", "Wella Professionals", "WP-00011"),
        ("Defrizzing Hair Cream", "Living Proof", "LP-00012"),
        ("Coconut & Hibiscus Curl Milk", "SheaMoisture", "SM-00013"),
        ("Styling Hair Pomade", "Suavecito", "SV-00014"),
        ("Matte Finish Hair Paste", "Hanz de Fuko", "HF-00015"),

        ("Beach Babe Texturizing Spray", "Not Your Mother's", "NYM-00016"),
        ("Argan Oil Styling Cream", "Moroccanoil", "MO-00017"),
        ("Extreme Freeze Spray", "TIGI Bed Head", "TG-00018"),
        ("Mega Control Hair Gel", "L'Oréal Paris Studio Line", "LR-00019"),
        ("Matte Separation Workable Wax", "Bed Head", "BH-00020"),

        ("Style + Protect Texture Finishing Spray", "Pureology", "PY-00021"),
        ("Root Pump Plus Volumizing Spray Mousse", "Big Sexy Hair", "BSH-00022"),
        ("Hydra Whip Styling Cream", "Pantene Pro-V", "PT-00023"),
        ("Texture Takeover Oomph Enhancing Hairspray", "amika", "AM-00024"),
        ("Elvive Dream Lengths Frizz Killer Serum", "L'Oréal Paris", "LR-00025"),

        ("High Shine Glossing Mist", "Ouai", "OU-00026"),
        ("Flexible Hold Hair Spray", "Kenra Professional", "KR-00027"),
        ("Volumizing Root Lift", "Paul Mitchell", "PM-00028"),
        ("Styling Putty for Men", "Nivea Men", "NV-00029"),
        ("Thickening Texture Paste", "Bumble and Bumble", "BB-00030"),

        ("Scalp & Hair Thickening Tonic", "Aveda", "AV-00031"),
        ("Mega Gel for Men", "Old Spice", "OS-00032"),
        ("Style Masters Modular Mousse", "Revlon Professional", "RV-00033"),
        ("Heat Styling Primer", "Kérastase", "KS-00034"),
        ("Texturizing Matte Paste", "Davines", "DV-00035"),

        ("Taming Cream for Curls", "DevaCurl", "DC-00036"),
        ("Flexible Style Sculpting Foam", "Paul Mitchell", "PM-00037"),
        ("Strong Fix Hairspray", "L'Oréal Professionnel", "LP-00038"),
        ("Hair Clay for Matte Finish", "Toni & Guy", "TG-00039"),
        ("Volume Lift Styling Spray", "John Frieda", "JF-00040"),

        ("Botanicals Fresh Care Styling Cream", "L'Oréal Paris", "LR-00041"),
        ("Mega Volume Collagen Mousse", "Schwarzkopf", "SK-00042"),
        ("Lightweight Styling Oil", "Ouai", "OU-00043"),
        ("Power Paste Texture Cream", "KMS", "KMS-00044"),
        ("Super Clean Extra Finishing Spray", "Paul Mitchell", "PM-00045"),

        ("Air Dry Curl Cream", "OGX", "OGX-00046"),
        ("Volumizing Hair Powder", "Batiste", "BT-00047"),
        ("Shine On Polishing Serum", "NatureLab Tokyo", "NL-00048"),
        ("Frizz Control Styling Gel", "Marc Anthony", "MA-00049"),
        ("Nourishing Hair Butter", "Carol’s Daughter", "CD-00050")
    ],
        "manicure-pedicure": [
        ("Gel Couture Nail Polish", "Essie", "ES-00001"),
        ("Miracle Gel Nail Color", "Sally Hansen", "SH-00002"),
        ("Nail Envy Strengthener", "OPI", "OP-00003"),
        ("Cuticle Oil Therapy", "Cuccio", "CU-00004"),
        ("Hard As Nails Nail Hardener", "Sally Hansen", "SH-00005"),

        ("Nail Lacquer Collection", "OPI", "OP-00006"),
        ("Hand & Nail Treatment Cream", "Clarins", "CL-00007"),
        ("Cuticle Remover Gel", "Blue Cross", "BC-00008"),
        ("Nail Repair Serum", "Mavala", "MV-00009"),
        ("Tea Tree Oil Foot Soak", "Dr Teal's", "DT-00010"),

        ("Nail Clippers Set", "Tweezerman", "TZ-00011"),
        ("Exfoliating Foot Mask", "Aveeno", "AV-00012"),
        ("Nail Polish Remover Wipes", "Cutex", "CX-00013"),
        ("Glass Nail File", "GerManikure", "GM-00014"),
        ("Manicure Essentials Kit", "Revlon", "RV-00015"),

        ("Professional Nail Drill Kit", "MelodySusie", "MS-00016"),
        ("Crystal Nail File", "OPI", "OP-00017"),
        ("Daily Moisture Therapy Cream", "Burt's Bees", "BB-00018"),
        ("Quick Dry Top Coat", "Seche Vite", "SV-00019"),
        ("ColorStay Gel Envy Nail Polish", "Revlon", "RV-00020"),

        ("Nail & Cuticle Oil", "CND SolarOil", "CND-00021"),
        ("Pedi Perfect Electronic Foot File", "Scholl", "SC-00022"),
        ("Pumice Stone Foot Scrubber", "Earth Therapeutics", "ET-00023"),
        ("Vitamin E Cuticle Cream", "Burt's Bees", "BB-00024"),
        ("Coconut Milk Foot Cream", "Tree Hut", "TH-00025"),

        ("No More Cuticles", "Sally Hansen", "SH-00026"),
        ("Lemon Butter Cuticle Cream", "Burt's Bees", "BB-00027"),
        ("Foot & Nail Balm", "O'Keeffe's", "OK-00028"),
        ("Nail Growth Treatment", "Essie", "ES-00029"),
        ("Professional Pedicure Kit", "Tweezerman", "TZ-00030"),

        ("Foot Repair Balm", "Neutrogena", "NG-00031"),
        ("Nail Treatment Set", "OPI", "OP-00032"),
        ("Moisturizing Hand Mask", "Aveeno", "AV-00033"),
        ("Heel & Toe Foot Cream", "Sally Hansen", "SH-00034"),
        ("Foot Peel Mask", "Baby Foot", "BF-00035"),

        ("Pedi Scrub Exfoliating Cleanser", "Earth Therapeutics", "ET-00036"),
        ("4-Way Nail Buffer Block", "Revlon", "RV-00037"),
        ("Nail Brightener", "Orly", "OR-00038"),
        ("Top & Base Coat Duo", "CND Vinylux", "CND-00039"),
        ("Lavender Cuticle Oil", "Deborah Lippmann", "DL-00040"),

        ("Vitamin C Foot Scrub", "The Body Shop", "BS-00041"),
        ("Pro Spa Nail & Cuticle Cream", "OPI", "OP-00042"),
        ("Cuticle Oil Pen", "Beetles Gel Polish", "BT-00043"),
        ("Foot Therapy Cream", "Gold Bond", "GB-00044"),
        ("Professional Nail Clippers", "Harperton", "HP-00045"),

        ("Nail Whitening Pencil", "Orly", "OR-00046"),
        ("Foot Cream with Shea Butter", "L’Occitane", "LO-00047"),
        ("Nail & Cuticle Revitalizer", "Ella+Mila", "EM-00048"),
        ("Spa Socks with Gel Lining", "Earth Therapeutics", "ET-00049"),
        ("Callus Remover Gel", "ProLinc", "PL-00050")
    ],
        "shavers-trimmers": [
        ("Multigroom Series 7000", "Philips Norelco", "PN-00001"),
        ("OneBlade Hybrid Electric Trimmer", "Philips Norelco", "PN-00002"),
        ("Series 9 Electric Shaver", "Braun", "BR-00003"),
        ("Beard Trimmer 3", "Braun", "BR-00004"),
        ("Multigroom All-in-One Trimmer", "Wahl", "WA-00005"),

        ("Lawn Mower 4.0 Groin Trimmer", "Manscaped", "MS-00006"),
        ("Fusion5 ProGlide Razor", "Gillette", "GL-00007"),
        ("Hydro Skin Comfort Razor", "Schick", "SK-00008"),
        ("Arc5 Electric Razor", "Panasonic", "PA-00009"),
        ("ES-LA63AA Wet/Dry Razor", "Panasonic", "PA-00010"),

        ("Electric Razor for Women", "Remington", "RM-00011"),
        ("Lithium-Ion Plus Beard Trimmer", "Wahl", "WA-00012"),
        ("i-Stubble Flexhead Trimmer", "Conair", "CN-00013"),
        ("Styler 3-in-1 Beard Trimmer", "Gillette", "GL-00014"),
        ("Trim & Shave Compact Razor", "Veet", "VT-00015"),

        ("XT5 Electric Shaver", "Braun", "BR-00016"),
        ("Bodygroom Series 5000", "Philips Norelco", "PN-00017"),
        ("Beard Boss Perfecter Stubble Trimmer", "Remington", "RM-00018"),
        ("Heritage Series Trimmer", "Wahl", "WA-00019"),
        ("Electric Facial Hair Remover", "Flawless", "FL-00020"),

        ("Beard and Stubble Trimmer", "Bevel", "BV-00021"),
        ("Series 3 ProSkin Shaver", "Braun", "BR-00022"),
        ("RotoShave Electric Razor", "MicroTouch", "MT-00023"),
        ("Pitbull Silver PRO Head Shaver", "Skull Shaver", "SS-00024"),
        ("Foil Shaver & Trimmer", "Andis", "AD-00025"),

        ("Hybrid Rechargeable Trimmer", "Hatteker", "HT-00026"),
        ("4D Electric Rotary Shaver", "Surker", "SKR-00027"),
        ("i-Light Pro Face & Body Trimmer", "Remington", "RM-00028"),
        ("Shaver 6000", "Philips Norelco", "PN-00029"),
        ("Beardscape Beard & Hair Trimmer", "Brio", "BR-00030"),

        ("Sensitive Touch Beauty Trimmer", "Veet", "VT-00031"),
        ("Titanium Beard Trimmer", "Wahl", "WA-00032"),
        ("Cordless Rechargeable Mustache Trimmer", "Conair", "CN-00033"),
        ("Triple Head Rotary Shaver", "Panasonic", "PA-00034"),
        ("Chrome Pro Haircut Kit", "Wahl", "WA-00035"),

        ("All-In-One Beard Trimmer", "Remington", "RM-00036"),
        ("LITHIUM MAXPlus Beard Trimmer", "Wahl", "WA-00037"),
        ("QuickGroom Body & Back Groomer", "Remington", "RM-00038"),
        ("Philips Lady Shaver", "Philips", "PH-00039"),
        ("Shaver 9300 Wet & Dry", "Philips Norelco", "PN-00040"),

        ("Trim Style Razor & Bikini Trimmer", "Schick", "SK-00041"),
        ("Magnum Lithium Precision Trimmer", "Conair", "CN-00042"),
        ("Multifunctional Hair Clipper Kit", "SUPRENT", "SP-00043"),
        ("Professional Balding Clipper", "Wahl", "WA-00044"),
        ("Rotary Electric Razor", "SweetLF", "SW-00045"),

        ("PowerTouch Electric Razor", "Philips", "PH-00046"),
        ("Pro Beard Trimmer Kit", "Kemei", "KM-00047"),
        ("Ergonomic Hair Clippers", "Remington", "RM-00048"),
        ("Ceramic Blade Beard Trimmer", "Hatteker", "HT-00049"),
        ("All-in-One Shaving Kit", "Manscaped", "MS-00050")
    ],
        "sunscreen": [
        ("Ultra Sheer Dry-Touch Sunscreen SPF 100+", "Neutrogena", "NT-00001"),
        ("Anthelios Melt-in Milk Sunscreen SPF 60", "La Roche-Posay", "LR-00002"),
        ("Sport Sunscreen Lotion SPF 50", "Coppertone", "CT-00003"),
        ("Mineral Sunscreen SPF 50", "EltaMD", "EM-00004"),
        ("Sensitive Skin Sunscreen SPF 30", "Aveeno", "AV-00005"),

        ("Invisible Zinc Sunscreen SPF 50", "Invisible Zinc", "IZ-00006"),
        ("Ultra Defense Sunscreen SPF 30", "Banana Boat", "BB-00007"),
        ("Daily Defense SPF 50", "Neutrogena", "NT-00008"),
        ("Broad Spectrum Sunscreen SPF 30", "Coppertone", "CT-00009"),
        ("Sunscreen Stick SPF 50", "Neutrogena", "NT-00010"),

        ("Sun Protection Lotion SPF 50", "Blue Lizard", "BL-00011"),
        ("Invisible Sunscreen SPF 50", "Supergoop!", "SG-00012"),
        ("Sport Sunscreen Spray SPF 30", "Coppertone", "CT-00013"),
        ("Hydrating Sunscreen SPF 50", "Neutrogena", "NT-00014"),
        ("Sensitive Skin SPF 50 Sunscreen", "Neutrogena", "NT-00015"),

        ("Sunshield Stick SPF 30", "Supergoop!", "SG-00016"),
        ("Sunscreen Lotion SPF 30", "Hawaiian Tropic", "HT-00017"),
        ("Aloe Vera Sunscreen SPF 50", "Banana Boat", "BB-00018"),
        ("Sheer Touch Sunscreen SPF 50", "Neutrogena", "NT-00019"),
        ("Mineral SPF 50 Sunscreen", "La Roche-Posay", "LR-00020"),

        ("Broad Spectrum Sunscreen SPF 50", "Coppertone", "CT-00021"),
        ("Sunblock SPF 30", "Aveeno", "AV-00022"),
        ("HydroBoost Sunscreen SPF 50", "Neutrogena", "NT-00023"),
        ("SPF 50+ Sport Sunscreen Lotion", "Banana Boat", "BB-00024"),
        ("Water-Resistant SPF 30 Sunscreen", "Coppertone", "CT-00025"),

        ("Antioxidant Sunscreen SPF 50", "EltaMD", "EM-00026"),
        ("Sunscreen Spray SPF 50", "Hawaiian Tropic", "HT-00027"),
        ("Glow Screen Sunscreen SPF 40", "Supergoop!", "SG-00028"),
        ("Ultra Light Sunscreen SPF 50", "Neutrogena", "NT-00029"),
        ("Sensitive Sunscreen SPF 50", "Blue Lizard", "BL-00030"),

        ("Sport Sunscreen SPF 50+", "Banana Boat", "BB-00031"),
        ("Mineral Sunscreen SPF 30", "La Roche-Posay", "LR-00032"),
        ("Matte Sunscreen SPF 50", "EltaMD", "EM-00033"),
        ("SPF 50 Mineral Sunscreen", "Neutrogena", "NT-00034"),
        ("Mineral SPF 30 Sunscreen", "Badger", "BD-00035"),

        ("Anti-Aging Sunscreen SPF 50", "La Roche-Posay", "LR-00036"),
        ("Sunscreen Spray SPF 50", "Neutrogena", "NT-00037"),
        ("Sport Sunscreen SPF 30", "Coppertone", "CT-00038"),
        ("Hydrating Sunscreen SPF 30", "Neutrogena", "NT-00039"),
        ("Aloe Vera Sunscreen SPF 30", "Banana Boat", "BB-00040"),

        ("SPF 50+ Mineral Sunscreen", "Aveeno", "AV-00041"),
        ("Water Resistant Sunscreen SPF 50", "Coppertone", "CT-00042"),
        ("Clear Sunscreen Spray SPF 50", "Banana Boat", "BB-00043"),
        ("Tinted Sunscreen SPF 30", "EltaMD", "EM-00044"),
        ("Sunscreen Stick SPF 50", "Neutrogena", "NT-00045"),

        ("Aloe Infused Sunscreen SPF 30", "Hawaiian Tropic", "HT-00046"),
        ("Broad Spectrum Sunscreen SPF 50", "La Roche-Posay", "LR-00047"),
        ("Daily Sunscreen SPF 30", "Neutrogena", "NT-00048"),
        ("Water-Resistant Sunscreen SPF 30", "Coppertone", "CT-00049"),
        ("Invisible Sunscreen SPF 40", "Supergoop!", "SG-00050")
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

with open("fake_products_books_and_stationery.json", "w") as f:
    json.dump(dataset, f, indent=4)

print("Fake product dataset with 500 products generated successfully!")
