import json
import random
import uuid
from fakeData.electronics.faker_electronics import Faker

fake = Faker()
Faker.seed(42)

categories = {
    "home-appliances": [
        "refrigerators", "washing-machines", "air-conditioners", "vacuum-cleaners", "microwaves",
        "coffee-makers", "dishwashers", "water-purifiers", "air-purifiers", "induction-cooktops"
    ]
}

product_data = {
    "refrigerators": [
        # Samsung
        ("French Door Refrigerator", "Samsung", "RF-####"),
        ("Smart 4-Door Flex", "Samsung", "SF-####"),
        ("Bespoke Counter-Depth", "Samsung", "BC-####"),
        ("Family Hub French Door", "Samsung", "FH-####"),
        ("Convertible 5-in-1 Refrigerator", "Samsung", "C5-####"),

        # LG
        ("InstaView Door-in-Door", "LG", "LG-####"),
        ("LG French Door Refrigerator", "LG", "LFD-####"),
        ("LG Side-by-Side Smart Refrigerator", "LG", "LSS-####"),
        ("LG Bottom Freezer Refrigerator", "LG", "LBF-####"),
        ("LG Door-in-Door Refrigerator", "LG", "LDI-####"),

        # Whirlpool
        ("Side-by-Side Refrigerator", "Whirlpool", "WH-####"),
        ("Whirlpool 4-Door Refrigerator", "Whirlpool", "W4D-####"),
        ("Whirlpool Top-Freezer Refrigerator", "Whirlpool", "WTF-####"),
        ("Whirlpool Bottom-Freezer Refrigerator", "Whirlpool", "WBF-####"),
        ("Whirlpool Counter-Depth Refrigerator", "Whirlpool", "WCD-####"),

        # Haier
        ("Double Door Refrigerator", "Haier", "HD-####"),
        ("Haier Inverter Refrigerator", "Haier", "HI-####"),
        ("Haier Mini Fridge", "Haier", "HM-####"),
        ("Haier Side-by-Side Refrigerator", "Haier", "HS-####"),
        ("Haier French Door Refrigerator", "Haier", "HF-####"),

        # Bosch
        ("Bosch 800 Series Refrigerator", "Bosch", "B8S-####"),
        ("Bosch Counter-Depth Refrigerator", "Bosch", "BCD-####"),
        ("Bosch Freestanding Refrigerator", "Bosch", "BFR-####"),
        ("Bosch Built-in Refrigerator", "Bosch", "BBI-####"),
        ("Bosch French Door Refrigerator", "Bosch", "BFD-####"),

        # GE
        ("GE Profile Series Refrigerator", "GE", "GE-####"),
        ("GE Side-by-Side Refrigerator", "GE", "GSS-####"),
        ("GE Counter-Depth French Door", "GE", "GCD-####"),
        ("GE Energy Star Refrigerator", "GE", "GES-####"),
        ("GE Top-Freezer Refrigerator", "GE", "GTF-####"),

        # Frigidaire
        ("Frigidaire Gallery Refrigerator", "Frigidaire", "FG-####"),
        ("Frigidaire French Door Refrigerator", "Frigidaire", "FFD-####"),
        ("Frigidaire Side-by-Side Refrigerator", "Frigidaire", "FSS-####"),
        ("Frigidaire 4-Door Refrigerator", "Frigidaire", "F4D-####"),
        ("Frigidaire Counter-Depth Refrigerator", "Frigidaire", "FCD-####"),

        # Panasonic
        ("Panasonic PrimeFresh Refrigerator", "Panasonic", "PPF-####"),
        ("Panasonic Frost-Free Refrigerator", "Panasonic", "PFF-####"),
        ("Panasonic Multi-Door Refrigerator", "Panasonic", "PMD-####"),
        ("Panasonic Bottom Freezer", "Panasonic", "PBF-####"),
        ("Panasonic Double Door Refrigerator", "Panasonic", "PDD-####"),

        # Hisense
        ("Hisense Smart Refrigerator", "Hisense", "HSR-####"),
        ("Hisense French Door Refrigerator", "Hisense", "HFD-####"),
        ("Hisense Side-by-Side Refrigerator", "Hisense", "HSS-####"),
        ("Hisense Convertible Refrigerator", "Hisense", "HCR-####"),
        ("Hisense Mini Fridge", "Hisense", "HMF-####"),

        # Electrolux
        ("Electrolux French Door Refrigerator", "Electrolux", "EFD-####"),
        ("Electrolux Counter-Depth Refrigerator", "Electrolux", "ECD-####"),
        ("Electrolux Side-by-Side Refrigerator", "Electrolux", "ESS-####"),
        ("Electrolux Multi-Door Refrigerator", "Electrolux", "EMD-####"),
        ("Electrolux Smart Refrigerator", "Electrolux", "ESR-####")
    ],
    "washing-machines": [
        # LG
        ("Front Load Washer", "LG", "FL-####"),
        ("TwinWash System", "LG", "TW-####"),
        ("LG TurboWash 360", "LG", "LTW-####"),
        ("LG Smart Wi-Fi Enabled Washer", "LG", "LSW-####"),
        ("LG Direct Drive Washer", "LG", "LDD-####"),

        # Samsung
        ("Top Load Washer", "Samsung", "TL-####"),
        ("Samsung FlexWash", "Samsung", "SFW-####"),
        ("Samsung QuickDrive Washer", "Samsung", "SQQ-####"),
        ("Samsung EcoBubble Washer", "Samsung", "SEB-####"),
        ("Samsung AI Control Washer", "Samsung", "SAI-####"),

        # Bosch
        ("Fully Automatic", "Bosch", "FA-####"),
        ("Bosch Serie 6 Front Load", "Bosch", "BS6-####"),
        ("Bosch Serie 8 Front Load", "Bosch", "BS8-####"),
        ("Bosch Top Load Washer", "Bosch", "BTL-####"),
        ("Bosch Compact Washer", "Bosch", "BCW-####"),

        # Whirlpool
        ("Semi-Automatic", "Whirlpool", "SA-####"),
        ("Whirlpool Stainwash Pro", "Whirlpool", "WSP-####"),
        ("Whirlpool FreshCare 7kg", "Whirlpool", "WFC-####"),
        ("Whirlpool 360 BloomWash Pro", "Whirlpool", "WBW-####"),
        ("Whirlpool Inverter Washer", "Whirlpool", "WIW-####"),

        # IFB
        ("IFB Front Load Washer", "IFB", "IFL-####"),
        ("IFB Top Load Washer", "IFB", "ITL-####"),
        ("IFB Executive Plus VX", "IFB", "IEP-####"),
        ("IFB Aqua Energie Washer", "IFB", "IAE-####"),
        ("IFB Senator Smart Touch", "IFB", "IST-####"),

        # Haier
        ("Haier Fully Automatic Washer", "Haier", "HFA-####"),
        ("Haier Top Load Washer", "Haier", "HTL-####"),
        ("Haier Front Load Washer", "Haier", "HFL-####"),
        ("Haier Direct Motion Washer", "Haier", "HDM-####"),
        ("Haier Dual Drum Washer", "Haier", "HDD-####"),

        # Panasonic
        ("Panasonic 8kg Front Load", "Panasonic", "PFL-####"),
        ("Panasonic Econavi Washer", "Panasonic", "PEC-####"),
        ("Panasonic Top Load Washer", "Panasonic", "PTL-####"),
        ("Panasonic StainMaster+", "Panasonic", "PSM-####"),
        ("Panasonic AI Smart Washer", "Panasonic", "PAI-####"),

        # Electrolux
        ("Electrolux UltimateCare 500", "Electrolux", "EUC-####"),
        ("Electrolux AutoDose Washer", "Electrolux", "EAD-####"),
        ("Electrolux Front Load Washer", "Electrolux", "EFL-####"),
        ("Electrolux SteamCare System", "Electrolux", "ESC-####"),
        ("Electrolux TimeManager Washer", "Electrolux", "ETM-####"),

        # Godrej
        ("Godrej Fully Automatic", "Godrej", "GFA-####"),
        ("Godrej Top Load Washer", "Godrej", "GTL-####"),
        ("Godrej Edge Pro Washer", "Godrej", "GEP-####"),
        ("Godrej Eon Washer", "Godrej", "GEW-####"),
        ("Godrej Ultra Wash", "Godrej", "GUW-####"),

        # Hitachi
        ("Hitachi Big Drum Washer", "Hitachi", "HBD-####"),
        ("Hitachi Auto Dosing Washer", "Hitachi", "HAD-####"),
        ("Hitachi Fully Automatic", "Hitachi", "HFA-####"),
        ("Hitachi Wind Iron Washer", "Hitachi", "HWI-####"),
        ("Hitachi Top Load Washer", "Hitachi", "HTL-####")
    ],
    "air-conditioners": [
        # LG
        ("Dual Inverter AC", "LG", "LGAC-####"),
        ("LG Smart ThinQ AC", "LG", "LGSQ-####"),
        ("LG Split AC 1.5 Ton", "LG", "LGSP-####"),
        ("LG Window AC 1 Ton", "LG", "LGWA-####"),
        ("LG 4-in-1 Convertible AC", "LG", "LGCV-####"),

        # Daikin
        ("Split AC 1.5 Ton", "Daikin", "DKAC-####"),
        ("Daikin Inverter AC", "Daikin", "DKIV-####"),
        ("Daikin 5-Star Energy Saver AC", "Daikin", "DKES-####"),
        ("Daikin Cassette AC", "Daikin", "DKCS-####"),
        ("Daikin Floor Standing AC", "Daikin", "DKFL-####"),

        # Hitachi
        ("Window AC 1 Ton", "Hitachi", "HTAC-####"),
        ("Hitachi iClean+ Split AC", "Hitachi", "HTIC-####"),
        ("Hitachi Expandable Inverter AC", "Hitachi", "HTEI-####"),
        ("Hitachi Smart WiFi AC", "Hitachi", "HTSW-####"),
        ("Hitachi Tower AC", "Hitachi", "HTTW-####"),

        # Samsung
        ("Smart AC with WiFi", "Samsung", "SMAC-####"),
        ("Samsung WindFree AC", "Samsung", "SMWF-####"),
        ("Samsung 8-Pole Digital Inverter AC", "Samsung", "SMDI-####"),
        ("Samsung Triple Inverter AC", "Samsung", "SMTI-####"),
        ("Samsung 5-Star Energy Efficient AC", "Samsung", "SMEE-####"),

        # Blue Star
        ("Portable AC", "Blue Star", "BPAC-####"),
        ("Blue Star Inverter Split AC", "Blue Star", "BSIV-####"),
        ("Blue Star Cassette AC", "Blue Star", "BSCAS-####"),
        ("Blue Star 1.5 Ton Window AC", "Blue Star", "BSWA-####"),
        ("Blue Star Heavy Duty AC", "Blue Star", "BSHD-####"),

        # Voltas
        ("Voltas 2 Ton Split AC", "Voltas", "VTS2-####"),
        ("Voltas Adjustable Inverter AC", "Voltas", "VTAI-####"),
        ("Voltas Tower AC", "Voltas", "VTTA-####"),
        ("Voltas Window AC 1.5 Ton", "Voltas", "VTWA-####"),
        ("Voltas 5-Star AC", "Voltas", "VT5S-####"),

        # Carrier
        ("Carrier Estrella Inverter AC", "Carrier", "CRST-####"),
        ("Carrier 2 Ton Split AC", "Carrier", "CRSP-####"),
        ("Carrier Window AC 1.5 Ton", "Carrier", "CRWA-####"),
        ("Carrier Durafresh AC", "Carrier", "CRDF-####"),
        ("Carrier XPower Gold AC", "Carrier", "CRXP-####"),

        # Panasonic
        ("Panasonic Twin Cool AC", "Panasonic", "PNTC-####"),
        ("Panasonic Smart AI AC", "Panasonic", "PNSA-####"),
        ("Panasonic 5-Star Inverter AC", "Panasonic", "PNIV-####"),
        ("Panasonic Floor Standing AC", "Panasonic", "PNFL-####"),
        ("Panasonic Compact Split AC", "Panasonic", "PNCS-####"),

        # Whirlpool
        ("Whirlpool Magicool Inverter AC", "Whirlpool", "WPMC-####"),
        ("Whirlpool 1.5 Ton Split AC", "Whirlpool", "WPSP-####"),
        ("Whirlpool 3D Cool AC", "Whirlpool", "WP3D-####"),
        ("Whirlpool Window AC 1 Ton", "Whirlpool", "WPWA-####"),
        ("Whirlpool TurboCool AC", "Whirlpool", "WPTC-####"),

        # Godrej
        ("Godrej Green Inverter AC", "Godrej", "GDGI-####"),
        ("Godrej Nano Smart AC", "Godrej", "GDNS-####"),
        ("Godrej 1.5 Ton Window AC", "Godrej", "GDWA-####"),
        ("Godrej 5-Star Dual Inverter AC", "Godrej", "GD5S-####"),
        ("Godrej Convertible 6-in-1 AC", "Godrej", "GD6I-####")
    ],
    "vacuum-cleaners": [
        # iRobot
        ("Robotic Vacuum Cleaner", "iRobot", "RV-####"),
        ("iRobot Roomba i7+", "iRobot", "RVI7-####"),
        ("iRobot Roomba s9+", "iRobot", "RVS9-####"),
        ("iRobot Roomba 692", "iRobot", "RV69-####"),
        ("iRobot Braava Jet M6", "iRobot", "RVBJ-####"),

        # Dyson
        ("Handheld Vacuum", "Dyson", "HV-####"),
        ("Dyson V11 Torque Drive", "Dyson", "DV11-####"),
        ("Dyson V15 Detect", "Dyson", "DV15-####"),
        ("Dyson Omni-glide", "Dyson", "DVO-####"),
        ("Dyson Outsize Absolute+", "Dyson", "DVOA-####"),

        # Karcher
        ("Wet & Dry Vacuum", "Karcher", "WD-####"),
        ("Karcher WD 3", "Karcher", "KWD3-####"),
        ("Karcher WD 5 Premium", "Karcher", "KWD5-####"),
        ("Karcher DS 6 Water Filter Vacuum", "Karcher", "KDS6-####"),
        ("Karcher VC 3 Bagless Vacuum", "Karcher", "KVC3-####"),

        # Shark
        ("Cordless Stick Vacuum", "Shark", "CSV-####"),
        ("Shark Vertex Cordless", "Shark", "SVC-####"),
        ("Shark Navigator Lift-Away", "Shark", "SNL-####"),
        ("Shark Rocket Ultra-Light", "Shark", "SRU-####"),
        ("Shark Rotator Powered Lift-Away", "Shark", "SRP-####"),

        # Eureka Forbes
        ("Canister Vacuum", "Eureka Forbes", "CV-####"),
        ("Eureka Forbes Wet & Dry", "Eureka Forbes", "EWD-####"),
        ("Eureka Forbes Trendy Zip", "Eureka Forbes", "ETZ-####"),
        ("Eureka Forbes Super Clean", "Eureka Forbes", "ESC-####"),
        ("Eureka Forbes Robo Vac", "Eureka Forbes", "ERV-####"),

        # Bissell
        ("Bissell CrossWave Pet Pro", "Bissell", "BCPP-####"),
        ("Bissell MultiClean Wet & Dry", "Bissell", "BMWD-####"),
        ("Bissell CleanView Swivel", "Bissell", "BCS-####"),
        ("Bissell TurboClean PowerBrush", "Bissell", "BTP-####"),
        ("Bissell SpotClean ProHeat", "Bissell", "BSP-####"),

        # Philips
        ("Philips PowerPro Compact", "Philips", "PPC-####"),
        ("Philips SpeedPro Max", "Philips", "PSM-####"),
        ("Philips 2000 Series Bagless", "Philips", "P2SB-####"),
        ("Philips Performer Silent", "Philips", "PPS-####"),
        ("Philips AquaTrio Cordless", "Philips", "PAQ-####"),

        # Xiaomi
        ("Xiaomi Mi Robot Vacuum Mop", "Xiaomi", "XRM-####"),
        ("Xiaomi Dreame V11", "Xiaomi", "XDV-####"),
        ("Xiaomi Roidmi F8 Storm", "Xiaomi", "XRF-####"),
        ("Xiaomi Mi Handheld Vacuum", "Xiaomi", "XMHV-####"),
        ("Xiaomi Mijia Vacuum Cleaner", "Xiaomi", "XMV-####"),

        # Black+Decker
        ("Black+Decker 20V Max", "Black+Decker", "BD20-####"),
        ("Black+Decker Dustbuster", "Black+Decker", "BDD-####"),
        ("Black+Decker 3-in-1 Stick Vacuum", "Black+Decker", "BDS-####"),
        ("Black+Decker AdvancedClean+", "Black+Decker", "BDAC-####"),
        ("Black+Decker Flex Car Vacuum", "Black+Decker", "BDFC-####"),

        # Samsung
        ("Samsung Jet 90 Stick Vacuum", "Samsung", "SJ90-####"),
        ("Samsung POWERbot R7040", "Samsung", "SPR7-####"),
        ("Samsung Jet Bot AI+", "Samsung", "SJBA-####"),
        ("Samsung Clean Station", "Samsung", "SCS-####"),
        ("Samsung Jet 75 Pet", "Samsung", "SJP-####")
    ],
    "microwaves": [
        # Samsung
        ("Convection Microwave", "Samsung", "CMW-####"),
        ("Samsung Grill Microwave", "Samsung", "SGM-####"),
        ("Samsung Solo Microwave", "Samsung", "SSM-####"),
        ("Samsung Smart Microwave", "Samsung", "SSMW-####"),
        ("Samsung Countertop Microwave", "Samsung", "SCMW-####"),

        # LG
        ("Grill Microwave", "LG", "GMW-####"),
        ("LG NeoChef Microwave", "LG", "LNC-####"),
        ("LG Over-the-Range Microwave", "LG", "LOTR-####"),
        ("LG Smart Inverter Microwave", "LG", "LSI-####"),
        ("LG 1.5 Cu Ft Microwave", "LG", "L15C-####"),

        # Panasonic
        ("Solo Microwave", "Panasonic", "SMW-####"),
        ("Panasonic Inverter Microwave", "Panasonic", "PIM-####"),
        ("Panasonic Genius Sensor Microwave", "Panasonic", "PGS-####"),
        ("Panasonic Compact Microwave", "Panasonic", "PCM-####"),
        ("Panasonic Stainless Steel Microwave", "Panasonic", "PSSM-####"),

        # Toshiba
        ("Inverter Microwave", "Toshiba", "IMW-####"),
        ("Toshiba Smart Sensor Microwave", "Toshiba", "TSSM-####"),
        ("Toshiba Countertop Microwave", "Toshiba", "TCMW-####"),
        ("Toshiba Convection Microwave", "Toshiba", "TCM-####"),
        ("Toshiba Eco Mode Microwave", "Toshiba", "TEMW-####"),

        # Whirlpool
        ("Over-the-Range Microwave", "Whirlpool", "OTR-####"),
        ("Whirlpool Low Profile Microwave", "Whirlpool", "WLP-####"),
        ("Whirlpool Smart Microwave", "Whirlpool", "WSM-####"),
        ("Whirlpool Countertop Microwave", "Whirlpool", "WCM-####"),
        ("Whirlpool Over-the-Counter Microwave", "Whirlpool", "WOTC-####"),

        # GE
        ("GE Profile Microwave", "GE", "GEP-####"),
        ("GE Over-the-Range Microwave", "GE", "GEOTR-####"),
        ("GE Smart Microwave", "GE", "GESM-####"),
        ("GE Countertop Microwave", "GE", "GECM-####"),
        ("GE Compact Microwave", "GE", "GECP-####"),

        # Breville
        ("Breville Quick Touch Microwave", "Breville", "BQT-####"),
        ("Breville Smooth Wave Microwave", "Breville", "BSW-####"),
        ("Breville Smart Inverter Microwave", "Breville", "BSI-####"),
        ("Breville Compact Wave Soft Microwave", "Breville", "BCW-####"),
        ("Breville Convection Microwave", "Breville", "BCMW-####"),

        # Sharp
        ("Sharp Carousel Microwave", "Sharp", "SCM-####"),
        ("Sharp Smart Sensor Microwave", "Sharp", "SSSM-####"),
        ("Sharp Over-the-Range Microwave", "Sharp", "SOTR-####"),
        ("Sharp Convection Microwave", "Sharp", "SCMW-####"),
        ("Sharp Stainless Steel Microwave", "Sharp", "SSSM-####"),

        # Bosch
        ("Bosch Built-in Microwave", "Bosch", "BBM-####"),
        ("Bosch Over-the-Range Microwave", "Bosch", "BOTR-####"),
        ("Bosch Series 800 Microwave", "Bosch", "B800-####"),
        ("Bosch Smart Microwave", "Bosch", "BSM-####"),
        ("Bosch Convection Microwave", "Bosch", "BCM-####"),

        # Haier
        ("Haier Countertop Microwave", "Haier", "HCM-####"),
        ("Haier Compact Microwave", "Haier", "HCPM-####"),
        ("Haier Convection Microwave", "Haier", "HCMW-####"),
        ("Haier Digital Microwave", "Haier", "HDM-####"),
        ("Haier Stainless Steel Microwave", "Haier", "HSSM-####")
    ],
    "coffee-makers": [
        # De'Longhi
        ("Espresso Machine", "De'Longhi", "EM-####"),
        ("De'Longhi Cappuccino Maker", "De'Longhi", "DCM-####"),
        ("De'Longhi Latte Machine", "De'Longhi", "DLM-####"),
        ("De'Longhi Fully Automatic Espresso", "De'Longhi", "DFAE-####"),
        ("De'Longhi Dedica Coffee Machine", "De'Longhi", "DDCM-####"),

        # Keurig
        ("Drip Coffee Maker", "Keurig", "DCM-####"),
        ("Keurig K-Elite", "Keurig", "KKE-####"),
        ("Keurig K-Duo", "Keurig", "KKD-####"),
        ("Keurig K-Mini", "Keurig", "KKM-####"),
        ("Keurig K-Slim", "Keurig", "KKS-####"),

        # Bodum
        ("French Press", "Bodum", "FP-####"),
        ("Bodum Travel Press", "Bodum", "BTP-####"),
        ("Bodum Pour Over Coffee Maker", "Bodum", "BPO-####"),
        ("Bodum Electric Coffee Maker", "Bodum", "BEC-####"),
        ("Bodum Bistro Coffee Maker", "Bodum", "BBC-####"),

        # Ninja
        ("Cold Brew Maker", "Ninja", "CBM-####"),
        ("Ninja Hot and Cold Brewed System", "Ninja", "NHCB-####"),
        ("Ninja DualBrew Pro", "Ninja", "NDBP-####"),
        ("Ninja Specialty Coffee Maker", "Ninja", "NSCM-####"),
        ("Ninja Programmable Coffee Maker", "Ninja", "NPCM-####"),

        # Nespresso
        ("Single Serve Coffee Maker", "Nespresso", "SSCM-####"),
        ("Nespresso Vertuo Plus", "Nespresso", "NVP-####"),
        ("Nespresso Essenza Mini", "Nespresso", "NEM-####"),
        ("Nespresso CitiZ", "Nespresso", "NC-####"),
        ("Nespresso Lattissima Pro", "Nespresso", "NLP-####"),

        # Breville
        ("Breville Barista Express", "Breville", "BBE-####"),
        ("Breville Barista Touch", "Breville", "BBT-####"),
        ("Breville Oracle Touch", "Breville", "BOT-####"),
        ("Breville Precision Brewer", "Breville", "BPB-####"),
        ("Breville Café Roma", "Breville", "BCR-####"),

        # Cuisinart
        ("Cuisinart Grind & Brew", "Cuisinart", "CGB-####"),
        ("Cuisinart Single Serve", "Cuisinart", "CSS-####"),
        ("Cuisinart DCC-3200", "Cuisinart", "CD3200-####"),
        ("Cuisinart Programmable Coffee Maker", "Cuisinart", "CPCM-####"),
        ("Cuisinart Burr Grind & Brew", "Cuisinart", "CBGB-####"),

        # Hamilton Beach
        ("Hamilton Beach FlexBrew", "Hamilton Beach", "HBF-####"),
        ("Hamilton Beach BrewStation", "Hamilton Beach", "HBB-####"),
        ("Hamilton Beach Cold Brew", "Hamilton Beach", "HBCB-####"),
        ("Hamilton Beach Espresso Maker", "Hamilton Beach", "HBEM-####"),
        ("Hamilton Beach Stainless Steel Coffee Maker", "Hamilton Beach", "HBSSC-####"),

        # Mr. Coffee
        ("Mr. Coffee 12-Cup", "Mr. Coffee", "MC12-####"),
        ("Mr. Coffee Iced Coffee Maker", "Mr. Coffee", "MCIC-####"),
        ("Mr. Coffee Espresso and Cappuccino Maker", "Mr. Coffee", "MCEC-####"),
        ("Mr. Coffee Programmable Coffee Maker", "Mr. Coffee", "MCPCM-####"),
        ("Mr. Coffee Single-Serve Frappe Maker", "Mr. Coffee", "MCSF-####"),

        # Philips
        ("Philips 3200 Series Espresso Machine", "Philips", "P3200-####"),
        ("Philips LatteGo Coffee Machine", "Philips", "PLG-####"),
        ("Philips Grind & Brew Coffee Maker", "Philips", "PGB-####"),
        ("Philips Drip Coffee Maker", "Philips", "PDC-####"),
        ("Philips Compact Espresso Machine", "Philips", "PCE-####")
    ],
    "dishwashers": [
        # Bosch
        ("Built-in Dishwasher", "Bosch", "BDW-####"),
        ("Bosch 800 Series", "Bosch", "B800-####"),
        ("Bosch 500 Series", "Bosch", "B500-####"),
        ("Bosch 300 Series", "Bosch", "B300-####"),
        ("Bosch Ascenta Dishwasher", "Bosch", "BADW-####"),

        # Whirlpool
        ("Portable Dishwasher", "Whirlpool", "PDW-####"),
        ("Whirlpool Heavy-Duty Dishwasher", "Whirlpool", "WHDW-####"),
        ("Whirlpool Smart Dishwasher", "Whirlpool", "WSDW-####"),
        ("Whirlpool Stainless Steel Dishwasher", "Whirlpool", "WSSD-####"),
        ("Whirlpool 24-inch Tall Tub Dishwasher", "Whirlpool", "WTTD-####"),

        # Farberware
        ("Countertop Dishwasher", "Farberware", "CTD-####"),
        ("Farberware Professional Dishwasher", "Farberware", "FPDW-####"),
        ("Farberware Compact Dishwasher", "Farberware", "FCDW-####"),
        ("Farberware Touch Control Dishwasher", "Farberware", "FTCD-####"),
        ("Farberware Energy Efficient Dishwasher", "Farberware", "FEED-####"),

        # Samsung
        ("Smart Dishwasher", "Samsung", "SDW-####"),
        ("Samsung StormWash Dishwasher", "Samsung", "SSWD-####"),
        ("Samsung Bespoke Dishwasher", "Samsung", "SBDW-####"),
        ("Samsung Quiet Drive Dishwasher", "Samsung", "SQDW-####"),
        ("Samsung WaterWall Dishwasher", "Samsung", "SWWD-####"),

        # Midea
        ("Compact Dishwasher", "Midea", "CDW-####"),
        ("Midea 6-Place Countertop Dishwasher", "Midea", "M6PD-####"),
        ("Midea Built-in Dishwasher", "Midea", "MBDW-####"),
        ("Midea Stainless Steel Dishwasher", "Midea", "MSSD-####"),
        ("Midea High-Capacity Dishwasher", "Midea", "MHCD-####"),

        # GE Appliances
        ("GE Profile Dishwasher", "GE", "GPDW-####"),
        ("GE Smart Dishwasher", "GE", "GSDW-####"),
        ("GE 24-inch Built-in Dishwasher", "GE", "G24B-####"),
        ("GE Front Control Dishwasher", "GE", "GFCW-####"),
        ("GE Fingerprint Resistant Dishwasher", "GE", "GFRD-####"),

        # LG
        ("LG TrueSteam Dishwasher", "LG", "LGTSD-####"),
        ("LG QuadWash Dishwasher", "LG", "LGQW-####"),
        ("LG Smart Wi-Fi Dishwasher", "LG", "LGSW-####"),
        ("LG Front Control Dishwasher", "LG", "LGFC-####"),
        ("LG Stainless Steel Tub Dishwasher", "LG", "LGST-####"),

        # Frigidaire
        ("Frigidaire Gallery Dishwasher", "Frigidaire", "FGDW-####"),
        ("Frigidaire Portable Dishwasher", "Frigidaire", "FPDW-####"),
        ("Frigidaire Energy Star Dishwasher", "Frigidaire", "FESD-####"),
        ("Frigidaire 18-inch Dishwasher", "Frigidaire", "F18D-####"),
        ("Frigidaire Black Stainless Dishwasher", "Frigidaire", "FBSD-####"),

        # KitchenAid
        ("KitchenAid FreeFlex Dishwasher", "KitchenAid", "KFFD-####"),
        ("KitchenAid Panel-Ready Dishwasher", "KitchenAid", "KPRD-####"),
        ("KitchenAid Third Rack Dishwasher", "KitchenAid", "K3RD-####"),
        ("KitchenAid PrintShield Dishwasher", "KitchenAid", "KPSD-####"),
        ("KitchenAid Quiet Dishwasher", "KitchenAid", "KQDW-####"),

        # Maytag
        ("Maytag Front Control Dishwasher", "Maytag", "MFCD-####"),
        ("Maytag Stainless Steel Dishwasher", "Maytag", "MSSD-####"),
        ("Maytag High-Pressure Dishwasher", "Maytag", "MHPD-####"),
        ("Maytag PowerBlast Dishwasher", "Maytag", "MPBD-####"),
        ("Maytag QuietSeries Dishwasher", "Maytag", "MQSD-####")
    ],
    "water-purifiers": [
        # Kent
        ("RO + UV Water Purifier", "Kent", "KWP-####"),
        ("Kent Grand Plus RO + UV", "Kent", "KGP-####"),
        ("Kent Pearl RO Water Purifier", "Kent", "KPR-####"),
        ("Kent Supreme Extra RO + UF + UV", "Kent", "KSE-####"),
        ("Kent Ultra Storage UV Purifier", "Kent", "KUS-####"),

        # Pureit
        ("Gravity-Based Purifier", "Pureit", "GBP-####"),
        ("Pureit Classic RO + UV", "Pureit", "PCR-####"),
        ("Pureit Copper+ RO", "Pureit", "PCP-####"),
        ("Pureit Ultima Eco RO + UV", "Pureit", "PUE-####"),
        ("Pureit Marvella RO + UV + MF", "Pureit", "PMR-####"),

        # Aquaguard
        ("Alkaline Water Purifier", "Aquaguard", "AWP-####"),
        ("Aquaguard Geneus RO + UV + UF", "Aquaguard", "AGG-####"),
        ("Aquaguard Magna NXT RO + UV", "Aquaguard", "AMN-####"),
        ("Aquaguard Enhance RO + UV + UF", "Aquaguard", "AER-####"),
        ("Aquaguard Superb RO + UV + UF", "Aquaguard", "ASU-####"),

        # Blue Star
        ("Under-Sink Water Purifier", "Blue Star", "USWP-####"),
        ("Blue Star Excella RO + UV", "Blue Star", "BSE-####"),
        ("Blue Star Aristo RO + UV", "Blue Star", "BSA-####"),
        ("Blue Star Stella RO + UV + Hot Water", "Blue Star", "BST-####"),
        ("Blue Star Majesto RO + UV", "Blue Star", "BSM-####"),

        # Livpure
        ("Tankless Water Purifier", "Livpure", "TWP-####"),
        ("Livpure Glo RO + UV + Mineralizer", "Livpure", "LGR-####"),
        ("Livpure Envy Alkaline RO", "Livpure", "LEA-####"),
        ("Livpure Touch Plus RO + UV", "Livpure", "LTP-####"),
        ("Livpure Pep Pro Plus RO + UV", "Livpure", "LPP-####"),

        # Havells
        ("Havells Max RO + UV + UF", "Havells", "HMX-####"),
        ("Havells Digitouch Alkaline RO + UV", "Havells", "HDA-####"),
        ("Havells Pro Alkaline Water Purifier", "Havells", "HPA-####"),
        ("Havells Delite Alkaline RO + UV", "Havells", "HDA-####"),
        ("Havells Fab Alkaline RO + UV", "Havells", "HFA-####"),

        # AO Smith
        ("AO Smith Z9 RO + SCMT", "AO Smith", "ASZ-####"),
        ("AO Smith Z8 RO + Hot Water", "AO Smith", "ASZ8-####"),
        ("AO Smith X2 UV + UF", "AO Smith", "ASX2-####"),
        ("AO Smith ProPlanet P4 RO + UV", "AO Smith", "ASP4-####"),
        ("AO Smith Intellipure RO + UV", "AO Smith", "ASI-####"),

        # Tata Swach
        ("Tata Swach Non-Electric Gravity", "Tata Swach", "TSN-####"),
        ("Tata Swach Smart RO + UV", "Tata Swach", "TSS-####"),
        ("Tata Swach Ultima RO + UV + UF", "Tata Swach", "TSU-####"),
        ("Tata Swach Nova Silver RO + UV", "Tata Swach", "TSN2-####"),
        ("Tata Swach Cristella Gravity", "Tata Swach", "TSC-####"),

        # Nasaka
        ("Nasaka Tulip N1 RO + UV", "Nasaka", "NTN-####"),
        ("Nasaka Xtra Pure RO + UV", "Nasaka", "NXP-####"),
        ("Nasaka Cosmos Alkaline RO + UV", "Nasaka", "NCA-####"),
        ("Nasaka AquaSure RO + UF", "Nasaka", "NAS-####"),
        ("Nasaka Max Sure RO + UV", "Nasaka", "NMS-####"),

        # Eureka Forbes
        ("Eureka Forbes Aquasure Smart Plus RO", "Eureka Forbes", "EFA-####"),
        ("Eureka Forbes Dr. Aquaguard Magna RO + UV", "Eureka Forbes", "EFD-####"),
        ("Eureka Forbes Enhance RO + UV + MTDS", "Eureka Forbes", "EFE-####"),
        ("Eureka Forbes Sure RO + UV", "Eureka Forbes", "EFS-####"),
        ("Eureka Forbes Active Copper RO + UV", "Eureka Forbes", "EFA2-####")
    ],
    "air-purifiers": [
        # Dyson
        ("HEPA Air Purifier", "Dyson", "HAP-####"),
        ("Dyson Pure Cool Air Purifier", "Dyson", "DPC-####"),
        ("Dyson Pure Hot + Cool", "Dyson", "DPH-####"),
        ("Dyson TP04 HEPA Air Purifier", "Dyson", "DTP-####"),
        ("Dyson Big+Quiet Air Purifier", "Dyson", "DBQ-####"),

        # Philips
        ("Smart Air Purifier", "Philips", "SAP-####"),
        ("Philips 3000i Series Air Purifier", "Philips", "P3S-####"),
        ("Philips 2000i Series Air Purifier", "Philips", "P2S-####"),
        ("Philips 1000 Series Air Purifier", "Philips", "P1S-####"),
        ("Philips NanoProtect HEPA Purifier", "Philips", "PNH-####"),

        # Honeywell
        ("UV-C Air Purifier", "Honeywell", "UVP-####"),
        ("Honeywell Air Touch i8", "Honeywell", "HAT-####"),
        ("Honeywell HPA300 HEPA Air Purifier", "Honeywell", "HPA-####"),
        ("Honeywell Move Pure Car Purifier", "Honeywell", "HMP-####"),
        ("Honeywell AirGenius 5", "Honeywell", "HAG-####"),

        # Coway
        ("Activated Carbon Purifier", "Coway", "ACP-####"),
        ("Coway AirMega 250", "Coway", "CAM-####"),
        ("Coway AirMega 400S", "Coway", "CAM4-####"),
        ("Coway Sleek Pro AP-1009", "Coway", "CSP-####"),
        ("Coway Storm Air Purifier", "Coway", "CST-####"),

        # Sharp
        ("Portable Air Purifier", "Sharp", "PAP-####"),
        ("Sharp Plasmacluster Air Purifier", "Sharp", "SPA-####"),
        ("Sharp FP-F40E-T Air Purifier", "Sharp", "SFP-####"),
        ("Sharp FX-J80U HEPA Purifier", "Sharp", "SFJ-####"),
        ("Sharp KC-850U Humidifying Purifier", "Sharp", "SKC-####"),

        # Blueair
        ("Blueair Classic 480i Air Purifier", "Blueair", "BCA-####"),
        ("Blueair HealthProtect 7770i", "Blueair", "BHP-####"),
        ("Blueair Blue Pure 211+", "Blueair", "BBP-####"),
        ("Blueair Pro L Air Purifier", "Blueair", "BPL-####"),
        ("Blueair DustMagnet 5240i", "Blueair", "BDM-####"),

        # Levoit
        ("Levoit Core 300 HEPA Purifier", "Levoit", "LCP-####"),
        ("Levoit LV-H132 Air Purifier", "Levoit", "LLH-####"),
        ("Levoit Core 400S Smart Purifier", "Levoit", "LC4-####"),
        ("Levoit Core 600S Air Purifier", "Levoit", "LC6-####"),
        ("Levoit PlasmaPro 400S", "Levoit", "LPP-####"),

        # Winix
        ("Winix 5500-2 HEPA Air Purifier", "Winix", "W55-####"),
        ("Winix HR900 Ultimate Pet Purifier", "Winix", "WH9-####"),
        ("Winix AM90 Smart Purifier", "Winix", "WAM-####"),
        ("Winix 9800 HEPA Air Purifier", "Winix", "W98-####"),
        ("Winix XLC Large Room Purifier", "Winix", "WXL-####"),

        # Medify Air
        ("Medify MA-40 HEPA Purifier", "Medify Air", "MMA-####"),
        ("Medify MA-50 Medical Grade Purifier", "Medify Air", "MM5-####"),
        ("Medify MA-25 Compact HEPA", "Medify Air", "MM2-####"),
        ("Medify MA-125 Large Room Purifier", "Medify Air", "MM1-####"),
        ("Medify MA-15 Air Purifier", "Medify Air", "MM15-####"),

        # TruSens
        ("TruSens Z-2000 HEPA Purifier", "TruSens", "TZ2-####"),
        ("TruSens Z-3000 Smart Air Purifier", "TruSens", "TZ3-####"),
        ("TruSens Z-1000 Small Room Purifier", "TruSens", "TZ1-####"),
        ("TruSens UV-C Light Purifier", "TruSens", "TUV-####"),
        ("TruSens Pet HEPA Air Purifier", "TruSens", "TPH-####")
    ],
    "induction-cooktops": [
        # Prestige
        ("Single Burner Induction", "Prestige", "SBI-####"),
        ("Prestige PIC 20 1200W Induction", "Prestige", "P20-####"),
        ("Prestige PIC 16.0+ Induction", "Prestige", "P16-####"),
        ("Prestige PIC 6.1 V3 Induction", "Prestige", "P61-####"),
        ("Prestige PIC 3.1 V3 Induction", "Prestige", "P31-####"),

        # Philips
        ("Double Burner Induction", "Philips", "DBI-####"),
        ("Philips Viva Collection HD4928", "Philips", "PHD-####"),
        ("Philips HD4938/01 Sensor Touch", "Philips", "PHS-####"),
        ("Philips HD4929 2100W Induction", "Philips", "PH9-####"),
        ("Philips Daily Collection Induction", "Philips", "PDC-####"),

        # Bosch
        ("Smart Induction Cooktop", "Bosch", "SIC-####"),
        ("Bosch Serie 6 Induction Hob", "Bosch", "BS6-####"),
        ("Bosch PXX875D67E Induction", "Bosch", "BPX-####"),
        ("Bosch PIE631FB1E 4-Zone Induction", "Bosch", "BPI-####"),
        ("Bosch PVQ731F15E Frameless Induction", "Bosch", "BPV-####"),

        # Bajaj
        ("Infrared Induction", "Bajaj", "IIC-####"),
        ("Bajaj Majesty ICX 7 Induction", "Bajaj", "BMX-####"),
        ("Bajaj ICX Pearl Induction", "Bajaj", "BIP-####"),
        ("Bajaj Majesty Slim Induction", "Bajaj", "BMS-####"),
        ("Bajaj ICX Neo Induction", "Bajaj", "BIN-####"),

        # Panasonic
        ("Freestanding Induction Range", "Panasonic", "FIR-####"),
        ("Panasonic KY-T937V Induction", "Panasonic", "PKT-####"),
        ("Panasonic KY-E227D Induction", "Panasonic", "PKE-####"),
        ("Panasonic KY-B84A 4-Zone Induction", "Panasonic", "PKB-####"),
        ("Panasonic KY-C227E Induction", "Panasonic", "PKC-####"),

        # Havells
        ("Havells Insta Cook PT Induction", "Havells", "HIP-####"),
        ("Havells Insta Cook ST-X Induction", "Havells", "HIS-####"),
        ("Havells Insta Cook ET-X Induction", "Havells", "HIE-####"),
        ("Havells Crystal Induction", "Havells", "HCI-####"),
        ("Havells PT Induction with Digital Control", "Havells", "HDC-####"),

        # Pigeon
        ("Pigeon Rapido Slim Induction", "Pigeon", "PRS-####"),
        ("Pigeon Acer Plus Induction", "Pigeon", "PAP-####"),
        ("Pigeon Cruise 1800W Induction", "Pigeon", "PC8-####"),
        ("Pigeon Rapido Touch Induction", "Pigeon", "PRT-####"),
        ("Pigeon Stovekraft Induction", "Pigeon", "PSK-####"),

        # Usha
        ("Usha CookJoy Induction", "Usha", "UCJ-####"),
        ("Usha 2000W Induction Cooktop", "Usha", "U2W-####"),
        ("Usha IR Touch Induction", "Usha", "UIT-####"),
        ("Usha Electric Induction", "Usha", "UEI-####"),
        ("Usha Ebony Smart Induction", "Usha", "UES-####"),

        # Glen
        ("Glen 4-Zone Induction", "Glen", "G4Z-####"),
        ("Glen Glass Top Induction", "Glen", "GGT-####"),
        ("Glen Digital Touch Induction", "Glen", "GDT-####"),
        ("Glen 2000W Auto Cook Induction", "Glen", "GAI-####"),
        ("Glen Built-in Induction", "Glen", "GBI-####"),

        # Whirlpool
        ("Whirlpool 2000W Induction", "Whirlpool", "W2W-####"),
        ("Whirlpool Built-in Induction", "Whirlpool", "WBI-####"),
        ("Whirlpool Solo Induction", "Whirlpool", "WSI-####"),
        ("Whirlpool Smart Touch Induction", "Whirlpool", "WST-####"),
        ("Whirlpool Digital Induction", "Whirlpool", "WDI-####")
    ]
}

descriptions = {
    "refrigerators": [
        "A high-capacity refrigerator with multi-zone cooling, smart temperature control, and an energy-efficient inverter compressor.",
        "Designed for modern kitchens, this refrigerator features a sleek stainless steel finish, adjustable shelves, and an advanced humidity control system.",
        "A smart refrigerator with Wi-Fi connectivity, voice assistant support, and an interactive touchscreen for meal planning and grocery management.",
        "An energy-efficient refrigerator with a frost-free design, rapid cooling technology, and multi-airflow circulation for even temperature distribution.",
        "A compact and space-saving refrigerator with a powerful cooling system, optimized storage compartments, and an antibacterial deodorizer.",
        "A double-door refrigerator with convertible storage, precise temperature regulation, and a built-in ice maker for added convenience.",
        "A side-by-side refrigerator with touch panel controls, water and ice dispenser, and a large capacity for organized food storage.",
        "A four-door refrigerator with a digital inverter compressor, AI-powered freshness preservation, and a customizable cooling zone.",
        "A mini-refrigerator with a sleek design, energy-efficient cooling, and adjustable shelves, perfect for dorms and small apartments.",
        "A solar-powered refrigerator with advanced insulation, battery backup, and eco-friendly cooling for sustainable living."
    ],
    "washing-machines": [
        "A fully automatic front-load washing machine with AI-powered fabric care, multiple wash cycles, and low-noise operation.",
        "An advanced top-load washing machine with a high-spin speed, deep-clean technology, and an auto-restart function.",
        "A twin-load washing machine allowing you to wash two separate loads simultaneously, with smart app control and AI-powered detergent optimization.",
        "A powerful semi-automatic washing machine featuring a large drum, air turbo drying system, and durable rust-proof body.",
        "A compact and portable washing machine ideal for small spaces, with a powerful motor, water-saving technology, and multiple wash modes.",
        "A high-capacity washing machine with a stainless steel drum, smart load detection, and an anti-allergen wash cycle.",
        "A steam wash washing machine that removes tough stains, bacteria, and allergens while keeping fabrics fresh and soft.",
        "A Wi-Fi-enabled washing machine with remote control, voice assistant support, and auto detergent dispensing for effortless laundry management.",
        "An eco-friendly washing machine with water recycling technology, minimal detergent usage, and energy-efficient operation.",
        "A noise-free inverter washing machine with gentle drum motion, smart rinse technology, and an extra-large door for easy loading."
    ],
    "air-conditioners": [
        "A high-performance split air conditioner with inverter technology, rapid cooling, and anti-bacterial filters for pure air.",
        "A smart air conditioner with voice control compatibility, energy-efficient operation, and customizable cooling modes.",
        "A portable air conditioner designed for easy movement, offering multiple fan speeds, dehumidification mode, and auto temperature sensing.",
        "A window air conditioner with a powerful cooling system, eco-friendly refrigerant, and easy installation for efficient home cooling.",
        "An advanced air conditioner with humidity control, silent operation, and UV purification for a cleaner and healthier indoor environment.",
        "A dual-inverter AC with ultra-fast cooling, power-saving mode, and an auto-clean function for low maintenance.",
        "An AI-powered air conditioner with adaptive cooling, real-time energy tracking, and smart temperature regulation.",
        "A multi-split AC with multiple indoor units, zone-wise temperature control, and a compact outdoor unit for efficient cooling.",
        "A hybrid AC with both cooling and heating capabilities, ensuring comfort in all seasons.",
        "A solar-powered air conditioner with energy-efficient cooling and integrated battery storage for sustainable performance."
    ],
    "vacuum-cleaners": [
        "A robotic vacuum cleaner with smart mapping technology, voice assistant integration, and powerful suction for hands-free cleaning.",
        "A cordless stick vacuum with lightweight design, multi-surface adaptability, and an extended battery life for effortless home cleaning.",
        "A powerful wet & dry vacuum cleaner featuring high suction power, a large dust tank, and specialized attachments for deep cleaning.",
        "A handheld vacuum cleaner with compact design, HEPA filtration, and strong suction power for quick and easy spot cleaning.",
        "An advanced canister vacuum with a multi-cyclonic filtration system, silent motor operation, and an ergonomic design for enhanced mobility.",
        "A pet hair vacuum cleaner with tangle-free brush roll, powerful suction, and an odor-neutralizing HEPA filter.",
        "A UV sterilizing vacuum cleaner that eliminates dust mites, bacteria, and allergens for a healthier living space.",
        "A backpack vacuum cleaner with a lightweight design, powerful motor, and high-capacity dust bin for extended use.",
        "A commercial-grade vacuum cleaner with an industrial motor, wide nozzle, and large dust capacity for heavy-duty cleaning.",
        "A self-cleaning robotic vacuum with a docking station, automatic dust disposal, and real-time home mapping for efficient navigation."
    ],
    "microwaves": [
        "A high-power convection microwave with grill functionality, auto-cook menus, and touch control for effortless cooking.",
        "A solo microwave featuring quick heating, defrost functionality, and a durable scratch-resistant interior.",
        "A smart microwave with AI-assisted cooking, voice command support, and an interactive LED control panel.",
        "A large-capacity inverter microwave with even heating technology, energy-saving mode, and a sleek modern design.",
        "An over-the-range microwave with built-in exhaust fan, multiple cooking presets, and sensor technology for optimal cooking results.",
        "A retro-style microwave with a compact design, manual controls, and a nostalgic aesthetic.",
        "A child-safe microwave with a locking mechanism, cool-touch exterior, and pre-programmed child-friendly recipes.",
        "A voice-controlled microwave with smart assistant integration, gesture control, and app-based recipe guidance.",
        "A combination microwave with convection, grill, and air frying functions for versatile cooking.",
        "A microwave with steam cooking technology, ensuring moisture retention and nutrient preservation for healthier meals."
    ],
    "coffee-makers": [
        "A premium espresso machine with barista-style brewing, automatic milk frothing, and customizable coffee strength settings.",
        "A drip coffee maker with programmable brewing options, an insulated carafe, and a reusable filter for eco-friendly coffee preparation.",
        "A French press coffee maker with a durable borosilicate glass body, stainless steel filter, and an ergonomic handle for perfect brewing.",
        "A cold brew coffee maker with a compact design, easy-to-use filtration system, and airtight storage for fresh-tasting coffee.",
        "A smart single-serve coffee maker with pod compatibility, temperature control, and one-touch brewing for quick and convenient coffee preparation.",
        "A bean-to-cup coffee maker with an integrated grinder, adjustable settings, and automatic brewing for a personalized coffee experience.",
        "A stovetop espresso maker with an aluminum body, pressure valve, and classic Italian design for rich espresso.",
        "A capsule coffee maker with one-touch brewing, compact design, and a wide variety of flavor options.",
        "A dual-brew coffee machine supporting both ground coffee and pods, with multiple brew strength settings.",
        "A travel-friendly coffee maker with USB charging, built-in battery, and a compact design for on-the-go brewing."
    ],
    "dishwashers": [
        "A high-efficiency dishwasher with multiple wash cycles, steam cleaning technology, and ultra-quiet operation for a seamless kitchen experience.",
        "A smart dishwasher with Wi-Fi connectivity, voice assistant support, and AI-powered load sensing for optimized cleaning.",
        "A compact countertop dishwasher designed for small kitchens, featuring quick wash cycles and low water consumption.",
        "A freestanding dishwasher with an adjustable rack system, powerful spray arms, and energy-efficient drying technology.",
        "A built-in dishwasher with a stainless steel tub, auto-dosing detergent system, and a high-temperature sanitization mode.",
        "A double-drawer dishwasher with independent wash zones, customizable settings, and a sleek modern design.",
        "A rapid-wash dishwasher with turbo drying, low-noise operation, and an eco-friendly mode for reduced water usage.",
        "A sensor-equipped dishwasher with auto-soil detection, smart water distribution, and an anti-bacterial rinse cycle.",
        "A hybrid dishwasher with both wash and drying functions, offering UV sterilization for enhanced hygiene.",
        "A solar-powered dishwasher with energy-efficient water recycling and self-cleaning filters for sustainable performance."
    ],
    "water-purifiers": [
        "A smart RO water purifier with multi-stage filtration, UV sterilization, and real-time water quality monitoring.",
        "A high-capacity water purifier with advanced mineral retention technology and an energy-saving auto shut-off feature.",
        "A tankless water purifier with instant purification, compact design, and AI-powered filter life tracking.",
        "A UV + UF water purifier with zero water wastage, enhanced bacterial removal, and a sleek wall-mountable design.",
        "A gravity-based water purifier with no electricity requirement, long-lasting filters, and eco-friendly operation.",
        "A high-flow industrial water purifier with large-scale purification, smart filter indicators, and robust build quality.",
        "A portable water purifier with a rechargeable battery, lightweight design, and advanced nano-filtration technology.",
        "A hot and cold water purifier with temperature control, smart touch operation, and child safety lock features.",
        "A faucet-mounted water purifier with easy installation, multi-stage purification, and efficient chlorine removal.",
        "A solar-powered water purifier with built-in storage, sustainable UV filtration, and automatic self-cleaning capabilities."
    ],
    "air-purifiers": [
        "A high-performance split air conditioner with inverter technology, rapid cooling, and anti-bacterial filters for pure air.",
        "A smart air conditioner with voice control compatibility, energy-efficient operation, and customizable cooling modes.",
        "A portable air conditioner designed for easy movement, offering multiple fan speeds, dehumidification mode, and auto temperature sensing.",
        "A window air conditioner with a powerful cooling system, eco-friendly refrigerant, and easy installation for efficient home cooling.",
        "An advanced air conditioner with humidity control, silent operation, and UV purification for a cleaner and healthier indoor environment.",
        "A dual-inverter AC with ultra-fast cooling, power-saving mode, and an auto-clean function for low maintenance.",
        "An AI-powered air conditioner with adaptive cooling, real-time energy tracking, and smart temperature regulation.",
        "A multi-split AC with multiple indoor units, zone-wise temperature control, and a compact outdoor unit for efficient cooling.",
        "A hybrid AC with both cooling and heating capabilities, ensuring comfort in all seasons.",
        "A solar-powered air conditioner with energy-efficient cooling and integrated battery storage for sustainable performance."
    ],
    "induction-cooktops": [
        "A high-power induction cooktop with touch controls, auto pan detection, and precise temperature adjustment for seamless cooking.",
        "A portable induction cooktop with a slim design, fast heating technology, and multiple preset cooking modes.",
        "A dual-zone induction cooktop with independent heat controls, child lock safety, and an easy-to-clean glass surface.",
        "A smart induction cooktop with voice command integration, app-based control, and real-time temperature monitoring.",
        "A commercial-grade induction cooktop with heavy-duty build, powerful heating, and a rapid cooling mechanism.",
        "An energy-efficient induction cooktop with low power consumption, turbo boost heating, and a digital timer for precision cooking.",
        "A hybrid induction and gas cooktop with multi-fuel compatibility, auto-ignition, and seamless flame-to-electric transition.",
        "An ultra-slim induction cooktop with sensor-based safety shut-off, silent operation, and scratch-resistant surface.",
        "A built-in induction cooktop with seamless integration, flexible power levels, and an elegant frameless design.",
        "A solar-powered induction cooktop with a rechargeable battery, portable design, and high-efficiency heating for outdoor use."
    ]
}

features = {
    "refrigerators": {
        "Capacity": ["250L", "350L", "500L", "600L (French Door)", "800L (Side-by-Side)"],
        "Cooling Technology": ["Inverter Compressor", "Multi Air Flow", "Twin Cooling System", "No Frost", "AI Temperature Control"],
        "Energy Efficiency": ["5-star rating", "Eco Mode", "AI-powered energy optimization"],
        "Special Features": ["Convertible Freezer", "Smart Diagnosis", "Door-in-Door", "Water & Ice Dispenser", "Touch Display"],
        "Shelves & Storage": ["Tempered Glass Shelves", "Adjustable Racks", "Dedicated Fruit & Vegetable Box", "Bottle Storage"],
        "Defrosting": ["Frost-Free", "Manual Defrost", "Auto Defrost"],
        "Smart Features": ["WiFi & App Control", "Voice Assistant Support", "Temperature Alerts"],
        "Build Quality": ["Stainless Steel Finish", "Fingerprint-resistant coating", "LED interior lighting"],
    },
    "washing-machines": {
        "Type": ["Front Load", "Top Load", "Semi-Automatic", "Fully Automatic"],
        "Drum Capacity": ["6kg", "7.5kg", "9kg", "12kg"],
        "Washing Modes": ["Quick Wash", "Heavy Load", "Delicate", "Eco Mode", "Steam Wash"],
        "Spin Speed": ["1000 RPM", "1200 RPM", "1400 RPM"],
        "Energy Efficiency": ["5-star rating", "Inverter Motor", "AI Load Detection"],
        "Water Usage": ["Low Water Consumption", "Smart Water Control", "Auto Water Level Adjustment"],
        "Smart Features": ["App Connectivity", "Voice Commands", "Remote Monitoring", "Cycle Customization"],
        "Build Quality": ["Rust-proof Drum", "Shockproof Body", "Vibration Control"],
    },
    "microwaves": {
        "Type": ["Solo", "Grill", "Convection", "Inverter"],
        "Capacity": ["20L", "25L", "32L", "45L"],
        "Cooking Modes": ["Defrost", "Grill", "Convection Bake", "Auto Cook", "Air Fry"],
        "Power Levels": ["700W", "900W", "1200W"],
        "Smart Features": ["Voice Control", "WiFi App Control", "Pre-set Recipes"],
        "Safety Features": ["Child Lock", "Auto Shut-off", "Cool-Touch Exterior"],
        "Display & Controls": ["Touch Panel", "Rotary Knob", "LED Display"],
        "Build Quality": ["Stainless Steel Interior", "Scratch-resistant Coating", "Easy-to-clean Design"],
    },
    "vacuum-cleaners": {
        "Type": ["Cordless", "Robot", "Bagless", "Handheld"],
        "Suction Power": ["120AW", "150AW", "250AW"],
        "Battery Life": ["45 min", "60 min", "120 min"],
        "Filtration System": ["HEPA Filter", "Cyclone Filtration", "Multi-layer Dust Filtration"],
        "Smart Features": ["App Connectivity", "Voice Control", "Auto Dirt Disposal"],
        "Attachments": ["Pet Hair Brush", "Crevice Tool", "Multi-Surface Brush"],
        "Noise Level": ["Low-noise Motor", "Silent Mode"],
        "Build Quality": ["Lightweight Carbon Fiber Body", "Rubberized Wheels"],
    },
    "air-purifiers": {
        "Coverage Area": ["300 sq.ft", "500 sq.ft", "800 sq.ft"],
        "Filtration Technology": ["HEPA Filter", "Activated Carbon Filter", "UV Sterilization", "Ionizer"],
        "CADR Rating": ["250 m³/h", "400 m³/h", "600 m³/h"],
        "Smart Features": ["Air Quality Monitoring", "Auto Mode", "Smart App Control"],
        "Noise Level": ["Whisper-Quiet Operation", "Sleep Mode"],
        "Energy Efficiency": ["Low Power Consumption", "Eco Mode"],
        "Build Quality": ["Compact Design", "Anti-Microbial Coating"],
    },
    "dishwashers": {
        "Type": ["Freestanding", "Built-in", "Compact Countertop", "Double Drawer"],
        "Wash Programs": ["Normal", "Intensive", "Eco", "Glassware", "Quick Wash"],
        "Capacity": ["8 Place Settings", "12 Place Settings", "16 Place Settings"],
        "Energy Efficiency": ["5-Star Rating", "Low Water Consumption", "Auto Detergent Dispenser"],
        "Smart Features": ["WiFi Connectivity", "Voice Control", "Auto Door Opening"],
        "Noise Level": ["Ultra Quiet (42dB)", "Silent Mode"],
        "Build Quality": ["Stainless Steel Tub", "Fingerprint Resistant Finish"],
    },
    "water-purifiers": {
        "Filtration System": ["RO", "UV", "UF", "Carbon Filter", "Nano Filtration"],
        "Storage Capacity": ["5L", "7L", "10L"],
        "Purification Stages": ["3-Stage", "5-Stage", "7-Stage"],
        "Special Features": ["TDS Control", "Mineral Booster", "Auto Filter Change Indicator"],
        "Smart Features": ["App Connectivity", "Leakage Detection", "Water Quality Monitoring"],
        "Energy Efficiency": ["Low Power Consumption", "Auto Shut-off"],
        "Build Quality": ["Food-grade Plastic Tank", "Stainless Steel Finish"],
    },
    "air-purifiers": {
        "Type": ["Split AC", "Window AC", "Portable AC", "Multi-Split AC"],
        "Cooling Capacity": ["1 Ton", "1.5 Ton", "2 Ton"],
        "Inverter Technology": ["Dual Inverter", "Triple Inverter", "AI Smart Inverter"],
        "Cooling Features": ["Turbo Mode", "Humidity Control", "4-Way Swing"],
        "Energy Efficiency": ["5-Star Rating", "Eco Mode", "AI Power Optimization"],
        "Smart Features": ["WiFi Connectivity", "Voice Control", "Self-Diagnosis"],
        "Noise Level": ["Ultra Quiet (25dB)", "Silent Mode"],
        "Build Quality": ["Anti-Corrosion Coating", "Copper Condenser"],
    },
    "induction-cooktops": {
        "Power Levels": ["1200W", "1800W", "2500W"],
        "Cooking Modes": ["Boil", "Fry", "Slow Cook", "Grill", "Simmer"],
        "Safety Features": ["Auto Shut-off", "Overheat Protection", "Child Lock"],
        "Control Type": ["Touch Panel", "Knob Controls"],
        "Smart Features": ["App Control", "Voice Commands", "Pre-set Cooking Recipes"],
        "Build Quality": ["Ceramic Glass Surface", "Scratch-Resistant Coating"],
        "Energy Efficiency": ["Fast Heating", "Low Power Consumption"],
    },
    "coffee-makers": {
        "Type": ["Drip Coffee Maker", "Espresso Machine", "French Press", "Single-Serve Pod Machine", "Cold Brew Maker"],
        "Brewing Capacity": ["Single Cup", "4 Cups", "8 Cups", "12 Cups"],
        "Brewing Technology": ["Pressure Brewing", "Steam Extraction", "Drip Brewing", "Cold Brew Immersion"],
        "Grinder Type": ["Built-in Burr Grinder", "Blade Grinder", "Pre-Ground Coffee Compatible"],
        "Milk Frothing": ["Steam Wand", "Automatic Milk Frother", "Manual Frothing"],
        "Smart Features": ["WiFi & App Control", "Programmable Timer", "Auto Brew Scheduling"],
        "Brew Strength Control": ["Light", "Medium", "Strong", "Customizable"],
        "Temperature Control": ["Precision Temperature Adjustment", "PID Control", "Thermoblock Heating"],
        "Filter Type": ["Reusable Mesh Filter", "Paper Filter Compatible", "Charcoal Water Filter"],
        "Energy Efficiency": ["Auto Shut-off", "Low Power Consumption", "Eco Mode"],
        "Build Quality": ["Stainless Steel Body", "Heat-Resistant Glass Carafe", "Anti-Drip System"]
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
