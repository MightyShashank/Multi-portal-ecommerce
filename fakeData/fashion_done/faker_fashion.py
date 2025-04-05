import json
import random
import uuid
from fakeData.electronics.faker_electronics import Faker

fake = Faker()
Faker.seed(42)

categories = {
    "fashion": [
        "mens-clothing", "womens-clothing", "kids-clothing", "footwear", "bags-backpacks",
        "watches", "sunglasses", "hats-caps", "jewelry", "sportswear"
    ]
}

product_data = {
    "mens-clothing": [
        # Levi's
        ("Slim Fit Jeans", "Levi's", "LJ-###"),
        ("Straight Fit Jeans", "Levi's", "LSJ-###"),
        ("Denim Jacket", "Levi's", "LDJ-###"),
        ("Classic Trucker Jacket", "Levi's", "LTJ-###"),
        ("Relaxed Fit Jeans", "Levi's", "LRJ-###"),

        # H&M
        ("Oxford Shirt", "H&M", "HS-###"),
        ("Crew Neck T-Shirt", "H&M", "HT-###"),
        ("Slim Fit Blazer", "H&M", "HB-###"),
        ("Cotton Chinos", "H&M", "HC-###"),
        ("Casual Hoodie", "H&M", "HH-###"),

        # Zara
        ("Tailored Blazer", "Zara", "ZB-###"),
        ("Skinny Fit Jeans", "Zara", "ZJ-###"),
        ("Polo T-Shirt", "Zara", "ZP-###"),
        ("Wool Overcoat", "Zara", "ZO-###"),
        ("Bomber Jacket", "Zara", "ZBJ-###"),

        # Uniqlo
        ("Chinos", "Uniqlo", "UC-###"),
        ("Linen Shirt", "Uniqlo", "ULS-###"),
        ("Ultra Light Down Jacket", "Uniqlo", "UDJ-###"),
        ("Regular Fit Jeans", "Uniqlo", "URJ-###"),
        ("Crew Neck Sweater", "Uniqlo", "US-###"),

        # Ted Baker
        ("Leather Jacket", "Ted Baker", "TLJ-###"),
        ("Wool Suit Jacket", "Ted Baker", "TWJ-###"),
        ("Slim Fit Suit Pants", "Ted Baker", "TSP-###"),
        ("Checked Blazer", "Ted Baker", "TCB-###"),
        ("Tweed Waistcoat", "Ted Baker", "TWC-###"),

        # Ralph Lauren
        ("Polo Shirt", "Ralph Lauren", "RP-###"),
        ("Chino Shorts", "Ralph Lauren", "RCS-###"),
        ("Sweater Vest", "Ralph Lauren", "RSV-###"),
        ("Cotton Trousers", "Ralph Lauren", "RCT-###"),
        ("Double Breasted Blazer", "Ralph Lauren", "RDB-###"),

        # Adidas
        ("Sports Hoodie", "Adidas", "AH-###"),
        ("Training Joggers", "Adidas", "AJ-###"),
        ("Graphic Print T-Shirt", "Adidas", "AT-###"),
        ("Full-Zip Track Jacket", "Adidas", "ATJ-###"),
        ("Athletic Shorts", "Adidas", "AS-###"),

        # Nike
        ("Dri-FIT T-Shirt", "Nike", "NT-###"),
        ("Running Shorts", "Nike", "NS-###"),
        ("Compression Leggings", "Nike", "NL-###"),
        ("Pullover Hoodie", "Nike", "NH-###"),
        ("Basketball Jersey", "Nike", "NBJ-###"),

        # Tommy Hilfiger
        ("Striped Polo Shirt", "Tommy Hilfiger", "TP-###"),
        ("Slim Fit Dress Shirt", "Tommy Hilfiger", "TDS-###"),
        ("Cotton Cardigan", "Tommy Hilfiger", "TC-###"),
        ("V-Neck Sweater", "Tommy Hilfiger", "TVS-###"),
        ("Checked Flannel Shirt", "Tommy Hilfiger", "TFS-###"),

        # Calvin Klein
        ("Slim Fit Suit", "Calvin Klein", "CKS-###"),
        ("Performance Track Pants", "Calvin Klein", "CKP-###"),
        ("Minimalist Crew Sweatshirt", "Calvin Klein", "CKSW-###"),
        ("Lounge Joggers", "Calvin Klein", "CKJ-###"),
        ("Tailored Overcoat", "Calvin Klein", "CKO-###")
    ],
    "womens-clothing": [
        # Zara
        ("Floral Dress", "Zara", "ZD-###"),
        ("Pleated Midi Skirt", "Zara", "ZMS-###"),
        ("Satin Wrap Dress", "Zara", "ZWD-###"),
        ("Tailored Blazer", "Zara", "ZB-###"),
        ("Printed Maxi Dress", "Zara", "ZMD-###"),

        # Levi's
        ("Denim Jacket", "Levi's", "LJ-###"),
        ("High-Rise Skinny Jeans", "Levi's", "LJS-###"),
        ("Boyfriend Fit Jeans", "Levi's", "LBJ-###"),
        ("Denim Shirt Dress", "Levi's", "LSD-###"),
        ("Classic Trucker Jacket", "Levi's", "LTJ-###"),

        # H&M
        ("High-Waist Skirt", "H&M", "HS-###"),
        ("Basic Crew Neck T-Shirt", "H&M", "HT-###"),
        ("V-Neck Blouse", "H&M", "HVB-###"),
        ("Oversized Sweater", "H&M", "HOS-###"),
        ("Faux Leather Jacket", "H&M", "HLJ-###"),

        # Mango
        ("Casual Blouse", "Mango", "MB-###"),
        ("Tailored Trousers", "Mango", "MTT-###"),
        ("Wrap Midi Dress", "Mango", "MWD-###"),
        ("Striped Shirt", "Mango", "MSS-###"),
        ("Cropped Cardigan", "Mango", "MCC-###"),

        # Uniqlo
        ("Peacoat", "Uniqlo", "UC-###"),
        ("Linen Shirt", "Uniqlo", "ULS-###"),
        ("Knit Sweater", "Uniqlo", "UKS-###"),
        ("A-Line Skirt", "Uniqlo", "UAS-###"),
        ("Down Puffer Jacket", "Uniqlo", "UDP-###"),

        # Ralph Lauren
        ("Cable Knit Sweater", "Ralph Lauren", "RKS-###"),
        ("Wool Overcoat", "Ralph Lauren", "RWO-###"),
        ("Slim Fit Polo", "Ralph Lauren", "RSP-###"),
        ("Cotton Midi Dress", "Ralph Lauren", "RMD-###"),
        ("Tailored Vest", "Ralph Lauren", "RTV-###"),

        # Adidas
        ("Sports Leggings", "Adidas", "AL-###"),
        ("Performance Hoodie", "Adidas", "AH-###"),
        ("Training Shorts", "Adidas", "AS-###"),
        ("Full-Zip Track Jacket", "Adidas", "ATJ-###"),
        ("Athletic Tank Top", "Adidas", "ATT-###"),

        # Nike
        ("Dri-FIT Tights", "Nike", "NT-###"),
        ("Running Shorts", "Nike", "NS-###"),
        ("Compression Sports Bra", "Nike", "NB-###"),
        ("Pullover Hoodie", "Nike", "NH-###"),
        ("Training Joggers", "Nike", "NJ-###"),

        # Tommy Hilfiger
        ("Striped Wrap Dress", "Tommy Hilfiger", "TWD-###"),
        ("Casual Denim Shirt", "Tommy Hilfiger", "TDS-###"),
        ("Classic Polo Shirt", "Tommy Hilfiger", "TPS-###"),
        ("Cotton Trousers", "Tommy Hilfiger", "TCT-###"),
        ("V-Neck Knit Sweater", "Tommy Hilfiger", "TVS-###"),

        # Calvin Klein
        ("Slim Fit Suit", "Calvin Klein", "CKS-###"),
        ("Performance Leggings", "Calvin Klein", "CKL-###"),
        ("Minimalist Sweatshirt", "Calvin Klein", "CKSW-###"),
        ("Lounge Joggers", "Calvin Klein", "CKJ-###"),
        ("Tailored Overcoat", "Calvin Klein", "CKO-###")
    ],
    "kids-clothing": [
        # Carter's
        ("Graphic T-shirt", "Carter's", "CT-###"),
        ("Striped Pajamas", "Carter's", "CPJ-###"),
        ("Denim Shorts", "Carter's", "CDS-###"),
        ("Winter Sweater", "Carter's", "CWS-###"),
        ("Hooded Jacket", "Carter's", "CHJ-###"),

        # Nike
        ("Jogger Pants", "Nike", "JP-###"),
        ("Dri-FIT Training Shorts", "Nike", "NTS-###"),
        ("Performance Hoodie", "Nike", "NPH-###"),
        ("Sports Leggings", "Nike", "NSL-###"),
        ("Running Sneakers", "Nike", "NRS-###"),

        # Burt's Bees Baby
        ("Baby Onesie", "Burt's Bees Baby", "BB-###"),
        ("Organic Cotton Romper", "Burt's Bees Baby", "BBR-###"),
        ("Sleeper Gown", "Burt's Bees Baby", "BBSG-###"),
        ("Baby Mittens", "Burt's Bees Baby", "BBM-###"),
        ("Swaddle Blanket", "Burt's Bees Baby", "BBS-###"),

        # Old Navy
        ("Denim Overalls", "Old Navy", "ON-###"),
        ("Plaid Button-Up Shirt", "Old Navy", "ONB-###"),
        ("Fleece Pullover", "Old Navy", "ONF-###"),
        ("Cotton Chinos", "Old Navy", "ONC-###"),
        ("Printed Leggings", "Old Navy", "ONL-###"),

        # Columbia
        ("Puffer Jacket", "Columbia", "CJ-###"),
        ("Waterproof Raincoat", "Columbia", "CR-###"),
        ("Snow Bib Overalls", "Columbia", "CSB-###"),
        ("Insulated Gloves", "Columbia", "CIG-###"),
        ("Thermal Base Layer", "Columbia", "CTB-###"),

        # Gap
        ("Knit Sweater", "Gap", "GKS-###"),
        ("Cargo Pants", "Gap", "GCP-###"),
        ("Denim Jacket", "Gap", "GDJ-###"),
        ("Softshell Hoodie", "Gap", "GSH-###"),
        ("Printed Romper", "Gap", "GR-###"),

        # The Children's Place
        ("Plaid Flannel Shirt", "The Children's Place", "TCPF-###"),
        ("School Uniform Pants", "The Children's Place", "TCPS-###"),
        ("Winter Coat", "The Children's Place", "TCPW-###"),
        ("Knit Beanie", "The Children's Place", "TCPB-###"),
        ("Tulle Skirt", "The Children's Place", "TCPT-###"),

        # Adidas
        ("Track Suit", "Adidas", "ATS-###"),
        ("Soccer Jersey", "Adidas", "ASJ-###"),
        ("Fleece Sweatpants", "Adidas", "AFP-###"),
        ("Baseball Cap", "Adidas", "ABC-###"),
        ("Lightweight Windbreaker", "Adidas", "ALW-###"),

        # Tommy Hilfiger
        ("Classic Polo Shirt", "Tommy Hilfiger", "THP-###"),
        ("Cable Knit Cardigan", "Tommy Hilfiger", "THC-###"),
        ("Linen Shorts", "Tommy Hilfiger", "THLS-###"),
        ("Crew Neck Pullover", "Tommy Hilfiger", "THN-###"),
        ("Dress Shirt", "Tommy Hilfiger", "THD-###"),

        # H&M
        ("Long Sleeve Henley", "H&M", "HHL-###"),
        ("Stretch Denim Jeans", "H&M", "HJD-###"),
        ("Fleece Joggers", "H&M", "HFJ-###"),
        ("Waterproof Snow Boots", "H&M", "HSB-###"),
        ("Soft Cotton Hoodie", "H&M", "HCH-###")
    ],
    "footwear": [
        # Nike
        ("Air Jordan 1", "Nike", "AJ1-###"),
        ("Air Force 1", "Nike", "AF1-###"),
        ("React Infinity Run", "Nike", "RIR-###"),
        ("ZoomX Vaporfly", "Nike", "ZV-###"),
        ("Blazer Mid '77", "Nike", "BM77-###"),

        # Adidas
        ("Stan Smith Sneakers", "Adidas", "SS-###"),
        ("Ultraboost 22", "Adidas", "UB-###"),
        ("Superstar Sneakers", "Adidas", "SST-###"),
        ("NMD R1", "Adidas", "NMD-###"),
        ("Gazelle Shoes", "Adidas", "GZL-###"),

        # Dr. Martens
        ("Chelsea Boots", "Dr. Martens", "DM-###"),
        ("1460 Smooth Leather Boots", "Dr. Martens", "DM1460-###"),
        ("Jadon Platform Boots", "Dr. Martens", "DMJP-###"),
        ("1461 Oxford Shoes", "Dr. Martens", "DM1461-###"),
        ("Combs Tech Boots", "Dr. Martens", "DMCB-###"),

        # Birkenstock
        ("Classic Sandals", "Birkenstock", "BS-###"),
        ("Arizona Soft Footbed", "Birkenstock", "AZ-###"),
        ("Gizeh Sandals", "Birkenstock", "GZ-###"),
        ("Boston Clogs", "Birkenstock", "BC-###"),
        ("Mayari Sandals", "Birkenstock", "MY-###"),

        # Puma
        ("Running Shoes", "Puma", "RS-###"),
        ("Future Rider", "Puma", "FR-###"),
        ("Cali Star Sneakers", "Puma", "CS-###"),
        ("Suede Classic", "Puma", "SC-###"),
        ("Deviate Nitro", "Puma", "DN-###"),

        # Converse
        ("Chuck Taylor All Star", "Converse", "CTAS-###"),
        ("Run Star Hike", "Converse", "RSH-###"),
        ("Jack Purcell", "Converse", "JP-###"),
        ("One Star Sneakers", "Converse", "OS-###"),
        ("Chuck 70 High Top", "Converse", "C70-###"),

        # Reebok
        ("Classic Leather", "Reebok", "CL-###"),
        ("Club C 85", "Reebok", "CC85-###"),
        ("Nano X2 Training Shoes", "Reebok", "NX2-###"),
        ("Zig Kinetica 2.5", "Reebok", "ZK-###"),
        ("Pump Omni Zone II", "Reebok", "POZ-###"),

        # New Balance
        ("574 Core Sneakers", "New Balance", "NB574-###"),
        ("990v5", "New Balance", "NB990-###"),
        ("327 Sneakers", "New Balance", "NB327-###"),
        ("Fresh Foam 1080v12", "New Balance", "NBFF-###"),
        ("FuelCell Rebel v3", "New Balance", "NBFC-###"),

        # Vans
        ("Old Skool Sneakers", "Vans", "OSV-###"),
        ("Sk8-Hi", "Vans", "SHV-###"),
        ("Authentic Sneakers", "Vans", "ASV-###"),
        ("Slip-On Classic", "Vans", "SOC-###"),
        ("UltraRange EXO", "Vans", "URE-###"),

        # Timberland
        ("Premium 6-Inch Boots", "Timberland", "T6B-###"),
        ("Earthkeepers Boots", "Timberland", "TEB-###"),
        ("Chukka Boots", "Timberland", "TCB-###"),
        ("Pro Work Boots", "Timberland", "TPWB-###"),
        ("Euro Hiker Boots", "Timberland", "TEH-###")
    ],
    "bags-backpacks": [
        # North Face
        ("Backpack", "North Face", "NF-###"),
        ("Hiking Backpack", "North Face", "NFH-###"),
        ("Daypack", "North Face", "NFD-###"),
        ("Laptop Backpack", "North Face", "NFL-###"),
        ("Travel Backpack", "North Face", "NFT-###"),

        # Kate Spade
        ("Tote Bag", "Kate Spade", "KS-###"),
        ("Canvas Tote", "Kate Spade", "KSC-###"),
        ("Leather Tote", "Kate Spade", "KSL-###"),
        ("Quilted Tote", "Kate Spade", "KSQ-###"),
        ("Mini Tote", "Kate Spade", "KSM-###"),

        # Coach
        ("Leather Messenger Bag", "Coach", "CM-###"),
        ("Canvas Messenger Bag", "Coach", "CMC-###"),
        ("Slim Messenger Bag", "Coach", "CMS-###"),
        ("Flap Messenger Bag", "Coach", "CMF-###"),
        ("Vintage Messenger Bag", "Coach", "CMV-###"),

        # Under Armour
        ("Duffel Bag", "Under Armour", "UA-###"),
        ("Gym Duffel Bag", "Under Armour", "UAG-###"),
        ("Travel Duffel Bag", "Under Armour", "UAT-###"),
        ("Waterproof Duffel", "Under Armour", "UAW-###"),
        ("Compact Duffel", "Under Armour", "UAC-###"),

        # Michael Kors
        ("Crossbody Bag", "Michael Kors", "MK-###"),
        ("Mini Crossbody", "Michael Kors", "MKM-###"),
        ("Leather Crossbody", "Michael Kors", "MKL-###"),
        ("Convertible Crossbody", "Michael Kors", "MKC-###"),
        ("Chain Crossbody", "Michael Kors", "MKCH-###"),

        # Samsonite
        ("Rolling Suitcase", "Samsonite", "SRS-###"),
        ("Carry-On Suitcase", "Samsonite", "SCO-###"),
        ("Hard Shell Suitcase", "Samsonite", "SHS-###"),
        ("Expandable Suitcase", "Samsonite", "SES-###"),
        ("Spinner Luggage", "Samsonite", "SSL-###"),

        # Tumi
        ("Briefcase", "Tumi", "TB-###"),
        ("Expandable Briefcase", "Tumi", "TEB-###"),
        ("Laptop Briefcase", "Tumi", "TLB-###"),
        ("Leather Briefcase", "Tumi", "TLBR-###"),
        ("Convertible Briefcase", "Tumi", "TCB-###"),

        # Herschel
        ("Classic Backpack", "Herschel", "HB-###"),
        ("Little America Backpack", "Herschel", "HLA-###"),
        ("City Backpack", "Herschel", "HCB-###"),
        ("Hiking Backpack", "Herschel", "HHB-###"),
        ("Duffle Backpack", "Herschel", "HDB-###"),

        # Patagonia
        ("Eco-friendly Backpack", "Patagonia", "PB-###"),
        ("Waterproof Backpack", "Patagonia", "PWB-###"),
        ("Travel Backpack", "Patagonia", "PTB-###"),
        ("Climbing Backpack", "Patagonia", "PCB-###"),
        ("Sling Backpack", "Patagonia", "PSB-###"),

        # Louis Vuitton
        ("Designer Tote Bag", "Louis Vuitton", "LVT-###"),
        ("Luxury Crossbody", "Louis Vuitton", "LVC-###"),
        ("Monogram Handbag", "Louis Vuitton", "LVH-###"),
        ("Leather Shoulder Bag", "Louis Vuitton", "LVS-###"),
        ("Backpack Purse", "Louis Vuitton", "LVP-###")
    ],
    "watches": [
        # Rolex
        ("Rolex Submariner", "Rolex", "RS-###"),
        ("Rolex Daytona", "Rolex", "RD-###"),
        ("Rolex Datejust", "Rolex", "RDJ-###"),
        ("Rolex GMT-Master II", "Rolex", "RGMT-###"),
        ("Rolex Explorer", "Rolex", "RE-###"),

        # Apple
        ("Apple Watch Series 8", "Apple", "AW8-###"),
        ("Apple Watch Ultra", "Apple", "AWU-###"),
        ("Apple Watch SE", "Apple", "AWSE-###"),
        ("Apple Watch Nike Edition", "Apple", "AWN-###"),
        ("Apple Watch Hermes", "Apple", "AWH-###"),

        # Casio
        ("Casio G-Shock", "Casio", "GS-###"),
        ("Casio Edifice", "Casio", "CE-###"),
        ("Casio Pro Trek", "Casio", "CPT-###"),
        ("Casio Vintage", "Casio", "CV-###"),
        ("Casio Classic Digital", "Casio", "CCD-###"),

        # Omega
        ("Omega Speedmaster", "Omega", "OS-###"),
        ("Omega Seamaster", "Omega", "OSEA-###"),
        ("Omega Constellation", "Omega", "OC-###"),
        ("Omega De Ville", "Omega", "ODV-###"),
        ("Omega Aqua Terra", "Omega", "OAT-###"),

        # Fossil
        ("Fossil Hybrid HR", "Fossil", "FH-###"),
        ("Fossil Gen 6 Smartwatch", "Fossil", "FG6-###"),
        ("Fossil Townsman", "Fossil", "FT-###"),
        ("Fossil Neutra Chronograph", "Fossil", "FNC-###"),
        ("Fossil Minimalist", "Fossil", "FM-###"),

        # Seiko
        ("Seiko 5 Sports", "Seiko", "S5S-###"),
        ("Seiko Prospex", "Seiko", "SPX-###"),
        ("Seiko Presage", "Seiko", "SPG-###"),
        ("Seiko Astron", "Seiko", "SA-###"),
        ("Seiko Premier", "Seiko", "SPR-###"),

        # TAG Heuer
        ("TAG Heuer Carrera", "TAG Heuer", "THC-###"),
        ("TAG Heuer Monaco", "TAG Heuer", "THM-###"),
        ("TAG Heuer Aquaracer", "TAG Heuer", "THA-###"),
        ("TAG Heuer Formula 1", "TAG Heuer", "THF1-###"),
        ("TAG Heuer Link", "TAG Heuer", "THL-###"),

        # Tissot
        ("Tissot PRX", "Tissot", "TPRX-###"),
        ("Tissot Seastar", "Tissot", "TSS-###"),
        ("Tissot Heritage", "Tissot", "TH-###"),
        ("Tissot Supersport", "Tissot", "TSP-###"),
        ("Tissot Chrono XL", "Tissot", "TCXL-###"),

        # Citizen
        ("Citizen Eco-Drive", "Citizen", "CED-###"),
        ("Citizen Promaster", "Citizen", "CPR-###"),
        ("Citizen Aqualand", "Citizen", "CAQ-###"),
        ("Citizen Nighthawk", "Citizen", "CNH-###"),
        ("Citizen Satellite Wave", "Citizen", "CSW-###"),

        # Breitling
        ("Breitling Navitimer", "Breitling", "BN-###"),
        ("Breitling Superocean", "Breitling", "BSO-###"),
        ("Breitling Chronomat", "Breitling", "BCM-###"),
        ("Breitling Avenger", "Breitling", "BA-###"),
        ("Breitling Premier", "Breitling", "BP-###")
    ],
    "sunglasses": [
        # Ray-Ban
        ("Aviator Sunglasses", "Ray-Ban", "RB-###"),
        ("Wayfarer Sunglasses", "Ray-Ban", "WB-###"),
        ("Clubmaster", "Ray-Ban", "CB-###"),
        ("Round Metal Sunglasses", "Ray-Ban", "RM-###"),
        ("Justin Sunglasses", "Ray-Ban", "JRB-###"),

        # Oakley
        ("Polarized Sunglasses", "Oakley", "OS-###"),
        ("Flak 2.0 XL", "Oakley", "F2X-###"),
        ("Radar EV Path", "Oakley", "REP-###"),
        ("Holbrook Sunglasses", "Oakley", "HBS-###"),
        ("Frogskins Sunglasses", "Oakley", "FS-###"),

        # Maui Jim
        ("Round Sunglasses", "Maui Jim", "MJ-###"),
        ("Mavericks Polarized", "Maui Jim", "MJP-###"),
        ("Peahi Wrap Sunglasses", "Maui Jim", "PWS-###"),
        ("Kupuna Aviators", "Maui Jim", "KA-###"),
        ("Ho’okipa Rimless", "Maui Jim", "HR-###"),

        # Persol
        ("Persol 714 Foldable", "Persol", "P714-###"),
        ("Persol 649 Original", "Persol", "P649-###"),
        ("Persol Steve McQueen", "Persol", "PSM-###"),
        ("Persol Polarized", "Persol", "PP-###"),
        ("Persol Rectangular", "Persol", "PR-###"),

        # Prada
        ("Prada Linea Rossa", "Prada", "PLR-###"),
        ("Prada Catwalk", "Prada", "PCW-###"),
        ("Prada Square Sunglasses", "Prada", "PSS-###"),
        ("Prada Pilot Sunglasses", "Prada", "PPS-###"),
        ("Prada Rimless Shield", "Prada", "PRS-###"),

        # Gucci
        ("Gucci Oversized Sunglasses", "Gucci", "GOS-###"),
        ("Gucci Rectangular Sunglasses", "Gucci", "GRS-###"),
        ("Gucci Round Frame", "Gucci", "GRF-###"),
        ("Gucci Cat Eye", "Gucci", "GCE-###"),
        ("Gucci Geometric", "Gucci", "GG-###"),

        # Tom Ford
        ("Tom Ford Marko Aviator", "Tom Ford", "TFM-###"),
        ("Tom Ford Snowdon", "Tom Ford", "TFS-###"),
        ("Tom Ford Henry", "Tom Ford", "TFH-###"),
        ("Tom Ford Cary", "Tom Ford", "TFC-###"),
        ("Tom Ford FT0237", "Tom Ford", "TF237-###"),

        # Versace
        ("Versace Medusa Sunglasses", "Versace", "VMS-###"),
        ("Versace Pilot Sunglasses", "Versace", "VPS-###"),
        ("Versace Shield Sunglasses", "Versace", "VSS-###"),
        ("Versace Geometric Frame", "Versace", "VGF-###"),
        ("Versace Round Sunglasses", "Versace", "VRS-###"),

        # Burberry
        ("Burberry Square Sunglasses", "Burberry", "BSS-###"),
        ("Burberry Check Detail", "Burberry", "BCD-###"),
        ("Burberry Cat-Eye Sunglasses", "Burberry", "BCE-###"),
        ("Burberry Oversized Frames", "Burberry", "BOF-###"),
        ("Burberry Aviator", "Burberry", "BA-###"),

        # Dolce & Gabbana
        ("Dolce & Gabbana DG Logo", "Dolce & Gabbana", "DGL-###"),
        ("Dolce & Gabbana Round", "Dolce & Gabbana", "DGR-###"),
        ("Dolce & Gabbana Shield", "Dolce & Gabbana", "DGS-###"),
        ("Dolce & Gabbana Square", "Dolce & Gabbana", "DGQ-###"),
        ("Dolce & Gabbana Oversized", "Dolce & Gabbana", "DGO-###")
    ],
    "hats-caps": [
        # Nike
        ("Baseball Cap", "Nike", "BC-###"),
        ("Dri-FIT Cap", "Nike", "DFC-###"),
        ("Heritage86 Cap", "Nike", "H86-###"),
        ("Pro Futura Snapback", "Nike", "PFS-###"),
        ("Tech Cap", "Nike", "TC-###"),

        # Stetson
        ("Fedora", "Stetson", "ST-###"),
        ("Straw Fedora", "Stetson", "SF-###"),
        ("Wool Felt Fedora", "Stetson", "WFF-###"),
        ("Panama Fedora", "Stetson", "PF-###"),
        ("Trilby Hat", "Stetson", "TH-###"),

        # Carhartt
        ("Beanie", "Carhartt", "CB-###"),
        ("Acrylic Watch Hat", "Carhartt", "AWH-###"),
        ("Knit Cuffed Beanie", "Carhartt", "KCB-###"),
        ("Fleece Beanie", "Carhartt", "FB-###"),
        ("Insulated Beanie", "Carhartt", "IB-###"),

        # New Era
        ("Snapback Cap", "New Era", "NE-###"),
        ("59FIFTY Fitted Cap", "New Era", "59F-###"),
        ("9FORTY Adjustable Cap", "New Era", "9F-###"),
        ("Trucker Hat", "New Era", "TH-###"),
        ("Camouflage Snapback", "New Era", "CS-###"),

        # Adidas
        ("Bucket Hat", "Adidas", "AH-###"),
        ("Trefoil Cap", "Adidas", "TC-###"),
        ("Performance Cap", "Adidas", "PC-###"),
        ("Climacool Cap", "Adidas", "CC-###"),
        ("Running Cap", "Adidas", "RC-###"),

        # Under Armour
        ("UA Blitzing Cap", "Under Armour", "UAB-###"),
        ("HeatGear Cap", "Under Armour", "HGC-###"),
        ("Men's Adjustable Cap", "Under Armour", "MAC-###"),
        ("Stretch Fit Cap", "Under Armour", "SFC-###"),
        ("Shadow Run Cap", "Under Armour", "SRC-###"),

        # Kangol
        ("Kangol 504 Cap", "Kangol", "K504-###"),
        ("Bermuda Bucket Hat", "Kangol", "BBH-###"),
        ("Tropic 504 Ventair", "Kangol", "T504-###"),
        ("Kangol Beanie", "Kangol", "KB-###"),
        ("Wool Flexfit Cap", "Kangol", "WFC-###"),

        # Patagonia
        ("Patagonia P-6 Label Cap", "Patagonia", "P6L-###"),
        ("Trucker Hat", "Patagonia", "TPH-###"),
        ("Sun Runner Cap", "Patagonia", "SRC-###"),
        ("Wavefarer Bucket Hat", "Patagonia", "WBH-###"),
        ("Lightweight Travel Hat", "Patagonia", "LTH-###"),

        # Columbia
        ("Mesh Ball Cap", "Columbia", "MBC-###"),
        ("Columbia Bora Bora Booney", "Columbia", "BBB-###"),
        ("Columbia Snapback", "Columbia", "CSB-###"),
        ("PFG Mesh Cap", "Columbia", "PFG-###"),
        ("Trail Shaker Beanie", "Columbia", "TSB-###"),

        # The North Face
        ("TNF Logo Cap", "The North Face", "TNF-###"),
        ("Horizon Breeze Brimmer", "The North Face", "HBB-###"),
        ("TNF Beanie", "The North Face", "TNB-###"),
        ("Five Panel Cap", "The North Face", "FPC-###"),
        ("TNF Bucket Hat", "The North Face", "TNBH-###")
    ],
    "jewelry": [
        # Tiffany & Co.
        ("Gold Necklace", "Tiffany & Co.", "GN-###"),
        ("Platinum Engagement Ring", "Tiffany & Co.", "PER-###"),
        ("Silver Heart Pendant", "Tiffany & Co.", "SHP-###"),
        ("Diamond Stud Earrings", "Tiffany & Co.", "DSE-###"),
        ("Rose Gold Bracelet", "Tiffany & Co.", "RGB-###"),

        # De Beers
        ("Diamond Ring", "De Beers", "DR-###"),
        ("Halo Diamond Necklace", "De Beers", "HDN-###"),
        ("Platinum Wedding Band", "De Beers", "PWB-###"),
        ("Three-Stone Diamond Ring", "De Beers", "TDR-###"),
        ("Tennis Bracelet", "De Beers", "TB-###"),

        # Pandora
        ("Silver Bracelet", "Pandora", "SB-###"),
        ("Charm Bracelet", "Pandora", "CB-###"),
        ("Stackable Ring", "Pandora", "SR-###"),
        ("Birthstone Pendant", "Pandora", "BP-###"),
        ("Rose Gold Heart Ring", "Pandora", "RHR-###"),

        # Cartier
        ("Emerald Earrings", "Cartier", "EE-###"),
        ("Love Bracelet", "Cartier", "LB-###"),
        ("Sapphire Pendant", "Cartier", "SP-###"),
        ("Trinity Ring", "Cartier", "TR-###"),
        ("Panthère De Cartier Watch", "Cartier", "PCW-###"),

        # Mikimoto
        ("Pearl Pendant", "Mikimoto", "MP-###"),
        ("Classic Pearl Necklace", "Mikimoto", "CPN-###"),
        ("Akoya Pearl Earrings", "Mikimoto", "APE-###"),
        ("Golden South Sea Pearl Ring", "Mikimoto", "GSPR-###"),
        ("Pearl Strand Bracelet", "Mikimoto", "PSB-###"),

        # Bvlgari
        ("Serpenti Necklace", "Bvlgari", "SN-###"),
        ("B.zero1 Ring", "Bvlgari", "BZR-###"),
        ("Divas’ Dream Earrings", "Bvlgari", "DDE-###"),
        ("Onyx Pendant", "Bvlgari", "OP-###"),
        ("White Gold Bangle", "Bvlgari", "WGB-###"),

        # Van Cleef & Arpels
        ("Alhambra Necklace", "Van Cleef & Arpels", "AN-###"),
        ("Lucky Clover Ring", "Van Cleef & Arpels", "LCR-###"),
        ("Diamond Drop Earrings", "Van Cleef & Arpels", "DDE-###"),
        ("Magic Alhambra Bracelet", "Van Cleef & Arpels", "MAB-###"),
        ("Pearl Flower Brooch", "Van Cleef & Arpels", "PFB-###"),

        # Harry Winston
        ("Cluster Diamond Necklace", "Harry Winston", "CDN-###"),
        ("Emerald Cut Diamond Ring", "Harry Winston", "ECDR-###"),
        ("Ruby Tennis Bracelet", "Harry Winston", "RTB-###"),
        ("Sapphire Halo Pendant", "Harry Winston", "SHP-###"),
        ("Diamond Chandelier Earrings", "Harry Winston", "DCE-###"),

        # Chopard
        ("Happy Diamonds Necklace", "Chopard", "HDN-###"),
        ("Imperiale Watch", "Chopard", "IW-###"),
        ("L.U.C Perpetual Calendar", "Chopard", "LPC-###"),
        ("Floating Diamond Ring", "Chopard", "FDR-###"),
        ("Golden Heart Pendant", "Chopard", "GHP-###"),

        # Graff
        ("Butterfly Diamond Earrings", "Graff", "BDE-###"),
        ("Infinity Sapphire Ring", "Graff", "ISR-###"),
        ("Emerald Cut Diamond Necklace", "Graff", "ECDN-###"),
        ("Royal Blue Sapphire Bracelet", "Graff", "RBSB-###"),
        ("Graff Icon Pendant", "Graff", "GIP-###")
    ],
    "sportswear": [
        # Nike
        ("Running Shorts", "Nike", "RS-###"),
        ("Dri-FIT T-shirt", "Nike", "DFT-###"),
        ("Training Joggers", "Nike", "TJ-###"),
        ("Pro Compression Tights", "Nike", "PCT-###"),
        ("Windrunner Jacket", "Nike", "WJ-###"),

        # Adidas
        ("Sports Bra", "Adidas", "SB-###"),
        ("Climacool Training Pants", "Adidas", "CTP-###"),
        ("Predator Soccer Jersey", "Adidas", "PSJ-###"),
        ("Terrex Hiking Shorts", "Adidas", "THS-###"),
        ("Compression T-shirt", "Adidas", "CTS-###"),

        # Under Armour
        ("Compression Shirt", "Under Armour", "CS-###"),
        ("HeatGear Leggings", "Under Armour", "HGL-###"),
        ("Storm Hoodie", "Under Armour", "SH-###"),
        ("Performance Shorts", "Under Armour", "PS-###"),
        ("Rival Fleece Sweatpants", "Under Armour", "RFS-###"),

        # Puma
        ("Track Jacket", "Puma", "TJ-###"),
        ("Performance Tank Top", "Puma", "PTT-###"),
        ("Cross Training Shoes", "Puma", "CTS-###"),
        ("Evostripe Sweatpants", "Puma", "ESP-###"),
        ("DryCell Workout Tee", "Puma", "DWT-###"),

        # Lululemon
        ("Yoga Pants", "Lululemon", "YP-###"),
        ("Align High-Rise Leggings", "Lululemon", "AHL-###"),
        ("Metal Vent Tech Shirt", "Lululemon", "MVTS-###"),
        ("Swiftly Tech Racerback Tank", "Lululemon", "STRT-###"),
        ("License to Train Shorts", "Lululemon", "LTTS-###"),

        # Reebok
        ("CrossFit Shorts", "Reebok", "CFS-###"),
        ("Running Tights", "Reebok", "RT-###"),
        ("Workout Ready Tee", "Reebok", "WRT-###"),
        ("Athletic Joggers", "Reebok", "AJ-###"),
        ("Speedwick Training Hoodie", "Reebok", "STH-###"),

        # New Balance
        ("Fresh Foam Running Shoes", "New Balance", "FFRS-###"),
        ("Accelerate Running Tank", "New Balance", "ART-###"),
        ("Impact Run Shorts", "New Balance", "IRS-###"),
        ("Athletic Quarter-Zip Pullover", "New Balance", "AQZP-###"),
        ("Marathon Training Shirt", "New Balance", "MTS-###"),

        # ASICS
        ("Performance Running T-shirt", "ASICS", "PRT-###"),
        ("Gel-Kayano Running Shoes", "ASICS", "GKRS-###"),
        ("Compression Tights", "ASICS", "CT-###"),
        ("Training Hoodie", "ASICS", "TH-###"),
        ("Roadblast Running Shorts", "ASICS", "RRS-###"),

        # Columbia
        ("Omni-Wick Trail Shirt", "Columbia", "OWTS-###"),
        ("Fleece Lined Track Pants", "Columbia", "FLTP-###"),
        ("Titanium Active Jacket", "Columbia", "TAJ-###"),
        ("Hiking Shorts", "Columbia", "HS-###"),
        ("Winter Sports Gloves", "Columbia", "WSG-###"),

        # The North Face
        ("Apex Bionic Jacket", "The North Face", "ABJ-###"),
        ("Flight Series Running Tights", "The North Face", "FSRT-###"),
        ("Waterproof Trail Pants", "The North Face", "WTP-###"),
        ("Venture Rain Jacket", "The North Face", "VRJ-###"),
        ("Athletic Quarter-Zip Sweater", "The North Face", "AQZS-###")
    ]
}

descriptions = {
    "mens-clothing": [
        "A stylish collection of premium menswear designed for every occasion, featuring classic cuts and modern finishes.",
        "Tailored to perfection, this line of men’s clothing offers both comfort and sophistication with high-quality fabrics.",
        "Crafted for the modern man, this collection combines bold patterns and neutral tones for a versatile wardrobe.",
        "Fashion-forward menswear designed with attention to detail, perfect for both casual and formal settings.",
        "An everyday collection of comfortable and durable clothing, blending classic designs with contemporary elements.",
        "Elevate your wardrobe with this timeless collection of men’s clothing, focusing on premium quality and exceptional fit.",
        "From casual tees to refined blazers, this collection brings effortless style to your everyday life.",
        "Sleek and minimalistic, this range of menswear offers a sophisticated, modern aesthetic for fashion-conscious men.",
        "A versatile collection of clothing for men, from stylish basics to standout pieces for all occasions.",
        "Sporty and refined, this collection of menswear combines performance with fashion for an active lifestyle."
    ],
    "womens-clothing": [
        "Chic and comfortable, this collection of women’s clothing is designed to provide a perfect blend of style and ease.",
        "From flowy dresses to tailored blouses, this line offers a diverse selection for every woman’s wardrobe.",
        "Effortlessly stylish, this collection of women’s clothing is designed to keep you comfortable and fashionable all day.",
        "A versatile collection of elegant and casual clothing, featuring contemporary cuts and timeless styles.",
        "Embrace your inner fashionista with this line of trendy and high-quality women’s clothing, perfect for all seasons.",
        "From cozy sweaters to sleek dresses, this range of women’s clothing offers a stylish solution for every occasion.",
        "Bold, yet feminine, this collection of women’s clothing is designed to make a statement with every outfit.",
        "Lightweight, breathable fabrics and classic designs come together in this collection for a timeless look.",
        "A vibrant and chic collection of women’s clothing that brings sophistication and playfulness together in one.",
        "Celebrate your unique style with this eclectic mix of women’s clothing, from bohemian to contemporary."
    ],
    "kids-clothing": [
        "Bright, fun, and comfortable, this collection of kids' clothing is designed for play and adventure.",
        "Durable, cute, and cozy, this range of kids' clothing combines style with practicality for all-day wear.",
        "Soft fabrics and cheerful patterns make this collection of kids' clothing perfect for your little one’s daily activities.",
        "Made for movement, this kids' clothing collection is designed for comfort, durability, and endless fun.",
        "A vibrant collection of kids' clothing that combines comfort and style for all ages, from toddlers to teens.",
        "Designed with both parents and kids in mind, this collection blends easy-to-care-for fabrics with stylish designs.",
        "From adorable onesies to trendy toddler tees, this collection offers everything your child needs for every occasion.",
        "Crafted for growing kids, this collection of clothing combines comfort, durability, and cool designs.",
        "This kids' clothing line offers everything from sporty shorts to cute dresses, perfect for a busy lifestyle.",
        "Fun, fashionable, and functional, this kids' clothing collection offers great styles for boys and girls alike."
    ],
    "footwear": [
        "Step out in style with this collection of footwear, offering comfort, durability, and trendsetting designs.",
        "From sporty sneakers to classic boots, this collection of footwear has something for every occasion.",
        "Crafted for comfort and style, these shoes combine cutting-edge design with all-day wearability.",
        "Sleek, durable, and fashionable, this collection of footwear is designed to keep your feet happy and stylish.",
        "High-performance footwear designed for active lifestyles, from running shoes to hiking boots.",
        "Step into luxury with these premium shoes, featuring quality craftsmanship and modern design elements.",
        "From casual slip-ons to elegant heels, this footwear collection offers versatile styles for any outfit.",
        "Comfortable, stylish, and long-lasting, this collection of footwear is perfect for every season.",
        "Sporty and chic, this collection of footwear is designed to complement your active lifestyle while keeping you stylish.",
        "Discover timeless footwear styles that blend classic designs with contemporary twists for a modern look."
    ],
    "bags-backpacks": [
        "From sleek backpacks to stylish totes, this collection of bags offers functionality with flair.",
        "A versatile range of bags and backpacks designed for work, travel, and everyday use, combining style and practicality.",
        "Classic and modern styles collide in this collection of bags, perfect for the woman on the go.",
        "Travel in style with these premium bags and backpacks designed for durability, comfort, and aesthetics.",
        "Designed for fashion-conscious individuals, these bags and backpacks combine practicality with high-end design.",
        "Carry your essentials in style with this collection of chic handbags and functional backpacks.",
        "Elevate your look with these elegant bags, featuring timeless designs and practical compartments.",
        "Whether you’re commuting or exploring, this collection of bags and backpacks offers versatility and style.",
        "Durable, spacious, and stylish, these bags and backpacks are perfect for travel, work, and leisure.",
        "Bold and sophisticated, this collection of bags offers a mix of contemporary designs with classic elements."
    ],
    "watches": [
        "Timeless elegance and cutting-edge technology come together in this range of luxury and sports watches.",
        "Whether you’re after a statement piece or a durable everyday watch, this collection has something for everyone.",
        "Crafted to perfection, these watches combine precision, style, and sophistication in one stunning accessory.",
        "From classic designs to innovative smartwatches, this collection of timepieces is perfect for all occasions.",
        "A collection of elegant and modern watches, offering a variety of styles for every taste and need.",
        "Premium watches with impeccable craftsmanship, blending traditional techniques with contemporary designs.",
        "Durable and stylish, these watches offer both form and function, perfect for the active individual.",
        "Stay on time in style with these watches, featuring sleek designs and cutting-edge technology.",
        "From luxury to casual, this range of watches offers both performance and elegance for every lifestyle.",
        "A stunning collection of watches that combine classic designs with modern innovation."
    ],
    "sunglasses": [
        "Sleek, stylish, and functional, this collection of sunglasses offers protection and fashion in one.",
        "From aviators to oversized frames, this collection of sunglasses offers a range of designs to complement every face.",
        "UV protection meets high fashion in this collection of sunglasses, designed to elevate your style.",
        "Bold, chic, and protective, these sunglasses offer timeless designs for every occasion.",
        "Stay cool under the sun with these stylish sunglasses, combining fashion and functionality.",
        "From retro to contemporary, this collection of sunglasses offers a mix of classic and modern styles.",
        "Crafted with quality materials, these sunglasses combine eye protection with statement-making designs.",
        "Perfect for every season, these sunglasses offer superior UV protection with stylish frames.",
        "Chic, stylish, and designed to complement any look, this collection of sunglasses is a must-have accessory.",
        "Sophisticated designs and high-quality lenses come together in this collection of sunglasses."
    ],
    "hats-caps": [
        "From classic baseball caps to modern fedoras, this collection of hats offers versatile styles for every occasion.",
        "Stylish, functional, and comfortable, these hats are perfect for sun protection and fashion.",
        "Chic and trendy, these hats and caps are designed to elevate your look while keeping you cool.",
        "From bucket hats to snapbacks, this collection of hats offers a variety of styles for different tastes.",
        "Durable and stylish, these hats provide protection from the sun while complementing your outfit.",
        "Casual yet stylish, this range of hats and caps are perfect for everyday wear and special occasions.",
        "From sports caps to trendy berets, this collection of hats offers something for every style and mood.",
        "Fashion-forward and comfortable, these hats are perfect for adding a unique touch to any outfit.",
        "Effortless and stylish, this collection of hats and caps is perfect for the modern individual.",
        "A wide range of hats and caps, from sporty to chic, to complete your look in style."
    ],
    "jewelry": [
        "Luxury, elegance, and timeless beauty define this collection of fine jewelry, featuring stunning pieces for every occasion.",
        "From sparkling diamond rings to intricate gold necklaces, this collection offers high-end jewelry for every taste.",
        "Sleek and sophisticated, this collection of jewelry adds the perfect finishing touch to any outfit.",
        "From classic designs to modern twists, this range of jewelry features timeless pieces for every occasion.",
        "Elegant and refined, this jewelry collection offers sparkling diamonds, gold, and silver to complement any style.",
        "Crafted with precision, this jewelry collection offers both luxury and everyday elegance.",
        "Add a touch of glamour to your wardrobe with these exquisite jewelry pieces, perfect for any event.",
        "From delicate earrings to statement necklaces, this collection offers a wide range of luxurious jewelry.",
        "Sophisticated, beautiful, and meticulously crafted, this jewelry collection is made for the discerning individual.",
        "Timeless designs and intricate craftsmanship come together in this stunning collection of fine jewelry."
    ],
    "sportswear": [
        "This collection of sportswear offers both performance and style, combining comfort with cutting-edge design.",
        "From running tights to breathable tops, this sportswear collection is designed to keep you active and stylish.",
        "Whether you’re hitting the gym or going for a run, this sportswear range offers comfort and durability.",
        "High-performance sportswear designed for athletes who demand both function and fashion.",
        "From athletic leggings to performance jackets, this collection offers everything you need for an active lifestyle.",
        "Sporty, stylish, and functional, this sportswear collection is designed to keep you moving.",
        "Innovative sportswear designed with the latest fabric technology for comfort, flexibility, and performance.",
        "Built for performance, this sportswear collection combines durability with sleek, modern designs.",
        "Whether you’re working out or relaxing, this sportswear collection offers the perfect balance of comfort and style.",
        "This sportswear range blends functionality with fashion, providing athletic wear that’s as stylish as it is practical."
    ]
}

features = {
    "mens-clothing": {
        "Fabric": ["100% cotton", "Linen blend", "Polyester-spandex mix", "Merino wool", "Tencel fabric"],
        "Fit": ["Slim fit", "Regular fit", "Loose fit", "Athletic fit", "Tailored fit"],
        "Style": ["Casual", "Formal", "Streetwear", "Business casual", "Athleisure"],
        "Details": ["Button-down collar", "Double-breasted", "Distressed finish", "Zippered pockets", "Embroidered logo"],
        "Season": ["Spring/Summer", "Fall/Winter", "All-season", "Transitional"],
        "Care": ["Machine washable", "Dry clean only", "Hand wash", "Wrinkle-resistant"],
        "Sustainability": ["Eco-friendly fabrics", "Recycled polyester", "Organic cotton", "Fair trade certified"]
    },
    "womens-clothing": {
        "Fabric": ["Silk", "Chiffon", "Cotton blend", "Stretch jersey", "Velvet"],
        "Fit": ["Bodycon", "A-line", "High-waisted", "Straight-leg", "Loose fit"],
        "Style": ["Casual", "Evening wear", "Business formal", "Bohemian", "Minimalist"],
        "Details": ["Lace trim", "Pleated skirt", "Ruffle detailing", "Fringe accents", "Tulle overlay"],
        "Season": ["Spring/Summer", "Fall/Winter", "Resort", "Year-round"],
        "Care": ["Hand wash cold", "Dry clean", "Machine washable", "Delicate cycle"],
        "Sustainability": ["Recycled fabrics", "Fair trade materials", "Vegan leather", "Ethically produced"]
    },
    "kids-clothing": {
        "Fabric": ["Soft cotton", "Fleece", "Stretch denim", "Jersey knit", "Terrycloth"],
        "Fit": ["Relaxed fit", "Roomy fit", "Tapered fit", "Adjustable waistbands", "Easy-to-wear"],
        "Style": ["Playwear", "School uniforms", "Activewear", "Holiday attire", "Casual"],
        "Details": ["Elastic waistbands", "Cartoon character prints", "Button-down shirts", "Belt loops", "Knee patches"],
        "Season": ["Spring/Summer", "Fall/Winter", "Rainy season", "Layered clothing"],
        "Care": ["Machine washable", "Dry clean", "Easy-care fabric", "Quick-dry"],
        "Sustainability": ["Organic cotton", "Sustainable dyes", "Eco-friendly production", "Recycled materials"]
    },
    "footwear": {
        "Material": ["Leather", "Suede", "Mesh fabric", "Rubber", "Synthetic leather"],
        "Fit": ["Standard", "Wide fit", "Slim fit", "Ankle support", "Arch support"],
        "Style": ["Sneakers", "Boots", "Loafers", "Sandals", "High heels"],
        "Sole": ["Rubber sole", "Cushioned insole", "Leather sole", "Anti-slip sole", "Arch support sole"],
        "Season": ["Summer", "Winter", "Rainy season", "All-season"],
        "Details": ["Lace-up", "Velcro straps", "Buckle closures", "Elasticated bands", "Perforated design"],
        "Care": ["Waterproof", "Easy to clean", "Leather care instructions", "Machine washable"],
        "Sustainability": ["Recycled rubber", "Vegan leather", "Eco-friendly dyes", "Ethical manufacturing"]
    },
    "bags-backpacks": {
        "Material": ["Leather", "Nylon", "Canvas", "Polyester", "Vegan leather"],
        "Style": ["Backpack", "Tote", "Crossbody", "Clutch", "Duffel bag"],
        "Compartments": ["Laptop compartment", "Zippered pockets", "Hidden compartments", "Water bottle holder", "Cardholder slots"],
        "Closure": ["Zipper closure", "Magnetic flap", "Drawstring closure", "Buckle strap", "Snap button"],
        "Season": ["Year-round", "Spring/Summer", "Fall/Winter"],
        "Details": ["Gold hardware", "Tassel accents", "Embossed logo", "Quilted texture", "Rivets and studs"],
        "Sustainability": ["Recycled fabric", "Ethically sourced leather", "Eco-friendly packaging", "Fair trade certified"]
    },
    "watches": {
        "Material": ["Stainless steel", "Ceramic", "Titanium", "Leather", "Silicone"],
        "Style": ["Analog", "Digital", "Smartwatch", "Hybrid", "Luxury"],
        "Movement": ["Quartz", "Automatic", "Solar-powered", "Mechanical"],
        "Water Resistance": ["Waterproof", "Splash resistant", "Diving depth (50m, 100m, etc.)"],
        "Strap": ["Leather strap", "Metal band", "Silicone strap", "Nylon strap", "Stainless steel"],
        "Display": ["LCD", "LED", "Touchscreen", "Tachymeter", "Dual time zone"],
        "Features": ["Heart rate monitor", "GPS tracking", "Sleep tracking", "Altimeter", "Wireless charging"],
        "Sustainability": ["Recycled materials", "Solar-powered", "Eco-friendly packaging"]
    },
    "sunglasses": {
        "Frame Material": ["Metal", "Plastic", "Wood", "Acetate", "Titanium"],
        "Lens Type": ["Polarized", "UV protection", "Photochromic", "Mirror lenses", "Gradient lenses"],
        "Style": ["Aviator", "Wayfarer", "Round", "Cat-eye", "Square"],
        "Features": ["Scratch-resistant coating", "Anti-glare", "UV400 protection", "Impact-resistant", "Lightweight"],
        "Season": ["Summer", "All-year-round", "Beachwear", "Travel"],
        "Fit": ["Standard", "Wide fit", "Slim fit", "Unisex", "Custom fit"],
        "Care": ["Cleaning cloth included", "Case for storage", "Scratch-proof lens coating"],
        "Sustainability": ["Recycled frames", "Eco-friendly lenses", "Biodegradable packaging"]
    },
    "hats-caps": {
        "Material": ["Cotton", "Wool", "Polyester", "Leather", "Straw"],
        "Style": ["Baseball cap", "Fedora", "Beanie", "Bucket hat", "Panama hat"],
        "Fit": ["Adjustable", "Snapback", "Fitted", "Stretch-fit"],
        "Details": ["Embroidered logo", "Printed patterns", "Metal eyelets", "Braid detailing", "Woolen knit"],
        "Season": ["Summer", "Winter", "Transitional"],
        "Care": ["Machine washable", "Hand wash", "Spot clean", "Air dry"],
        "Sustainability": ["Organic cotton", "Recycled fabrics", "Vegan leather"]
    },
    "jewelry": {
        "Material": ["Gold", "Silver", "Platinum", "Diamond", "Gemstone"],
        "Style": ["Pendant", "Earrings", "Rings", "Bracelets", "Necklaces"],
        "Finish": ["Matte", "Polished", "Brushed", "Antique"],
        "Setting": ["Prong setting", "Bezel setting", "Channel setting", "Flush setting"],
        "Details": ["Engraved", "Gem-studded", "Pearl accents", "Diamond pave", "Textured design"],
        "Sustainability": ["Conflict-free diamonds", "Recycled gold", "Fair trade certified materials", "Eco-friendly production"]
    },
    "sportswear": {
        "Material": ["Spandex", "Polyester", "Nylon", "Mesh", "Cotton blend"],
        "Style": ["Compression gear", "Activewear", "Yoga pants", "Running shorts", "Training tops"],
        "Fit": ["Slim fit", "Loose fit", "Relaxed fit", "Body-hugging", "Athletic fit"],
        "Features": ["Moisture-wicking", "Breathable", "Quick-dry", "Anti-odor", "UV protection"],
        "Season": ["Summer", "Winter", "All-season", "Transitional"],
        "Care": ["Machine washable", "Dry clean", "Easy-care fabric", "Tumble dry low"],
        "Sustainability": ["Recycled fabrics", "Eco-friendly dyes", "Fair trade certified", "Sustainable materials"]
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

with open("fake_products.json", "w") as f:
    json.dump(dataset, f, indent=4)

print("Fake product dataset with 500 products generated successfully!")
