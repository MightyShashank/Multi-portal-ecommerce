import json
import random
import uuid
from faker import Faker

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
        ("Slim Fit Jeans", "Levi's", "LJ-001", []),
        ("Straight Fit Jeans", "Levi's", "LSJ-002", []),
        ("Denim Jacket", "Levi's", "LDJ-003", []),
        ("Classic Trucker Jacket", "Levi's", "LTJ-004", []),
        ("Relaxed Fit Jeans", "Levi's", "LRJ-005", []),

        # H&M
        ("Oxford Shirt", "H&M", "HS-001", []),
        ("Crew Neck T-Shirt", "H&M", "HT-002", []),
        ("Slim Fit Blazer", "H&M", "HB-003", []),
        ("Cotton Chinos", "H&M", "HC-004", []),
        ("Casual Hoodie", "H&M", "HH-005", []),

        # Zara
        ("Tailored Blazer", "Zara", "ZB-001", []),
        ("Skinny Fit Jeans", "Zara", "ZJ-002", []),
        ("Polo T-Shirt", "Zara", "ZP-003", []),
        ("Wool Overcoat", "Zara", "ZO-004", []),
        ("Bomber Jacket", "Zara", "ZBJ-005", []),

        # Uniqlo
        ("Chinos", "Uniqlo", "UC-001", []),
        ("Linen Shirt", "Uniqlo", "ULS-002", []),
        ("Ultra Light Down Jacket", "Uniqlo", "UDJ-003", []),
        ("Regular Fit Jeans", "Uniqlo", "URJ-004", []),
        ("Crew Neck Sweater", "Uniqlo", "US-005", []),

        # Ted Baker
        ("Leather Jacket", "Ted Baker", "TLJ-001", []),
        ("Wool Suit Jacket", "Ted Baker", "TWJ-002", []),
        ("Slim Fit Suit Pants", "Ted Baker", "TSP-003", []),
        ("Checked Blazer", "Ted Baker", "TCB-004", []),
        ("Tweed Waistcoat", "Ted Baker", "TWC-005", []),

        # Ralph Lauren
        ("Polo Shirt", "Ralph Lauren", "RP-001", []),
        ("Chino Shorts", "Ralph Lauren", "RCS-002", []),
        ("Sweater Vest", "Ralph Lauren", "RSV-003", []),
        ("Cotton Trousers", "Ralph Lauren", "RCT-004", []),
        ("Double Breasted Blazer", "Ralph Lauren", "RDB-005", []),

        # Adidas
        ("Sports Hoodie", "Adidas", "AH-001", []),
        ("Training Joggers", "Adidas", "AJ-002", []),
        ("Graphic Print T-Shirt", "Adidas", "AT-003", []),
        ("Full-Zip Track Jacket", "Adidas", "ATJ-004", []),
        ("Athletic Shorts", "Adidas", "AS-005", []),

        # Nike
        ("Dri-FIT T-Shirt", "Nike", "NT-001", []),
        ("Running Shorts", "Nike", "NS-002", []),
        ("Compression Leggings", "Nike", "NL-003", []),
        ("Pullover Hoodie", "Nike", "NH-004", []),
        ("Basketball Jersey", "Nike", "NBJ-005", []),

        # Tommy Hilfiger
        ("Striped Polo Shirt", "Tommy Hilfiger", "TP-001", []),
        ("Slim Fit Dress Shirt", "Tommy Hilfiger", "TDS-002", []),
        ("Cotton Cardigan", "Tommy Hilfiger", "TC-003", []),
        ("V-Neck Sweater", "Tommy Hilfiger", "TVS-004", []),
        ("Checked Flannel Shirt", "Tommy Hilfiger", "TFS-005", []),

        # Calvin Klein
        ("Slim Fit Suit", "Calvin Klein", "CKS-001", []),
        ("Performance Track Pants", "Calvin Klein", "CKP-002", []),
        ("Minimalist Crew Sweatshirt", "Calvin Klein", "CKSW-003", []),
        ("Lounge Joggers", "Calvin Klein", "CKJ-004", []),
        ("Tailored Overcoat", "Calvin Klein", "CKO-005", [])
    ],
    "womens-clothing": [
        # Zara
        ("Floral Dress", "Zara", "ZD-001", []),
        ("Pleated Midi Skirt", "Zara", "ZMS-002", []),
        ("Satin Wrap Dress", "Zara", "ZWD-003", []),
        ("Tailored Blazer", "Zara", "ZB-004", []),
        ("Printed Maxi Dress", "Zara", "ZMD-005", []),

        # Levi's
        ("Denim Jacket", "Levi's", "LJ-001", []),
        ("High-Rise Skinny Jeans", "Levi's", "LJS-002", []),
        ("Boyfriend Fit Jeans", "Levi's", "LBJ-003", []),
        ("Denim Shirt Dress", "Levi's", "LSD-004", []),
        ("Classic Trucker Jacket", "Levi's", "LTJ-005", []),

        # H&M
        ("High-Waist Skirt", "H&M", "HS-001", []),
        ("Basic Crew Neck T-Shirt", "H&M", "HT-002", []),
        ("V-Neck Blouse", "H&M", "HVB-003", []),
        ("Oversized Sweater", "H&M", "HOS-004", []),
        ("Faux Leather Jacket", "H&M", "HLJ-005", []),

        # Mango
        ("Casual Blouse", "Mango", "MB-001", []),
        ("Tailored Trousers", "Mango", "MTT-002", []),
        ("Wrap Midi Dress", "Mango", "MWD-003", []),
        ("Striped Shirt", "Mango", "MSS-004", []),
        ("Cropped Cardigan", "Mango", "MCC-005", []),

        # Uniqlo
        ("Peacoat", "Uniqlo", "UC-001", []),
        ("Linen Shirt", "Uniqlo", "ULS-002", []),
        ("Knit Sweater", "Uniqlo", "UKS-003", []),
        ("A-Line Skirt", "Uniqlo", "UAS-004", []),
        ("Down Puffer Jacket", "Uniqlo", "UDP-005", []),

        # Ralph Lauren
        ("Cable Knit Sweater", "Ralph Lauren", "RKS-001", []),
        ("Wool Overcoat", "Ralph Lauren", "RWO-002", []),
        ("Slim Fit Polo", "Ralph Lauren", "RSP-003", []),
        ("Cotton Midi Dress", "Ralph Lauren", "RMD-004", []),
        ("Tailored Vest", "Ralph Lauren", "RTV-005", []),

        # Adidas
        ("Sports Leggings", "Adidas", "AL-001", []),
        ("Performance Hoodie", "Adidas", "AH-002", []),
        ("Training Shorts", "Adidas", "AS-003", []),
        ("Full-Zip Track Jacket", "Adidas", "ATJ-004", []),
        ("Athletic Tank Top", "Adidas", "ATT-005", []),

        # Nike
        ("Dri-FIT Tights", "Nike", "NT-001", []),
        ("Running Shorts", "Nike", "NS-002", []),
        ("Compression Sports Bra", "Nike", "NB-003", []),
        ("Pullover Hoodie", "Nike", "NH-004", []),
        ("Training Joggers", "Nike", "NJ-005", []),

        # Tommy Hilfiger
        ("Striped Wrap Dress", "Tommy Hilfiger", "TWD-001", []),
        ("Casual Denim Shirt", "Tommy Hilfiger", "TDS-002", []),
        ("Classic Polo Shirt", "Tommy Hilfiger", "TPS-003", []),
        ("Cotton Trousers", "Tommy Hilfiger", "TCT-004", []),
        ("V-Neck Knit Sweater", "Tommy Hilfiger", "TVS-005", []),

        # Calvin Klein
        ("Slim Fit Suit", "Calvin Klein", "CKS-001", []),
        ("Performance Leggings", "Calvin Klein", "CKL-002", []),
        ("Minimalist Sweatshirt", "Calvin Klein", "CKSW-003", []),
        ("Lounge Joggers", "Calvin Klein", "CKJ-004", []),
        ("Tailored Overcoat", "Calvin Klein", "CKO-005", [])
    ],
    "kids-clothing": [
        # Carter's
        ("Graphic T-shirt", "Carter's", "CT-001", []),
        ("Striped Pajamas", "Carter's", "CPJ-002", []),
        ("Denim Shorts", "Carter's", "CDS-003", []),
        ("Winter Sweater", "Carter's", "CWS-004", []),
        ("Hooded Jacket", "Carter's", "CHJ-005", []),

        # Nike
        ("Jogger Pants", "Nike", "JP-006", []),
        ("Dri-FIT Training Shorts", "Nike", "NTS-007", []),
        ("Performance Hoodie", "Nike", "NPH-008", []),
        ("Sports Leggings", "Nike", "NSL-009", []),
        ("Running Sneakers", "Nike", "NRS-010", []),

        # Burt's Bees Baby
        ("Baby Onesie", "Burt's Bees Baby", "BB-011", []),
        ("Organic Cotton Romper", "Burt's Bees Baby", "BBR-012", []),
        ("Sleeper Gown", "Burt's Bees Baby", "BBSG-013", []),
        ("Baby Mittens", "Burt's Bees Baby", "BBM-014", []),
        ("Swaddle Blanket", "Burt's Bees Baby", "BBS-015", []),

        # Old Navy
        ("Denim Overalls", "Old Navy", "ON-016", []),
        ("Plaid Button-Up Shirt", "Old Navy", "ONB-017", []),
        ("Fleece Pullover", "Old Navy", "ONF-018", []),
        ("Cotton Chinos", "Old Navy", "ONC-019", []),
        ("Printed Leggings", "Old Navy", "ONL-020", []),

        # Columbia
        ("Puffer Jacket", "Columbia", "CJ-021", []),
        ("Waterproof Raincoat", "Columbia", "CR-022", []),
        ("Snow Bib Overalls", "Columbia", "CSB-023", []),
        ("Insulated Gloves", "Columbia", "CIG-024", []),
        ("Thermal Base Layer", "Columbia", "CTB-025", []),

        # Gap
        ("Knit Sweater", "Gap", "GKS-026", []),
        ("Cargo Pants", "Gap", "GCP-027", []),
        ("Denim Jacket", "Gap", "GDJ-028", []),
        ("Softshell Hoodie", "Gap", "GSH-029", []),
        ("Printed Romper", "Gap", "GR-030", []),

        # The Children's Place
        ("Plaid Flannel Shirt", "The Children's Place", "TCPF-031", []),
        ("School Uniform Pants", "The Children's Place", "TCPS-032", []),
        ("Winter Coat", "The Children's Place", "TCPW-033", []),
        ("Knit Beanie", "The Children's Place", "TCPB-034", []),
        ("Tulle Skirt", "The Children's Place", "TCPT-035", []),

        # Adidas
        ("Track Suit", "Adidas", "ATS-036", []),
        ("Soccer Jersey", "Adidas", "ASJ-037", []),
        ("Fleece Sweatpants", "Adidas", "AFP-038", []),
        ("Baseball Cap", "Adidas", "ABC-039", []),
        ("Lightweight Windbreaker", "Adidas", "ALW-040", []),

        # Tommy Hilfiger
        ("Classic Polo Shirt", "Tommy Hilfiger", "THP-041", []),
        ("Cable Knit Cardigan", "Tommy Hilfiger", "THC-042", []),
        ("Linen Shorts", "Tommy Hilfiger", "THLS-043", []),
        ("Crew Neck Pullover", "Tommy Hilfiger", "THN-044", []),
        ("Dress Shirt", "Tommy Hilfiger", "THD-045", []),

        # H&M
        ("Long Sleeve Henley", "H&M", "HHL-046", []),
        ("Stretch Denim Jeans", "H&M", "HJD-047", []),
        ("Fleece Joggers", "H&M", "HFJ-048", []),
        ("Waterproof Snow Boots", "H&M", "HSB-049", []),
        ("Soft Cotton Hoodie", "H&M", "HCH-050", [])
    ],
    "footwear": [
        # Nike
        ("Air Jordan 1", "Nike", "AJ1-001", []),
        ("Air Force 1", "Nike", "AF1-002", []),
        ("React Infinity Run", "Nike", "RIR-003", []),
        ("ZoomX Vaporfly", "Nike", "ZV-004", []),
        ("Blazer Mid '77", "Nike", "BM77-005", []),

        # Adidas
        ("Stan Smith Sneakers", "Adidas", "SS-006", []),
        ("Ultraboost 22", "Adidas", "UB-007", []),
        ("Superstar Sneakers", "Adidas", "SST-008", []),
        ("NMD R1", "Adidas", "NMD-009", []),
        ("Gazelle Shoes", "Adidas", "GZL-010", []),

        # Dr. Martens
        ("Chelsea Boots", "Dr. Martens", "DM-011", []),
        ("1460 Smooth Leather Boots", "Dr. Martens", "DM1460-012", []),
        ("Jadon Platform Boots", "Dr. Martens", "DMJP-013", []),
        ("1461 Oxford Shoes", "Dr. Martens", "DM1461-014", []),
        ("Combs Tech Boots", "Dr. Martens", "DMCB-015", []),

        # Birkenstock
        ("Classic Sandals", "Birkenstock", "BS-016", []),
        ("Arizona Soft Footbed", "Birkenstock", "AZ-017", []),
        ("Gizeh Sandals", "Birkenstock", "GZ-018", []),
        ("Boston Clogs", "Birkenstock", "BC-019", []),
        ("Mayari Sandals", "Birkenstock", "MY-020", []),

        # Puma
        ("Running Shoes", "Puma", "RS-021", []),
        ("Future Rider", "Puma", "FR-022", []),
        ("Cali Star Sneakers", "Puma", "CS-023", []),
        ("Suede Classic", "Puma", "SC-024", []),
        ("Deviate Nitro", "Puma", "DN-025", []),

        # Converse
        ("Chuck Taylor All Star", "Converse", "CTAS-026", []),
        ("Run Star Hike", "Converse", "RSH-027", []),
        ("Jack Purcell", "Converse", "JP-028", []),
        ("One Star Sneakers", "Converse", "OS-029", []),
        ("Chuck 70 High Top", "Converse", "C70-030", []),

        # Reebok
        ("Classic Leather", "Reebok", "CL-031", []),
        ("Club C 85", "Reebok", "CC85-032", []),
        ("Nano X2 Training Shoes", "Reebok", "NX2-033", []),
        ("Zig Kinetica 2.5", "Reebok", "ZK-034", []),
        ("Pump Omni Zone II", "Reebok", "POZ-035", []),

        # New Balance
        ("574 Core Sneakers", "New Balance", "NB574-036", []),
        ("990v5", "New Balance", "NB990-037", []),
        ("327 Sneakers", "New Balance", "NB327-038", []),
        ("Fresh Foam 1080v12", "New Balance", "NBFF-039", []),
        ("FuelCell Rebel v3", "New Balance", "NBFC-040", []),

        # Vans
        ("Old Skool Sneakers", "Vans", "OSV-041", []),
        ("Sk8-Hi", "Vans", "SHV-042", []),
        ("Authentic Sneakers", "Vans", "ASV-043", []),
        ("Slip-On Classic", "Vans", "SOC-044", []),
        ("UltraRange EXO", "Vans", "URE-045", []),

        # Timberland
        ("Premium 6-Inch Boots", "Timberland", "T6B-046", []),
        ("Earthkeepers Boots", "Timberland", "TEB-047", []),
        ("Chukka Boots", "Timberland", "TCB-048", []),
        ("Pro Work Boots", "Timberland", "TPWB-049", []),
        ("Euro Hiker Boots", "Timberland", "TEH-050", [])
    ],
    "bags-backpacks": [
        # North Face
        ("Backpack", "North Face", "NF-001", []),
        ("Hiking Backpack", "North Face", "NFH-002", []),
        ("Daypack", "North Face", "NFD-003", []),
        ("Laptop Backpack", "North Face", "NFL-004", []),
        ("Travel Backpack", "North Face", "NFT-005", []),

        # Kate Spade
        ("Tote Bag", "Kate Spade", "KS-001", []),
        ("Canvas Tote", "Kate Spade", "KSC-002", []),
        ("Leather Tote", "Kate Spade", "KSL-003", []),
        ("Quilted Tote", "Kate Spade", "KSQ-004", []),
        ("Mini Tote", "Kate Spade", "KSM-005", []),

        # Coach
        ("Leather Messenger Bag", "Coach", "CM-001", []),
        ("Canvas Messenger Bag", "Coach", "CMC-002", []),
        ("Slim Messenger Bag", "Coach", "CMS-003", []),
        ("Flap Messenger Bag", "Coach", "CMF-004", []),
        ("Vintage Messenger Bag", "Coach", "CMV-005", []),

        # Under Armour
        ("Duffel Bag", "Under Armour", "UA-001", []),
        ("Gym Duffel Bag", "Under Armour", "UAG-002", []),
        ("Travel Duffel Bag", "Under Armour", "UAT-003", []),
        ("Waterproof Duffel", "Under Armour", "UAW-004", []),
        ("Compact Duffel", "Under Armour", "UAC-005", []),

        # Michael Kors
        ("Crossbody Bag", "Michael Kors", "MK-001", []),
        ("Mini Crossbody", "Michael Kors", "MKM-002", []),
        ("Leather Crossbody", "Michael Kors", "MKL-003", []),
        ("Convertible Crossbody", "Michael Kors", "MKC-004", []),
        ("Chain Crossbody", "Michael Kors", "MKCH-005", []),

        # Samsonite
        ("Rolling Suitcase", "Samsonite", "SRS-001", []),
        ("Carry-On Suitcase", "Samsonite", "SCO-002", []),
        ("Hard Shell Suitcase", "Samsonite", "SHS-003", []),
        ("Expandable Suitcase", "Samsonite", "SES-004", []),
        ("Spinner Luggage", "Samsonite", "SSL-005", []),

        # Tumi
        ("Briefcase", "Tumi", "TB-001", []),
        ("Expandable Briefcase", "Tumi", "TEB-002", []),
        ("Laptop Briefcase", "Tumi", "TLB-003", []),
        ("Leather Briefcase", "Tumi", "TLBR-004", []),
        ("Convertible Briefcase", "Tumi", "TCB-005", []),

        # Herschel
        ("Classic Backpack", "Herschel", "HB-001", []),
        ("Little America Backpack", "Herschel", "HLA-002", []),
        ("City Backpack", "Herschel", "HCB-003", []),
        ("Hiking Backpack", "Herschel", "HHB-004", []),
        ("Duffle Backpack", "Herschel", "HDB-005", []),

        # Patagonia
        ("Eco-friendly Backpack", "Patagonia", "PB-001", []),
        ("Waterproof Backpack", "Patagonia", "PWB-002", []),
        ("Travel Backpack", "Patagonia", "PTB-003", []),
        ("Climbing Backpack", "Patagonia", "PCB-004", []),
        ("Sling Backpack", "Patagonia", "PSB-005", []),

        # Louis Vuitton
        ("Designer Tote Bag", "Louis Vuitton", "LVT-001", []),
        ("Luxury Crossbody", "Louis Vuitton", "LVC-002", []),
        ("Monogram Handbag", "Louis Vuitton", "LVH-003", []),
        ("Leather Shoulder Bag", "Louis Vuitton", "LVS-004", []),
        ("Backpack Purse", "Louis Vuitton", "LVP-005", [])
    ],
    "watches": [
        # Rolex
        ("Rolex Submariner", "Rolex", "RS-001", []),
        ("Rolex Daytona", "Rolex", "RD-002", []),
        ("Rolex Datejust", "Rolex", "RDJ-003", []),
        ("Rolex GMT-Master II", "Rolex", "RGMT-004", []),
        ("Rolex Explorer", "Rolex", "RE-005", []),

        # Apple
        ("Apple Watch Series 8", "Apple", "AW8-006", []),
        ("Apple Watch Ultra", "Apple", "AWU-007", []),
        ("Apple Watch SE", "Apple", "AWSE-008", []),
        ("Apple Watch Nike Edition", "Apple", "AWN-009", []),
        ("Apple Watch Hermes", "Apple", "AWH-010", []),

        # Casio
        ("Casio G-Shock", "Casio", "GS-011", []),
        ("Casio Edifice", "Casio", "CE-012", []),
        ("Casio Pro Trek", "Casio", "CPT-013", []),
        ("Casio Vintage", "Casio", "CV-014", []),
        ("Casio Classic Digital", "Casio", "CCD-015", []),

        # Omega
        ("Omega Speedmaster", "Omega", "OS-016", []),
        ("Omega Seamaster", "Omega", "OSEA-017", []),
        ("Omega Constellation", "Omega", "OC-018", []),
        ("Omega De Ville", "Omega", "ODV-019", []),
        ("Omega Aqua Terra", "Omega", "OAT-020", []),

        # Fossil
        ("Fossil Hybrid HR", "Fossil", "FH-021", []),
        ("Fossil Gen 6 Smartwatch", "Fossil", "FG6-022", []),
        ("Fossil Townsman", "Fossil", "FT-023", []),
        ("Fossil Neutra Chronograph", "Fossil", "FNC-024", []),
        ("Fossil Minimalist", "Fossil", "FM-025", []),

        # Seiko
        ("Seiko 5 Sports", "Seiko", "S5S-026", []),
        ("Seiko Prospex", "Seiko", "SPX-027", []),
        ("Seiko Presage", "Seiko", "SPG-028", []),
        ("Seiko Astron", "Seiko", "SA-029", []),
        ("Seiko Premier", "Seiko", "SPR-030", []),

        # TAG Heuer
        ("TAG Heuer Carrera", "TAG Heuer", "THC-031", []),
        ("TAG Heuer Monaco", "TAG Heuer", "THM-032", []),
        ("TAG Heuer Aquaracer", "TAG Heuer", "THA-033", []),
        ("TAG Heuer Formula 1", "TAG Heuer", "THF1-034", []),
        ("TAG Heuer Link", "TAG Heuer", "THL-035", []),

        # Tissot
        ("Tissot PRX", "Tissot", "TPRX-036", []),
        ("Tissot Seastar", "Tissot", "TSS-037", []),
        ("Tissot Heritage", "Tissot", "TH-038", []),
        ("Tissot Supersport", "Tissot", "TSP-039", []),
        ("Tissot Chrono XL", "Tissot", "TCXL-040", []),

        # Citizen
        ("Citizen Eco-Drive", "Citizen", "CED-041", []),
        ("Citizen Promaster", "Citizen", "CPR-042", []),
        ("Citizen Aqualand", "Citizen", "CAQ-043", []),
        ("Citizen Nighthawk", "Citizen", "CNH-044", []),
        ("Citizen Satellite Wave", "Citizen", "CSW-045", []),

        # Breitling
        ("Breitling Navitimer", "Breitling", "BN-046", []),
        ("Breitling Superocean", "Breitling", "BSO-047", []),
        ("Breitling Chronomat", "Breitling", "BCM-048", []),
        ("Breitling Avenger", "Breitling", "BA-049", []),
        ("Breitling Premier", "Breitling", "BP-050", [])
    ],
    "sunglasses": [
        # Ray-Ban
        ("Aviator Sunglasses", "Ray-Ban", "RB-001", []),
        ("Wayfarer Sunglasses", "Ray-Ban", "WB-002", []),
        ("Clubmaster", "Ray-Ban", "CB-003", []),
        ("Round Metal Sunglasses", "Ray-Ban", "RM-004", []),
        ("Justin Sunglasses", "Ray-Ban", "JRB-005", []),

        # Oakley
        ("Polarized Sunglasses", "Oakley", "OS-006", []),
        ("Flak 2.0 XL", "Oakley", "F2X-007", []),
        ("Radar EV Path", "Oakley", "REP-008", []),
        ("Holbrook Sunglasses", "Oakley", "HBS-009", []),
        ("Frogskins Sunglasses", "Oakley", "FS-010", []),

        # Maui Jim
        ("Round Sunglasses", "Maui Jim", "MJ-011", []),
        ("Mavericks Polarized", "Maui Jim", "MJP-012", []),
        ("Peahi Wrap Sunglasses", "Maui Jim", "PWS-013", []),
        ("Kupuna Aviators", "Maui Jim", "KA-014", []),
        ("Ho’okipa Rimless", "Maui Jim", "HR-015", []),

        # Persol
        ("Persol 714 Foldable", "Persol", "P714-016", []),
        ("Persol 649 Original", "Persol", "P649-017", []),
        ("Persol Steve McQueen", "Persol", "PSM-018", []),
        ("Persol Polarized", "Persol", "PP-019", []),
        ("Persol Rectangular", "Persol", "PR-020", []),

        # Prada
        ("Prada Linea Rossa", "Prada", "PLR-021", []),
        ("Prada Catwalk", "Prada", "PCW-022", []),
        ("Prada Square Sunglasses", "Prada", "PSS-023", []),
        ("Prada Pilot Sunglasses", "Prada", "PPS-024", []),
        ("Prada Rimless Shield", "Prada", "PRS-025", []),

        # Gucci
        ("Gucci Oversized Sunglasses", "Gucci", "GOS-026", []),
        ("Gucci Rectangular Sunglasses", "Gucci", "GRS-027", []),
        ("Gucci Round Frame", "Gucci", "GRF-028", []),
        ("Gucci Cat Eye", "Gucci", "GCE-029", []),
        ("Gucci Geometric", "Gucci", "GG-030", []),

        # Tom Ford
        ("Tom Ford Marko Aviator", "Tom Ford", "TFM-031", []),
        ("Tom Ford Snowdon", "Tom Ford", "TFS-032", []),
        ("Tom Ford Henry", "Tom Ford", "TFH-033", []),
        ("Tom Ford Cary", "Tom Ford", "TFC-034", []),
        ("Tom Ford FT0237", "Tom Ford", "TF237-035", []),

        # Versace
        ("Versace Medusa Sunglasses", "Versace", "VMS-036", []),
        ("Versace Pilot Sunglasses", "Versace", "VPS-037", []),
        ("Versace Shield Sunglasses", "Versace", "VSS-038", []),
        ("Versace Geometric Frame", "Versace", "VGF-039", []),
        ("Versace Round Sunglasses", "Versace", "VRS-040", []),

        # Burberry
        ("Burberry Square Sunglasses", "Burberry", "BSS-041", []),
        ("Burberry Check Detail", "Burberry", "BCD-042", []),
        ("Burberry Cat-Eye Sunglasses", "Burberry", "BCE-043", []),
        ("Burberry Oversized Frames", "Burberry", "BOF-044", []),
        ("Burberry Aviator", "Burberry", "BA-045", []),

        # Dolce & Gabbana
        ("Dolce & Gabbana DG Logo", "Dolce & Gabbana", "DGL-046", []),
        ("Dolce & Gabbana Round", "Dolce & Gabbana", "DGR-047", []),
        ("Dolce & Gabbana Shield", "Dolce & Gabbana", "DGS-048", []),
        ("Dolce & Gabbana Square", "Dolce & Gabbana", "DGQ-049", []),
        ("Dolce & Gabbana Oversized", "Dolce & Gabbana", "DGO-050", [])
    ],
    "hats-caps": [
        # Nike
        ("Baseball Cap", "Nike", "BC-001", []),
        ("Dri-FIT Cap", "Nike", "DFC-002", []),
        ("Heritage86 Cap", "Nike", "H86-003", []),
        ("Pro Futura Snapback", "Nike", "PFS-004", []),
        ("Tech Cap", "Nike", "TC-005", []),

        # Stetson
        ("Fedora", "Stetson", "ST-006", []),
        ("Straw Fedora", "Stetson", "SF-007", []),
        ("Wool Felt Fedora", "Stetson", "WFF-008", []),
        ("Panama Fedora", "Stetson", "PF-009", []),
        ("Trilby Hat", "Stetson", "TH-010", []),

        # Carhartt
        ("Beanie", "Carhartt", "CB-011", []),
        ("Acrylic Watch Hat", "Carhartt", "AWH-012", []),
        ("Knit Cuffed Beanie", "Carhartt", "KCB-013", []),
        ("Fleece Beanie", "Carhartt", "FB-014", []),
        ("Insulated Beanie", "Carhartt", "IB-015", []),

        # New Era
        ("Snapback Cap", "New Era", "NE-016", []),
        ("59FIFTY Fitted Cap", "New Era", "59F-017", []),
        ("9FORTY Adjustable Cap", "New Era", "9F-018", []),
        ("Trucker Hat", "New Era", "TH-019", []),
        ("Camouflage Snapback", "New Era", "CS-020", []),

        # Adidas
        ("Bucket Hat", "Adidas", "AH-021", []),
        ("Trefoil Cap", "Adidas", "TC-022", []),
        ("Performance Cap", "Adidas", "PC-023", []),
        ("Climacool Cap", "Adidas", "CC-024", []),
        ("Running Cap", "Adidas", "RC-025", []),

        # Under Armour
        ("UA Blitzing Cap", "Under Armour", "UAB-026", []),
        ("HeatGear Cap", "Under Armour", "HGC-027", []),
        ("Men's Adjustable Cap", "Under Armour", "MAC-028", []),
        ("Stretch Fit Cap", "Under Armour", "SFC-029", []),
        ("Shadow Run Cap", "Under Armour", "SRC-030", []),

        # Kangol
        ("Kangol 504 Cap", "Kangol", "K504-031", []),
        ("Bermuda Bucket Hat", "Kangol", "BBH-032", []),
        ("Tropic 504 Ventair", "Kangol", "T504-033", []),
        ("Kangol Beanie", "Kangol", "KB-034", []),
        ("Wool Flexfit Cap", "Kangol", "WFC-035", []),

        # Patagonia
        ("Patagonia P-6 Label Cap", "Patagonia", "P6L-036", []),
        ("Trucker Hat", "Patagonia", "TPH-037", []),
        ("Sun Runner Cap", "Patagonia", "SRC-038", []),
        ("Wavefarer Bucket Hat", "Patagonia", "WBH-039", []),
        ("Lightweight Travel Hat", "Patagonia", "LTH-040", []),

        # Columbia
        ("Mesh Ball Cap", "Columbia", "MBC-041", []),
        ("Columbia Bora Bora Booney", "Columbia", "BBB-042", []),
        ("Columbia Snapback", "Columbia", "CSB-043", []),
        ("PFG Mesh Cap", "Columbia", "PFG-044", []),
        ("Trail Shaker Beanie", "Columbia", "TSB-045", []),

        # The North Face
        ("TNF Logo Cap", "The North Face", "TNF-046", []),
        ("Horizon Breeze Brimmer", "The North Face", "HBB-047", []),
        ("TNF Beanie", "The North Face", "TNB-048", []),
        ("Five Panel Cap", "The North Face", "FPC-049", []),
        ("TNF Bucket Hat", "The North Face", "TNBH-050", [])
    ],
    "jewelry": [
        # Tiffany & Co.
        ("Gold Necklace", "Tiffany & Co.", "GN-001", []),
        ("Platinum Engagement Ring", "Tiffany & Co.", "PER-002", []),
        ("Silver Heart Pendant", "Tiffany & Co.", "SHP-003", []),
        ("Diamond Stud Earrings", "Tiffany & Co.", "DSE-004", []),
        ("Rose Gold Bracelet", "Tiffany & Co.", "RGB-005", []),

        # De Beers
        ("Diamond Ring", "De Beers", "DR-006", []),
        ("Halo Diamond Necklace", "De Beers", "HDN-007", []),
        ("Platinum Wedding Band", "De Beers", "PWB-008", []),
        ("Three-Stone Diamond Ring", "De Beers", "TDR-009", []),
        ("Tennis Bracelet", "De Beers", "TB-010", []),

        # Pandora
        ("Silver Bracelet", "Pandora", "SB-011", []),
        ("Charm Bracelet", "Pandora", "CB-012", []),
        ("Stackable Ring", "Pandora", "SR-013", []),
        ("Birthstone Pendant", "Pandora", "BP-014", []),
        ("Rose Gold Heart Ring", "Pandora", "RHR-015", []),

        # Cartier
        ("Emerald Earrings", "Cartier", "EE-016", []),
        ("Love Bracelet", "Cartier", "LB-017", []),
        ("Sapphire Pendant", "Cartier", "SP-018", []),
        ("Trinity Ring", "Cartier", "TR-019", []),
        ("Panthère De Cartier Watch", "Cartier", "PCW-020", []),

        # Mikimoto
        ("Pearl Pendant", "Mikimoto", "MP-021", []),
        ("Classic Pearl Necklace", "Mikimoto", "CPN-022", []),
        ("Akoya Pearl Earrings", "Mikimoto", "APE-023", []),
        ("Golden South Sea Pearl Ring", "Mikimoto", "GSPR-024", []),
        ("Pearl Strand Bracelet", "Mikimoto", "PSB-025", []),

        # Bvlgari
        ("Serpenti Necklace", "Bvlgari", "SN-026", []),
        ("B.zero1 Ring", "Bvlgari", "BZR-027", []),
        ("Divas’ Dream Earrings", "Bvlgari", "DDE-028", []),
        ("Onyx Pendant", "Bvlgari", "OP-029", []),
        ("White Gold Bangle", "Bvlgari", "WGB-030", []),

        # Van Cleef & Arpels
        ("Alhambra Necklace", "Van Cleef & Arpels", "AN-031", []),
        ("Lucky Clover Ring", "Van Cleef & Arpels", "LCR-032", []),
        ("Diamond Drop Earrings", "Van Cleef & Arpels", "DDE-033", []),
        ("Magic Alhambra Bracelet", "Van Cleef & Arpels", "MAB-034", []),
        ("Pearl Flower Brooch", "Van Cleef & Arpels", "PFB-035", []),

        # Harry Winston
        ("Cluster Diamond Necklace", "Harry Winston", "CDN-036", []),
        ("Emerald Cut Diamond Ring", "Harry Winston", "ECDR-037", []),
        ("Ruby Tennis Bracelet", "Harry Winston", "RTB-038", []),
        ("Sapphire Halo Pendant", "Harry Winston", "SHP-039", []),
        ("Diamond Chandelier Earrings", "Harry Winston", "DCE-040", []),

        # Chopard
        ("Happy Diamonds Necklace", "Chopard", "HDN-041", []),
        ("Imperiale Watch", "Chopard", "IW-042", []),
        ("L.U.C Perpetual Calendar", "Chopard", "LPC-043", []),
        ("Floating Diamond Ring", "Chopard", "FDR-044", []),
        ("Golden Heart Pendant", "Chopard", "GHP-045", []),

        # Graff
        ("Butterfly Diamond Earrings", "Graff", "BDE-046", []),
        ("Infinity Sapphire Ring", "Graff", "ISR-047", []),
        ("Emerald Cut Diamond Necklace", "Graff", "ECDN-048", []),
        ("Royal Blue Sapphire Bracelet", "Graff", "RBSB-049", []),
        ("Graff Icon Pendant", "Graff", "GIP-050", [])
    ],
    "sportswear": [
        # Nike
        ("Running Shorts", "Nike", "RS-001", []),
        ("Dri-FIT T-shirt", "Nike", "DFT-002", []),
        ("Training Joggers", "Nike", "TJ-003", []),
        ("Pro Compression Tights", "Nike", "PCT-004", []),
        ("Windrunner Jacket", "Nike", "WJ-005", []),

        # Adidas
        ("Sports Bra", "Adidas", "SB-001", []),
        ("Climacool Training Pants", "Adidas", "CTP-002", []),
        ("Predator Soccer Jersey", "Adidas", "PSJ-003", []),
        ("Terrex Hiking Shorts", "Adidas", "THS-004", []),
        ("Compression T-shirt", "Adidas", "CTS-005", []),

        # Under Armour
        ("Compression Shirt", "Under Armour", "CS-001", []),
        ("HeatGear Leggings", "Under Armour", "HGL-002", []),
        ("Storm Hoodie", "Under Armour", "SH-003", []),
        ("Performance Shorts", "Under Armour", "PS-004", []),
        ("Rival Fleece Sweatpants", "Under Armour", "RFS-005", []),

        # Puma
        ("Track Jacket", "Puma", "TJ-001", []),
        ("Performance Tank Top", "Puma", "PTT-002", []),
        ("Cross Training Shoes", "Puma", "CTS-003", []),
        ("Evostripe Sweatpants", "Puma", "ESP-004", []),
        ("DryCell Workout Tee", "Puma", "DWT-005", []),

        # Lululemon
        ("Yoga Pants", "Lululemon", "YP-001", []),
        ("Align High-Rise Leggings", "Lululemon", "AHL-002", []),
        ("Metal Vent Tech Shirt", "Lululemon", "MVTS-003", []),
        ("Swiftly Tech Racerback Tank", "Lululemon", "STRT-004", []),
        ("License to Train Shorts", "Lululemon", "LTTS-005", []),

        # Reebok
        ("CrossFit Shorts", "Reebok", "CFS-001", []),
        ("Running Tights", "Reebok", "RT-002", []),
        ("Workout Ready Tee", "Reebok", "WRT-003", []),
        ("Athletic Joggers", "Reebok", "AJ-004", []),
        ("Speedwick Training Hoodie", "Reebok", "STH-005", []),

        # New Balance
        ("Fresh Foam Running Shoes", "New Balance", "FFRS-001", []),
        ("Accelerate Running Tank", "New Balance", "ART-002", []),
        ("Impact Run Shorts", "New Balance", "IRS-003", []),
        ("Athletic Quarter-Zip Pullover", "New Balance", "AQZP-004", []),
        ("Marathon Training Shirt", "New Balance", "MTS-005", []),

        # ASICS
        ("Performance Running T-shirt", "ASICS", "PRT-001", []),
        ("Gel-Kayano Running Shoes", "ASICS", "GKRS-002", []),
        ("Compression Tights", "ASICS", "CT-003", []),
        ("Training Hoodie", "ASICS", "TH-004", []),
        ("Roadblast Running Shorts", "ASICS", "RRS-005", []),

        # Columbia
        ("Omni-Wick Trail Shirt", "Columbia", "OWTS-001", []),
        ("Fleece Lined Track Pants", "Columbia", "FLTP-002", []),
        ("Titanium Active Jacket", "Columbia", "TAJ-003", []),
        ("Hiking Shorts", "Columbia", "HS-004", []),
        ("Winter Sports Gloves", "Columbia", "WSG-005", []),

        # The North Face
        ("Apex Bionic Jacket", "The North Face", "ABJ-001", []),
        ("Flight Series Running Tights", "The North Face", "FSRT-002", []),
        ("Waterproof Trail Pants", "The North Face", "WTP-003", []),
        ("Venture Rain Jacket", "The North Face", "VRJ-004", []),
        ("Athletic Quarter-Zip Sweater", "The North Face", "AQZS-005", [])
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


with open('./fake_fashion_sellers.json', 'r') as f:
    sellers_data = json.load(f)

def find_seller_by_product(product_id, subcategory):
    """
    Takes a product_id and searches for it in the sellers_data.
    Returns the seller_id if found, else returns None.
    """
    for sub_category, sellers in sellers_data.items():
        for seller in sellers:
            if sub_category == subcategory:
                if product_id in seller.get('sellsProducts', []):
                    return seller


# def get_image(product_name):


def generate_fake_product(category, subcategory, index_i):
    name, brand, model_pattern, images_array = random.choice(product_data[subcategory])
    product_id = f"amazon_{category}_{subcategory}_{index_i}"
    seller = find_seller_by_product(product_id, subcategory)
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
    
    CONDITIONS_SET = [
        "Product must be unused and in original packaging.",
        "Return request must be made within 14 days of purchase.",
        "Only defective products are eligible for returns.",
        "Items marked as non-returnable cannot be returned.",
        "Customer must provide proof of purchase for returns."
    ]

    is_return_eligible = fake.boolean()
    return_policy = {}
    if not is_return_eligible:
        return_policy = {
            "isReturnEligible": False
        }
    else:
        return_policy = {
            "return_period_days": fake.random_int(min=7, max=30),
            "return_fee": {
                "return_fee_price": fake.random_int(min=0, max=100),
                "return_fee_currency": fake.currency_code(),
            },
            "conditions": random.choice(CONDITIONS_SET),
            "isReturnEligible": True,
        }

    # Shipping options
    shipping_methods = ["Standard", "Express", "Overnight", "Same Day"]
    method = fake.random_element(shipping_methods)

    # Generating random price between $5 and $50
    price = {
        "cost": f"{fake.random_int(min=5, max=50)}.00",
        "currency": fake.currency_code()
    }

    # Generating random delivery time between 3 and 10 days
    delivery_time = {
        "delivery_time": fake.random_int(min=3, max=10),
        "Metric": "days"
    }

    shipping_options = {
        "method": method,
        "price": price,
        "estimated_delivery_time": delivery_time
    }
    
    return {
        "images": images_array,
        "features": selected_features,  # Directly use the selected features
        "color": random.sample(["Black", "White", "Silver", "Blue", "Red", "Gold"], k=3),
        "model_number": model_number,
        "product_name": name,
        "description": " ".join(selected_descriptions),  # Join all selected descriptions
        "id": product_id,
        "brand": {
            "brand_name": brand
        },
        "category": {
            "category_name": category,
            "sub_category": {
                "sub-_category_name": subcategory
            }
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
        "return_policy": return_policy,
        "rating": {
            "rating_average": round(random.uniform(1, 5), 1),
            "number_of_reviews": random.randint(0, 5000)
        },
        "dimensions": {
            "height_cm": round(random.uniform(5, 50), 2),
            "width_cm": round(random.uniform(5, 50), 2),
            "depth_cm": round(random.uniform(1, 20), 2),
            "weight_kg": round(random.uniform(0.1, 5), 2)
        },
        "shipping_options": shipping_options,
        "seller": seller
    }

##########################

dataset = []
for category, subcategories in categories.items():
    for subcategory in subcategories:
        dataset.extend([generate_fake_product(category, subcategory, i) for i in range(1, 51)])  # 50 products per subcategory

with open("./fake_products_fashion.json", "w") as f:
    json.dump(dataset, f, indent=4)

print(f"Fake product dataset with {len(dataset)} products generated successfully!")
