import json
import random
import uuid
from fakeData.electronics.faker_electronics import Faker

fake = Faker()
Faker.seed(42)

categories = {
    "electronics": [
        "smartphones", "laptops", "tablets", "smartwatches", "headphones",
        "cameras", "gaming-consoles", "drones", "power-banks", "smart-home"
    ]
}

product_data = {
    "smartphones": [
        # Apple iPhones
        ("iPhone 14 Pro", "Apple", "A12345"),
        ("iPhone 14", "Apple", "A23456"),
        ("iPhone 13 Pro", "Apple", "A34567"),
        ("iPhone 13", "Apple", "A45678"),
        ("iPhone 12 Pro", "Apple", "A56789"),
        
        # Samsung Galaxy Series
        ("Galaxy S23 Ultra", "Samsung", "SM-12345"),
        ("Galaxy S23+", "Samsung", "SM-23456"),
        ("Galaxy S22 Ultra", "Samsung", "SM-34567"),
        ("Galaxy S21 FE", "Samsung", "SM-45678"),
        ("Galaxy A73", "Samsung", "SM-56789"),
        
        # Google Pixel Series
        ("Pixel 7 Pro", "Google", "G-12345"),
        ("Pixel 7", "Google", "G-23456"),
        ("Pixel 6 Pro", "Google", "G-34567"),
        ("Pixel 6a", "Google", "G-45678"),
        ("Pixel 5", "Google", "G-56789"),
        
        # OnePlus Series
        ("OnePlus 11", "OnePlus", "OP-12345"),
        ("OnePlus 10 Pro", "OnePlus", "OP-23456"),
        ("OnePlus 9R", "OnePlus", "OP-34567"),
        ("OnePlus 8T", "OnePlus", "OP-45678"),
        ("OnePlus Nord 2", "OnePlus", "OP-56789"),
        
        # Sony Xperia Series
        ("Xperia 1 IV", "Sony", "X-12345"),
        ("Xperia 5 IV", "Sony", "X-23456"),
        ("Xperia 10 IV", "Sony", "X-34567"),
        ("Xperia 1 III", "Sony", "X-45678"),
        ("Xperia 5 III", "Sony", "X-56789"),
        
        # Xiaomi Mi and Redmi Series
        ("Mi 12 Pro", "Xiaomi", "MI-12345"),
        ("Mi 11X", "Xiaomi", "MI-23456"),
        ("Redmi Note 12 Pro", "Xiaomi", "R-34567"),
        ("Redmi 11 Prime", "Xiaomi", "R-45678"),
        ("Poco F4", "Xiaomi", "P-56789"),
        
        # Oppo Series
        ("Find X5 Pro", "Oppo", "O-12345"),
        ("Reno 8 Pro", "Oppo", "O-23456"),
        ("A96", "Oppo", "O-34567"),
        ("F21 Pro", "Oppo", "O-45678"),
        ("K10", "Oppo", "O-56789"),
        
        # Vivo Series
        ("X80 Pro", "Vivo", "V-12345"),
        ("V25 Pro", "Vivo", "V-23456"),
        ("Y75 5G", "Vivo", "V-34567"),
        ("T1 Pro", "Vivo", "V-45678"),
        ("iQOO 9T", "Vivo", "V-56789"),
        
        # Asus ROG and Zenfone Series
        ("ROG Phone 6", "Asus", "AS-12345"),
        ("ROG Phone 5", "Asus", "AS-23456"),
        ("Zenfone 9", "Asus", "AS-34567"),
        ("Zenfone 8", "Asus", "AS-45678"),
        ("ROG Phone 3", "Asus", "AS-56789"),
        
        # Realme Series
        ("GT 2 Pro", "Realme", "RLM-12345"),
        ("Narzo 50 Pro", "Realme", "RLM-23456"),
        ("C35", "Realme", "RLM-34567"),
        ("9 Pro+", "Realme", "RLM-45678"),
        ("GT Neo 3", "Realme", "RLM-56789"),
    ],
    "laptops": [
        # Apple MacBook Series
        ("MacBook Pro M3", "Apple", "MBP-123"),
        ("MacBook Air M2", "Apple", "MBA-234"),
        ("MacBook Pro M2", "Apple", "MBP-345"),
        ("MacBook Air M1", "Apple", "MBA-456"),
        ("MacBook Pro 16 M1", "Apple", "MBP-567"),
        
        # Dell XPS & Inspiron Series
        ("XPS 15", "Dell", "XPS-1234"),
        ("XPS 13", "Dell", "XPS-2345"),
        ("Inspiron 16 Plus", "Dell", "INS-3456"),
        ("Inspiron 15", "Dell", "INS-4567"),
        ("Alienware X17", "Dell", "ALI-5678"),
        
        # Lenovo ThinkPad & Legion Series
        ("ThinkPad X1 Carbon", "Lenovo", "T-1234"),
        ("ThinkPad P16", "Lenovo", "T-2345"),
        ("Legion 7i", "Lenovo", "L-3456"),
        ("Legion 5 Pro", "Lenovo", "L-4567"),
        ("Yoga 9i", "Lenovo", "Y-5678"),
        
        # Asus ROG & ZenBook Series
        ("ROG Zephyrus G14", "Asus", "ROG-1234"),
        ("ROG Strix Scar 17", "Asus", "ROG-2345"),
        ("ROG Flow X13", "Asus", "ROG-3456"),
        ("ZenBook 14 OLED", "Asus", "ZB-4567"),
        ("Vivobook Pro 16X", "Asus", "VB-5678"),
        
        # HP Spectre & Pavilion Series
        ("Spectre x360", "HP", "S-1234"),
        ("Spectre x360 16", "HP", "S-2345"),
        ("Omen 16", "HP", "O-3456"),
        ("Pavilion Plus 14", "HP", "P-4567"),
        ("Elite Dragonfly G3", "HP", "E-5678"),
        
        # Acer Predator & Swift Series
        ("Predator Helios 300", "Acer", "PH-1234"),
        ("Predator Triton 500 SE", "Acer", "PT-2345"),
        ("Nitro 5", "Acer", "N-3456"),
        ("Swift 5", "Acer", "SF-4567"),
        ("Aspire 7", "Acer", "A-5678"),
        
        # MSI Stealth & Katana Series
        ("Stealth 17", "MSI", "ST-1234"),
        ("Raider GE78", "MSI", "RD-2345"),
        ("Katana GF76", "MSI", "KT-3456"),
        ("Pulse GL66", "MSI", "PL-4567"),
        ("Modern 15", "MSI", "MD-5678"),
        
        # Razer Blade Series
        ("Blade 18", "Razer", "BL-1234"),
        ("Blade 17", "Razer", "BL-2345"),
        ("Blade 15", "Razer", "BL-3456"),
        ("Blade 14", "Razer", "BL-4567"),
        ("Blade Stealth 13", "Razer", "BL-5678"),
        
        # Samsung Galaxy Book Series
        ("Galaxy Book 3 Ultra", "Samsung", "GB-1234"),
        ("Galaxy Book 2 Pro", "Samsung", "GB-2345"),
        ("Galaxy Book Odyssey", "Samsung", "GB-3456"),
        ("Galaxy Book 360", "Samsung", "GB-4567"),
        ("Galaxy Chromebook 2", "Samsung", "GC-5678"),
        
        # Microsoft Surface Series
        ("Surface Laptop 5", "Microsoft", "SL-1234"),
        ("Surface Pro 9", "Microsoft", "SP-2345"),
        ("Surface Laptop Studio", "Microsoft", "SLS-3456"),
        ("Surface Go 3", "Microsoft", "SG-4567"),
        ("Surface Book 3", "Microsoft", "SB-5678"),
    ],
    "tablets": [
        # Apple iPad Series
        ("iPad Pro 12.9", "Apple", "A1234"),
        ("iPad Pro 11", "Apple", "A2345"),
        ("iPad Air 5", "Apple", "A3456"),
        ("iPad 10th Gen", "Apple", "A4567"),
        ("iPad Mini 6", "Apple", "A5678"),

        # Samsung Galaxy Tab Series
        ("Galaxy Tab S8 Ultra", "Samsung", "SM-12345"),
        ("Galaxy Tab S8+", "Samsung", "SM-23456"),
        ("Galaxy Tab S8", "Samsung", "SM-34567"),
        ("Galaxy Tab A8", "Samsung", "SM-45678"),
        ("Galaxy Tab S7 FE", "Samsung", "SM-56789"),

        # Microsoft Surface Series
        ("Surface Pro 9", "Microsoft", "SP-1234"),
        ("Surface Pro 8", "Microsoft", "SP-2345"),
        ("Surface Pro 7+", "Microsoft", "SP-3456"),
        ("Surface Go 3", "Microsoft", "SP-4567"),
        ("Surface Book 3", "Microsoft", "SP-5678"),

        # Huawei MatePad Series
        ("MatePad Pro 13.2", "Huawei", "MP-12345"),
        ("MatePad Pro 12.6", "Huawei", "MP-23456"),
        ("MatePad Pro 10.8", "Huawei", "MP-34567"),
        ("MatePad 11", "Huawei", "MP-45678"),
        ("MatePad Paper", "Huawei", "MP-56789"),

        # Amazon Fire Series
        ("Fire HD 10", "Amazon", "FD-1234"),
        ("Fire HD 8", "Amazon", "FD-2345"),
        ("Fire HD 7", "Amazon", "FD-3456"),
        ("Fire 7", "Amazon", "FD-4567"),
        ("Fire Max 11", "Amazon", "FD-5678"),

        # Lenovo Tab Series
        ("Tab P12 Pro", "Lenovo", "LT-1234"),
        ("Tab P11 Pro Gen 2", "Lenovo", "LT-2345"),
        ("Tab P11 Plus", "Lenovo", "LT-3456"),
        ("Tab M10 Plus", "Lenovo", "LT-4567"),
        ("Yoga Tab 13", "Lenovo", "LT-5678"),

        # Asus ROG Flow & ZenPad Series
        ("ROG Flow Z13", "Asus", "RF-1234"),
        ("ZenPad 3S 10", "Asus", "ZP-2345"),
        ("ZenPad 8.0", "Asus", "ZP-3456"),
        ("ROG Flow X13", "Asus", "RF-4567"),
        ("Vivobook 13 Slate", "Asus", "VB-5678"),

        # Xiaomi Pad Series
        ("Xiaomi Pad 6 Pro", "Xiaomi", "XP-1234"),
        ("Xiaomi Pad 6", "Xiaomi", "XP-2345"),
        ("Xiaomi Pad 5", "Xiaomi", "XP-3456"),
        ("Mi Pad 4", "Xiaomi", "XP-4567"),
        ("Mi Pad 3", "Xiaomi", "XP-5678"),

        # Google Pixel Tablet Series
        ("Pixel Tablet 2023", "Google", "PT-1234"),
        ("Pixel Slate", "Google", "PT-2345"),
        ("Pixel C", "Google", "PT-3456"),
        ("Nexus 9", "Google", "PT-4567"),
        ("Nexus 7", "Google", "PT-5678"),

        # Oppo & Realme Tablets
        ("Oppo Pad 2", "Oppo", "OP-1234"),
        ("Oppo Pad Air", "Oppo", "OP-2345"),
        ("Realme Pad X", "Realme", "RP-3456"),
        ("Realme Pad Mini", "Realme", "RP-4567"),
        ("Realme Pad", "Realme", "RP-5678"),
    ],
    "smartwatches": [
        # Apple Watch Series
        ("Apple Watch Series 9", "Apple", "A-1234"),
        ("Apple Watch Series 8", "Apple", "A-2345"),
        ("Apple Watch Series 7", "Apple", "A-3456"),
        ("Apple Watch SE (2nd Gen)", "Apple", "A-4567"),
        ("Apple Watch Ultra 2", "Apple", "A-5678"),

        # Samsung Galaxy Watch Series
        ("Galaxy Watch 6 Classic", "Samsung", "SM-R1234"),
        ("Galaxy Watch 6", "Samsung", "SM-R2345"),
        ("Galaxy Watch 5 Pro", "Samsung", "SM-R3456"),
        ("Galaxy Watch 5", "Samsung", "SM-R4567"),
        ("Galaxy Watch 4 Classic", "Samsung", "SM-R5678"),

        # Google Pixel Watch Series
        ("Pixel Watch 2", "Google", "G-W1234"),
        ("Pixel Watch", "Google", "G-W2345"),
        
        # Fossil Smartwatch Series
        ("Fossil Gen 6", "Fossil", "F-1234"),
        ("Fossil Gen 5", "Fossil", "F-2345"),
        ("Fossil Hybrid HR", "Fossil", "F-3456"),
        ("Fossil Sport", "Fossil", "F-4567"),
        ("Fossil Gen 4 Explorist", "Fossil", "F-5678"),

        # Amazfit Smartwatches
        ("Amazfit GTR 4", "Amazfit", "A-1234"),
        ("Amazfit GTR 3 Pro", "Amazfit", "A-2345"),
        ("Amazfit GTS 4 Mini", "Amazfit", "A-3456"),
        ("Amazfit T-Rex 2", "Amazfit", "A-4567"),
        ("Amazfit Bip 3 Pro", "Amazfit", "A-5678"),

        # Garmin Smartwatches
        ("Garmin Fenix 7X", "Garmin", "G-F1234"),
        ("Garmin Forerunner 955", "Garmin", "G-F2345"),
        ("Garmin Venu 2 Plus", "Garmin", "G-F3456"),
        ("Garmin Instinct 2", "Garmin", "G-F4567"),
        ("Garmin Epix 2", "Garmin", "G-F5678"),

        # Xiaomi Smartwatches
        ("Xiaomi Watch S1 Pro", "Xiaomi", "X-W1234"),
        ("Xiaomi Watch S1", "Xiaomi", "X-W2345"),
        ("Mi Watch Revolve", "Xiaomi", "X-W3456"),
        ("Mi Band 7 Pro", "Xiaomi", "X-W4567"),
        ("Mi Watch Lite", "Xiaomi", "X-W5678"),

        # Huawei Smartwatches
        ("Huawei Watch GT 3", "Huawei", "H-W1234"),
        ("Huawei Watch GT Runner", "Huawei", "H-W2345"),
        ("Huawei Watch 3 Pro", "Huawei", "H-W3456"),
        ("Huawei Band 7", "Huawei", "H-W4567"),
        ("Huawei Watch Fit 2", "Huawei", "H-W5678"),

        # OnePlus Smartwatches
        ("OnePlus Watch 2", "OnePlus", "O-W1234"),
        ("OnePlus Nord Watch", "OnePlus", "O-W2345"),
        ("OnePlus Watch Cobalt", "OnePlus", "O-W3456"),
        ("OnePlus Watch", "OnePlus", "O-W4567"),
        ("OnePlus Band", "OnePlus", "O-W5678"),

        # Realme Smartwatches
        ("Realme Watch 3 Pro", "Realme", "R-W1234"),
        ("Realme Watch 3", "Realme", "R-W2345"),
        ("Realme Watch S Pro", "Realme", "R-W3456"),
        ("Realme Band 2", "Realme", "R-W4567"),
        ("Realme Watch S", "Realme", "R-W5678"),

        # Oppo Smartwatches
        ("Oppo Watch 3 Pro", "Oppo", "OP-W1234"),
        ("Oppo Watch 3", "Oppo", "OP-W2345"),
        ("Oppo Watch 2", "Oppo", "OP-W3456"),
        ("Oppo Watch Free", "Oppo", "OP-W4567"),
        ("Oppo Band 2", "Oppo", "OP-W5678"),
    ],
    "headphones": [
        # Apple AirPods Series
        ("AirPods Max", "Apple", "A1234"),
        ("AirPods Pro (2nd Gen)", "Apple", "A2345"),
        ("AirPods Pro", "Apple", "A3456"),
        ("AirPods (3rd Gen)", "Apple", "A4567"),
        ("AirPods (2nd Gen)", "Apple", "A5678"),

        # Sony WH & WF Series
        ("WH-1000XM5", "Sony", "WH-12345"),
        ("WH-1000XM4", "Sony", "WH-23456"),
        ("WH-1000XM3", "Sony", "WH-34567"),
        ("WH-XB910N", "Sony", "WH-45678"),
        ("WH-CH710N", "Sony", "WH-56789"),
        ("WF-1000XM4", "Sony", "WF-12345"),
        ("WF-1000XM3", "Sony", "WF-23456"),
        ("WF-C500", "Sony", "WF-34567"),
        
        # Bose QuietComfort & SoundSport Series
        ("Bose QuietComfort Ultra", "Bose", "QC-12345"),
        ("Bose QuietComfort 45", "Bose", "QC-23456"),
        ("Bose QuietComfort 35 II", "Bose", "QC-34567"),
        ("Bose QuietComfort Earbuds II", "Bose", "QC-45678"),
        ("Bose QuietComfort Earbuds", "Bose", "QC-56789"),
        ("Bose SoundSport Free", "Bose", "QC-67890"),
        ("Bose Sport Earbuds", "Bose", "QC-78901"),
        
        # Beats Studio & Solo Series
        ("Beats Studio Pro", "Beats", "B-12345"),
        ("Beats Studio 3", "Beats", "B-23456"),
        ("Beats Studio Buds", "Beats", "B-34567"),
        ("Beats Fit Pro", "Beats", "B-45678"),
        ("Beats Solo 3", "Beats", "B-56789"),
        ("Beats Powerbeats Pro", "Beats", "B-67890"),
        ("Beats Flex", "Beats", "B-78901"),
        
        # Samsung Galaxy Buds Series
        ("Galaxy Buds Pro 2", "Samsung", "SM-R123"),
        ("Galaxy Buds Pro", "Samsung", "SM-R234"),
        ("Galaxy Buds 2 Pro", "Samsung", "SM-R345"),
        ("Galaxy Buds 2", "Samsung", "SM-R456"),
        ("Galaxy Buds Live", "Samsung", "SM-R567"),
        ("Galaxy Buds+", "Samsung", "SM-R678"),
        
        # Sennheiser Momentum & CX Series
        ("Sennheiser Momentum 4", "Sennheiser", "SEN-12345"),
        ("Sennheiser Momentum 3", "Sennheiser", "SEN-23456"),
        ("Sennheiser Momentum True Wireless 3", "Sennheiser", "SEN-34567"),
        ("Sennheiser CX Plus", "Sennheiser", "SEN-45678"),
        ("Sennheiser HD 450BT", "Sennheiser", "SEN-56789"),
        
        # JBL Headphones
        ("JBL Tour One M2", "JBL", "JBL-12345"),
        ("JBL Tour Pro 2", "JBL", "JBL-23456"),
        ("JBL Live 660NC", "JBL", "JBL-34567"),
        ("JBL Tune 760NC", "JBL", "JBL-45678"),
        ("JBL Endurance Peak 3", "JBL", "JBL-56789"),
        
        # Anker Soundcore Series
        ("Soundcore Space Q45", "Anker", "ANK-12345"),
        ("Soundcore Liberty 4", "Anker", "ANK-23456"),
        ("Soundcore Life Q35", "Anker", "ANK-34567"),
        ("Soundcore Life Q30", "Anker", "ANK-45678"),
        ("Soundcore Liberty Air 2 Pro", "Anker", "ANK-56789"),
        
        # Skullcandy Headphones
        ("Skullcandy Crusher Evo", "Skullcandy", "SC-12345"),
        ("Skullcandy Indy ANC", "Skullcandy", "SC-23456"),
        ("Skullcandy Push Active", "Skullcandy", "SC-34567"),
        ("Skullcandy Sesh Evo", "Skullcandy", "SC-45678"),
        ("Skullcandy Hesh ANC", "Skullcandy", "SC-56789"),
    ],
    "cameras": [
        # Sony Alpha Series
        ("Alpha 7 IV", "Sony", "A7-001"),
        ("Alpha 7 III", "Sony", "A7-002"),
        ("Alpha 7R V", "Sony", "A7R-003"),
        ("Alpha 7R IV", "Sony", "A7R-004"),
        ("Alpha 7S III", "Sony", "A7S-005"),
        ("Alpha 9 II", "Sony", "A9-006"),
        ("Alpha 1", "Sony", "A1-007"),
        ("Alpha 6600", "Sony", "A6-008"),
        ("Alpha 6400", "Sony", "A6-009"),
        ("Alpha 6100", "Sony", "A6-010"),

        # Canon EOS Series
        ("EOS R5", "Canon", "R5-011"),
        ("EOS R6 II", "Canon", "R6-012"),
        ("EOS R3", "Canon", "R3-013"),
        ("EOS R8", "Canon", "R8-014"),
        ("EOS R10", "Canon", "R10-015"),
        ("EOS RP", "Canon", "RP-016"),
        ("EOS 5D Mark IV", "Canon", "5D-017"),
        ("EOS 6D Mark II", "Canon", "6D-018"),
        ("EOS 90D", "Canon", "90D-019"),
        ("EOS M50 Mark II", "Canon", "M50-020"),

        # Panasonic Lumix Series
        ("Lumix GH6", "Panasonic", "GH6-021"),
        ("Lumix GH5 II", "Panasonic", "GH5-022"),
        ("Lumix G9", "Panasonic", "G9-023"),
        ("Lumix S1H", "Panasonic", "S1H-024"),
        ("Lumix S5", "Panasonic", "S5-025"),
        ("Lumix FZ1000 II", "Panasonic", "FZ1-026"),
        ("Lumix GX9", "Panasonic", "GX9-027"),
        ("Lumix TZ200", "Panasonic", "TZ2-028"),
        ("Lumix G85", "Panasonic", "G85-029"),
        ("Lumix ZS100", "Panasonic", "ZS1-030"),

        # Nikon Z and D Series
        ("Z9", "Nikon", "Z9-031"),
        ("Z8", "Nikon", "Z8-032"),
        ("Z7 II", "Nikon", "Z7-033"),
        ("Z6 II", "Nikon", "Z6-034"),
        ("Z5", "Nikon", "Z5-035"),
        ("D850", "Nikon", "D8-036"),
        ("D750", "Nikon", "D7-037"),
        ("D500", "Nikon", "D5-038"),
        ("D7500", "Nikon", "D75-039"),
        ("D5600", "Nikon", "D56-040"),

        # Fujifilm GFX and X Series
        ("GFX 100S", "Fujifilm", "GFX-041"),
        ("GFX 50S II", "Fujifilm", "GFX-042"),
        ("X-T5", "Fujifilm", "XT5-043"),
        ("X-T4", "Fujifilm", "XT4-044"),
        ("X-S10", "Fujifilm", "XS10-045"),
        ("X-Pro3", "Fujifilm", "XP3-046"),
        ("X100V", "Fujifilm", "X100-047"),
        ("X-T30 II", "Fujifilm", "XT30-048"),
        ("X-E4", "Fujifilm", "XE4-049"),
        ("X-A7", "Fujifilm", "XA7-050"),
    ],
    "gaming-consoles": [
        # Sony PlayStation Series
        ("PlayStation 5", "Sony", "PS5-001"),
        ("PlayStation 5 Digital Edition", "Sony", "PS5D-002"),
        ("PlayStation 4 Pro", "Sony", "PS4P-003"),
        ("PlayStation 4 Slim", "Sony", "PS4S-004"),
        ("PlayStation 4", "Sony", "PS4-005"),
        ("PlayStation 3 Slim", "Sony", "PS3S-006"),
        ("PlayStation 3", "Sony", "PS3-007"),
        ("PlayStation 2 Slim", "Sony", "PS2S-008"),
        ("PlayStation 2", "Sony", "PS2-009"),
        ("PlayStation Vita", "Sony", "PSV-010"),

        # Microsoft Xbox Series
        ("Xbox Series X", "Microsoft", "XSX-011"),
        ("Xbox Series S", "Microsoft", "XSS-012"),
        ("Xbox One X", "Microsoft", "X1X-013"),
        ("Xbox One S", "Microsoft", "X1S-014"),
        ("Xbox One", "Microsoft", "X1-015"),
        ("Xbox 360 Elite", "Microsoft", "X360E-016"),
        ("Xbox 360 Slim", "Microsoft", "X360S-017"),
        ("Xbox 360", "Microsoft", "X360-018"),
        ("Xbox", "Microsoft", "XB-019"),

        # Nintendo Consoles
        ("Nintendo Switch OLED", "Nintendo", "NS-020"),
        ("Nintendo Switch", "Nintendo", "NS-021"),
        ("Nintendo Switch Lite", "Nintendo", "NSL-022"),
        ("Nintendo Wii U", "Nintendo", "WiiU-023"),
        ("Nintendo Wii", "Nintendo", "Wii-024"),
        ("Nintendo 3DS XL", "Nintendo", "3DSXL-025"),
        ("Nintendo 3DS", "Nintendo", "3DS-026"),
        ("Nintendo 2DS", "Nintendo", "2DS-027"),
        ("Nintendo DS Lite", "Nintendo", "DSL-028"),
        ("Nintendo DS", "Nintendo", "DS-029"),

        # Sega Consoles
        ("Sega Dreamcast", "Sega", "SDC-030"),
        ("Sega Saturn", "Sega", "SS-031"),
        ("Sega Genesis", "Sega", "SG-032"),
        ("Sega Master System", "Sega", "SMS-033"),
        ("Sega Game Gear", "Sega", "SGG-034"),

        # Other Popular Consoles
        ("Atari 2600", "Atari", "A2600-035"),
        ("Atari 5200", "Atari", "A5200-036"),
        ("Atari 7800", "Atari", "A7800-037"),
        ("Atari Jaguar", "Atari", "AJ-038"),
        ("Atari Lynx", "Atari", "AL-039"),

        ("Neo Geo AES", "SNK", "NGAES-040"),
        ("Neo Geo CD", "SNK", "NGCD-041"),
        ("Neo Geo Pocket", "SNK", "NGP-042"),
        ("Neo Geo Pocket Color", "SNK", "NGPC-043"),

        ("TurboGrafx-16", "NEC", "TG16-044"),
        ("PC Engine", "NEC", "PCE-045"),

        ("ColecoVision", "Coleco", "CV-046"),
        ("Intellivision", "Mattel", "INTV-047"),
        ("Philips CD-i", "Philips", "CDI-048"),
        ("3DO Interactive Multiplayer", "3DO", "3DO-049"),
        ("Magnavox Odyssey 2", "Magnavox", "MO2-050"),
    ],
    "drones": [
        # DJI Drones
        ("Mavic 3", "DJI", "M3-001"),
        ("Mavic 3 Pro", "DJI", "M3P-002"),
        ("Mavic 3 Classic", "DJI", "M3C-003"),
        ("Mavic Air 2S", "DJI", "MA2S-004"),
        ("Mavic Mini 2", "DJI", "MM2-005"),
        ("Mavic Mini 3 Pro", "DJI", "MM3P-006"),
        ("Phantom 4 Pro V2.0", "DJI", "P4-007"),
        ("Phantom 4 Advanced", "DJI", "P4A-008"),
        ("Phantom 3 Professional", "DJI", "P3P-009"),
        ("Phantom 3 Standard", "DJI", "P3S-010"),
        ("Inspire 2", "DJI", "I2-011"),
        ("Inspire 1 RAW", "DJI", "I1R-012"),
        ("Inspire 1 V2.0", "DJI", "I1V2-013"),
        ("DJI FPV", "DJI", "FPV-014"),
        ("Avata", "DJI", "A-015"),

        # Autel Drones
        ("Autel EVO II Pro", "Autel", "E2P-016"),
        ("Autel EVO II 8K", "Autel", "E28K-017"),
        ("Autel EVO Lite+", "Autel", "ELP-018"),
        ("Autel EVO Nano+", "Autel", "ENP-019"),
        ("Autel Dragonfish Standard", "Autel", "DS-020"),

        # Skydio Drones
        ("Skydio 2", "Skydio", "S2-021"),
        ("Skydio 2+", "Skydio", "S2P-022"),
        ("Skydio X2D", "Skydio", "SX2D-023"),
        ("Skydio R1", "Skydio", "SR1-024"),

        # Parrot Drones
        ("Parrot Anafi", "Parrot", "PA-025"),
        ("Parrot Anafi FPV", "Parrot", "PAF-026"),
        ("Parrot Bebop 2", "Parrot", "PB2-027"),
        ("Parrot Disco", "Parrot", "PD-028"),
        ("Parrot Swing", "Parrot", "PS-029"),

        # Yuneec Drones
        ("Yuneec Typhoon H Plus", "Yuneec", "YTHP-030"),
        ("Yuneec Typhoon H", "Yuneec", "YTH-031"),
        ("Yuneec H520E", "Yuneec", "YH52E-032"),
        ("Yuneec Mantis Q", "Yuneec", "YMQ-033"),
        ("Yuneec Mantis G", "Yuneec", "YMG-034"),

        # PowerVision Drones
        ("PowerEgg X", "PowerVision", "PEX-035"),
        ("PowerRay", "PowerVision", "PR-036"),

        # Walkera Drones
        ("Walkera Voyager 5", "Walkera", "WV5-037"),
        ("Walkera F210 FPV", "Walkera", "WF2-038"),
        ("Walkera Vitus", "Walkera", "WV-039"),

        # Holy Stone Drones
        ("Holy Stone HS720E", "Holy Stone", "HS72E-040"),
        ("Holy Stone HS710", "Holy Stone", "HS71-041"),
        ("Holy Stone HS175D", "Holy Stone", "HS175-042"),
        ("Holy Stone HS110D", "Holy Stone", "HS11D-043"),

        # Eachine Drones
        ("Eachine EX5", "Eachine", "EEX5-044"),
        ("Eachine E520S", "Eachine", "EE52S-045"),
        ("Eachine E58", "Eachine", "EE58-046"),
        ("Eachine Tyro79", "Eachine", "ETY79-047"),

        # Ryze Drones
        ("Ryze Tello", "Ryze", "RT-048"),
        ("Ryze Tello EDU", "Ryze", "RTE-049"),

        # Zero Zero Robotics
        ("HoverAir X1", "Zero Zero Robotics", "HAX1-050")
    ],
    "power-banks": [
        # Anker Power Banks
        ("Anker PowerCore 26800", "Anker", "APC-001"),
        ("Anker PowerCore 20100", "Anker", "APC-002"),
        ("Anker PowerCore 10000", "Anker", "APC-003"),
        ("Anker PowerCore+ 26800 PD", "Anker", "APC-004"),
        ("Anker PowerCore Slim 10000", "Anker", "APC-005"),
        ("Anker PowerCore Essential 20000 PD", "Anker", "APC-006"),
        ("Anker PowerCore III Elite 25600", "Anker", "APC-007"),
        ("Anker PowerCore Fusion 5000", "Anker", "APC-008"),
        ("Anker PowerHouse 200", "Anker", "APH-009"),
        ("Anker PowerCore Magnetic 5K", "Anker", "APC-010"),

        # RAVPower Power Banks
        ("RAVPower 20000mAh", "RAVPower", "RP-011"),
        ("RAVPower PD Pioneer 26800mAh", "RAVPower", "RP-012"),
        ("RAVPower 16750mAh", "RAVPower", "RP-013"),
        ("RAVPower 32000mAh", "RAVPower", "RP-014"),
        ("RAVPower 10000mAh PD", "RAVPower", "RP-015"),
        ("RAVPower 30000mAh", "RAVPower", "RP-016"),
        ("RAVPower 20100mAh QC 3.0", "RAVPower", "RP-017"),
        ("RAVPower PD 60W 20000mAh", "RAVPower", "RP-018"),
        ("RAVPower 15000mAh", "RAVPower", "RP-019"),
        ("RAVPower Wireless Charging 10000mAh", "RAVPower", "RP-020"),

        # Zendure Power Banks
        ("Zendure SuperTank Pro", "Zendure", "ZSP-021"),
        ("Zendure A8PD 26800mAh", "Zendure", "ZSP-022"),
        ("Zendure A6PD 20100mAh", "Zendure", "ZSP-023"),
        ("Zendure X6 20000mAh", "Zendure", "ZSP-024"),
        ("Zendure X5 15000mAh", "Zendure", "ZSP-025"),
        ("Zendure SuperMini 10000mAh", "Zendure", "ZSP-026"),
        ("Zendure SuperMini 5000mAh", "Zendure", "ZSP-027"),
        ("Zendure SuperTank 27000mAh", "Zendure", "ZSP-028"),
        ("Zendure A2 6700mAh", "Zendure", "ZSP-029"),
        ("Zendure A5 16750mAh", "Zendure", "ZSP-030"),

        # OmniCharge Power Banks
        ("Omni 20+ Power Bank", "OmniCharge", "O20P-031"),
        ("Omni Ultimate 38400mAh", "OmniCharge", "O20P-032"),
        ("Omni 13+ Power Bank", "OmniCharge", "O20P-033"),
        ("Omni Mobile 25600mAh", "OmniCharge", "O20P-034"),
        ("Omni Mobile 12800mAh", "OmniCharge", "O20P-035"),
        ("Omni Mobile 9600mAh", "OmniCharge", "O20P-036"),
        ("Omni Mobile 8000mAh", "OmniCharge", "O20P-037"),
        ("Omni Power Station", "OmniCharge", "O20P-038"),
        ("Omni Power Hub", "OmniCharge", "O20P-039"),
        ("Omni 20C+ USB-C", "OmniCharge", "O20P-040"),

        # Mophie Power Banks
        ("Mophie Powerstation XXL", "Mophie", "MPX-041"),
        ("Mophie Powerstation Plus XL", "Mophie", "MPX-042"),
        ("Mophie Powerstation 10K", "Mophie", "MPX-043"),
        ("Mophie Powerstation 5K", "Mophie", "MPX-044"),
        ("Mophie Powerstation PD XL", "Mophie", "MPX-045"),
        ("Mophie Powerstation Hub", "Mophie", "MPX-046"),
        ("Mophie Powerstation Go Rugged", "Mophie", "MPX-047"),
        ("Mophie Snap+ Juice Pack Mini", "Mophie", "MPX-048"),
        ("Mophie Snap+ Wireless Charger", "Mophie", "MPX-049"),
        ("Mophie Powerstation Mini", "Mophie", "MPX-050")
    ],
    "smart-home": [
        ("Echo Dot (4th Gen)", "Amazon", "ED4G-###"),
        ("Echo Show 8", "Amazon", "ES8-###"),
        ("Echo Studio", "Amazon", "ES-###"),
        ("Google Nest Hub", "Google", "GNH-###"),
        ("Google Nest Audio", "Google", "GNA-###"),
        ("Google Nest Mini", "Google", "GNM-###"),
        ("Philips Hue White and Color Ambiance", "Philips", "HUE-###"),
        ("Philips Hue Lightstrip Plus", "Philips", "HUE-LS###"),
        ("Philips Hue Play Light Bar", "Philips", "HUE-PL###"),
        ("Ring Video Doorbell 4", "Ring", "RVD-###"),
        ("Ring Floodlight Cam", "Ring", "RFC-###"),
        ("Ring Alarm Security Kit", "Ring", "RAK-###"),
        ("Nest Thermostat", "Google", "NT-###"),
        ("Nest Learning Thermostat", "Google", "NLT-###"),
        ("Nest Cam (Battery)", "Google", "NCB-###"),
        ("Wyze Cam v3", "Wyze", "WCV3-###"),
        ("Wyze Bulb Color", "Wyze", "WBC-###"),
        ("Arlo Pro 4", "Arlo", "AP4-###"),
        ("Arlo Essential Video Doorbell", "Arlo", "AEVD-###"),
        ("TP-Link Kasa Smart Plug", "TP-Link", "KSP-###"),
        ("TP-Link Kasa Smart Bulb", "TP-Link", "KSB-###"),
        ("August Smart Lock Pro", "August", "ASL-###"),
        ("Yale Assure Lock SL", "Yale", "YALS-###"),
        ("Eufy Security Smart Lock", "Eufy", "ESSL-###"),
        ("EufyCam 2 Pro", "Eufy", "ECP-###"),
        ("SimpliSafe Home Security System", "SimpliSafe", "SHS-###"),
        ("Lutron Caseta Wireless Dimmer", "Lutron", "LCD-###"),
        ("Ecobee SmartThermostat", "Ecobee", "EST-###"),
        ("Ecobee SmartCamera", "Ecobee", "ESC-###"),
        ("Blink Outdoor Camera", "Blink", "BOC-###"),
        ("Blink Mini", "Blink", "BM-###"),
        ("Sonos One (Gen 2)", "Sonos", "SO2-###"),
        ("Sonos Arc Soundbar", "Sonos", "SAS-###"),
        ("Nanoleaf Shapes Light Panels", "Nanoleaf", "NSLP-###"),
        ("Nanoleaf Lines", "Nanoleaf", "NL-###"),
        ("WeMo Smart Plug", "WeMo", "WSP-###"),
        ("WeMo Smart Dimmer", "WeMo", "WSD-###"),
        ("Logitech Harmony Elite", "Logitech", "LHE-###"),
        ("SwitchBot Smart Curtain", "SwitchBot", "SSC-###"),
        ("SwitchBot Smart Plug", "SwitchBot", "SSP-###"),
        ("Meross Smart Plug", "Meross", "MSP-###"),
        ("Meross Smart Light Switch", "Meross", "MSLS-###"),
        ("Govee Smart LED Light Strips", "Govee", "GSL-###"),
        ("Govee Smart Table Lamp", "Govee", "GSTL-###"),
        ("Sengled Smart Bulb", "Sengled", "SSB-###"),
        ("LIFX Smart Bulb", "LIFX", "LSB-###"),
        ("Tado Smart AC Control", "Tado", "TSAC-###"),
        ("Bosch Smart Home Controller", "Bosch", "BSHC-###")
    ]
}

descriptions = {
    "smartphones": [
        "A high-end smartphone featuring a powerful processor, advanced AI-driven camera system, and long-lasting battery optimized for all-day use.",
        "An ultra-fast 5G smartphone with an immersive OLED display, pro-grade cameras, and AI-enhanced photography features.",
        "Designed for performance and style, this smartphone features cutting-edge AI capabilities, an all-day adaptive battery, and ultra-fast wireless charging.",
        "A flagship smartphone with seamless multitasking capabilities, a high refresh rate display, and a professional-grade camera system.",
        "A compact yet powerful smartphone with an advanced chipset, optimized gaming performance, and an IP68 water-resistant rating.",
        "An innovative smartphone featuring under-display fingerprint scanning, ultra-fast face unlock, and a high-resolution quad-camera setup.",
        "An all-screen smartphone with an edge-to-edge OLED display, 120Hz refresh rate, and HDR10+ support for stunning visuals.",
        "Built for creators, this smartphone includes a high-resolution main sensor, enhanced low-light photography, and professional-grade video recording.",
        "A premium foldable smartphone offering dual-display functionality, multitasking enhancements, and improved hinge durability.",
        "A gaming-centric smartphone with a cooling system, customizable RGB lighting, and a 144Hz refresh rate display for smooth gameplay."
    ],
    "laptops": [
        "A premium laptop with a sleek design, high-resolution display, and cutting-edge performance for professionals and creators.",
        "Designed for productivity, this laptop features a high-performance Intel Core i9 processor, ultra-fast SSD storage, and a long battery life.",
        "An ultra-lightweight and powerful laptop, perfect for gaming, content creation, and heavy multitasking, featuring a high-refresh-rate OLED display.",
        "Equipped with a dedicated GPU, this laptop is ideal for coding, gaming, and design work, offering top-tier performance and advanced cooling.",
        "A convertible 2-in-1 laptop with a touchscreen display, stylus support, and seamless transition between laptop and tablet modes.",
        "A workstation-grade laptop built for professionals, featuring ECC memory, high-speed Thunderbolt ports, and advanced security features.",
        "An ultra-thin ultrabook with an aluminum chassis, fanless cooling, and AI-powered battery optimization for maximum efficiency.",
        "A gaming laptop with an RGB keyboard, high refresh rate panel, and dedicated ray-tracing graphics for an immersive experience.",
        "A business-class laptop with enterprise-grade security, fingerprint authentication, and 5G connectivity for seamless remote work.",
        "A laptop optimized for developers, featuring Linux compatibility, high-performance CPUs, and an extended keyboard with a numpad."
    ],
    "tablets": [
        "A versatile tablet with a stunning high-resolution display, powerful chipset, and seamless stylus support for productivity and creativity.",
        "Perfect for entertainment and work, this tablet offers all-day battery life, a slim design, and an advanced camera system.",
        "A high-performance tablet with a sleek metal build, fast refresh rate display, and studio-quality speakers for immersive experiences.",
        "An all-in-one tablet with a desktop-class processor, 5G connectivity, and a detachable keyboard for maximum versatility.",
        "A powerful tablet designed for artists and designers, featuring precision pen input, color-accurate display, and AI-driven software enhancements.",
        "A rugged tablet built for industrial use, offering waterproofing, MIL-STD certification, and extreme temperature resistance.",
        "A family-friendly tablet with advanced parental controls, educational apps, and kid-proof casing for durability.",
        "A compact e-ink tablet designed for reading and note-taking, featuring a paper-like display and ultra-long battery life.",
        "An AI-powered tablet with smart handwriting recognition, real-time voice translation, and split-screen multitasking capabilities.",
        "A gaming-focused tablet featuring a high-refresh-rate display, ultra-responsive touch input, and console-grade gaming performance."
    ],
    "smartwatches": [
        "A stylish smartwatch with advanced health tracking, built-in GPS, and seamless integration with your smartphone for a connected experience.",
        "Designed for fitness enthusiasts, this smartwatch features an always-on AMOLED display, heart rate monitoring, and VO2 max tracking.",
        "A rugged smartwatch built for adventure, offering offline maps, barometric altimeter, and water resistance up to 100 meters.",
        "A premium smartwatch with ECG monitoring, advanced sleep tracking, and AI-powered insights to optimize daily activity.",
        "A hybrid smartwatch with an analog design, e-ink display, and up to 30 days of battery life on a single charge.",
        "A smartwatch with LTE connectivity, allowing for calls, texts, and streaming music without needing a smartphone.",
        "A smartwatch designed for extreme sports, featuring real-time performance analytics, altitude tracking, and multi-sport mode support.",
        "An elegant smartwatch with a stainless steel frame, sapphire crystal display, and luxury watch face customization.",
        "A smartwatch designed for runners, offering real-time cadence tracking, stride analysis, and adaptive training programs.",
        "A smartwatch with a rotating bezel, customizable widgets, and an AI-powered assistant for hands-free control."
    ],
    "headphones": [
        "Premium noise-canceling headphones with high-fidelity audio and immersive 3D sound for an unmatched listening experience.",
        "Wireless headphones with adaptive noise cancellation, AI-enhanced sound optimization, and up to 40 hours of battery life.",
        "Designed for audiophiles, these headphones deliver crystal-clear sound, deep bass, and lossless audio streaming capabilities.",
        "A perfect balance of comfort and sound quality, featuring memory foam ear cushions, active noise isolation, and multi-device pairing.",
        "Gaming headphones with a high-fidelity microphone, customizable surround sound, and ultra-low latency connectivity.",
        "Bone-conduction headphones designed for outdoor sports, offering open-ear awareness and sweat-proof durability.",
        "Studio-quality headphones with flat frequency response, balanced audio output, and high-impedance compatibility.",
        "Wireless earbuds with adaptive EQ, smart noise filtering, and AI-powered speech enhancement for crystal-clear calls.",
        "Headphones with built-in AI assistant integration, touch controls, and real-time language translation support.",
        "Over-ear headphones with foldable design, 90-degree rotating ear cups, and Hi-Res Audio certification."
    ],
    "gaming-consoles": [
        "A next-generation gaming console with ultra-fast load times, 4K resolution, and ray tracing support for stunning visuals.",
        "Experience immersive gameplay with a high-performance console featuring VR support, adaptive triggers, and 120Hz refresh rates.",
        "A portable gaming console with a powerful processor, ergonomic design, and exclusive game library optimized for high performance.",
        "A console built for competitive gaming, offering reduced latency, cloud gaming capabilities, and AI-driven frame optimization.",
        "A modular gaming console with upgradable hardware, customizable RGB lighting, and expandable storage options.",
        "A retro gaming console with a modern twist, featuring pre-loaded classic titles, HDMI output, and wireless controllers.",
        "A cloud gaming device with zero-latency streaming, 5G compatibility, and instant access to a vast digital library.",
        "A console designed for family gaming, featuring motion controls, interactive accessories, and kid-friendly content modes.",
        "A high-end console with 8K support, real-time ray tracing, and dynamic resolution scaling for ultra-smooth gameplay.",
        "A handheld gaming console with hybrid docked mode, customizable game controls, and haptic feedback for immersive gameplay."
    ],
    "cameras": [
        "A professional-grade mirrorless camera with a high-resolution full-frame sensor, fast autofocus, and advanced image stabilization for stunning visuals.",
        "A compact yet powerful DSLR camera featuring 4K video recording, high-speed burst mode, and interchangeable lenses for creative flexibility.",
        "An action camera designed for adventure, offering waterproof durability, 8K video support, and AI-powered image stabilization.",
        "A travel-friendly compact camera with a superzoom lens, built-in Wi-Fi for instant sharing, and intuitive touchscreen controls.",
        "A high-end cinema camera designed for filmmakers, featuring RAW video recording, dual-native ISO, and professional audio inputs.",
        "A smart security camera with AI-based motion detection, real-time alerts, and night vision capabilities for enhanced home security.",
        "A vlog-focused camera with a flip-out touchscreen, real-time face tracking, and professional-grade microphone input.",
        "A medium format camera with ultra-high megapixel resolution, wide dynamic range, and tethered shooting support for studio photography.",
        "A point-and-shoot camera with an AI-enhanced portrait mode, optical image stabilization, and seamless integration with cloud storage.",
        "A 360-degree camera with dual-lens technology, real-time stitching, and immersive VR content creation capabilities."
    ],
    "drones": [
        "A professional-grade drone with a 4K camera, obstacle avoidance system, and AI-powered subject tracking for stunning aerial shots.",
        "A compact foldable drone featuring a high-resolution camera, extended battery life, and intuitive gesture controls for effortless flying.",
        "A racing drone optimized for speed and agility, equipped with FPV goggles, low-latency video transmission, and customizable flight modes.",
        "A high-end cinematography drone with dual-camera stabilization, 8K video recording, and long-range transmission for professional filmmakers.",
        "A beginner-friendly drone with auto takeoff, altitude hold, and one-touch return-to-home functionality for easy piloting.",
        "A rugged industrial drone designed for surveying and mapping, featuring LiDAR sensors, thermal imaging, and autonomous flight capabilities.",
        "A drone equipped with AI-driven object tracking, real-time obstacle detection, and 3-axis gimbal stabilization for ultra-smooth footage.",
        "An agricultural drone with precision spraying technology, multispectral imaging, and AI-powered crop health analysis.",
        "A compact selfie drone with facial recognition, automated flight patterns, and seamless social media sharing integration.",
        "A military-grade drone with encrypted communication, long-endurance flight, and high-definition reconnaissance camera capabilities."
    ],
    "power-banks": [
        "A high-capacity 20,000mAh power bank with fast charging, multiple USB-C ports, and an LED battery status indicator.",
        "An ultra-slim power bank with wireless charging, MagSafe compatibility, and intelligent power distribution for multiple devices.",
        "A rugged solar-powered power bank featuring waterproof durability, built-in flashlight, and emergency SOS mode for outdoor adventures.",
        "A graphene-enhanced power bank with ultra-fast charging, intelligent temperature control, and extended lifespan.",
        "A compact 10,000mAh power bank with USB-PD support, low-power mode for wearables, and lightweight portability.",
        "A massive 50,000mAh power station designed for camping and emergency use, featuring AC outlets and DC input for solar charging.",
        "A power bank with built-in wall plug, foldable prongs, and auto-adjust voltage detection for universal compatibility.",
        "A smart power bank with a digital display, pass-through charging support, and AI-powered energy efficiency optimization.",
        "A gaming power bank with RGB lighting, ultra-low latency power delivery, and heat-resistant casing for uninterrupted gaming sessions.",
        "A multi-port power bank with high-speed charging, surge protection, and simultaneous support for laptops, smartphones, and tablets."
    ],
    "smart-home": [
        "A voice-controlled smart speaker with AI integration, high-fidelity audio, and seamless connectivity with all smart home devices.",
        "A smart thermostat with AI-powered climate control, remote access via mobile app, and energy efficiency optimization.",
        "A smart security system with 4K cameras, facial recognition, motion detection alerts, and real-time cloud storage backup.",
        "A Wi-Fi-enabled smart lighting system with voice control, customizable color temperature, and automated scheduling.",
        "A robotic vacuum cleaner with AI-powered room mapping, self-emptying dustbin, and adaptive cleaning algorithms.",
        "A smart doorbell with HD video, two-way audio communication, and AI-based package detection for added security.",
        "A multi-room smart home hub that integrates lighting, security, and entertainment for seamless automation.",
        "A smart lock with biometric authentication, remote access control, and encrypted key-sharing functionality.",
        "A smart plug with energy monitoring, voice assistant compatibility, and automated on/off scheduling.",
        "A smart kitchen assistant with voice-controlled recipe guidance, nutrition tracking, and meal planning integration."
    ]
}

features = {
    "smartphones": {
        "Display": ["6.7\" LTPO AMOLED", "120Hz refresh rate", "HDR10+", "1440 x 3200 resolution", "Gorilla Glass Victus"],
        "Processor": ["Qualcomm Snapdragon 8 Gen 3", "Apple A17 Pro", "Exynos 2400 (5nm)"],
        "Camera System": ["108MP primary sensor", "periscope telephoto (10x optical zoom)", "ultra-wide", "macro", "AI-enhanced image processing"],
        "Video Recording": ["8K 30fps", "4K 120fps", "Dolby Vision HDR recording", "gimbal-like stabilization"],
        "Connectivity": ["WiFi 7", "Bluetooth 5.3", "5G mmWave/sub-6", "UWB support", "NFC"],
        "Battery & Charging": ["5000mAh", "120W wired charging (0-100 in 15 minutes)", "50W wireless", "10W reverse wireless"],
        "Security": ["Under-display ultrasonic fingerprint sensor", "facial recognition (3D ToF sensor)"],
        "Build Quality": ["IP68 water & dust resistance", "titanium/aluminum frame", "ceramic back"]
    },
    "laptops": {
        "Processor": ["Intel Core i9-14900HX", "AMD Ryzen 9 7945HX", "Apple M3 Max (3nm)"],
        "Graphics": ["NVIDIA RTX 4090 (16GB GDDR6)", "AMD Radeon RX 7900", "Apple GPU (40-core)"],
        "Memory (RAM)": ["32GB LPDDR5X 7200MHz (expandable to 64GB)"],
        "Storage": ["2TB NVMe PCIe 4.0 SSD (7000MB/s read, 6500MB/s write)"],
        "Display": ["16\" Mini-LED 4K", "165Hz", "1000 nits brightness", "HDR1000", "AdobeRGB 100%"],
        "Battery": ["99.9Wh (FAA limit)", "150W fast charging", "24-hour battery life"],
        "Connectivity": ["WiFi 6E", "Bluetooth 5.3", "Thunderbolt 4", "HDMI 2.1", "SD Express 7.0"],
        "Build & Features": ["CNC aluminum chassis", "per-key RGB backlit keyboard", "fingerprint scanner", "IR facial recognition"]
    },
    "tablets": {
        "Processor": ["Apple M2", "Qualcomm Snapdragon 8cx Gen 3", "Exynos 2200"],
        "Display": ["12.9\" OLED", "120Hz", "Dolby Vision", "HDR10+", "TrueTone"],
        "Stylus Support": ["Apple Pencil 2", "Samsung S Pen", "Microsoft Surface Pen (2ms latency, 4096 pressure levels)"],
        "Storage & RAM": ["Up to 1TB UFS 4.0 SSD", "16GB LPDDR5X RAM"],
        "Battery": ["12,000mAh", "65W USB-C fast charging", "15W reverse wireless charging"],
        "Security": ["Under-display fingerprint scanner", "Face ID", "Secure Enclave"],
        "Connectivity": ["WiFi 7", "Bluetooth 5.3", "5G (mmWave & Sub-6)", "USB 4.0"]
    },
    "smartwatches": {
        "Display": ["1.9\" LTPO AMOLED", "Always-On Display", "1000 nits brightness"],
        "Processor": ["Apple S9", "Qualcomm Snapdragon W5+ Gen 1", "Exynos W930"],
        "Health Tracking": ["ECG", "SpO2", "heart rate", "sleep monitoring", "temperature sensor", "stress tracking"],
        "Battery": ["500mAh", "10-day battery life", "30W fast charging", "wireless charging"],
        "Connectivity": ["WiFi 6", "Bluetooth 5.3", "LTE", "GPS", "NFC"],
        "Build Quality": ["IP68", "MIL-STD-810H durability", "Sapphire glass", "titanium frame"]
    },
    "headphones": {
        "Drivers": ["50mm Neodymium dynamic drivers", "THX-certified", "Hi-Res Audio support"],
        "Noise Cancellation": ["Hybrid ANC (Active + Adaptive) with up to 45dB noise reduction"],
        "Latency": ["Ultra-low latency (20ms) for gaming & VR support"],
        "Connectivity": ["Bluetooth 5.3 LE Audio", "aptX Lossless", "LDAC support"],
        "Battery": ["60 hours playback", "15-minute charge = 6-hour playback"],
        "Build & Comfort": ["Memory foam earpads", "aluminum frame", "sweatproof coating"]
    },
    "cameras": {
        "Sensor": ["Full-frame 50MP BSI CMOS", "Dual ISO", "AI-enhanced low-light performance"],
        "Autofocus": ["1024-point AI phase detection autofocus with eye-tracking"],
        "Video Recording": ["8K 60fps", "4K 120fps", "10-bit HDR RAW", "ProRes support"],
        "Connectivity": ["WiFi 6", "Bluetooth 5.3", "dual CFExpress Type B slots"],
        "Battery": ["3500mAh", "USB-C PD charging", "hot-swappable battery grip"]
    },
    "gaming-consoles": {
        "GPU": ["14 TFLOP AMD RDNA 4", "NVIDIA Ada Lovelace (RTX 4080 equivalent)"],
        "CPU": ["Custom Zen 4-based 8-core processor @ 3.6GHz"],
        "RAM": ["32GB GDDR6 (unified memory)"],
        "Storage": ["2TB NVMe PCIe 5.0 SSD (9GB/s read speed)"],
        "Ray Tracing": ["Real-time path tracing with AI-driven denoising"],
        "Cloud Gaming": ["Xbox Cloud Gaming", "PS Now", "NVIDIA GeForce Now support"],
        "Connectivity": ["WiFi 6E", "Bluetooth 5.3", "HDMI 2.1 (8K 120Hz output)"]
    },
    "drones": {
        "Camera": ["8K HDR", "1-inch CMOS sensor", "gimbal-stabilized"],
        "Flight Time": ["45 minutes", "15km range", "150km/h top speed"],
        "Navigation": ["Dual-band GPS", "AI-assisted object tracking", "return-to-home feature"],
        "Connectivity": ["5G transmission", "real-time video streaming"],
        "Build": ["Carbon fiber body", "foldable", "weatherproof"]
    },
    "power-banks": {
        "Capacity": ["30,000mAh Li-polymer battery"],
        "Charging Speed": ["100W USB-C PD 3.1", "45W Quick Charge 4+"],
        "Ports": ["Dual USB-C", "Dual USB-A", "wireless charging pad"],
        "Features": ["Pass-through charging", "LED display", "smart temperature control"]
    },
    "smart-home": {
        "Voice Assistants": ["Amazon Alexa", "Google Assistant", "Apple Siri"],
        "Security Features": ["AI facial recognition", "motion detection", "night vision"],
        "Automation": ["Smart schedules", "routines", "IFTTT integration"],
        "Connectivity": ["WiFi 6", "Zigbee", "Z-Wave", "Matter support"]
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
