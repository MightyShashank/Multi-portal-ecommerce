import json
import random
import uuid
from fakeData.electronics.faker_electronics import Faker

fake = Faker()
Faker.seed(42)

categories = {
    "toys-and-games": [
        "action-figures", "board-games", "puzzles", "soft-toys", "rc-toys",
        "educational-toys", "lego", "card-games", "playsets", "video-games"
    ]
}

product_data = {
        "action-figures": [
            ("Spider-Man Action Figure", "Hasbro", "AF-####"),
            ("Iron Man 3.75\" Action Figure", "Marvel Legends", "ML-####"),
            ("Transformers Optimus Prime", "Hasbro", "TF-####"),
            ("Star Wars Darth Vader", "LEGO", "SW-####"),
            ("Batman Action Figure", "Mattel", "BA-####")
        ],
        "board-games": [
            ("Monopoly", "Hasbro", "BG-####"),
            ("Catan", "Catan Studio", "CT-####"),
            ("Scrabble", "Mattel", "SC-####"),
            ("Risk", "Hasbro", "RS-####"),
            ("Clue", "Hasbro", "CL-####")
        ],
        "puzzles": [
            ("Jigsaw Puzzle 1000 Pieces", "Ravensburger", "JP-####"),
            ("3D Puzzle Globe", "Cube World", "3D-####"),
            ("Sudoku Puzzle", "Hasbro", "SP-####"),
            ("Wooden Puzzle Set", "Melissa & Doug", "WP-####"),
            ("Puzzle Cube", "Rubik's", "PC-####")
        ],
        "soft-toys": [
            ("Teddy Bear", "Build-A-Bear", "TB-####"),
            ("Stuffed Unicorn", "Gund", "SU-####"),
            ("Plush Dog Toy", "Cuddly Creations", "PD-####"),
            ("Penguin Plush", "Disney", "PP-####"),
            ("Baby Doll", "Fisher Price", "BD-####")
        ],
        "rc-toys": [
            ("RC Helicopter", "Syma", "RC-####"),
            ("RC Car", "Traxxas", "TR-####"),
            ("RC Boat", "ProBoat", "PB-####"),
            ("RC Drone", "DJI", "DJ-####"),
            ("RC Tank", "Tamiya", "TT-####")
        ],
        "educational-toys": [
            ("Counting Blocks", "Fisher Price", "CB-####"),
            ("STEM Learning Kit", "LittleBits", "STEM-####"),
            ("Magnetic Building Set", "Magna-Tiles", "MB-####"),
            ("Learning Tablet", "VTech", "LT-####"),
            ("Robot Kit", "Lego", "RK-####")
        ],
        "lego": [
            ("Lego Star Wars Set", "Lego", "LSW-####"),
            ("Lego Creator Expert", "Lego", "LCX-####"),
            ("Lego Technic Car", "Lego", "LTC-####"),
            ("Lego Friends Set", "Lego", "LFR-####"),
            ("Lego City Police", "Lego", "LCP-####")
        ],
        "card-games": [
            ("Uno", "Mattel", "UC-####"),
            ("Exploding Kittens", "Exploding Kittens", "EK-####"),
            ("Poker Set", "Kangaroo", "PS-####"),
            ("Magic: The Gathering", "Wizards of the Coast", "MTG-####"),
            ("Cards Against Humanity", "Cards Against Humanity", "CAH-####")
        ],
        "playsets": [
            ("Kitchen Playset", "KidKraft", "KP-####"),
            ("Action Hero Playset", "Playmobil", "AH-####"),
            ("Princess Castle Playset", "Fisher Price", "PCP-####"),
            ("Train Set", "Thomas & Friends", "TS-####"),
            ("Farm Animal Playset", "Green Toys", "FAP-####")
        ],
        "video-games": [
            ("Super Mario Odyssey", "Nintendo", "SMO-####"),
            ("The Legend of Zelda: Breath of the Wild", "Nintendo", "ZBW-####"),
            ("Call of Duty: Modern Warfare", "Activision", "COD-####"),
            ("Minecraft", "Mojang", "MC-####"),
            ("FIFA 23", "EA Sports", "FIFA-####")
        ]
    }

descriptions = {
        "action-figures": [
            "A detailed action figure of Spider-Man with movable joints and realistic web-slinging action.",
            "An action-packed Iron Man figure with light-up arc reactor and articulated limbs for dynamic posing.",
            "A fully articulated Optimus Prime figure from Transformers, featuring transforming capabilities and weapons.",
            "A highly detailed Darth Vader figure from Star Wars, equipped with a lightsaber and poseable features.",
            "A Batman action figure with a cape, batarang, and a highly detailed design, perfect for collectors.",
            "A Superman figure with poseable limbs, classic red cape, and laser vision for exciting adventures.",
            "A fully articulated Captain America figure with a shield and interchangeable facial expressions for added realism.",
            "An incredible Hulk figure with large, muscular body, movable limbs, and crushing fists for battle scenes.",
            "A Black Panther action figure with kinetic energy suit design, poseable limbs, and accessories.",
            "A Wonder Woman action figure with a lasso, sword, shield, and a highly detailed armor design."
        ],
        "board-games": [
            "A classic board game of Monopoly, featuring updated designs and tokens, perfect for family game night.",
            "Catan board game with resource trading, development cards, and an island expansion theme for strategic play.",
            "A word game of Scrabble with premium wooden tiles and a rotating board for hours of entertainment.",
            "Risk board game that offers global domination strategy with multiple expansions for a greater challenge.",
            "Clue board game, where players solve a thrilling murder mystery with secret rooms and suspect characters.",
            "Pandemic board game, where players work together to stop the global spread of deadly diseases.",
            "Ticket to Ride, a strategy game where players collect cards to claim train routes and complete destinations.",
            "Chess set with a premium wooden board and high-quality pieces for competitive play.",
            "The Game of Life board game, where players navigate through life’s major milestones with excitement and surprise.",
            "Battleship game where players strategically deploy their ships and attempt to sink their opponent’s fleet."
        ],
        "puzzles": [
            "A 1000-piece jigsaw puzzle featuring stunning landscapes and vibrant colors to challenge your puzzle-solving skills.",
            "A 3D puzzle globe that allows you to build a rotating world map with intricate details and vibrant colors.",
            "A challenging 500-piece puzzle of a beautiful mountain scene, perfect for experienced puzzlers.",
            "A crystal-clear 3D puzzle of the Eiffel Tower, ideal for puzzle lovers and collectors alike.",
            "A vintage-style map puzzle with pieces that fit together to reveal a detailed geographical design.",
            "A puzzle cube with rotating sides and color-coded sections for challenging your spatial reasoning.",
            "A brain-bending 3D wooden puzzle with interlocking pieces to form a complex geometric structure.",
            "A giant floor puzzle of the solar system, perfect for learning about planets while putting the puzzle together.",
            "A wildlife puzzle featuring detailed images of animals in their natural habitats, designed for nature lovers.",
            "A 3D puzzle of the Titanic, where pieces are intricately designed to create a highly detailed ship replica."
        ],
        "soft-toys": [
            "A soft and cuddly teddy bear with a satin ribbon, perfect for snuggling and comforting little ones.",
            "A plush unicorn toy with a rainbow mane and sparkly wings, perfect for imaginative play.",
            "A huggable plush elephant with floppy ears, great for both babies and toddlers to cuddle.",
            "A soft, oversized panda bear plush toy that’s perfect for hugging and relaxing with.",
            "A plush puppy dog with velvety fur and floppy ears, great for pet lovers of all ages.",
            "A fuzzy koala bear stuffed animal with adorable features and soft, high-quality fabric.",
            "A cute and squishy plush rabbit with long ears and a soft, plush body for endless snuggles.",
            "A plush sloth with an ultra-soft body and adorable sleepy eyes, perfect for those who love slow-paced fun.",
            "A plush giraffe with long legs, soft spots, and a cute face for endless hours of cuddly fun.",
            "A soft and fuzzy polar bear stuffed animal with snow-white fur and a sweet expression."
        ],
        "rc-toys": [
            "A high-performance RC car with all-terrain tires, perfect for off-road adventures and racing.",
            "An RC helicopter with a durable body, advanced flight features, and a long-lasting battery.",
            "A remote-controlled drone with HD camera, real-time video transmission, and stable flight technology.",
            "An RC boat with a sleek design, high-speed propellers, and waterproof construction for water fun.",
            "A fast RC racing car with responsive controls, sleek design, and shock-resistant body.",
            "A remote-controlled monster truck with oversized tires, ideal for crushing obstacles and performing stunts.",
            "A remote-controlled tank with realistic sounds, working turret, and durable design for battle play.",
            "A RC stunt car that can flip, roll, and perform high-speed tricks with a durable chassis.",
            "A RC airplane with beginner-friendly controls, advanced stabilization technology, and a lightweight frame.",
            "A high-speed RC racing boat with a streamlined body for fast water races and stunts."
        ],
        "educational-toys": [
            "A STEM toy set that allows kids to build their own robotic arms and learn basic engineering principles.",
            "A chemistry set that encourages kids to explore science through fun and safe experiments.",
            "An interactive learning globe that provides information on countries, capitals, and geography.",
            "A building block set that develops fine motor skills while teaching engineering concepts.",
            "A puzzle that helps children learn the alphabet and numbers while having fun.",
            "A magnetic drawing board that helps kids develop their creative skills while learning to write and draw.",
            "A solar-powered robot kit that teaches kids about renewable energy and engineering.",
            "A Montessori toy set for learning colors, shapes, and counting in an interactive and hands-on way.",
            "An educational art kit that encourages children to create masterpieces while learning about different artists.",
            "A wooden toy set that helps young children learn about shapes, patterns, and colors in a tactile way."
        ],
        "lego": [
            "A Lego City set with fire trucks, police cars, and adventure-filled buildings for hours of fun.",
            "A Lego Star Wars set with iconic vehicles and characters for recreating scenes from the galaxy far, far away.",
            "A Lego Friends set featuring a luxury pool party scene with minifigures and detailed accessories.",
            "A Lego Technic set for advanced builders, featuring a working crane with moving parts.",
            "A Lego Creator set for building a multi-functional modular house with interchangeable pieces.",
            "A Lego Architecture set for building detailed replicas of famous landmarks around the world.",
            "A Lego Ninjago set with minifigures, weapons, and exciting battle scenes for young ninja fans.",
            "A Lego Minecraft set that allows players to build their own Minecraft world with iconic characters and items.",
            "A Lego Duplo set for toddlers, featuring oversized pieces and fun, colorful designs for early learning.",
            "A Lego Disney Princess set, with princesses, castles, and magical adventures to enjoy."
        ],
        "card-games": [
            "A classic deck of playing cards with a premium design, perfect for games of Poker, Bridge, or Solitaire.",
            "Uno card game with colorful number cards and special action cards for competitive family fun.",
            "Exploding Kittens, a hilarious card game where players try to avoid drawing the 'exploding kitten' card.",
            "Cards Against Humanity, the party game of inappropriate humor with endless hilarious combinations.",
            "Go Fish card game with a fun and easy-to-understand design for younger players.",
            "Codenames, a word association game where teams try to guess words based on cryptic clues.",
            "Phase 10, a rummy-type card game with fun phases that players must complete before their opponents.",
            "Magic: The Gathering, the strategy card game featuring creatures, spells, and mystical lands.",
            "Skip-Bo, a fast-paced card game where players race to be the first to play all their cards in sequence.",
            "The Game of Life: Journey to the Millionaire Mansion, where players make decisions on their way to financial success."
        ],
        "playsets": [
            "A dollhouse playset with multiple rooms, furniture, and accessories for hours of imaginative play.",
            "A pirate ship playset with pirates, treasure, and a working cannon for epic adventures on the high seas.",
            "A farm playset with animals, barns, and accessories for kids to create their own countryside world.",
            "A construction site playset with toy tools, workers, and vehicles for young builders to create their own projects.",
            "A kitchen playset with pots, pans, and cooking accessories for budding chefs.",
            "A princess castle playset with towers, princesses, and a royal carriage for magical adventures.",
            "A car racing playset with tracks, cars, and ramps for high-speed racing fun.",
            "A zoo playset featuring a variety of animals, cages, and zookeepers for wildlife-themed play.",
            "A spaceship playset with astronauts, rockets, and planets for intergalactic exploration.",
            "A police station playset with officers, cars, and a jail for solving mysteries and keeping the city safe."
        ],
        "video-games": [
            "A fun and engaging video game featuring an open-world environment where players explore, create, and battle.",
            "A racing game with fast-paced action, customizable cars, and exciting tracks for endless thrills.",
            "A puzzle game that challenges players to solve mind-bending riddles and uncover hidden mysteries.",
            "An action-adventure game with immersive storytelling, dynamic gameplay, and stunning graphics.",
            "A simulation game where players can build and manage their own city, farm, or amusement park.",
            "A multiplayer first-person shooter game that pits teams against each other in fast-paced combat.",
            "A platformer video game featuring colorful characters, challenging levels, and epic adventures.",
            "A role-playing game with a deep storyline, character customization, and a vast world to explore.",
            "A fighting game featuring iconic characters, combo moves, and intense one-on-one battles.",
            "A strategy game where players must use their wits and tactical skills to conquer their enemies."
        ]
    }

features = {
        "action-figures": {
            "Material": ["Plastic", "Die-Cast", "Vinyl", "Soft Fabric", "Rubber"],
            "Articulation": ["Fully Poseable", "Movable Joints", "Static", "Rotating Head", "Pivoting Limbs"],
            "Accessories": ["Weapons", "Shield", "Belt", "Helmet", "Cape"],
            "Size": ["3-inch", "6-inch", "12-inch", "16-inch", "24-inch"],
            "Suitability": ["Ages 4+", "Ages 6+", "Ages 8+", "Ages 12+"],
            "Special Features": ["Light-up Features", "Sound Effects", "Transformation", "Poseable Hands", "Interchangeable Parts"],
            "Theme": ["Superheroes", "Fantasy", "Military", "Dinosaurs", "Robots"],
            "Packaging": ["Collector's Box", "Blister Packaging", "Window Box", "Display Stand"],
        },
        "board-games": {
            "Game Type": ["Strategy", "Trivia", "Adventure", "Family", "Party"],
            "Players": ["2-4 Players", "4-6 Players", "6-10 Players", "Solo"],
            "Age Group": ["Ages 8+", "Ages 10+", "Ages 12+", "Ages 16+"],
            "Material": ["Cardboard", "Plastic", "Wooden Pieces", "Metal", "Magnetic"],
            "Play Time": ["15-30 minutes", "30-60 minutes", "60-120 minutes", "Over 2 hours"],
            "Special Features": ["Interactive", "Portable", "Cooperative", "Trivia-based", "Role-Playing"],
            "Theme": ["Historical", "Fantasy", "Mystery", "Science Fiction", "Sports"],
            "Packaging": ["Compact Box", "Travel Size", "Deluxe Edition"],
        },
        "puzzles": {
            "Piece Count": ["100 pieces", "500 pieces", "1000 pieces", "1500 pieces", "2000 pieces"],
            "Material": ["Cardboard", "Wood", "Foam", "Plastic", "Magnetic"],
            "Difficulty Level": ["Easy", "Medium", "Hard", "Expert"],
            "Theme": ["Landscapes", "Animals", "Architecture", "Abstract", "Art"],
            "Packaging": ["Boxed", "Tinned", "Roll-up Mat", "Wooden Box"],
            "Special Features": ["Glow-in-the-Dark", "3D Puzzles", "Shape-Specific Pieces", "Educational"],
            "Size": ["Standard", "Mini", "Large Format"],
            "Suitable For": ["Kids", "Adults", "Families", "Collectors"],
        },
        "soft-toys": {
            "Material": ["Plush", "Velour", "Cotton", "Fleece", "Bamboo Fabric"],
            "Size": ["Small", "Medium", "Large", "Extra-Large"],
            "Washable": ["Machine Washable", "Hand Wash Only", "Spot Clean"],
            "Age Group": ["Ages 0+", "Ages 3+", "Ages 5+", "Ages 7+"],
            "Special Features": ["Sound Effects", "Movable Parts", "Interactive", "Reversible", "Light-Up Features"],
            "Animal Types": ["Bear", "Dog", "Cat", "Unicorn", "Dinosaur"],
            "Packaging": ["Gift Box", "Hanging Tag", "Resealable Bag"],
            "Eco-Friendly": ["Biodegradable", "Recycled Materials", "Organic Cotton"],
        },
        "rc-toys": {
            "Type": ["Car", "Boat", "Helicopter", "Airplane", "Drone"],
            "Control Range": ["10m", "30m", "50m", "100m", "200m"],
            "Battery Type": ["Rechargeable", "AA Batteries", "AAA Batteries"],
            "Material": ["Plastic", "Metal", "Rubber", "Carbon Fiber", "ABS"],
            "Special Features": ["LED Lights", "Shock Absorbers", "Speed Control", "Camera Integration", "Waterproof"],
            "Age Group": ["Ages 6+", "Ages 8+", "Ages 12+"],
            "Speed": ["Up to 10 km/h", "Up to 30 km/h", "Up to 50 km/h"],
            "Control Type": ["2.4 GHz Remote", "Bluetooth", "Wi-Fi App Control"],
            "Suitability": ["Indoor", "Outdoor", "All-terrain", "Off-road", "On-road"],
        },
        "educational-toys": {
            "Type": ["STEM", "Montessori", "Math", "Reading", "Art"],
            "Material": ["Wood", "Plastic", "Metal", "Fabric", "Magnetic"],
            "Age Group": ["Ages 1+", "Ages 3+", "Ages 5+", "Ages 7+", "Ages 10+"],
            "Learning Focus": ["Problem Solving", "Motor Skills", "Critical Thinking", "Creativity", "STEM Skills"],
            "Special Features": ["Interactive", "App Integrated", "Augmented Reality", "Hands-On", "Puzzle-based"],
            "Packaging": ["Portable", "Storage Box", "Portable Carrying Case"],
            "Certification": ["BPA Free", "Non-Toxic", "Lead-Free", "Eco-Friendly"],
        },
        "lego": {
            "Set Type": ["City", "Friends", "Technic", "Creator", "Architecture"],
            "Piece Count": ["50 pieces", "200 pieces", "500 pieces", "1000 pieces", "2000+ pieces"],
            "Age Group": ["Ages 3+", "Ages 6+", "Ages 10+", "Ages 14+"],
            "Theme": ["Superheroes", "Dinosaurs", "Cars", "Space", "Castles"],
            "Material": ["Plastic", "ABS Plastic", "Rubber"],
            "Compatibility": ["Compatible with Other Sets", "Exclusive Pieces", "Expansion Packs"],
            "Special Features": ["Motorized Parts", "Interchangeable Pieces", "Moveable Elements", "Modular"],
            "Packaging": ["Boxed", "Travel-Friendly", "Eco-Packaging"],
        },
        "card-games": {
            "Game Type": ["Strategy", "Family", "Party", "Trivia", "Deck-Building"],
            "Players": ["2 Players", "3-4 Players", "5-8 Players"],
            "Card Material": ["Plastic", "Paper", "Premium"],
            "Game Duration": ["30 minutes", "45 minutes", "60 minutes"],
            "Special Features": ["Easy to Learn", "Portable", "Party-Ready", "Theme-Based", "Strategy-Oriented"],
            "Suitable For": ["Children", "Adults", "Teens", "Families"],
            "Age Group": ["Ages 6+", "Ages 10+", "Ages 12+", "Ages 16+"],
            "Packaging": ["Compact Box", "Collector's Edition Box", "Tinned Box"],
        },
        "playsets": {
            "Material": ["Plastic", "Wood", "Metal", "Cardboard", "Foam"],
            "Theme": ["Pirate", "Castle", "Space", "Dinosaur", "Farm"],
            "Age Group": ["Ages 3+", "Ages 5+", "Ages 8+", "Ages 12+"],
            "Special Features": ["Interactive", "Voice-Activated", "Transforming Parts", "Removable Figures", "Accessories Included"],
            "Packaging": ["Playset Box", "Reusable Bag", "Gift-Ready Box"],
            "Dimensions": ["Small", "Medium", "Large", "Extra-Large"],
            "Action Figures Included": ["1 Figure", "2-5 Figures", "6+ Figures"],
            "Build Time": ["Instant", "1-2 Hours", "Multiple Sessions"],
        },
        "video-games": {
            "Platform": ["PC", "PlayStation", "Xbox", "Switch", "Mobile"],
            "Genre": ["Action", "Adventure", "Puzzle", "Strategy", "RPG"],
            "Age Rating": ["Everyone", "Teen", "Mature", "Adults Only"],
            "Multiplayer": ["Single-player", "Multiplayer Online", "Co-Op", "Local Multiplayer"],
            "Special Features": ["DLC Available", "VR Compatible", "Online Play", "Achievement System"],
            "Game Mode": ["Single Player", "Multiplayer", "Open World", "Linear Progression"],
            "Graphics": ["2D", "3D", "HD", "Ultra HD", "4K"],
            "Sound": ["Stereo", "Surround Sound", "Dolby Atmos", "Voice Commands"],
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

with open("fake_products_toys_and_games.json", "w") as f:
    json.dump(dataset, f, indent=4)

print("Fake product dataset with 500 products generated successfully!")
