import json
import random
import uuid
from fakeData.electronics.faker_electronics import Faker

fake = Faker()
Faker.seed(42)

categories = {
    "computers": [
        "desktop", "monitors", "keyboards-mice", "storage", "printers-scanners",
        "graphics-cards", "ram-storage", "cooling-pads", "networking", "usb-hubs"
    ]
}

product_data = {
    "desktop": [
        # Apple
        ("iMac 24-inch", "Apple", "IMAC-####"),
        ("Mac Studio", "Apple", "MACS-####"),
        ("Mac Pro", "Apple", "MACP-####"),
        ("iMac Pro", "Apple", "IMACP-####"),
        ("Mac Mini M2", "Apple", "MACM-####"),
        
        # Dell
        ("Inspiron 3880", "Dell", "INS-####"),
        ("Inspiron 5400 AIO", "Dell", "INS-####"),
        ("XPS Desktop", "Dell", "XPS-####"),
        ("XPS 8950", "Dell", "XPS-####"),
        ("Alienware Aurora R15", "Dell", "AW-####"),
        ("OptiPlex 7090", "Dell", "OPT-####"),
        ("Vostro 3888", "Dell", "VOS-####"),
        ("Vostro 5890", "Dell", "VOS-####"),
        ("Precision 3650", "Dell", "PRC-####"),
        
        # Lenovo
        ("ThinkCentre M90a", "Lenovo", "TCM-####"),
        ("ThinkCentre M75s", "Lenovo", "TCM-####"),
        ("ThinkStation P620", "Lenovo", "TSP-####"),
        ("ThinkCentre Neo 50s", "Lenovo", "TCN-####"),
        ("Legion Tower 5", "Lenovo", "LEG-####"),
        ("ThinkSmart Hub", "Lenovo", "TSH-####"),
        ("Legion T7", "Lenovo", "LEG-####"),
        ("IdeaCentre AIO 3", "Lenovo", "ICA-####"),
        ("IdeaCentre Gaming 5", "Lenovo", "ICG-####"),
        
        # Asus
        ("ROG Strix GA15", "Asus", "ROG-####"),
        ("ROG Strix GT15", "Asus", "ROG-####"),
        ("ROG Strix G35", "Asus", "ROG-####"),
        ("ExpertCenter D7", "Asus", "EXD-####"),
        ("ExpertCenter E5 AiO", "Asus", "EXE-####"),
        ("ProArt Station PD5", "Asus", "PRO-####"),
        ("ASUS Mini PC PB62", "Asus", "MINI-####"),
        ("ASUS ExpertCenter D9", "Asus", "EXD-####"),
        
        # HP
        ("Pavilion TP01", "HP", "PAV-####"),
        ("Pavilion Gaming TG01", "HP", "PAV-####"),
        ("Envy TE02", "HP", "ENV-####"),
        ("OMEN 45L", "HP", "OMEN-####"),
        ("OMEN 30L", "HP", "OMEN-####"),
        ("EliteDesk 800 G6", "HP", "ELD-####"),
        ("ProDesk 400 G7", "HP", "PRD-####"),
        ("HP Z2 G9 Tower", "HP", "HPZ-####"),
        ("HP Z4 G5", "HP", "HPZ-####"),
        ("Elite Slice G2", "HP", "ESG-####"),
        
        # Acer
        ("Aspire C24", "Acer", "ASC-####"),
        ("Aspire TC-1760", "Acer", "AST-####"),
        ("Predator Orion 3000", "Acer", "PRED-####"),
        ("Predator Orion 7000", "Acer", "PRED-####"),
        ("Veriton X", "Acer", "VTX-####"),
        ("SwiftEdge 16", "Acer", "SE-####"),
        ("Chromebox CXI4", "Acer", "CBX-####"),
        ("Acer ConceptD 100", "Acer", "CD-####"),
        ("Acer ConceptD 500", "Acer", "CD-####")
    ],
    "monitors": [
        # Dell
        ("UltraSharp U2723QE", "Dell", "U27-####"),
        ("UltraSharp U3223QE", "Dell", "U32-####"),
        ("UltraSharp U3224KB", "Dell", "U32-####"),
        ("P2723D", "Dell", "P27-####"),
        ("P3222QE", "Dell", "P32-####"),
        ("Alienware AW3423DW", "Dell", "AW34-####"),
        ("S3222DGM", "Dell", "S32-####"),
        ("G3223Q", "Dell", "G32-####"),
        ("U4021QW", "Dell", "U40-####"),
        ("C2723H", "Dell", "C27-####"),
        
        # Samsung
        ("Odyssey G7", "Samsung", "ODG7-####"),
        ("Odyssey G8 OLED", "Samsung", "ODG8-####"),
        ("Odyssey Ark", "Samsung", "ODARK-####"),
        ("Smart Monitor M8", "Samsung", "SMM8-####"),
        ("Odyssey Neo G9", "Samsung", "ODNG9-####"),
        ("Odyssey G5", "Samsung", "ODG5-####"),
        ("Smart Monitor M7", "Samsung", "SMM7-####"),
        ("ViewFinity S8", "Samsung", "VFS8-####"),
        ("Odyssey G3", "Samsung", "ODG3-####"),
        ("CJ791", "Samsung", "CJ79-####"),
        
        # Apple
        ("Pro Display XDR", "Apple", "XDR-####"),
        ("Studio Display", "Apple", "STD-####"),
        ("Thunderbolt Display", "Apple", "TBD-####"),
        ("iMac 5K Retina Display", "Apple", "IM5K-####"),
        ("Apple Cinema Display", "Apple", "ACD-####"),
        
        # Asus
        ("ROG Swift PG259QN", "Asus", "ROG-####"),
        ("ROG Swift PG32UQ", "Asus", "ROG-####"),
        ("ProArt Display PA32UCX", "Asus", "PA32-####"),
        ("TUF Gaming VG27AQ", "Asus", "TUF-####"),
        ("ROG Strix XG438Q", "Asus", "ROG-####"),
        ("ZenScreen MB16AC", "Asus", "ZEN-####"),
        ("ROG Swift OLED PG42UQ", "Asus", "ROGO-####"),
        ("ROG Swift PG259QNR", "Asus", "ROG-####"),
        ("VA24EHE", "Asus", "VA24-####"),
        ("TUF Gaming VG32VQ1B", "Asus", "TUF-####"),
        
        # Lenovo
        ("ThinkVision P27h", "Lenovo", "TVP-####"),
        ("ThinkVision T24i", "Lenovo", "TVT-####"),
        ("ThinkVision M14", "Lenovo", "TVM-####"),
        ("Legion Y44w", "Lenovo", "LY44-####"),
        ("ThinkVision X1", "Lenovo", "TVX-####"),
        ("ThinkVision S24q", "Lenovo", "TVS-####"),
        ("ThinkVision P34w", "Lenovo", "TVP-####"),
        ("Lenovo G34w", "Lenovo", "LG34-####"),
        
        # LG
        ("UltraFine 5K", "LG", "UF5K-####"),
        ("UltraGear 34GN850", "LG", "UG34-####"),
        ("UltraFine 4K", "LG", "UF4K-####"),
        ("34WN80C-B", "LG", "LG34-####"),
        ("27GP850-B", "LG", "LG27-####"),
        ("UltraGear 27GN950", "LG", "UG27-####"),
        ("OLED Flex LX3", "LG", "OLX3-####"),
        
        # Acer
        ("Predator X38", "Acer", "PX38-####"),
        ("Nitro XV272U", "Acer", "NXV27-####"),
        ("ConceptD CP7", "Acer", "CDCP-####"),
        ("Acer SB220Q", "Acer", "SB22-####"),
        ("Predator CG437K", "Acer", "PCG43-####")
    ],
    "keyboards-mice": [
        # Logitech
        ("MX Keys", "Logitech", "MXK-####"),
        ("MX Keys Mini", "Logitech", "MXKM-####"),
        ("G915 TKL", "Logitech", "G915-####"),
        ("G213 Prodigy", "Logitech", "G213-####"),
        ("K380 Multi-Device", "Logitech", "K380-####"),
        ("K845 Mechanical", "Logitech", "K845-####"),
        ("G502 HERO", "Logitech", "G502-####"),
        ("G Pro X Superlight", "Logitech", "GPSL-####"),
        ("MX Master 3S", "Logitech", "MXM3-####"),
        ("Pebble M350", "Logitech", "PBM3-####"),

        # Apple
        ("Magic Keyboard", "Apple", "MAGK-####"),
        ("Magic Keyboard with Touch ID", "Apple", "MAGT-####"),
        ("Magic Keyboard with Numeric Keypad", "Apple", "MAGN-####"),
        ("Magic Mouse 2", "Apple", "MAGM-####"),
        ("Magic Trackpad", "Apple", "MAGT-####"),

        # Corsair
        ("K70 RGB PRO", "Corsair", "K70-####"),
        ("K100 RGB", "Corsair", "K100-####"),
        ("K95 RGB Platinum", "Corsair", "K95-####"),
        ("K60 RGB Pro", "Corsair", "K60-####"),
        ("Harpoon RGB Wireless", "Corsair", "HRW-####"),
        ("M65 RGB Elite", "Corsair", "M65-####"),
        ("Dark Core RGB Pro", "Corsair", "DCRP-####"),

        # Razer
        ("Razer DeathAdder V3", "Razer", "DA3-####"),
        ("Razer BlackWidow V4 Pro", "Razer", "BWV4-####"),
        ("Razer Huntsman Mini", "Razer", "HMIN-####"),
        ("Razer Cynosa V2", "Razer", "CYNO-####"),
        ("Razer Viper Ultimate", "Razer", "VIPU-####"),
        ("Razer Naga X", "Razer", "NAGX-####"),
        ("Razer Orochi V2", "Razer", "OROV-####"),
        ("Razer Basilisk V3", "Razer", "BAS3-####"),

        # SteelSeries
        ("Apex Pro", "SteelSeries", "APEX-####"),
        ("Apex 7", "SteelSeries", "APX7-####"),
        ("Rival 600", "SteelSeries", "R600-####"),
        ("Aerox 3 Wireless", "SteelSeries", "A3W-####"),
        ("Prime Wireless", "SteelSeries", "PRMW-####"),

        # Keychron
        ("Keychron K2", "Keychron", "K2-####"),
        ("Keychron K6", "Keychron", "K6-####"),
        ("Keychron K10", "Keychron", "K10-####"),
        ("Keychron Q1", "Keychron", "Q1-####"),

        # HyperX
        ("HyperX Alloy Origins", "HyperX", "HXAO-####"),
        ("HyperX Alloy FPS Pro", "HyperX", "HXFP-####"),
        ("HyperX Pulsefire Haste", "HyperX", "HXP-####"),
        
        # ASUS ROG
        ("ROG Strix Scope RX", "ASUS", "RSSR-####"),
        ("ROG Falchion Wireless", "ASUS", "RFW-####"),
        ("ROG Gladius III Wireless", "ASUS", "RGW-####"),
        
        # Cooler Master
        ("CK552 Gaming Keyboard", "Cooler Master", "CK552-####"),
        ("MM720 Lightweight Mouse", "Cooler Master", "MM720-####")
    ],
    "storage": [
        # Samsung
        ("Samsung 980 Pro 1TB", "Samsung", "SSD-####"),
        ("Samsung 990 Pro 2TB", "Samsung", "SSD-####"),
        ("Samsung T7 Shield 1TB", "Samsung", "T7S-####"),
        ("Samsung 870 EVO 2TB", "Samsung", "870E-####"),
        ("Samsung X5 Thunderbolt 2TB", "Samsung", "X5T-####"),

        # Western Digital
        ("WD Black SN850 2TB", "Western Digital", "WDB-####"),
        ("WD Black SN770 1TB", "Western Digital", "WDB-####"),
        ("WD Blue 3D NAND 1TB", "Western Digital", "WDB-####"),
        ("WD Red Plus 4TB", "Western Digital", "WDR-####"),
        ("WD Elements 5TB", "Western Digital", "WDE-####"),

        # Crucial
        ("Crucial P5 Plus 1TB", "Crucial", "CRP-####"),
        ("Crucial P3 2TB", "Crucial", "CRP-####"),
        ("Crucial X8 1TB", "Crucial", "CRX-####"),
        ("Crucial MX500 2TB", "Crucial", "CRM-####"),
        ("Crucial BX500 1TB", "Crucial", "CRB-####"),

        # Seagate
        ("Seagate BarraCuda 4TB", "Seagate", "ST-####"),
        ("Seagate FireCuda 530 2TB", "Seagate", "STF-####"),
        ("Seagate IronWolf Pro 8TB", "Seagate", "STI-####"),
        ("Seagate Expansion 6TB", "Seagate", "STE-####"),
        ("Seagate One Touch 5TB", "Seagate", "STO-####"),

        # SanDisk
        ("SanDisk Extreme 1TB", "SanDisk", "SDX-####"),
        ("SanDisk Ultra 3D SSD 2TB", "SanDisk", "SDU-####"),
        ("SanDisk Professional G-Drive 4TB", "SanDisk", "SDG-####"),
        ("SanDisk Extreme Portable SSD 2TB", "SanDisk", "SDE-####"),
        ("SanDisk iXpand Flash Drive 256GB", "SanDisk", "SDI-####"),

        # Kingston
        ("Kingston KC3000 2TB", "Kingston", "KNG-####"),
        ("Kingston A2000 1TB", "Kingston", "KNG-####"),
        ("Kingston DataTraveler Max 1TB", "Kingston", "KNG-####"),
        ("Kingston XS2000 Portable SSD 2TB", "Kingston", "KNG-####"),
        ("Kingston FURY Renegade 4TB", "Kingston", "KNG-####"),

        # Adata
        ("Adata XPG Gammix S70 2TB", "Adata", "ADX-####"),
        ("Adata SU800 1TB", "Adata", "ADS-####"),
        ("Adata HD710 Pro 5TB", "Adata", "ADH-####"),
        ("Adata SE800 1TB", "Adata", "ADS-####"),
        ("Adata SC680 480GB", "Adata", "ADS-####"),

        # Toshiba
        ("Toshiba X300 6TB", "Toshiba", "TX3-####"),
        ("Toshiba Canvio Advance 2TB", "Toshiba", "TCA-####"),
        ("Toshiba N300 NAS 8TB", "Toshiba", "TN3-####"),
        ("Toshiba P300 3TB", "Toshiba", "TP3-####"),
        ("Toshiba Canvio Flex 4TB", "Toshiba", "TCF-####"),

        # LaCie
        ("LaCie Rugged Mini 2TB", "LaCie", "LCM-####"),
        ("LaCie d2 Professional 4TB", "LaCie", "LCD-####"),
        ("LaCie Mobile Drive 5TB", "LaCie", "LCM-####"),
        ("LaCie 2big Dock 8TB", "LaCie", "LC2-####"),
        ("LaCie Rugged SSD Pro 2TB", "LaCie", "LCR-####")
    ],
    "printers-scanners": [
        # HP
        ("HP LaserJet Pro MFP", "HP", "LJM-####"),
        ("HP DeskJet 3755", "HP", "DJ3-####"),
        ("HP OfficeJet Pro 9025e", "HP", "OJP-####"),
        ("HP Smart Tank 7602", "HP", "HST-####"),
        ("HP ENVY 6055e", "HP", "ENV-####"),

        # Epson
        ("Epson EcoTank ET-3850", "Epson", "ETE-####"),
        ("Epson WorkForce WF-4830", "Epson", "EWF-####"),
        ("Epson SureColor P600", "Epson", "ESC-####"),
        ("Epson Expression Home XP-5100", "Epson", "EXP-####"),
        ("Epson Perfection V600", "Epson", "EPV-####"),

        # Canon
        ("Canon PIXMA TR8520", "Canon", "CPT-####"),
        ("Canon imageCLASS MF743Cdw", "Canon", "CIM-####"),
        ("Canon MAXIFY GX7020", "Canon", "CMG-####"),
        ("Canon PIXMA G6020", "Canon", "CPG-####"),
        ("Canon CanoScan LiDE 400", "Canon", "CCL-####"),

        # Brother
        ("Brother HL-L2350DW", "Brother", "BHL-####"),
        ("Brother MFC-J4535DW", "Brother", "BMF-####"),
        ("Brother DCP-L2550DW", "Brother", "BDL-####"),
        ("Brother ADS-1700W", "Brother", "BAD-####"),
        ("Brother P-touch PTD600", "Brother", "BPT-####"),

        # Xerox
        ("Xerox WorkCentre 6515", "Xerox", "XWC-####"),
        ("Xerox VersaLink C405", "Xerox", "XVL-####"),
        ("Xerox B205 Monochrome", "Xerox", "XB2-####"),
        ("Xerox Phaser 6510", "Xerox", "XPH-####"),
        ("Xerox DocuMate 3125", "Xerox", "XDM-####"),

        # Lexmark
        ("Lexmark MB3442adw", "Lexmark", "LMB-####"),
        ("Lexmark CX431adw", "Lexmark", "LCX-####"),
        ("Lexmark B3442dw", "Lexmark", "LB3-####"),
        ("Lexmark MS431dn", "Lexmark", "LMS-####"),
        ("Lexmark MC3224i", "Lexmark", "LMC-####"),

        # Fujitsu
        ("Fujitsu ScanSnap iX1600", "Fujitsu", "FSI-####"),
        ("Fujitsu fi-8170", "Fujitsu", "FF8-####"),
        ("Fujitsu SP-1120N", "Fujitsu", "FSP-####"),
        ("Fujitsu ScanSnap S1300i", "Fujitsu", "FSS-####"),
        ("Fujitsu fi-7160", "Fujitsu", "FF7-####"),

        # Ricoh
        ("Ricoh SP 3710DN", "Ricoh", "RSP-####"),
        ("Ricoh IM C3000", "Ricoh", "RIC-####"),
        ("Ricoh P C600", "Ricoh", "RPC-####"),
        ("Ricoh Pro C7210X", "Ricoh", "RPR-####"),
        ("Ricoh Aficio MP 305SPF", "Ricoh", "RAM-####"),

        # Kodak
        ("Kodak i3300 Scanner", "Kodak", "KIS-####"),
        ("Kodak Alaris S2050", "Kodak", "KAS-####"),
        ("Kodak ScanMate i1150", "Kodak", "KSM-####"),
        ("Kodak i2900 Scanner", "Kodak", "KIS-####"),
        ("Kodak Mobile Scanner", "Kodak", "KMS-####"),

        # Panasonic
        ("Panasonic KV-S5076H", "Panasonic", "PKV-####"),
        ("Panasonic KV-S1057C", "Panasonic", "PKV-####"),
        ("Panasonic KV-S2087", "Panasonic", "PKV-####"),
        ("Panasonic KX-MB1520", "Panasonic", "PKX-####"),
        ("Panasonic KV-S1027C", "Panasonic", "PKS-####")
    ],
    "graphics-cards": [
        # Nvidia
        ("GeForce RTX 4090", "Nvidia", "RTX-####"),
        ("GeForce RTX 4080", "Nvidia", "RTX-####"),
        ("GeForce RTX 4070 Ti", "Nvidia", "RTX-####"),
        ("GeForce RTX 4060", "Nvidia", "RTX-####"),
        ("GeForce RTX 3090 Ti", "Nvidia", "RTX-####"),
        ("GeForce RTX 3080", "Nvidia", "RTX-####"),
        ("GeForce RTX 3070 Ti", "Nvidia", "RTX-####"),
        ("GeForce RTX 3060", "Nvidia", "RTX-####"),
        ("GeForce RTX 2080 Ti", "Nvidia", "RTX-####"),
        ("GeForce GTX 1660 Super", "Nvidia", "GTX-####"),

        # AMD Radeon
        ("Radeon RX 7900 XTX", "AMD", "RX7-####"),
        ("Radeon RX 7900 XT", "AMD", "RX7-####"),
        ("Radeon RX 7800 XT", "AMD", "RX7-####"),
        ("Radeon RX 7700 XT", "AMD", "RX7-####"),
        ("Radeon RX 7600", "AMD", "RX7-####"),
        ("Radeon RX 6950 XT", "AMD", "RX6-####"),
        ("Radeon RX 6900 XT", "AMD", "RX6-####"),
        ("Radeon RX 6800 XT", "AMD", "RX6-####"),
        ("Radeon RX 6750 XT", "AMD", "RX6-####"),
        ("Radeon RX 6600 XT", "AMD", "RX6-####"),

        # Intel Arc
        ("Intel Arc A770", "Intel", "ARC-####"),
        ("Intel Arc A750", "Intel", "ARC-####"),
        ("Intel Arc A580", "Intel", "ARC-####"),
        ("Intel Arc A380", "Intel", "ARC-####"),
        ("Intel Arc A310", "Intel", "ARC-####"),

        # Nvidia Professional GPUs
        ("Nvidia RTX 6000 Ada", "Nvidia", "RTXP-####"),
        ("Nvidia A100", "Nvidia", "A100-####"),
        ("Nvidia H100", "Nvidia", "H100-####"),
        ("Nvidia RTX A6000", "Nvidia", "RTXA-####"),
        ("Nvidia Quadro RTX 5000", "Nvidia", "QRTX-####"),

        # AMD Workstation GPUs
        ("AMD Radeon Pro W7900", "AMD", "RPW7-####"),
        ("AMD Radeon Pro W7800", "AMD", "RPW7-####"),
        ("AMD Radeon Pro W6800", "AMD", "RPW6-####"),
        ("AMD Radeon Pro WX 9100", "AMD", "RPWX-####"),
        ("AMD Radeon Pro W6600", "AMD", "RPW6-####"),

        # Entry-Level GPUs
        ("Nvidia GTX 1650", "Nvidia", "GTX-####"),
        ("Nvidia GTX 1050 Ti", "Nvidia", "GTX-####"),
        ("AMD Radeon RX 5500 XT", "AMD", "RX5-####"),
        ("AMD Radeon RX 5600 XT", "AMD", "RX5-####"),
        ("Intel UHD Graphics 770", "Intel", "IUG-####"),

        # Special Edition GPUs
        ("GeForce RTX 3090 Founders Edition", "Nvidia", "RTXF-####"),
        ("Radeon RX 6900 XT Midnight Black", "AMD", "RX6M-####"),
        ("Intel Arc A770 Limited Edition", "Intel", "ARCL-####"),
        ("Nvidia Titan RTX", "Nvidia", "TITAN-####"),
        ("AMD Radeon VII", "AMD", "R7-####")
    ],
    "ram-storage": [
        # Corsair
        ("Corsair Vengeance 32GB DDR5", "Corsair", "CVG-####"),
        ("Corsair Vengeance 16GB DDR4", "Corsair", "CVG-####"),
        ("Corsair Dominator Platinum 64GB DDR5", "Corsair", "CDP-####"),
        ("Corsair Vengeance LPX 8GB DDR4", "Corsair", "CVL-####"),
        ("Corsair Vengeance RGB Pro 32GB", "Corsair", "CVR-####"),

        # G.SKILL
        ("G.SKILL Trident Z5 16GB", "G.SKILL", "TZZ-####"),
        ("G.SKILL Ripjaws V 32GB", "G.SKILL", "GRV-####"),
        ("G.SKILL Royal Elite 64GB DDR4", "G.SKILL", "GRE-####"),
        ("G.SKILL Trident Z RGB 16GB", "G.SKILL", "TZR-####"),
        ("G.SKILL Sniper X 8GB DDR4", "G.SKILL", "GSX-####"),

        # Kingston
        ("Kingston Fury Beast 32GB", "Kingston", "KFB-####"),
        ("Kingston Fury Renegade 16GB", "Kingston", "KFR-####"),
        ("Kingston HyperX Predator 64GB", "Kingston", "KHP-####"),
        ("Kingston ValueRAM 8GB DDR4", "Kingston", "KVR-####"),
        ("Kingston Fury Impact 32GB DDR4", "Kingston", "KFI-####"),

        # Crucial
        ("Crucial Ballistix 16GB", "Crucial", "CBL-####"),
        ("Crucial Ballistix Max 32GB", "Crucial", "CBM-####"),
        ("Crucial DDR5 Pro 64GB", "Crucial", "CDP-####"),
        ("Crucial DDR4 8GB", "Crucial", "CDD-####"),
        ("Crucial P5 Plus 1TB SSD", "Crucial", "CPS-####"),

        # TeamGroup
        ("TeamGroup T-Force Delta 64GB", "TeamGroup", "TFD-####"),
        ("TeamGroup Vulcan Z 32GB", "TeamGroup", "TFV-####"),
        ("TeamGroup XTREEM ARGB 16GB", "TeamGroup", "TFX-####"),
        ("TeamGroup Zeus 8GB DDR4", "TeamGroup", "TFZ-####"),
        ("TeamGroup Elite 64GB DDR5", "TeamGroup", "TFE-####"),

        # Samsung SSDs
        ("Samsung 980 Pro 1TB", "Samsung", "SSD-####"),
        ("Samsung 970 Evo Plus 2TB", "Samsung", "SSD-####"),
        ("Samsung 860 QVO 4TB", "Samsung", "SSD-####"),
        ("Samsung T7 Portable 2TB", "Samsung", "SSD-####"),
        ("Samsung 990 Pro 1TB", "Samsung", "SSD-####"),

        # Western Digital SSDs
        ("WD Black SN850X 2TB", "Western Digital", "WDB-####"),
        ("WD Blue 1TB SATA SSD", "Western Digital", "WDB-####"),
        ("WD Red 4TB NAS SSD", "Western Digital", "WDR-####"),
        ("WD My Passport 2TB External", "Western Digital", "WDP-####"),
        ("WD Green 500GB SSD", "Western Digital", "WDG-####"),

        # Seagate SSDs
        ("Seagate FireCuda 530 2TB", "Seagate", "STF-####"),
        ("Seagate BarraCuda 4TB", "Seagate", "STB-####"),
        ("Seagate IronWolf 8TB", "Seagate", "STI-####"),
        ("Seagate One Touch 5TB", "Seagate", "STO-####"),
        ("Seagate Expansion 2TB", "Seagate", "STE-####"),

        # SanDisk SSDs
        ("SanDisk Extreme 1TB", "SanDisk", "SDX-####"),
        ("SanDisk Ultra 500GB", "SanDisk", "SDU-####"),
        ("SanDisk Professional 4TB", "SanDisk", "SDP-####"),
        ("SanDisk Extreme Pro 2TB", "SanDisk", "SDP-####"),
        ("SanDisk Portable SSD 1TB", "SanDisk", "SDP-####")
    ],
    "cooling-pads": [
        # Cooler Master
        ("Cooler Master Notepal X3", "Cooler Master", "CMX-####"),
        ("Cooler Master Notepal XL", "Cooler Master", "CMXL-####"),
        ("Cooler Master Storm SF-17", "Cooler Master", "CMSF-####"),
        ("Cooler Master NotePal U3 Plus", "Cooler Master", "CMU3-####"),
        ("Cooler Master Ergostand III", "Cooler Master", "CME3-####"),

        # Thermaltake
        ("Thermaltake Massive 20 RGB", "Thermaltake", "TTM-####"),
        ("Thermaltake Massive V20", "Thermaltake", "TTV-####"),
        ("Thermaltake Massive TM", "Thermaltake", "TTT-####"),
        ("Thermaltake Massive 14X", "Thermaltake", "TT14X-####"),
        ("Thermaltake GTEK RGB", "Thermaltake", "TTG-####"),

        # Havit
        ("Havit HV-F2056", "Havit", "HVF-####"),
        ("Havit F2073", "Havit", "HVF2-####"),
        ("Havit RGB Cooling Pad", "Havit", "HVRGB-####"),
        ("Havit HV-F2068", "Havit", "HVF2068-####"),
        ("Havit F2024", "Havit", "HVF2024-####"),

        # Kootek
        ("Kootek Laptop Cooling Pad", "Kootek", "KLP-####"),
        ("Kootek Chill Mat 5", "Kootek", "KCM5-####"),
        ("Kootek Adjustable Laptop Stand", "Kootek", "KALS-####"),
        ("Kootek Blue LED Cooling Pad", "Kootek", "KBLP-####"),
        ("Kootek Ultra-Slim Cooling Pad", "Kootek", "KUSP-####"),

        # TopMate
        ("TopMate C5", "TopMate", "TMC-####"),
        ("TopMate C7", "TopMate", "TMC7-####"),
        ("TopMate C302", "TopMate", "TMC3-####"),
        ("TopMate K5", "TopMate", "TMK5-####"),
        ("TopMate GXT 278", "TopMate", "TMGXT-####"),

        # Klim
        ("Klim Wind Laptop Cooling Pad", "Klim", "KLW-####"),
        ("Klim Cyclone", "Klim", "KLC-####"),
        ("Klim Cool+ Metal", "Klim", "KLM-####"),
        ("Klim Ultimate RGB", "Klim", "KLU-####"),
        ("Klim Swift", "Klim", "KLS-####"),

        # Targus
        ("Targus Chill Mat+ Lap Desk", "Targus", "TCM-####"),
        ("Targus Portable Cooling Pad", "Targus", "TPC-####"),
        ("Targus Dual Fan Chill Mat", "Targus", "TDC-####"),
        ("Targus X-Stand Cooling Pad", "Targus", "TXS-####"),
        ("Targus Ultra-Slim Cooling Stand", "Targus", "TUS-####"),

        # Deepcool
        ("Deepcool Multi Core X6", "Deepcool", "DMX6-####"),
        ("Deepcool N9 EX", "Deepcool", "DN9-####"),
        ("Deepcool U Pal", "Deepcool", "DUP-####"),
        ("Deepcool Wind Pal FS", "Deepcool", "DWP-####"),
        ("Deepcool M6 Audio Cooling Pad", "Deepcool", "DM6-####"),

        # Aicheson
        ("Aicheson Laptop Cooling Pad", "Aicheson", "ACP-####"),
        ("Aicheson S035", "Aicheson", "ACS-####"),
        ("Aicheson Adjustable Stand", "Aicheson", "ACA-####"),
        ("Aicheson Ultra-Slim Cooler", "Aicheson", "ACU-####"),
        ("Aicheson Large Gaming Cooling Pad", "Aicheson", "ACG-####")
    ],
    "networking": [
        # Netgear
        ("Netgear Nighthawk AX12", "Netgear", "NGA-####"),
        ("Netgear Orbi RBK852", "Netgear", "NGO-####"),
        ("Netgear Nighthawk XR1000", "Netgear", "NGX-####"),
        ("Netgear Orbi Pro SXK80", "Netgear", "NGP-####"),
        ("Netgear Nighthawk M5", "Netgear", "NGM-####"),

        # TP-Link
        ("TP-Link Archer AX90", "TP-Link", "TPL-####"),
        ("TP-Link Deco X20", "TP-Link", "TPD-####"),
        ("TP-Link Archer C80", "TP-Link", "TPC-####"),
        ("TP-Link RE650 Range Extender", "TP-Link", "TPR-####"),
        ("TP-Link TL-SG108", "TP-Link", "TPS-####"),

        # Asus
        ("ASUS ROG Rapture GT-AX11000", "Asus", "ROG-####"),
        ("ASUS ZenWiFi AX XT8", "Asus", "AZX-####"),
        ("ASUS RT-AX86U", "Asus", "ARA-####"),
        ("ASUS RT-AC5300", "Asus", "ARC-####"),
        ("ASUS USB-AC68 WiFi Adapter", "Asus", "AUA-####"),

        # Google
        ("Google Nest WiFi", "Google", "GNW-####"),
        ("Google Nest WiFi Pro", "Google", "GNP-####"),
        ("Google WiFi AC1200", "Google", "GWA-####"),
        ("Google Fiber Router", "Google", "GFR-####"),
        ("Google Nest Point", "Google", "GNP-####"),

        # Linksys
        ("Linksys Velop MX10", "Linksys", "LVM-####"),
        ("Linksys EA7500", "Linksys", "LEA-####"),
        ("Linksys RE7000", "Linksys", "LRE-####"),
        ("Linksys MR9600", "Linksys", "LMR-####"),
        ("Linksys WRT3200ACM", "Linksys", "LWR-####"),

        # D-Link
        ("D-Link DIR-X5460", "D-Link", "DLX-####"),
        ("D-Link COVR-2202", "D-Link", "DLC-####"),
        ("D-Link DGS-108", "D-Link", "DLG-####"),
        ("D-Link EXO AX AX4800", "D-Link", "DLA-####"),
        ("D-Link DAP-1650 Range Extender", "D-Link", "DLE-####"),

        # Ubiquiti
        ("Ubiquiti AmpliFi Alien", "Ubiquiti", "UAA-####"),
        ("Ubiquiti UniFi Dream Machine", "Ubiquiti", "UUD-####"),
        ("Ubiquiti EdgeRouter X", "Ubiquiti", "UEX-####"),
        ("Ubiquiti UniFi 6 Lite", "Ubiquiti", "UUL-####"),
        ("Ubiquiti AirFiber 60", "Ubiquiti", "UAF-####"),

        # Synology
        ("Synology RT6600ax", "Synology", "SRT-####"),
        ("Synology MR2200ac", "Synology", "SMR-####"),
        ("Synology RT2600ac", "Synology", "SRT2-####"),
        ("Synology Mesh Router", "Synology", "SME-####"),
        ("Synology WRX560", "Synology", "SWR-####"),

        # Cisco
        ("Cisco RV260", "Cisco", "CRV-####"),
        ("Cisco Meraki MX64", "Cisco", "CMM-####"),
        ("Cisco Aironet 2800", "Cisco", "CAA-####"),
        ("Cisco Business 110", "Cisco", "CB1-####"),
        ("Cisco Catalyst 1000", "Cisco", "CC1-####")
    ],
    "usb-hubs": [
        # Anker
        ("Anker PowerExpand 8-in-1", "Anker", "APE-####"),
        ("Anker 10-Port USB 3.0 Hub", "Anker", "A10-####"),
        ("Anker 7-in-1 USB-C Hub", "Anker", "A7U-####"),
        ("Anker PowerExpand 5-in-1", "Anker", "A5U-####"),
        ("Anker PowerExpand Elite 13-in-1", "Anker", "APE13-####"),

        # Sabrent
        ("Sabrent 4-Port USB 3.0", "Sabrent", "S4U-####"),
        ("Sabrent 10-Port USB 3.0", "Sabrent", "S10U-####"),
        ("Sabrent 7-Port USB 3.0 Hub", "Sabrent", "S7U-####"),
        ("Sabrent USB Type-C Hub", "Sabrent", "SUC-####"),
        ("Sabrent 6-Port USB Power Hub", "Sabrent", "S6P-####"),

        # Belkin
        ("Belkin USB-C 6-in-1", "Belkin", "B6U-####"),
        ("Belkin 7-Port USB 3.0 Hub", "Belkin", "B7U-####"),
        ("Belkin USB-C Multimedia Hub", "Belkin", "BUM-####"),
        ("Belkin 10-Port USB Hub", "Belkin", "B10U-####"),
        ("Belkin Thunderbolt 3 Dock", "Belkin", "BT3D-####"),

        # UGREEN
        ("UGREEN 7-in-1 USB Hub", "UGREEN", "UG7-####"),
        ("UGREEN 4-Port USB 3.0 Hub", "UGREEN", "UG4-####"),
        ("UGREEN USB-C to 5-Port Hub", "UGREEN", "UG5-####"),
        ("UGREEN Multi-Port Adapter", "UGREEN", "UGM-####"),
        ("UGREEN 9-in-1 USB Dock", "UGREEN", "UG9-####"),

        # Hyper
        ("HyperDrive 12-in-1", "Hyper", "H12-####"),
        ("HyperDrive 10-in-1 USB Hub", "Hyper", "H10-####"),
        ("HyperDrive USB-C 8-in-1", "Hyper", "H8U-####"),
        ("HyperDrive DUO 7-in-2", "Hyper", "H7D-####"),
        ("HyperDrive GEN2 6-in-1", "Hyper", "H6G-####"),

        # TP-Link
        ("TP-Link UH720 7-Port", "TP-Link", "TPL7-####"),
        ("TP-Link UH400 4-Port", "TP-Link", "TPL4-####"),
        ("TP-Link UH700 7-Port", "TP-Link", "TPL7P-####"),
        ("TP-Link USB 3.0 Hub with Ethernet", "TP-Link", "TPE-####"),
        ("TP-Link USB-C to Multi-Port", "TP-Link", "TPM-####"),

        # Aukey
        ("Aukey CB-C71 12-in-1", "Aukey", "A12-####"),
        ("Aukey 4-Port USB 3.0", "Aukey", "A4U-####"),
        ("Aukey USB-C Hub with HDMI", "Aukey", "AUH-####"),
        ("Aukey Link PD USB Hub", "Aukey", "ALP-####"),
        ("Aukey 7-in-1 USB Dock", "Aukey", "A7D-####"),

        # VAVA
        ("VAVA 8-in-1 USB Hub", "VAVA", "V8U-####"),
        ("VAVA USB-C 9-in-1 Hub", "VAVA", "V9U-####"),
        ("VAVA USB 3.0 5-Port Hub", "VAVA", "V5U-####"),
        ("VAVA 12-in-1 USB Dock", "VAVA", "V12D-####"),
        ("VAVA 4-Port USB Splitter", "VAVA", "V4S-####"),

        # Kensington
        ("Kensington SD5700T Thunderbolt 4", "Kensington", "KST-####"),
        ("Kensington UH1400P 10-Port", "Kensington", "K10U-####"),
        ("Kensington USB-C Travel Hub", "Kensington", "KTH-####"),
        ("Kensington 7-in-1 USB-C Hub", "Kensington", "K7U-####"),
        ("Kensington Universal USB 3.0 Dock", "Kensington", "KU3-####")
    ]
}

descriptions = {
    "desktop": [
        "A high-performance desktop PC designed for professionals, offering powerful processors, ample storage, and seamless multitasking capabilities.",
        "An ultra-compact desktop with a space-saving design, energy-efficient performance, and integrated security features.",
        "A gaming desktop built for high frame rates, featuring advanced cooling systems, overclockable CPUs, and cutting-edge GPUs.",
        "A business-class desktop designed for productivity, featuring enterprise-grade security, remote management, and powerful processing.",
        "A modular desktop with customizable components, allowing users to upgrade storage, RAM, and graphics for enhanced performance.",
        "An all-in-one desktop with a sleek, minimalistic design, integrating a vibrant display, powerful hardware, and premium speakers.",
        "A workstation-class desktop designed for intensive workloads such as 3D rendering, AI training, and video editing, featuring top-tier GPUs and CPUs.",
        "A silent desktop PC optimized for home or office use, designed with noise-reduction technology and energy-efficient cooling systems.",
        "A custom-built desktop designed for enthusiasts, allowing full component customization, RGB lighting, and liquid cooling options.",
        "A budget-friendly desktop featuring reliable hardware, essential computing performance, and upgradability for future needs."
    ],
    
    "monitors": [
        "A high-resolution 4K monitor with stunning color accuracy, HDR support, and an ultra-thin bezel design for immersive visuals.",
        "A gaming monitor featuring a 240Hz refresh rate, low response time, and adaptive sync technology for smooth and tear-free gameplay.",
        "A professional-grade monitor with factory-calibrated color accuracy, wide color gamut, and high brightness levels for creative professionals.",
        "An ultrawide curved monitor designed for multitasking, featuring a high refresh rate, immersive field of view, and multiple connectivity options.",
        "A portable monitor with a lightweight design, USB-C connectivity, and a built-in battery for on-the-go productivity.",
        "A budget-friendly FHD monitor offering crisp visuals, flicker-free technology, and an anti-glare screen for everyday computing needs.",
        "A touch-screen monitor with stylus support, perfect for creative professionals, designers, and touch-based interactions.",
        "A dual-monitor setup with ergonomic stands, designed for enhanced productivity and efficient workflow management.",
        "A high-brightness monitor built for outdoor and high-light environments, featuring anti-reflective coating and superior contrast ratios.",
        "A curved gaming monitor with QHD resolution, HDR support, and an ultra-fast refresh rate for an immersive gaming experience."
    ],
    
    "keyboards-mice": [
        "A mechanical keyboard with customizable RGB lighting, hot-swappable switches, and dedicated macro keys for gaming enthusiasts.",
        "A wireless ergonomic keyboard designed for comfort, featuring a split layout, cushioned palm rest, and long battery life.",
        "A compact 60% keyboard optimized for portability, featuring responsive keys, Bluetooth connectivity, and customizable shortcuts.",
        "A high-precision gaming mouse with adjustable DPI settings, ultra-lightweight design, and customizable RGB lighting.",
        "An ergonomic vertical mouse designed to reduce wrist strain, featuring silent clicks and programmable buttons for enhanced productivity.",
        "A wireless mouse with multi-device connectivity, seamless switching, and an ergonomic shape for long hours of use.",
        "A keyboard-mouse combo set designed for office productivity, offering quiet keystrokes, spill-resistant keys, and long battery life.",
        "A trackball mouse with precision scrolling, adjustable sensitivity, and a comfortable palm grip for professionals.",
        "A rechargeable Bluetooth mouse with fast-charging capabilities, silent clicking, and a high-resolution optical sensor.",
        "A minimalist keyboard with a sleek aluminum frame, low-profile keys, and cross-platform compatibility for modern workspaces."
    ],
    
    "storage": [
        "An ultra-fast NVMe SSD with high read/write speeds, designed for gaming, content creation, and fast system boot-ups.",
        "A high-capacity external HDD with durable casing, shock resistance, and USB 3.2 connectivity for reliable backup storage.",
        "A portable SSD with rugged durability, water and dust resistance, and lightning-fast transfer speeds for professionals on the go.",
        "A NAS (Network Attached Storage) system featuring multi-bay expansion, cloud integration, and RAID configurations for data redundancy.",
        "An encrypted USB flash drive with biometric security, designed for storing sensitive documents and personal data securely.",
        "A high-speed microSD card with UHS-II support, optimized for 4K video recording, drone footage, and high-speed data transfers.",
        "A gaming SSD with RGB lighting, heat dissipation technology, and PCIe Gen4 interface for maximum performance.",
        "A budget-friendly SATA SSD offering reliable performance, extended lifespan, and efficient power consumption for everyday computing.",
        "A hybrid SSHD with adaptive storage technology, combining HDD capacity with SSD-like performance for gaming and multimedia applications.",
        "A high-speed external SSD with Thunderbolt 4 connectivity, optimized for professional workflows and fast data access."
    ],
    
    "printers-scanners": [
        "A wireless all-in-one printer with seamless mobile connectivity, high-resolution printing, and automatic duplex printing.",
        "A high-speed laser printer designed for offices, offering efficient toner usage, duplex printing, and enterprise-level security features.",
        "A portable photo printer with instant ink technology, wireless printing capabilities, and borderless photo prints.",
        "A 3D printer with high-precision extrusion, auto-bed leveling, and multi-material compatibility for creative projects.",
        "A flatbed scanner with high-resolution scanning, OCR support, and multiple document format saving options.",
        "A compact inkjet printer with refillable ink tanks, low-cost printing, and wireless connectivity for home and office use.",
        "A document scanner with fast batch scanning, automatic page feeding, and cloud integration for seamless workflow management.",
        "A laser all-in-one printer with built-in fax, scanner, copier, and auto document feeder for business productivity.",
        "A large-format printer designed for architects, engineers, and designers, offering superior print quality and poster-sized output.",
        "A barcode scanner with wireless connectivity, rapid scanning technology, and multi-code compatibility for inventory management."
    ],
    
    "graphics-cards": [
        "A high-end graphics card with real-time ray tracing, AI-powered upscaling, and ultra-fast VRAM for next-gen gaming.",
        "A professional workstation GPU optimized for 3D rendering, AI processing, and high-performance computing tasks.",
        "A budget-friendly GPU with solid performance for 1080p gaming, power-efficient design, and enhanced cooling.",
        "A compact low-profile GPU designed for small form-factor PCs, featuring efficient cooling and VR support.",
        "A dual-fan graphics card with robust thermal management, enhanced overclocking capabilities, and high refresh rate gaming support.",
        "An external GPU enclosure with plug-and-play compatibility, allowing laptop users to enjoy desktop-grade graphics performance.",
        "A liquid-cooled GPU with advanced cooling technology, minimal noise, and optimized performance for demanding applications.",
        "A mining-optimized graphics card featuring low power consumption and efficient blockchain processing performance.",
        "A workstation GPU with ECC memory support, optimized for machine learning, CAD, and scientific simulations.",
        "A graphics card with a reinforced PCB, military-grade components, and RGB lighting for ultimate gaming customization."
    ],

    "ram-storage": [
        "A high-performance DDR5 RAM module with ultra-fast speeds, low latency, and RGB lighting for gamers and content creators.",
        "An energy-efficient DDR4 RAM designed for laptops, offering enhanced multitasking capabilities and improved power consumption.",
        "A workstation-grade ECC RAM module ensuring data integrity and stability for mission-critical applications and enterprise servers.",
        "A high-capacity RAM upgrade kit optimized for high-end gaming, video editing, and data-intensive applications.",
        "A budget-friendly DDR4 RAM stick with stable performance, making it ideal for upgrading everyday computing systems.",
        "An overclockable RAM module with an advanced heat spreader, ensuring optimal thermal management for demanding workloads.",
        "A laptop RAM upgrade with low-voltage operation, improved power efficiency, and seamless plug-and-play installation.",
        "A server-class RAM module with advanced error correction, built for handling large-scale data processing and virtualization.",
        "A dual-channel RAM kit designed for enhanced bandwidth, smoother multitasking, and improved gaming performance.",
        "An ultra-fast DDR5 RAM with XMP support, designed for extreme overclocking and peak system efficiency."
    ],
    
    "cooling-pads": [
        "A high-performance laptop cooling pad featuring adjustable fan speeds, an ergonomic design, and USB-powered operation.",
        "A gaming laptop cooling pad with RGB lighting, powerful turbo fans, and enhanced airflow for heat dissipation.",
        "An ultra-portable cooling pad with a slim design, whisper-quiet operation, and improved laptop ventilation.",
        "A multi-angle cooling stand with adjustable height settings, designed for ergonomic comfort and improved laptop cooling.",
        "A heavy-duty cooling pad with multiple high-speed fans, ensuring optimal heat management for high-performance laptops.",
        "A USB-powered laptop cooler with an anti-slip surface, improving airflow and extending the lifespan of internal components.",
        "A silent cooling pad optimized for office and home use, featuring efficient cooling technology and durable construction.",
        "A laptop cooling dock with built-in USB hubs, additional connectivity options, and superior heat dissipation capabilities.",
        "A modular cooling pad with interchangeable fans, allowing users to customize airflow based on laptop hot zones.",
        "A compact laptop cooling solution with passive cooling technology, improving thermal efficiency without additional power consumption."
    ],
    
    "networking": [
        "A high-speed Wi-Fi 6 router with advanced beamforming technology, improved security, and ultra-low latency for gaming and streaming.",
        "A mesh Wi-Fi system offering seamless whole-home coverage, intelligent band steering, and easy app-based management.",
        "A dual-band gigabit router optimized for smooth video conferencing, smart home devices, and lag-free browsing.",
        "A high-performance gaming router featuring dedicated gaming traffic prioritization, ultra-fast speeds, and optimized latency reduction.",
        "A secure VPN router with enterprise-grade encryption, ensuring safe and private browsing across all connected devices.",
        "A 4G LTE mobile hotspot with fast data speeds, long battery life, and multi-device connectivity for on-the-go networking.",
        "A powerline adapter kit designed for extending wired internet coverage through existing electrical wiring, ensuring stable connectivity.",
        "A high-speed network switch with multiple gigabit ports, VLAN support, and QoS optimization for efficient data management.",
        "A dual-band Wi-Fi extender designed to eliminate dead zones, improve signal strength, and enhance connectivity in large spaces.",
        "A high-gain USB Wi-Fi adapter with plug-and-play compatibility, boosting wireless signal reception for desktops and laptops."
    ],
    
    "usb-hubs": [
        "A compact USB-C hub with multiple ports, including HDMI, USB 3.0, and SD card slots, for seamless connectivity on the go.",
        "A high-speed USB 3.2 hub offering multiple expansion ports, fast data transfer rates, and plug-and-play compatibility.",
        "A powered USB hub with dedicated charging ports, ensuring efficient power delivery and fast charging for multiple devices.",
        "A premium docking station with dual 4K display support, Thunderbolt 4 connectivity, and multiple expansion ports for professionals.",
        "A gaming-focused USB hub with customizable RGB lighting, additional USB ports, and enhanced data transfer speeds.",
        "A travel-friendly USB hub with a slim design, foldable connectors, and universal compatibility for all USB devices.",
        "A USB hub with integrated surge protection, ensuring safe and stable connections for sensitive peripherals.",
        "A multi-functional USB hub with Ethernet support, HDMI output, and high-speed data transfer for enhanced productivity.",
        "A dual-purpose USB-C adapter with PD (Power Delivery) charging, allowing simultaneous charging and data transfer.",
        "A rugged USB hub with reinforced cables, durable aluminum casing, and anti-overheating protection for long-lasting performance."
    ]
}

features = {
    "desktop": {
        "Display": ["27\" 4K IPS", "144Hz refresh rate", "HDR10 support", "178° wide viewing angle", "Anti-glare coating"],
        "Processor": ["Intel Core i9-13900K", "AMD Ryzen 9 7900X", "Intel Core i7-13700K", "AMD Ryzen 7 7800X"],
        "Graphics": ["NVIDIA GeForce RTX 4090", "AMD Radeon RX 7900 XT", "NVIDIA RTX 3080 Ti", "AMD Radeon RX 6800"],
        "Storage": ["1TB SSD (NVMe)", "2TB HDD", "500GB SSD", "1TB M.2 PCIe 4.0"],
        "RAM": ["64GB DDR5", "32GB DDR4", "16GB DDR5", "128GB ECC RAM"],
        "Connectivity": ["WiFi 6E", "Bluetooth 5.2", "10Gb Ethernet", "USB 3.2 Gen 2x2"],
        "Ports": ["4x USB 3.0", "2x Thunderbolt 4", "HDMI 2.1", "DisplayPort 1.4", "Ethernet RJ45"],
        "Cooling": ["Custom liquid cooling", "Dual-fan cooling system", "Air cooling with high CFM fans"]
    },
    
    "monitors": {
        "Display": ["27\" 4K UHD", "144Hz refresh rate", "IPS panel", "HDR1000", "G-Sync/FreeSync support"],
        "Resolution": ["1920x1080", "2560x1440", "3840x2160", "5120x1440"],
        "Connectivity": ["HDMI 2.1", "DisplayPort 1.4", "USB-C", "USB 3.0 hub"],
        "Refresh Rate": ["60Hz", "120Hz", "144Hz", "240Hz"],
        "Color Accuracy": ["100% sRGB", "99% AdobeRGB", "98% DCI-P3"],
        "Brightness": ["350 nits", "600 nits peak", "HDR support"],
        "Ergonomics": ["Tilt, swivel, height adjustable", "VESA mountable", "Curved design (1800R)"]
    },

    "keyboards-mice": {
        "Key Type": ["Mechanical switches", "Membrane switches", "Optical switches", "Razer Green", "Cherry MX Blue"],
        "Connectivity": ["Wired", "Wireless (Bluetooth 5.0)", "2.4 GHz wireless"],
        "Features": ["RGB lighting", "Customizable macros", "Dedicated media controls", "Hot-swappable keys"],
        "Form Factor": ["Full-size", "Tenkeyless", "60% compact"],
        "Mouse DPI": ["8000 DPI", "16000 DPI", "3200 DPI adjustable"],
        "Ergonomics": ["Ergonomic design", "Detachable wrist rest", "Ambidextrous"],
        "Battery": ["Rechargeable (USB-C)", "Up to 50 hours battery life", "AA battery (up to 1 year)"]
    },

    "storage": {
        "SSD": ["1TB NVMe M.2", "2TB SATA III", "500GB PCIe Gen 3", "512GB NVMe PCIe 4.0"],
        "HDD": ["1TB", "2TB", "4TB", "6TB", "8TB"],
        "Read Speed": ["5000MB/s", "550MB/s", "3000MB/s"],
        "Write Speed": ["4500MB/s", "520MB/s", "2800MB/s"],
        "Form Factor": ["2.5\" SATA", "M.2 2280", "3.5\""],
        "Reliability": ["MTBF: 1.5 million hours", "Endurance: 1TBW", "Low power consumption"],
        "Encryption": ["256-bit AES encryption", "Hardware encryption support"]
    },

    "printers-scanners": {
        "Printer Type": ["Inkjet", "Laser", "All-in-One (Print, Scan, Copy)"],
        "Print Speed": ["20 pages per minute (ppm)", "35 ppm", "60 ppm"],
        "Connectivity": ["Wi-Fi", "Ethernet", "Bluetooth", "USB 2.0"],
        "Resolution": ["4800 x 1200 DPI", "600 x 600 DPI", "1200 x 1200 DPI"],
        "Scanner Type": ["Flatbed", "Sheet-fed", "Duplex scanning"],
        "Paper Handling": ["Automatic document feeder (ADF)", "Manual duplex", "Up to A3 paper size"],
        "Cartridge": ["Toner", "Ink cartridges", "Refillable ink tank system"]
    },

    "graphics-cards": {
        "GPU": ["NVIDIA GeForce RTX 4090", "AMD Radeon RX 7900 XTX", "NVIDIA RTX 3080", "AMD Radeon RX 6800"],
        "VRAM": ["24GB GDDR6X", "16GB GDDR6", "12GB GDDR6"],
        "Ports": ["3x DisplayPort 1.4", "HDMI 2.1", "USB-C (VirtualLink)"],
        "Clock Speed": ["2.5 GHz", "1.8 GHz", "1.9 GHz"],
        "Cooling": ["Triple-fan cooling", "Dual-fan", "Liquid cooling"],
        "Ray Tracing": ["Yes", "Real-time ray tracing support", "DLSS support"],
        "Power Consumption": ["350W", "300W", "250W"]
    },

    "ram-storage": {
        "RAM": ["32GB DDR5", "64GB DDR4", "16GB DDR4", "128GB DDR5"],
        "Storage": ["1TB SSD", "2TB SSD", "500GB HDD", "2TB HDD"],
        "Speed": ["5500MB/s read, 4000MB/s write", "3200MHz RAM speed", "7200RPM HDD speed"],
        "Features": ["Low voltage", "Overclockable", "Energy-efficient"],
        "Form Factor": ["DIMM", "SO-DIMM", "M.2", "PCIe"],
        "Compatibility": ["XMP supported", "Works with Intel and AMD platforms"]
    },

    "cooling-pads": {
        "Fan Speed": ["3000 RPM", "5000 RPM", "6000 RPM"],
        "Fan Size": ["120mm", "140mm", "160mm"],
        "Portability": ["Slim design", "Foldable stand", "Lightweight"],
        "Cooling Technology": ["Active fan cooling", "Passive cooling", "Heat dissipation pads"],
        "Power Source": ["USB-powered", "Battery-powered", "AC adapter"],
        "Ergonomics": ["Adjustable height", "Anti-slip surface", "Multi-angle support"]
    },

    "networking": {
        "Wi-Fi Standard": ["Wi-Fi 6E", "Wi-Fi 6", "Wi-Fi 5"],
        "Ports": ["4x Gigabit Ethernet", "1x 10Gb Ethernet", "2x USB 3.0", "USB-C"],
        "Speed": ["2.4 Gbps", "5.6 Gbps", "1.2 Gbps"],
        "Security": ["WPA3 encryption", "Firewall support", "Guest network support"],
        "Antennas": ["4x high-gain antennas", "Detachable antennas", "Beamforming technology"],
        "QoS": ["Traffic prioritization", "Bandwidth control", "Latency optimization"]
    },

    "usb-hubs": {
        "Ports": ["4x USB 3.0", "2x USB-C", "6x USB 2.0", "2x HDMI"],
        "Power Delivery": ["PD 3.0", "60W PD", "100W PD"],
        "Compatibility": ["Windows, macOS, Linux", "Plug and play", "No drivers needed"],
        "Material": ["Aluminum body", "Plastic casing", "Magnetic base"],
        "Additional Features": ["Data transfer up to 5Gbps", "Ethernet support", "SD card slot"],
        "Design": ["Compact", "Portable", "Multi-angle adjustable"]
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
