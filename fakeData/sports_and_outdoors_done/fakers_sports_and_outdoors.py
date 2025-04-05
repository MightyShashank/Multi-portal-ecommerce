import json
import random
import uuid
from faker import Faker

fake = Faker()
Faker.seed(42)

categories = {
    "sports-and-outdoors": [
        "gym-equivalent", "shoes-clothing", "camping-hiking", "yoga-mats", "bicycles",
        "swimming", "cricket", "badminton-tennis", "fishing", "boxing-martial-arts"
    ]
}

product_data = {
        "gym-equivalent": [
            # Bowflex
            ("Adjustable Dumbbell Set", "Bowflex", "BF-####"),
            ("Kettlebell Select", "Bowflex", "BFK-####"),
            ("Home Gym Station", "Bowflex", "BFG-####"),
            ("Treadmill 22", "Bowflex", "BFT-####"),
            ("Adjustable Barbell Set", "Bowflex", "BFB-####"),

            # Marcy
            ("Multi-Function Workout Bench", "Marcy", "MC-#####"),
            ("Smith Machine Home Gym", "Marcy", "MCS-#####"),
            ("Olympic Weight Bench", "Marcy", "MCW-#####"),
            ("Recumbent Exercise Bike", "Marcy", "MCB-#####"),
            ("Dumbbell Rack", "Marcy", "MCD-#####"),

            # NordicTrack
            ("Smart Treadmill", "NordicTrack", "NT-#####"),
            ("Incline Trainer", "NordicTrack", "NTI-#####"),
            ("Rowing Machine", "NordicTrack", "NTR-#####"),
            ("Exercise Bike", "NordicTrack", "NTB-#####"),
            ("Strength Training System", "NordicTrack", "NTS-#####"),

            # Fit Simplify
            ("Resistance Bands Set", "Fit Simplify", "FS-####"),
            ("Pull-Up Assistance Bands", "Fit Simplify", "FSP-####"),
            ("Loop Resistance Bands", "Fit Simplify", "FSL-####"),
            ("Yoga Stretch Bands", "Fit Simplify", "FSY-####"),
            ("Heavy Duty Resistance Bands", "Fit Simplify", "FSH-####"),

            # ProForm
            ("Elliptical Machine", "ProForm", "PF-####"),
            ("Hybrid Trainer", "ProForm", "PFH-####"),
            ("Carbon Strength Machine", "ProForm", "PFC-####"),
            ("Pro Treadmill", "ProForm", "PFT-####"),
            ("Rowing Machine", "ProForm", "PFR-####"),

            # Rogue Fitness
            ("Power Rack", "Rogue Fitness", "RF-####"),
            ("Weightlifting Barbell", "Rogue Fitness", "RFB-####"),
            ("Bumper Plates Set", "Rogue Fitness", "RFP-####"),
            ("Medicine Ball", "Rogue Fitness", "RFM-####"),
            ("Weighted Vest", "Rogue Fitness", "RFV-####"),

            # TRX
            ("Suspension Training Kit", "TRX", "TRX-####"),
            ("Battle Ropes", "TRX", "TRB-####"),
            ("Slam Ball", "TRX", "TRS-####"),
            ("Wall-Mounted Pull-Up Bar", "TRX", "TRP-####"),
            ("Dip Bars", "TRX", "TRD-####"),

            # Concept2
            ("RowErg Rowing Machine", "Concept2", "C2R-####"),
            ("SkiErg Trainer", "Concept2", "C2S-####"),
            ("BikeErg Exercise Bike", "Concept2", "C2B-####"),
            ("Dynamic Rower", "Concept2", "C2D-####"),
            ("Performance Monitor", "Concept2", "C2P-####"),

            # Life Fitness
            ("Smith Machine", "Life Fitness", "LF-####"),
            ("Multi-Press Machine", "Life Fitness", "LFP-####"),
            ("Cable Crossover Machine", "Life Fitness", "LFC-####"),
            ("Leg Press Machine", "Life Fitness", "LFL-####"),
            ("Seated Row Machine", "Life Fitness", "LFR-####"),

            # Bowflex (Additional)
            ("Home Gym Tower", "Bowflex", "BFTG-####"),
            ("Seated Calf Raise Machine", "Bowflex", "BFC-####"),
            ("Rowing Machine 10", "Bowflex", "BFR-####"),
            ("Lat Pulldown Machine", "Bowflex", "BFL-####"),
            ("Adjustable Incline Bench", "Bowflex", "BFI-####")
        ],
        "shoes-clothing": [
            # Nike
            ("Running Shoes", "Nike", "NS-#####"),
            ("Basketball Shoes", "Nike", "NB-#####"),
            ("Soccer Cleats", "Nike", "NC-#####"),
            ("Training Shoes", "Nike", "NT-#####"),
            ("Trail Running Shoes", "Nike", "NTR-#####"),

            # Adidas
            ("Sports Jacket", "Adidas", "AD-#####"),
            ("Soccer Jersey", "Adidas", "AJ-#####"),
            ("Basketball Shorts", "Adidas", "ABS-#####"),
            ("Training Pants", "Adidas", "ATP-#####"),
            ("Athletic T-Shirt", "Adidas", "ATT-#####"),

            # Under Armour
            ("Compression Shorts", "Under Armour", "UA-#####"),
            ("Base Layer Leggings", "Under Armour", "UAL-#####"),
            ("HeatGear Tights", "Under Armour", "UAT-#####"),
            ("Performance Hoodie", "Under Armour", "UAH-#####"),
            ("Compression Shirt", "Under Armour", "UACS-#####"),

            # Puma
            ("Performance Socks", "Puma", "PU-#####"),
            ("Track Pants", "Puma", "PTP-#####"),
            ("Training Jacket", "Puma", "PTJ-#####"),
            ("Running Tights", "Puma", "PRT-#####"),
            ("Gym Vest", "Puma", "PGV-#####"),

            # Reebok
            ("Fitness Gloves", "Reebok", "RB-#####"),
            ("Athletic Shorts", "Reebok", "RAS-#####"),
            ("Workout Tank Top", "Reebok", "RTT-#####"),
            ("CrossFit Shoes", "Reebok", "RCS-#####"),
            ("Training Hoodie", "Reebok", "RTH-#####"),

            # ASICS
            ("Gel Running Shoes", "ASICS", "AS-#####"),
            ("Trail Running Shoes", "ASICS", "ATRS-#####"),
            ("Volleyball Shoes", "ASICS", "AVS-#####"),
            ("Tennis Shoes", "ASICS", "ATS-#####"),
            ("Walking Shoes", "ASICS", "AWS-#####"),

            # New Balance
            ("Running Sneakers", "New Balance", "NBRS-#####"),
            ("Casual Sneakers", "New Balance", "NBCS-#####"),
            ("Trail Running Sneakers", "New Balance", "NBTR-#####"),
            ("Athletic Socks", "New Balance", "NBAS-#####"),
            ("Performance Tank", "New Balance", "NBPT-#####"),

            # Columbia
            ("Outdoor Hiking Shoes", "Columbia", "CHS-#####"),
            ("Insulated Jacket", "Columbia", "CIJ-#####"),
            ("Waterproof Boots", "Columbia", "CWB-#####"),
            ("Softshell Jacket", "Columbia", "CSJ-#####"),
            ("Convertible Pants", "Columbia", "CCP-#####"),

            # The North Face
            ("Trail Running Jacket", "The North Face", "TNFJ-#####"),
            ("Hiking Boots", "The North Face", "TNFH-#####"),
            ("Winter Parka", "The North Face", "TNFP-#####"),
            ("Thermal Baselayer", "The North Face", "TNFT-#####"),
            ("Rainproof Pants", "The North Face", "TNFR-#####"),

            # Salomon
            ("Mountain Trail Shoes", "Salomon", "SMS-#####"),
            ("Alpine Ski Jacket", "Salomon", "SAJ-#####"),
            ("Trail Running Backpack", "Salomon", "STB-#####"),
            ("Waterproof Running Shoes", "Salomon", "SWS-#####"),
            ("Technical Hiking Pants", "Salomon", "SHP-#####")
        ],
        "camping-hiking": [
            # Tents
            ("2-Person Tent", "Coleman", "CO-####"),
            ("4-Person Tent", "Coleman", "CO4-####"),
            ("Ultralight Tent", "Big Agnes", "BA-####"),
            ("All-Season Tent", "The North Face", "TNF-####"),
            ("Backpacking Tent", "MSR", "MSR-####"),

            # Sleeping Bags
            ("Backpacking Sleeping Bag", "Marmot", "MA-#####"),
            ("Winter Sleeping Bag", "The North Face", "TNF-#####"),
            ("Lightweight Sleeping Bag", "Kelty", "KE-#####"),
            ("Down Sleeping Bag", "Western Mountaineering", "WM-#####"),
            ("Double Sleeping Bag", "Teton Sports", "TS-#####"),

            # Hiking Boots
            ("Hiking Boots", "Merrell", "ME-#####"),
            ("Waterproof Hiking Boots", "Salomon", "SA-#####"),
            ("Lightweight Trail Shoes", "Altra", "AL-#####"),
            ("Backpacking Boots", "La Sportiva", "LS-#####"),
            ("Insulated Hiking Boots", "Columbia", "CL-#####"),

            # Cooking & Stoves
            ("Portable Camping Stove", "Jetboil", "JB-#####"),
            ("Backpacking Stove", "MSR", "MSRS-#####"),
            ("Propane Camp Stove", "Coleman", "CPS-#####"),
            ("Wood Burning Stove", "Solo Stove", "SS-#####"),
            ("Compact Cookware Set", "GSI Outdoors", "GSI-#####"),

            # Backpacks
            ("Hydration Backpack", "Osprey", "OS-#####"),
            ("Multi-Day Hiking Backpack", "Deuter", "DE-#####"),
            ("Daypack", "Gregory", "GR-#####"),
            ("Lightweight Pack", "REI Co-op", "REI-#####"),
            ("Technical Hiking Pack", "Black Diamond", "BD-#####"),

            # Navigation & Safety
            ("GPS Handheld Device", "Garmin", "GA-#####"),
            ("Compass", "Suunto", "SU-#####"),
            ("Satellite Communicator", "Garmin", "GS-#####"),
            ("Emergency Whistle", "Fox 40", "FW-#####"),
            ("First Aid Kit", "Adventure Medical Kits", "AMK-#####"),

            # Lighting
            ("Headlamp", "Black Diamond", "BDH-#####"),
            ("LED Lantern", "Goal Zero", "GZ-#####"),
            ("Handheld Flashlight", "Fenix", "FX-#####"),
            ("Solar Camping Light", "LuminAID", "LA-#####"),
            ("Rechargeable Lantern", "Coleman", "CLR-#####"),

            # Hydration
            ("Water Filter", "Sawyer", "SW-#####"),
            ("Collapsible Water Bottle", "HydraPak", "HP-#####"),
            ("Stainless Steel Water Bottle", "Hydro Flask", "HF-#####"),
            ("Gravity Water Filter", "Platypus", "PL-#####"),
            ("Personal Water Purifier", "LifeStraw", "LS-#####"),

            # Trekking Poles
            ("Adjustable Trekking Poles", "Black Diamond", "BDT-#####"),
            ("Carbon Fiber Trekking Poles", "Leki", "LE-#####"),
            ("Hiking Staff", "Cascade Mountain Tech", "CMT-#####"),
            ("Collapsible Trekking Poles", "Montem", "MT-#####"),
            ("Snowshoe Poles", "MSR", "MSRP-#####"),

            # Apparel
            ("Insulated Hiking Jacket", "Patagonia", "PA-#####"),
            ("Convertible Hiking Pants", "Columbia", "CLP-#####"),
            ("Merino Wool Base Layer", "Icebreaker", "IB-#####"),
            ("Gore-Tex Rain Jacket", "Arc'teryx", "AR-#####"),
            ("UV Protection Hat", "Outdoor Research", "OR-#####")
        ],
        "yoga-mats": [
            # Eco-Friendly Yoga Mats
            ("Eco-Friendly Yoga Mat", "Liforme", "LF-####"),
            ("Biodegradable Yoga Mat", "Jade Yoga", "JY-####"),
            ("Sustainable Cork Yoga Mat", "Scoria", "SC-####"),
            ("Recycled Rubber Yoga Mat", "Manduka", "MR-####"),
            ("Natural Jute Yoga Mat", "Gaiam", "GJ-####"),

            # TPE & PVC Yoga Mats
            ("TPE Yoga Mat", "Gaiam", "GA-#####"),
            ("PVC-Free Yoga Mat", "Alo Yoga", "AY-#####"),
            ("Lightweight TPE Yoga Mat", "BalanceFrom", "BF-#####"),
            ("Eco-Conscious TPE Yoga Mat", "IUGA", "IU-#####"),
            ("Non-Toxic PVC Yoga Mat", "Liforme", "LPVC-#####"),

            # Non-Slip Yoga Mats
            ("Non-Slip Yoga Mat", "Manduka", "MA-#####"),
            ("Ultra-Grip Yoga Mat", "Heathyoga", "HY-#####"),
            ("Non-Skid Alignment Yoga Mat", "TOPLUS", "TP-#####"),
            ("Anti-Slip PU Yoga Mat", "Sugarmat", "SU-#####"),
            ("Sweat-Resistant Yoga Mat", "Aurorae", "AU-#####"),

            # Extra-Thick & Padded Yoga Mats
            ("Extra-Thick Yoga Mat", "BalanceFrom", "BF-#####"),
            ("1-Inch Thick Yoga Mat", "Crown Sporting Goods", "CSG-#####"),
            ("Extra Cushion Yoga Mat", "ProsourceFit", "PSF-#####"),
            ("Double-Layer Padded Yoga Mat", "Retrospec", "RS-#####"),
            ("Memory Foam Yoga Mat", "Incline Fit", "IF-#####"),

            # Travel & Portable Yoga Mats
            ("Travel Yoga Mat", "Manduka", "MT-#####"),
            ("Foldable Yoga Mat", "Gaiam", "GF-#####"),
            ("Ultra-Light Yoga Mat", "YOGO", "YO-#####"),
            ("Thin Compact Yoga Mat", "Jade Yoga", "JYT-#####"),
            ("Portable Roll-Up Yoga Mat", "PrAna", "PA-#####"),

            # Luxury & High-End Yoga Mats
            ("Luxury Yoga Mat", "Jade Yoga", "JY-#####"),
            ("Designer Yoga Mat", "Sugarmat", "SUG-#####"),
            ("Premium Performance Yoga Mat", "Alo Yoga", "ALP-#####"),
            ("High-Density Luxury Mat", "Liforme", "LFLX-#####"),
            ("Handcrafted Yoga Mat", "Samadhi Cushions", "SC-#####"),

            # Hot Yoga & Sweat-Resistant Mats
            ("Hot Yoga Mat", "Manduka", "MHY-#####"),
            ("Sweat-Absorbent Yoga Mat", "Gaiam", "GHY-#####"),
            ("Microfiber Hot Yoga Mat", "Yoga Design Lab", "YDL-#####"),
            ("Quick-Dry Yoga Mat", "Liforme", "LQD-#####"),
            ("Towel-Integrated Hot Yoga Mat", "Ewedoos", "EW-#####"),

            # Alignment & Training Yoga Mats
            ("Alignment Yoga Mat", "Heathyoga", "HA-#####"),
            ("Yoga Mat with Position Lines", "Liforme", "LP-#####"),
            ("Guided Alignment Mat", "Manduka", "MGA-#####"),
            ("Body Position Yoga Mat", "PrAna", "PRA-#####"),
            ("Training Support Yoga Mat", "IUGA", "IT-#####"),

            # Specialized Yoga Mats
            ("Extra-Wide Yoga Mat", "Gorilla Mats", "GM-#####"),
            ("Round Yoga Mat", "Shape Yoga", "SY-#####"),
            ("Yoga Mat for Seniors", "Sivan Health", "SH-#####"),
            ("Yoga Mat for Kids", "Gaiam Kids", "GK-#####"),
            ("Yoga Mat for Pilates", "ProsourceFit", "PP-#####")
        ],
        "bicycles": [
            # Mountain Bikes
            ("Mountain Bike", "Trek", "TR-####"),
            ("Full Suspension Mountain Bike", "Specialized", "SP-####"),
            ("Hardtail Mountain Bike", "Cannondale", "CA-####"),
            ("Fat Tire Mountain Bike", "Mongoose", "MG-####"),
            ("Downhill Mountain Bike", "Santa Cruz", "SC-####"),

            # Road Bikes
            ("Road Bike", "Cannondale", "CA-#####"),
            ("Endurance Road Bike", "Trek", "TE-#####"),
            ("Aero Road Bike", "Giant", "GI-#####"),
            ("Touring Road Bike", "Surly", "SU-#####"),
            ("Lightweight Road Bike", "Cervélo", "CE-#####"),

            # Hybrid Bikes
            ("Hybrid Bike", "Schwinn", "SW-#####"),
            ("Commuter Hybrid Bike", "Giant", "GC-#####"),
            ("Flat Bar Hybrid Bike", "Cannondale", "CF-#####"),
            ("Dual-Sport Hybrid Bike", "Trek", "TD-#####"),
            ("Fitness Hybrid Bike", "Specialized", "SF-#####"),

            # Electric Bicycles
            ("Electric Bicycle", "Rad Power", "RP-#####"),
            ("E-Mountain Bike", "Specialized", "EM-#####"),
            ("Folding Electric Bike", "Brompton", "BE-#####"),
            ("Commuter E-Bike", "Aventon", "AV-#####"),
            ("Cargo Electric Bike", "Tern", "TC-#####"),

            # Folding Bicycles
            ("Folding Bike", "Brompton", "BR-#####"),
            ("Compact Folding Bike", "Dahon", "DC-#####"),
            ("Lightweight Folding Bike", "Tern", "TL-#####"),
            ("Electric Folding Bike", "Gocycle", "GE-#####"),
            ("City Folding Bike", "Citizen", "CC-#####"),

            # BMX & Freestyle Bikes
            ("BMX Bike", "Mongoose", "MB-#####"),
            ("Freestyle BMX", "Sunday", "FS-#####"),
            ("Race BMX", "GT Bicycles", "GR-#####"),
            ("Dirt Jump BMX", "Haro", "HD-#####"),
            ("Street BMX", "Fit Bike Co.", "FB-#####"),

            # Cruiser Bicycles
            ("Beach Cruiser Bike", "Electra", "EC-#####"),
            ("Classic Cruiser Bike", "Schwinn", "SC-#####"),
            ("Lowrider Cruiser Bike", "Firmstrong", "LF-#####"),
            ("Comfort Cruiser Bike", "Huffy", "HC-#####"),
            ("Step-Through Cruiser Bike", "Retrospec", "RS-#####"),

            # Touring & Gravel Bikes
            ("Touring Bicycle", "Surly", "ST-#####"),
            ("Gravel Bike", "Canyon", "CG-#####"),
            ("Adventure Gravel Bike", "Salsa", "SA-#####"),
            ("All-Terrain Gravel Bike", "Giant", "AG-#####"),
            ("Lightweight Gravel Bike", "Trek", "TG-#####"),

            # Kids' Bicycles
            ("Kids' Balance Bike", "Strider", "SB-#####"),
            ("12-inch Kids' Bike", "Huffy", "HK-#####"),
            ("16-inch Kids' Bike", "Guardian", "GK-#####"),
            ("20-inch BMX for Kids", "Mongoose", "MK-#####"),
            ("24-inch Hybrid Bike", "Trek", "TK-#####"),

            # Specialty Bicycles
            ("Recumbent Bike", "Catrike", "CR-#####"),
            ("Tandem Bicycle", "Co-Motion", "CT-#####"),
            ("Unicycle", "Nimbus", "NU-#####"),
            ("Tricycle", "Schwinn", "TS-#####"),
            ("Cargo Bike", "Yuba", "YC-#####")
        ],
        "swimming": [
            # Goggles
            ("Swim Goggles", "Speedo", "SP-####"),
            ("Anti-Fog Swim Goggles", "TYR", "TF-####"),
            ("Mirrored Swim Goggles", "Arena", "AM-####"),
            ("Prescription Swim Goggles", "Aqua Sphere", "AP-####"),
            ("Junior Swim Goggles", "Nike", "NJ-####"),

            # Swim Caps
            ("Swimming Cap", "Arena", "AR-#####"),
            ("Silicone Swim Cap", "Speedo", "SC-#####"),
            ("Latex Swim Cap", "TYR", "TL-#####"),
            ("Waterproof Swim Cap", "Aqua Sphere", "AW-#####"),
            ("Printed Swim Cap", "Adidas", "AC-#####"),

            # Swimwear for Men
            ("Men's Swim Trunks", "Nike", "NI-#####"),
            ("Men's Swim Briefs", "Speedo", "SB-#####"),
            ("Men's Jammers", "TYR", "TJ-#####"),
            ("Board Shorts", "Quiksilver", "QS-#####"),
            ("Men's Racing Swimsuit", "Arena", "MR-#####"),

            # Swimwear for Women
            ("Women's One-Piece Swimsuit", "TYR", "TY-#####"),
            ("Women's Two-Piece Swimsuit", "Nike", "NT-#####"),
            ("Women's Bikini Set", "Roxy", "RB-#####"),
            ("Women's Racing Swimsuit", "Speedo", "WR-#####"),
            ("Women's Tankini", "Adidas", "WT-#####"),

            # Swimwear for Kids
            ("Kids' Swim Trunks", "Hurley", "KT-#####"),
            ("Toddler Swimwear Set", "Carter's", "TC-#####"),
            ("Girls' One-Piece Swimsuit", "Nike", "GO-#####"),
            ("Boys' Rash Guard Set", "Speedo", "BR-#####"),
            ("UV Protection Swimsuit", "TYR", "UV-#####"),

            # Swimming Equipment
            ("Waterproof Bluetooth Speaker", "JBL", "JB-#####"),
            ("Swimming Kickboard", "Speedo", "SK-#####"),
            ("Pull Buoy", "TYR", "PB-#####"),
            ("Swim Training Fins", "Arena", "SF-#####"),
            ("Hand Paddles", "FINIS", "HP-#####"),

            # Water Shoes & Accessories
            ("Aqua Socks", "Nike", "AS-#####"),
            ("Water Shoes", "Columbia", "WS-#####"),
            ("Neoprene Swim Gloves", "TYR", "NG-#####"),
            ("Swim Earplugs", "Mack's", "SE-#####"),
            ("Waterproof Swim Bag", "Speedo", "WB-#####"),

            # Pool & Open Water Swimming Gear
            ("Swim Snorkel", "Arena", "SS-#####"),
            ("Open Water Swimming Buoy", "New Wave", "OB-#####"),
            ("Waterproof Fitness Tracker", "Garmin", "GF-#####"),
            ("Swim Belt Flotation Device", "AquaJogger", "SB-#####"),
            ("Swim Lap Counter", "SportCount", "LC-#####"),

            # Sun Protection & Towels
            ("Waterproof Sunscreen", "Banana Boat", "WS-#####"),
            ("Swim Robe", "TYR", "SR-#####"),
            ("Microfiber Swim Towel", "Speedo", "MT-#####"),
            ("Cooling Towel", "Mission", "CT-#####"),
            ("Hooded Beach Towel", "Disney", "HT-#####"),

            # Diving & Snorkeling Gear
            ("Full-Face Snorkel Mask", "Tribord", "FM-#####"),
            ("Diving Mask", "Cressi", "DM-#####"),
            ("Swim Fins for Diving", "Mares", "DF-#####"),
            ("Underwater Camera", "GoPro", "UC-#####"),
            ("Wetsuit for Swimming", "O'Neill", "WS-#####")
        ],
        "cricket": [
            # Bats
            ("Cricket Bat", "Kookaburra", "KB-####"),
            ("English Willow Cricket Bat", "SG", "EW-####"),
            ("Kashmir Willow Cricket Bat", "SS Ton", "KW-####"),
            ("Tennis Ball Cricket Bat", "MRF", "TB-####"),
            ("Junior Cricket Bat", "GM", "JB-####"),

            # Balls
            ("Cricket Ball", "SG", "SG-#####"),
            ("Leather Cricket Ball", "Kookaburra", "LC-#####"),
            ("Tennis Cricket Ball", "Cosco", "TC-#####"),
            ("White Cricket Ball", "Dukes", "WB-#####"),
            ("Pink Cricket Ball", "Kookaburra", "PB-#####"),

            # Shoes
            ("Cricket Shoes", "Adidas", "AD-#####"),
            ("All-Rounder Cricket Shoes", "Puma", "AR-#####"),
            ("Spiked Cricket Shoes", "New Balance", "SC-#####"),
            ("Rubber Sole Cricket Shoes", "Nike", "RS-#####"),
            ("Batting Cricket Shoes", "Asics", "BC-#####"),

            # Gloves
            ("Wicket Keeping Gloves", "Puma", "PU-#####"),
            ("Batting Gloves", "SG", "BG-#####"),
            ("Junior Batting Gloves", "Kookaburra", "JG-#####"),
            ("Pro-Level Batting Gloves", "Gray-Nicolls", "PL-#####"),
            ("All-Weather Wicket Keeping Gloves", "SS Ton", "AW-#####"),

            # Helmets & Protection
            ("Cricket Helmet", "Shrey", "SH-#####"),
            ("Cricket Thigh Guard", "Moonwalkr", "TG-#####"),
            ("Cricket Chest Guard", "SG", "CG-#####"),
            ("Cricket Elbow Guard", "SS", "EG-#####"),
            ("Cricket Abdominal Guard", "SG", "AG-#####"),

            # Pads
            ("Batting Pads", "Kookaburra", "BP-#####"),
            ("Wicket Keeping Pads", "Gray-Nicolls", "WP-#####"),
            ("Youth Batting Pads", "Adidas", "YP-#####"),
            ("Lightweight Batting Pads", "SS", "LB-#####"),
            ("Thigh Pads", "Moonwalkr", "TP-#####"),

            # Cricket Clothing
            ("Cricket Jersey", "Nike", "CJ-#####"),
            ("Cricket Trousers", "Adidas", "CT-#####"),
            ("Cricket Cap", "Puma", "CC-#####"),
            ("Sweat Absorbing Wristbands", "SG", "SW-#####"),
            ("Full-Sleeve Cricket Shirt", "New Balance", "FS-#####"),

            # Training Equipment
            ("Cricket Net", "SG", "CN-#####"),
            ("Bowling Machine", "Leverage", "BM-#####"),
            ("Cricket Training Cones", "DSC", "TC-#####"),
            ("Cricket Ball Thrower", "Sidearm", "BT-#####"),
            ("Cricket Target Stumps", "GM", "TS-#####"),

            # Accessories
            ("Cricket Kit Bag", "Kookaburra", "KB-#####"),
            ("Bat Grip", "SG", "BG-#####"),
            ("Cricket Bat Mallet", "SS", "BM-#####"),
            ("Cricket Scorebook", "Gray-Nicolls", "SB-#####"),
            ("Bat Toe Guard", "Kookaburra", "TG-#####"),

            # Ground Equipment
            ("Cricket Stumps", "SG", "CS-#####"),
            ("Bails", "Kookaburra", "BL-#####"),
            ("Cricket Pitch Roller", "Heavy Duty", "PR-#####"),
            ("Cricket Sight Screen", "SG", "SS-#####"),
            ("Cricket Umpire Counter", "Gray-Nicolls", "UC-#####")
        ],
        "badminton-tennis": [
            # Badminton Rackets
            ("Badminton Racket", "Yonex", "YN-####"),
            ("Carbon Fiber Badminton Racket", "Li-Ning", "CF-####"),
            ("Lightweight Badminton Racket", "Victor", "LW-####"),
            ("Professional Badminton Racket", "Babolat", "PB-####"),
            ("Junior Badminton Racket", "Carlton", "JR-####"),

            # Tennis Rackets
            ("Tennis Racket", "Wilson", "WI-#####"),
            ("Graphite Tennis Racket", "Babolat", "GT-#####"),
            ("Pro-Level Tennis Racket", "Yonex", "PT-#####"),
            ("Junior Tennis Racket", "Head", "JT-#####"),
            ("Lightweight Tennis Racket", "Dunlop", "LT-#####"),

            # Shuttlecocks
            ("Badminton Shuttlecock", "Li-Ning", "LN-#####"),
            ("Feather Shuttlecock", "Yonex", "FS-#####"),
            ("Plastic Shuttlecock", "Victor", "PS-#####"),
            ("Tournament Grade Shuttlecock", "Babolat", "TG-#####"),
            ("Training Shuttlecock", "Carlton", "TS-#####"),

            # Tennis Balls
            ("Tennis Balls (Pack of 3)", "Babolat", "BA-#####"),
            ("Tennis Balls (Pack of 6)", "Wilson", "TB-#####"),
            ("Professional Tennis Balls", "Dunlop", "PTB-#####"),
            ("Junior Tennis Balls", "Head", "JTB-#####"),
            ("All-Surface Tennis Balls", "Penn", "ATB-#####"),

            # Badminton Nets
            ("Badminton Net", "Victor", "VI-#####"),
            ("Portable Badminton Net", "Yonex", "PN-#####"),
            ("Tournament Grade Badminton Net", "Li-Ning", "TG-#####"),
            ("Training Badminton Net", "Babolat", "TB-#####"),
            ("Adjustable Badminton Net", "Carlton", "AN-#####"),

            # Tennis Nets
            ("Tennis Net", "Wilson", "TN-#####"),
            ("Portable Tennis Net", "Head", "PTN-#####"),
            ("Tournament Grade Tennis Net", "Dunlop", "TTN-#####"),
            ("Training Tennis Net", "Babolat", "TRN-#####"),
            ("Adjustable Tennis Net", "Penn", "ATN-#####"),

            # Shoes
            ("Badminton Shoes", "Yonex", "BS-#####"),
            ("Tennis Shoes", "Nike", "TS-#####"),
            ("Professional Tennis Shoes", "Adidas", "PTS-#####"),
            ("Lightweight Badminton Shoes", "Li-Ning", "LBS-#####"),
            ("High-Performance Tennis Shoes", "Babolat", "HPTS-#####"),

            # Clothing
            ("Badminton T-Shirt", "Yonex", "BT-#####"),
            ("Tennis Polo Shirt", "Nike", "TPS-#####"),
            ("Badminton Shorts", "Li-Ning", "BSH-#####"),
            ("Tennis Skirt", "Adidas", "TSK-#####"),
            ("Sweat-Absorbing Wristbands", "Babolat", "SWR-#####"),

            # Accessories
            ("Tennis Grip Tape", "Wilson", "TG-#####"),
            ("Badminton Overgrip", "Yonex", "BO-#####"),
            ("Tennis Dampener", "Babolat", "TD-#####"),
            ("Badminton String Reel", "Li-Ning", "BSR-#####"),
            ("Tennis Ball Hopper", "Dunlop", "TBH-#####"),

            # Protective Gear
            ("Badminton Knee Pads", "Yonex", "BK-#####"),
            ("Tennis Elbow Support", "Nike", "TES-#####"),
            ("Wrist Support Brace", "Wilson", "WSB-#####"),
            ("Ankle Support Guard", "Li-Ning", "ASG-#####"),
            ("Compression Leg Sleeves", "Babolat", "CLS-#####"),

            # Training Equipment
            ("Badminton Training Cones", "Victor", "BTC-#####"),
            ("Tennis Training Ladder", "Wilson", "TTL-#####"),
            ("Badminton Smash Trainer", "Yonex", "BST-#####"),
            ("Tennis Ball Machine", "Babolat", "TBM-#####"),
            ("Badminton Footwork Markers", "Li-Ning", "BFM-#####")
        ],
        "fishing": [
            # Fishing Rods
            ("Fishing Rod", "Shimano", "SH-####"),
            ("Spinning Fishing Rod", "Daiwa", "SF-####"),
            ("Casting Fishing Rod", "Abu Garcia", "CF-####"),
            ("Telescopic Fishing Rod", "Sougayilang", "TF-####"),
            ("Ultralight Fishing Rod", "Fenwick", "UF-####"),

            # Fishing Reels
            ("Fishing Reel", "Abu Garcia", "AG-#####"),
            ("Baitcasting Reel", "Shimano", "BR-#####"),
            ("Spinning Reel", "Daiwa", "SR-#####"),
            ("Trolling Reel", "Penn", "TR-#####"),
            ("Fly Fishing Reel", "Orvis", "FR-#####"),

            # Fishing Lines
            ("Fishing Line (100m)", "Berkley", "BE-#####"),
            ("Braided Fishing Line", "PowerPro", "BF-#####"),
            ("Fluorocarbon Fishing Line", "Seaguar", "FL-#####"),
            ("Monofilament Fishing Line", "Stren", "ML-#####"),
            ("Saltwater Fishing Line", "Sufix", "SW-#####"),

            # Fishing Hooks
            ("Barbed Fishing Hooks (Pack of 50)", "Eagle Claw", "BH-#####"),
            ("Barbless Fishing Hooks (Pack of 50)", "Mustad", "BLH-#####"),
            ("Circle Fishing Hooks", "Gamakatsu", "CH-#####"),
            ("Treble Fishing Hooks", "Owner", "TH-#####"),
            ("Long Shank Hooks", "VMC", "LSH-#####"),

            # Fishing Lures
            ("Crankbait Lure", "Rapala", "CL-#####"),
            ("Soft Plastic Lure", "Zoom Baits", "SPL-#####"),
            ("Spinnerbait Lure", "Strike King", "SL-#####"),
            ("Topwater Frog Lure", "Booyah", "TFL-#####"),
            ("Jigging Lure", "Z-Man", "JL-#####"),

            # Fishing Baits
            ("Live Worm Bait", "Magic Bait", "WB-#####"),
            ("Artificial Minnow Bait", "Berkley", "MB-#####"),
            ("Shrimp Scented Bait", "Gulp!", "SB-#####"),
            ("Crab Imitation Bait", "Savage Gear", "CB-#####"),
            ("Floating Trout Bait", "PowerBait", "TB-#####"),

            # Fishing Nets
            ("Fishing Landing Net", "Frabill", "FN-#####"),
            ("Collapsible Fishing Net", "Plusinno", "CFN-#####"),
            ("Rubber Mesh Net", "KastKing", "RMN-#####"),
            ("Telescopic Fishing Net", "Goture", "TFN-#####"),
            ("Saltwater Fishing Net", "EGO", "SFN-#####"),

            # Tackle Boxes
            ("Fishing Tackle Box", "Plano", "PL-#####"),
            ("Waterproof Tackle Box", "Flambeau", "WTB-#####"),
            ("Soft-Sided Tackle Bag", "KastKing", "STB-#####"),
            ("Multi-Layer Tackle Organizer", "RUNCL", "MTO-#####"),
            ("Portable Tackle Storage", "Piscifun", "PTS-#####"),

            # Fishing Accessories
            ("Portable Fish Finder", "Deeper", "DP-#####"),
            ("Fishing Rod Holder", "Scotty", "RH-#####"),
            ("Baitcasting Gloves", "KastKing", "BG-#####"),
            ("Fishing Line Cutter", "Booms", "LC-#####"),
            ("Fishing Headlamp", "Petzl", "FH-#####"),

            # Fishing Clothing & Safety Gear
            ("Waterproof Fishing Jacket", "Columbia", "FJ-#####"),
            ("Fishing Waders", "Hodgman", "FW-#####"),
            ("Fishing Hat with UV Protection", "Simms", "FH-#####"),
            ("Polarized Fishing Sunglasses", "Costa Del Mar", "FS-#####"),
            ("Fishing Life Vest", "Onyx", "FLV-#####"),

            # Ice Fishing Gear
            ("Ice Fishing Auger", "Eskimo", "IA-#####"),
            ("Ice Fishing Rod", "13 Fishing", "IFR-#####"),
            ("Ice Fishing Tent", "Clam Outdoors", "IFT-#####"),
            ("Ice Fishing Tip-Up", "HT Enterprises", "IFTU-#####"),
            ("Ice Fishing Heater", "Mr. Heater", "IFH-#####"),

            # Saltwater & Deep Sea Fishing
            ("Saltwater Fishing Rod", "Penn", "SWR-#####"),
            ("Deep Sea Fishing Reel", "Okuma", "DSR-#####"),
            ("Offshore Fishing Harness", "Black Magic", "OFH-#####"),
            ("Heavy-Duty Saltwater Hooks", "Mustad", "SDH-#####"),
            ("Tuna Jigging Lure", "Shimano", "TJL-#####")
        ],
        "boxing-martial-arts": [
            # Gloves
            ("Boxing Gloves", "Everlast", "EV-####"),
            ("MMA Grappling Gloves", "Venum", "VG-####"),
            ("Muay Thai Gloves", "Fairtex", "MTG-####"),
            ("Sparring Gloves", "Hayabusa", "SG-####"),
            ("Heavy Bag Gloves", "RDX", "HBG-####"),

            # Training Bags
            ("Boxing Punch Bag", "RDX", "RD-#####"),
            ("Freestanding Punching Bag", "Century", "FPB-#####"),
            ("Heavy Duty Punching Bag", "Title Boxing", "HPB-#####"),
            ("Speed Bag", "Everlast", "SB-#####"),
            ("Reflex Bag", "Ringside", "RB-#####"),

            # Protective Gear
            ("Boxing Headgear", "Winning", "BH-#####"),
            ("MMA Shin Guards", "Venum", "MSG-#####"),
            ("Mouthguard", "Shock Doctor", "MG-#####"),
            ("Groin Protector", "Fairtex", "GP-#####"),
            ("Kickboxing Arm Pads", "Hayabusa", "KAP-#####"),

            # Apparel
            ("MMA Shorts", "Venum", "VE-#####"),
            ("Muay Thai Shorts", "Fairtex", "MTS-#####"),
            ("Boxing Robe", "Title Boxing", "BR-#####"),
            ("Jiu-Jitsu Gi", "Tatami", "JJG-#####"),
            ("Rash Guard", "Scramble", "RG-#####"),

            # Training Equipment
            ("Jump Rope", "Everlast", "JR-#####"),
            ("Focus Mitts", "Ringside", "FM-#####"),
            ("Thai Pads", "Fairtex", "TP-#####"),
            ("MMA Dummy Grappling Bag", "Combat Sports", "GD-#####"),
            ("Reaction Ball", "BlazePod", "RB-#####"),

            # Coaching & Sparring Equipment
            ("Boxing Strike Shield", "Title Boxing", "BSS-#####"),
            ("MMA Cage Wall Padding", "Dollamur", "CWP-#####"),
            ("Hand Wraps", "Everlast", "HW-#####"),
            ("Sparring Chest Guard", "Adidas", "SCG-#####"),
            ("Karate Breaking Boards", "ProForce", "KBB-#####"),

            # Accessories
            ("Boxing Glove Deodorizers", "Meister", "BGD-#####"),
            ("Hand Wrap Roller", "RDX", "HWR-#####"),
            ("Sweat Absorbing Headband", "Nike", "SHB-#####"),
            ("Boxing Timer", "TITLE", "BT-#####"),
            ("Punch Counter", "Everlast", "PC-#####"),

            # Martial Arts Weapons
            ("Training Nunchaku", "Century", "TN-#####"),
            ("Bo Staff", "Tiger Claw", "BS-#####"),
            ("Sai Set", "BladesUSA", "SS-#####"),
            ("Training Katana", "Cold Steel", "TK-#####"),
            ("Escrima Sticks", "Doce Pares", "ES-#####"),

            # Home Training Gear
            ("Doorway Pull-Up Bar", "Iron Gym", "PUB-#####"),
            ("Agility Ladder", "SKLZ", "AL-#####"),
            ("Resistance Bands", "Fit Simplify", "RB-#####"),
            ("Speed Training Parachute", "SKLZ", "STP-#####"),
            ("Core Balance Trainer", "BOSU", "CBT-#####"),

            # Recovery & Strength Training
            ("Foam Roller", "TriggerPoint", "FR-#####"),
            ("Hand Grip Strengthener", "Captains of Crush", "HGS-#####"),
            ("Ankle Weights", "Gaiam", "AW-#####"),
            ("Weighted Vest", "RUNMax", "WV-#####"),
            ("Muscle Massage Gun", "Theragun", "MMG-#####")
        ]
}

descriptions = {
        "gym-equivalent": [
            "A versatile adjustable dumbbell set, perfect for building strength and muscle with a range of weight options for various exercises.",
            "A multi-function workout bench designed for a full-body workout, featuring adjustable positions for different exercises.",
            "A smart treadmill with personalized workout programs, real-time fitness tracking, and incline options for maximum performance.",
            "An easy-to-use resistance bands set ideal for toning and strengthening muscles, suitable for home workouts or on-the-go training.",
            "An elliptical machine with adjustable resistance, multiple workout modes, and a sleek, space-saving design for home use.",
            "A rowing machine with adjustable resistance, ergonomic seat, and an LCD monitor to track your workout progress.",
            "A power rack for weight training, with a sturdy build, adjustable height, and a pull-up bar for added strength exercises.",
            "A kettlebell set with ergonomic handles, perfect for dynamic workouts that improve strength and cardiovascular endurance.",
            "A medicine ball with durable outer material and anti-slip texture, ideal for a range of functional fitness exercises.",
            "An ab roller designed to strengthen core muscles, featuring a non-slip grip and ultra-smooth rolling motion for efficient workouts.",
            "A yoga wheel designed for deep stretches, balance exercises, and improving flexibility during yoga sessions.",
            "A weighted jump rope, designed to improve cardiovascular health and coordination while adding resistance to your workout.",
            "A smart fitness tracker wristband that syncs with your phone to track calories, heart rate, and workout duration.",
            "A balance board for improving core strength, stability, and coordination, ideal for rehabilitation or advanced fitness routines.",
        ],
        "shoes-clothing": [
            "A pair of lightweight and breathable running shoes, designed for comfort and support during long-distance runs.",
            "A stylish sports jacket made with moisture-wicking fabric to keep you dry and comfortable during workouts or outdoor activities.",
            "Compression shorts designed to reduce muscle fatigue and enhance recovery, providing optimal support for athletes.",
            "Performance socks crafted with advanced fabric technology, offering moisture control, arch support, and comfort during intense physical activity.",
            "Fitness gloves designed for enhanced grip and wrist support, ideal for weightlifting and strength training.",
            "A moisture-wicking tank top designed to keep you cool and dry during intense workouts, perfect for running or gym training.",
            "A lightweight, breathable pair of hiking boots designed for maximum comfort and support on long treks and rugged terrain.",
            "Running tights with compression technology that boosts circulation and supports muscle recovery during high-performance runs.",
            "A versatile and durable sports bra, designed to offer comfort, breathability, and full support during intense exercise sessions.",
            "A premium pair of cycling shorts with strategically placed padding, providing all-day comfort and support during long rides.",
            "A reflective jacket designed for safety during early morning or evening runs, offering visibility and protection from wind and rain.",
            "Thermal leggings for cold-weather workouts, designed to trap body heat while allowing for full range of motion.",
            "A waterproof and breathable rain jacket, perfect for outdoor runners who need to stay dry without sacrificing comfort.",
            "A moisture-wicking cap designed to keep sweat off your face during exercise, with ventilation for breathability.",
            "An insulated sports vest, perfect for layering during cold-weather runs or hiking trips, offering lightweight warmth.",
        ],
        "camping-hiking": [
            "A durable 2-person tent designed for outdoor adventures, featuring quick setup, weather resistance, and excellent ventilation.",
            "A high-performance backpacking backpack with adjustable straps, waterproof material, and multiple compartments for organized storage.",
            "A portable camping stove with adjustable heat settings, lightweight design, and wind resistance for outdoor cooking.",
            "A compact sleeping bag with temperature-regulating technology, ideal for various weather conditions and camping trips.",
            "A collapsible camping chair with cup holders, designed for comfort and easy portability during outdoor adventures.",
            "A multi-tool kit with over 15 functions, including knife, screwdrivers, can opener, and pliers, perfect for camping and survival situations.",
            "A heavy-duty cooler with insulation technology to keep food and drinks cold for up to 48 hours, perfect for outdoor activities.",
            "A set of trekking poles with ergonomic handles, adjustable height, and anti-shock technology for a more comfortable hiking experience.",
            "A waterproof and windproof jacket designed for protection in extreme weather conditions while hiking or camping.",
            "A lightweight hammock with tree straps, designed for easy setup and relaxation during outdoor activities.",
            "A solar-powered lantern with adjustable brightness levels, ideal for lighting up your campsite or hiking trails at night.",
            "A set of camping cookware with non-stick surfaces and compact designs, perfect for outdoor cooking and meals.",
            "A portable water filter system for ensuring safe drinking water on hiking or camping trips, suitable for outdoor use.",
            "A lightweight, durable rain cover for backpacks, designed to keep your gear dry during unexpected showers.",
            "A camping axe with a sharp blade and comfortable grip, designed for chopping wood and other outdoor tasks.",
        ],
        "yoga-mats": [
            "A high-density, non-slip yoga mat that provides optimal cushioning and stability during your practice.",
            "A foldable yoga mat with a portable carrying strap, perfect for yogis on the go.",
            "A thick memory foam yoga mat designed to offer enhanced comfort and support for longer yoga sessions.",
            "A lightweight and eco-friendly yoga mat made from TPE material, offering superior grip and durability.",
            "A textured yoga mat designed for extra grip during hot yoga sessions, preventing slippage during poses.",
            "A premium cork yoga mat that combines sustainability with comfort, providing a smooth surface for your practice.",
            "A travel-friendly yoga mat with a slim profile, designed to roll up easily and fit into a carrying bag for portability.",
            "A double-sided yoga mat with different textures for varying levels of grip and comfort, ideal for all types of practice.",
            "A yoga mat with integrated alignment lines to help you maintain proper positioning and posture during poses.",
            "A non-toxic and eco-friendly yoga mat that provides excellent cushioning and durability for daily use.",
            "A thick, extra-large yoga mat perfect for practicing Pilates, stretching, or yoga with extra room to move.",
            "A hot yoga mat designed to resist moisture absorption, preventing slipping during intense, sweaty sessions.",
            "A reversible yoga mat with different colors and textures on each side, giving you two options to choose from for your practice.",
            "A multi-purpose yoga mat that can also be used for meditation, stretching, and other fitness exercises.",
            "A durable, machine-washable yoga mat that’s easy to clean after every session and made to last through regular use.",
        ],
        "bicycles": [
            "A lightweight carbon fiber road bike designed for speed and agility, perfect for long-distance cycling.",
            "An electric mountain bike with powerful motor support, designed for off-road trails and rugged terrain.",
            "A hybrid bike with a comfortable saddle, wide tires, and a sturdy frame, ideal for city commuting and casual rides.",
            "A foldable bike with compact design, ideal for people with limited storage space or for commuting.",
            "A professional-grade racing bike featuring aero handlebars, lightweight frame, and high-performance gears.",
            "A fat tire bike with extra-wide tires, built to tackle sand, snow, and other rough terrains with ease.",
            "A children's bike with training wheels, designed for learning to ride safely and comfortably.",
            "A mountain bike with front suspension and hydraulic brakes, perfect for downhill rides and cross-country trails.",
            "A cruiser bike with a retro design, comfortable seat, and easy-to-use gears for leisurely rides around town.",
            "A gravel bike designed for versatility, allowing you to ride both on and off-road with comfort and control.",
            "A commuter bike with integrated lights, a comfortable saddle, and a durable frame, perfect for urban cycling.",
            "A BMX bike designed for stunt riders, featuring a reinforced frame and high-impact wheels for extreme tricks.",
            "A recumbent bike designed for a low-to-the-ground position, offering a more relaxed and comfortable riding experience.",
            "A single-speed bike designed for simplicity and ease of maintenance, ideal for city commuting or casual rides.",
            "A mountain bike with 29-inch wheels, offering greater speed and control on uneven and rocky surfaces.",
        ],
        "swimming": [
            "A high-performance swimsuit made from chlorine-resistant fabric, offering compression and support for competitive swimmers.",
            "A set of silicone swimming caps that provide a snug fit and keep your hair dry during swimming sessions.",
            "A pair of professional goggles designed with anti-fog lenses and UV protection for clear vision in the pool.",
            "A waterproof smartwatch designed for swimmers, with tracking capabilities for lap count, heart rate, and calories burned.",
            "A swim paddle set designed to improve upper body strength and technique by increasing water resistance.",
            "A snorkel mask set with an anti-leak design, ideal for open-water swimming and scuba diving.",
            "A quick-drying towel made from microfiber, perfect for use after swimming practice or a trip to the beach.",
            "A swim buoy designed to increase visibility and provide flotation for open-water swimmers.",
            "A swimming kickboard to help improve leg strength and body position while practicing kicking techniques.",
            "A swim fin set designed to improve kicking strength and accelerate your speed in the water.",
            "A waterproof bag to store your wet swim gear, made from durable, leak-proof material.",
            "A swim training snorkel that helps swimmers focus on technique by allowing them to breathe more efficiently.",
            "A water-resistant phone pouch for safe and secure storage of your mobile device during swimming activities.",
            "A full-body swimsuit designed for water aerobics and resistance training, providing maximum coverage and comfort.",
            "A pool float with adjustable headrest and cup holder for relaxation in the water."
        ],
        "cricket": [
            "A high-quality cricket bat made from premium willow, offering excellent power and control for all levels of play.",
            "A durable set of cricket stumps and bails, perfect for both practice and competitive matches.",
            "A professional cricket ball designed for improved swing and accuracy, ideal for both training and matches.",
            "A lightweight and breathable cricket helmet with adjustable straps, offering full protection during play.",
            "A cricket glove set designed to provide grip, comfort, and protection while batting and fielding.",
            "A pair of cricket pads offering maximum protection without compromising mobility for batting or wicket-keeping.",
            "A cricket bag with ample space for carrying bats, pads, gloves, and other accessories, perfect for travel.",
            "A stylish cricket shirt made from moisture-wicking fabric, designed for comfort during intense matches.",
            "A cricket wicket-keeping set with padded gloves, pads, and a high-quality keeping glove for professional use.",
            "A range of cricket shoes offering superior grip, comfort, and support for players on all types of pitches.",
            "A practice net designed for training, featuring high-quality mesh for safe and effective batting practice.",
            "A cricket umpire kit, including a high-quality whistle, counter, and clothing suitable for officiating games.",
            "A cricket training aid set that includes bowling machines, nets, and stumps to help improve your skills.",
            "A cricket protective gear set including a thigh guard, arm guard, and chest guard for extra protection during play.",
            "A pair of lightweight cricket shorts designed for comfort, breathability, and flexibility during long matches."
        ],
        "badminton-tennis": [
            "A professional-grade badminton racket with lightweight carbon fiber construction for maximum power and control.",
            "A premium quality shuttlecock made from feather material, designed for professional and recreational badminton play.",
            "A pair of comfortable, non-slip badminton shoes providing excellent grip and support during intense matches.",
            "A durable tennis racket with a large sweet spot, ideal for players seeking power and consistency in their game.",
            "A high-performance tennis ball with extra durability, designed for use on hard courts and prolonged rallies.",
            "A padded tennis racket cover for added protection during travel, preventing damage to strings and frame.",
            "A set of badminton net posts designed for regulation play, with adjustable height and easy setup.",
            "A pair of tennis wristbands designed to absorb sweat and provide added comfort during long matches.",
            "A badminton net with adjustable tension, designed for both indoor and outdoor play.",
            "A lightweight and breathable tennis cap offering sun protection and moisture-wicking performance during matches.",
            "A set of tennis balls made from premium felt material, providing a consistent bounce and durability.",
            "A portable badminton net set, perfect for casual games at the beach, park, or backyard.",
            "A racket bag with multiple compartments for storing rackets, shoes, and other essential gear for both badminton and tennis.",
            "A stylish tennis polo shirt made from moisture-wicking fabric for comfort and breathability during games.",
            "A pair of shock-absorbing badminton socks designed to reduce the impact on feet and ankles during fast movements."
        ],
        "fishing": [
            "A high-quality fishing rod with a lightweight, durable design, ideal for long hours of fishing in various conditions.",
            "A versatile fishing reel with smooth drag and high line capacity, perfect for both freshwater and saltwater fishing.",
            "A complete fishing tackle box with compartments for hooks, lures, baits, and other fishing accessories.",
            "A durable fishing net with a long handle, designed to safely land fish without damaging them.",
            "A set of fishing lures designed for different types of fish, featuring various colors and sizes to attract a wide range of species.",
            "A pair of waterproof fishing boots with excellent traction, designed for use in slippery, wet environments.",
            "A comfortable fishing vest with multiple pockets, perfect for carrying essential fishing gear and accessories.",
            "A fishing line spool with high tensile strength, ideal for catching large fish in both fresh and saltwater.",
            "A portable fish finder device that helps locate fish underwater using sonar technology, perfect for serious anglers.",
            "A stylish and functional fishing hat designed for sun protection, made from breathable fabric for comfort.",
            "A fishing tackle bag with padded compartments to safely store reels, rods, and tackle, ensuring easy access and organization.",
            "A collapsible fishing rod that’s compact and easy to carry, perfect for traveling and fishing on the go.",
            "A high-performance fishing pole with adjustable length, ideal for different fishing techniques like fly fishing or deep sea fishing.",
            "A fish scaler tool designed to remove scales quickly and efficiently without damaging the fish.",
            "A multi-tool designed specifically for fishing, with built-in features like a hook remover, knife, and bottle opener."
        ],
        "boxing-martial-arts": [
            "A high-quality punching bag designed for durability and resistance, perfect for boxing and martial arts training.",
            "A pair of boxing gloves with padded wrist support and a breathable design, offering maximum comfort and protection during sparring.",
            "A durable pair of MMA gloves designed for grappling, striking, and supporting all forms of mixed martial arts training.",
            "A speed bag set with an adjustable stand, ideal for improving hand-eye coordination, reflexes, and speed in boxing.",
            "A lightweight and breathable rash guard designed for comfort during Brazilian Jiu-Jitsu, MMA, or other grappling sports.",
            "A professional-grade Muay Thai shin guard set, offering maximum protection and comfort for both beginners and professionals.",
            "A sturdy jump rope with adjustable length and smooth rotation, ideal for cardio workouts and improving footwork in boxing.",
            "A heavy-duty punching mitt set designed for trainers to improve accuracy and power in boxing punches.",
            "A pair of boxing hand wraps for extra wrist and knuckle support, providing protection during intense boxing or martial arts sessions.",
            "A high-performance martial arts uniform made with durable fabric, designed for various disciplines such as Karate, Taekwondo, and Judo.",
            "An adjustable boxing ring with sturdy ropes, perfect for home training and competitive matches.",
            "A set of punching gloves for beginners, designed to offer the right amount of padding and wrist support for training.",
            "A martial arts belt display rack for organizing your collection of belts in an elegant and functional way.",
            "A foam roller for muscle recovery, designed to help reduce soreness and increase flexibility after intense boxing or martial arts workouts.",
            "A high-quality kick shield for martial arts training, designed for practicing kicks, punches, and elbow strikes with maximum durability.",
            "A combat sports mouthguard designed for protecting teeth during sparring and full-contact martial arts training.",
            "A boxing timer with interval settings, perfect for tracking rounds, rest periods, and work time during training sessions.",
            "A training dummy for Muay Thai, Karate, or Kickboxing, built to withstand heavy strikes while providing realistic training conditions.",
            "A weighted vest for enhancing strength, endurance, and explosive power during boxing or martial arts workouts.",
            "A protective groin guard designed for safe and comfortable sparring in both boxing and martial arts."
        ]
}

features = {
        "gym-equivalent": {
            "Weight Capacity": ["100kg", "200kg", "300kg", "500kg"],
            "Material": ["Steel", "Durable Plastic", "Carbon Fiber", "Rubberized"],
            "Adjustable Resistance": ["12 levels", "16 levels", "20 levels"],
            "Resistance Type": ["Magnetic", "Electromagnetic", "Mechanical"],
            "Comfort Features": ["Padded Seats", "Ergonomic Handles", "Adjustable Footrests"],
            "Technology": ["Bluetooth Connectivity", "App Integration", "Heart Rate Monitoring"],
            "Build Quality": ["Sturdy Metal Frame", "Anti-slip Surface", "Heavy-duty Bearings"],
            "Assembly": ["Easy Assembly", "Quick Release", "Foldable Design"]
        },

        "shoes-clothing": {
            "Material": ["Breathable Mesh", "Leather", "Synthetic Fabrics", "Spandex"],
            "Fit Type": ["Compression Fit", "Loose Fit", "Regular Fit"],
            "Shoe Features": ["Arch Support", "Cushioning Technology", "Slip-resistant Sole", "Waterproof"],
            "Clothing Features": ["Moisture-wicking", "UV Protection", "Quick Drying", "Reflective Strips"],
            "Shoe Categories": ["Running Shoes", "Cross Training Shoes", "Hiking Boots", "Casual Sneakers"],
            "Clothing Categories": ["T-Shirts", "Jackets", "Tights", "Compression Sleeves"],
            "Durability": ["Water-resistant", "UV Resistant", "Anti-odor Technology"],
            "Fit & Comfort": ["Memory Foam Insoles", "Breathable Lining", "Padded Collar"]
        },

        "camping-hiking": {
            "Tent Capacity": ["2 Person", "4 Person", "6 Person", "8 Person"],
            "Material": ["Water-resistant Nylon", "Polyester", "Canvas", "Ripstop"],
            "Features": ["Pop-up Tent", "Double Layer", "UV Protection", "Easy Setup"],
            "Weather Resistance": ["Rainproof", "Windproof", "UV Resistant"],
            "Sleeping Bags": ["Mummy Style", "Rectangular", "Insulated", "Waterproof Lining"],
            "Footwear": ["Hiking Boots", "Trekking Shoes", "Waterproof Shoes"],
            "Accessories": ["Camping Lantern", "Portable Stove", "Camping Chairs"],
            "Backpacks": ["Hydration Reservoir", "Multiple Compartments", "Adjustable Straps"]
        },

        "yoga-mats": {
            "Material": ["PVC", "TPE", "Rubber", "Cork"],
            "Thickness": ["3mm", "5mm", "8mm", "10mm"],
            "Non-slip Features": ["Textured Surface", "Sticky Mats", "High-Traction Grip"],
            "Durability": ["Eco-friendly", "Odor-free", "Tear-resistant"],
            "Comfort": ["Extra Cushioning", "Soft Texture", "Anti-fatigue"],
            "Size": ["Standard", "Extra-long", "Extra-wide"],
            "Design Features": ["Printed Designs", "Solid Colors", "Embossed Texture"]
        },

        "bicycles": {
            "Type": ["Mountain Bike", "Road Bike", "Hybrid Bike", "Electric Bike"],
            "Frame Material": ["Aluminum", "Carbon Fiber", "Steel"],
            "Brakes": ["Disc Brakes", "V-Brakes", "Hydraulic Brakes"],
            "Wheel Size": ["26\"", "27.5\"", "29\""],
            "Gear System": ["21-Speed", "24-Speed", "Shimano Gear System"],
            "Suspension": ["Full Suspension", "Front Suspension", "Rigid"],
            "Weight": ["Lightweight", "Medium Weight", "Heavy Duty"],
            "Additional Features": ["Mudguards", "Kickstand", "Reflective Strips"]
        },

        "swimming": {
            "Swimsuits": ["Racing Swimsuit", "Full Coverage", "Speedo Tech Suit", "Bikini"],
            "Material": ["Lycra", "Spandex", "Nylon", "Polyester"],
            "Goggles": ["Anti-Fog Coating", "UV Protection", "Wide Vision Lens", "Comfort Seal"],
            "Swim Caps": ["Latex", "Silicone", "Elastic Fit", "No-slip"],
            "Accessories": ["Kickboard", "Swim Fins", "Pull Buoy", "Swim Paddles"],
            "Swimwear Features": ["Quick Dry", "Chlorine Resistance", "Sun Protection"]
        },

        "cricket": {
            "Bat Material": ["Kashmir Willow", "English Willow", "Carbon Fiber"],
            "Ball Type": ["Leather", "Rubber", "Training Balls"],
            "Protective Gear": ["Knee Guards", "Helmet", "Pads", "Gloves"],
            "Bat Weight": ["Light", "Medium", "Heavy"],
            "Bat Size": ["Short Handle", "Long Handle", "Extra Long"],
            "Accessories": ["Wicket Keeping Gloves", "Cricket Bags", "Thigh Guards", "Sunglasses"]
        },

        "badminton-tennis": {
            "Racket Material": ["Carbon Fiber", "Aluminum", "Graphite"],
            "String Tension": ["Medium", "High", "Low"],
            "Grip Size": ["Small", "Medium", "Large"],
            "Shuttlecock Type": ["Feathered", "Plastic"],
            "Tennis Balls": ["Pressurized", "Non-pressurized", "High Altitude"],
            "Tennis Rackets": ["Beginner", "Intermediate", "Professional"],
            "Badminton Shoes": ["Non-slip", "Breathable", "Lightweight"]
        },

        "fishing": {
            "Rod Type": ["Spinning Rod", "Casting Rod", "Fly Rod", "Telescopic Rod"],
            "Reel Type": ["Spinning Reel", "Baitcasting Reel", "Fly Reel", "Trolling Reel"],
            "Fishing Line": ["Monofilament", "Braided", "Fluorocarbon"],
            "Bait": ["Live Bait", "Lures", "Artificial Bait"],
            "Fishing Accessories": ["Tackle Box", "Fishing Net", "Hooks", "Bobbers"],
            "Fishing Rod Features": ["Telescoping", "Portable", "Anti-corrosion"]
        },

        "boxing-martial-arts": {
            "Material": ["Leather", "Synthetic Leather", "Vinyl"],
            "Glove Type": ["Boxing Gloves", "MMA Gloves", "Kickboxing Gloves"],
            "Padding": ["Foam Padding", "Gel Padding", "Latex Padding"],
            "Protection Features": ["Wrist Support", "Knuckle Protection", "Breathable Mesh"],
            "Ring Type": ["Professional Boxing Ring", "Home Boxing Ring", "Portable Rings"],
            "Training Equipment": ["Punching Bags", "Speed Bags", "Focus Mitts"],
            "Apparel": ["Compression Shirts", "MMA Shorts", "Fight Shorts", "Rash Guards"],
            "Headgear": ["Headguards", "Facial Shields"],
            "Footwear": ["Boxing Shoes", "MMA Boots", "Wrestling Shoes"],
            "Additional Features": ["Adjustable Straps", "Velcro Fastening", "Customizable"]
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

with open("fake_products_sports_and_outdoors.json", "w") as f:
    json.dump(dataset, f, indent=4)

print("Fake product dataset with 500 products generated successfully!")
