import json
import random
import uuid
from fakeData.electronics.faker_electronics import Faker

fake = Faker()
Faker.seed(42)

categories = {
    "books-and-stationery": [
        "fiction", "non-fiction", "educational", "comics", "notebooks-diaries",
        "pens-writing", "art-supplies", "office-supplies", "calculators", "ehomes"
    ]
}

product_data = {
    "fiction": [
        # Classic Literature 📖
        ("The Great Gatsby", "F. Scott Fitzgerald", "FIC-001"),
        ("To Kill a Mockingbird", "Harper Lee", "FIC-002"),
        ("1984", "George Orwell", "FIC-003"),
        ("Pride and Prejudice", "Jane Austen", "FIC-004"),
        ("The Catcher in the Rye", "J.D. Salinger", "FIC-005"),
        ("Moby-Dick", "Herman Melville", "FIC-006"),
        ("Jane Eyre", "Charlotte Brontë", "FIC-007"),
        ("Wuthering Heights", "Emily Brontë", "FIC-008"),
        ("Crime and Punishment", "Fyodor Dostoevsky", "FIC-009"),
        ("Brave New World", "Aldous Huxley", "FIC-010"),

        # Modern Fiction 📖
        ("The Road", "Cormac McCarthy", "FIC-011"),
        ("The Book Thief", "Markus Zusak", "FIC-012"),
        ("A Man Called Ove", "Fredrik Backman", "FIC-013"),
        ("Where the Crawdads Sing", "Delia Owens", "FIC-014"),
        ("The Night Circus", "Erin Morgenstern", "FIC-015"),
        ("The Goldfinch", "Donna Tartt", "FIC-016"),
        ("Shantaram", "Gregory David Roberts", "FIC-017"),
        ("The Shadow of the Wind", "Carlos Ruiz Zafón", "FIC-018"),
        ("The Kite Runner", "Khaled Hosseini", "FIC-019"),
        ("Life of Pi", "Yann Martel", "FIC-020"),

        # Fantasy & Sci-Fi 📖✨
        ("Harry Potter and the Sorcerer’s Stone", "J.K. Rowling", "FIC-021"),
        ("The Hobbit", "J.R.R. Tolkien", "FIC-022"),
        ("The Lord of the Rings", "J.R.R. Tolkien", "FIC-023"),
        ("A Game of Thrones", "George R.R. Martin", "FIC-024"),
        ("Dune", "Frank Herbert", "FIC-025"),
        ("The Name of the Wind", "Patrick Rothfuss", "FIC-026"),
        ("Mistborn: The Final Empire", "Brandon Sanderson", "FIC-027"),
        ("The Way of Kings", "Brandon Sanderson", "FIC-028"),
        ("Good Omens", "Neil Gaiman & Terry Pratchett", "FIC-029"),
        ("American Gods", "Neil Gaiman", "FIC-030"),

        # Mystery & Thriller 🔍
        ("Gone Girl", "Gillian Flynn", "FIC-031"),
        ("The Girl with the Dragon Tattoo", "Stieg Larsson", "FIC-032"),
        ("Big Little Lies", "Liane Moriarty", "FIC-033"),
        ("The Da Vinci Code", "Dan Brown", "FIC-034"),
        ("The Silent Patient", "Alex Michaelides", "FIC-035"),
        ("The Woman in the Window", "A.J. Finn", "FIC-036"),
        ("Sharp Objects", "Gillian Flynn", "FIC-037"),
        ("Before We Were Strangers", "Renée Carlino", "FIC-038"),
        ("The Couple Next Door", "Shari Lapena", "FIC-039"),
        ("Verity", "Colleen Hoover", "FIC-040"),

        # Historical Fiction 🏰
        ("The Nightingale", "Kristin Hannah", "FIC-041"),
        ("The Alice Network", "Kate Quinn", "FIC-042"),
        ("The Tattooist of Auschwitz", "Heather Morris", "FIC-043"),
        ("All the Light We Cannot See", "Anthony Doerr", "FIC-044"),
        ("Beneath a Scarlet Sky", "Mark Sullivan", "FIC-045"),
        ("The Book Thief", "Markus Zusak", "FIC-046"),
        ("The Paris Library", "Janet Skeslien Charles", "FIC-047"),
        ("Before We Were Strangers", "Renée Carlino", "FIC-048"),
        ("The Light We Lost", "Jill Santopolo", "FIC-049"),
        ("We Were Liars", "E. Lockhart", "FIC-050")
    ],

    "non-fiction": [
        # History & Society 🌍
        ("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "NF-001"),
        ("Homo Deus: A Brief History of Tomorrow", "Yuval Noah Harari", "NF-002"),
        ("Guns, Germs, and Steel", "Jared Diamond", "NF-003"),
        ("The Silk Roads", "Peter Frankopan", "NF-004"),
        ("A People's History of the United States", "Howard Zinn", "NF-005"),
        ("The Wright Brothers", "David McCullough", "NF-006"),
        ("The Diary of a Young Girl", "Anne Frank", "NF-007"),
        ("The Immortal Life of Henrietta Lacks", "Rebecca Skloot", "NF-008"),
        ("The Sixth Extinction", "Elizabeth Kolbert", "NF-009"),
        ("A Short History of Nearly Everything", "Bill Bryson", "NF-010"),

        # Self-Help & Personal Growth 📈
        ("The Subtle Art of Not Giving a F*ck", "Mark Manson", "NF-011"),
        ("Atomic Habits", "James Clear", "NF-012"),
        ("The 7 Habits of Highly Effective People", "Stephen R. Covey", "NF-013"),
        ("How to Win Friends and Influence People", "Dale Carnegie", "NF-014"),
        ("Daring Greatly", "Brené Brown", "NF-015"),
        ("The Power of Habit", "Charles Duhigg", "NF-016"),
        ("Mindset: The New Psychology of Success", "Carol S. Dweck", "NF-017"),
        ("The Four Agreements", "Don Miguel Ruiz", "NF-018"),
        ("You Are a Badass", "Jen Sincero", "NF-019"),
        ("Can't Hurt Me", "David Goggins", "NF-020"),

        # Biographies & Memoirs 👤
        ("Becoming", "Michelle Obama", "NF-021"),
        ("Steve Jobs", "Walter Isaacson", "NF-022"),
        ("Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future", "Ashlee Vance", "NF-023"),
        ("The Glass Castle", "Jeannette Walls", "NF-024"),
        ("When Breath Becomes Air", "Paul Kalanithi", "NF-025"),
        ("Educated", "Tara Westover", "NF-026"),
        ("Long Walk to Freedom", "Nelson Mandela", "NF-027"),
        ("Shoe Dog", "Phil Knight", "NF-028"),
        ("Bossypants", "Tina Fey", "NF-029"),
        ("Born a Crime", "Trevor Noah", "NF-030"),

        # Business & Leadership 💼
        ("The Lean Startup", "Eric Ries", "NF-031"),
        ("Zero to One", "Peter Thiel", "NF-032"),
        ("Good to Great", "Jim Collins", "NF-033"),
        ("Thinking, Fast and Slow", "Daniel Kahneman", "NF-034"),
        ("The Psychology of Money", "Morgan Housel", "NF-035"),
        ("Rich Dad Poor Dad", "Robert Kiyosaki", "NF-036"),
        ("The Millionaire Next Door", "Thomas J. Stanley", "NF-037"),
        ("The Hard Thing About Hard Things", "Ben Horowitz", "NF-038"),
        ("The 4-Hour Workweek", "Tim Ferriss", "NF-039"),
        ("Measure What Matters", "John Doerr", "NF-040"),

        # Science & Technology 🔬
        ("Cosmos", "Carl Sagan", "NF-041"),
        ("Brief Answers to the Big Questions", "Stephen Hawking", "NF-042"),
        ("The Gene: An Intimate History", "Siddhartha Mukherjee", "NF-043"),
        ("The Code Breaker", "Walter Isaacson", "NF-044"),
        ("Why We Sleep", "Matthew Walker", "NF-045"),
        ("AI Superpowers", "Kai-Fu Lee", "NF-046"),
        ("Astrophysics for People in a Hurry", "Neil deGrasse Tyson", "NF-047"),
        ("Godel, Escher, Bach", "Douglas Hofstadter", "NF-048"),
        ("The Emperor of All Maladies", "Siddhartha Mukherjee", "NF-049"),
        ("The Body: A Guide for Occupants", "Bill Bryson", "NF-050")
    ],

    "educational": [
        # Computer Science & Programming 💻
        ("Introduction to Algorithms", "Thomas H. Cormen", "EDU-001"),
        ("The Art of Computer Programming", "Donald Knuth", "EDU-002"),
        ("Design Patterns: Elements of Reusable Object-Oriented Software", "Erich Gamma et al.", "EDU-003"),
        ("Structure and Interpretation of Computer Programs", "Harold Abelson", "EDU-004"),
        ("Clean Code", "Robert C. Martin", "EDU-005"),
        ("Computer Networking: A Top-Down Approach", "Kurose & Ross", "EDU-006"),
        ("Operating System Concepts", "Abraham Silberschatz", "EDU-007"),
        ("Compilers: Principles, Techniques, and Tools", "Aho, Lam, Sethi, Ullman", "EDU-008"),
        ("Database System Concepts", "Abraham Silberschatz", "EDU-009"),
        ("Artificial Intelligence: A Modern Approach", "Stuart Russell & Peter Norvig", "EDU-010"),

        # Mathematics 🧮
        ("Linear Algebra Done Right", "Sheldon Axler", "EDU-011"),
        ("Introduction to Probability", "Dimitri P. Bertsekas", "EDU-012"),
        ("Abstract Algebra", "David S. Dummit & Richard M. Foote", "EDU-013"),
        ("Real Analysis", "H.L. Royden", "EDU-014"),
        ("Calculus", "James Stewart", "EDU-015"),
        ("Topology", "James R. Munkres", "EDU-016"),
        ("Mathematical Methods for Physics and Engineering", "K.F. Riley", "EDU-017"),
        ("A Course in Number Theory and Cryptography", "Neal Koblitz", "EDU-018"),
        ("Game Theory", "Roger B. Myerson", "EDU-019"),
        ("Graph Theory", "Reinhard Diestel", "EDU-020"),

        # Physics 🔬
        ("Concepts of Physics", "H.C. Verma", "EDU-021"),
        ("Fundamentals of Physics", "David Halliday & Robert Resnick", "EDU-022"),
        ("Introduction to Electrodynamics", "David J. Griffiths", "EDU-023"),
        ("Classical Mechanics", "Herbert Goldstein", "EDU-024"),
        ("Quantum Mechanics and Path Integrals", "Richard P. Feynman", "EDU-025"),
        ("Statistical Mechanics", "R.K. Pathria", "EDU-026"),
        ("The Feynman Lectures on Physics", "Richard Feynman", "EDU-027"),
        ("Modern Classical Physics", "Kip S. Thorne", "EDU-028"),
        ("Gravitation", "Charles W. Misner, Kip S. Thorne, John A. Wheeler", "EDU-029"),
        ("Thermodynamics and Statistical Mechanics", "Walter Greiner", "EDU-030"),

        # Engineering & Applied Sciences ⚙️
        ("Advanced Engineering Mathematics", "Erwin Kreyszig", "EDU-031"),
        ("Signals and Systems", "Alan V. Oppenheim", "EDU-032"),
        ("Control Systems Engineering", "Norman S. Nise", "EDU-033"),
        ("Mechanical Engineering Design", "Joseph Edward Shigley", "EDU-034"),
        ("Electrical Engineering: Principles and Applications", "Allan R. Hambley", "EDU-035"),
        ("Fluid Mechanics", "Frank M. White", "EDU-036"),
        ("Materials Science and Engineering", "William D. Callister", "EDU-037"),
        ("Digital Design", "M. Morris Mano", "EDU-038"),
        ("Microelectronic Circuits", "Sedra & Smith", "EDU-039"),
        ("Introduction to Robotics: Mechanics and Control", "John J. Craig", "EDU-040"),

        # Chemistry & Biology 🧪
        ("Organic Chemistry", "Paula Yurkanis Bruice", "EDU-041"),
        ("Principles of Biochemistry", "Lehninger", "EDU-042"),
        ("Physical Chemistry", "Peter Atkins", "EDU-043"),
        ("Biology", "Campbell & Reece", "EDU-044"),
        ("Inorganic Chemistry", "Catherine Housecroft", "EDU-045"),
        ("Molecular Biology of the Cell", "Bruce Alberts", "EDU-046"),
        ("Genetics: Analysis and Principles", "Robert Brooker", "EDU-047"),
        ("An Introduction to Medicinal Chemistry", "Graham Patrick", "EDU-048"),
        ("Essentials of Ecology", "Colin R. Townsend", "EDU-049"),
        ("Introduction to Environmental Engineering", "Mackenzie L. Davis", "EDU-050")
    ],

    "comics": [
        # Superhero Comics 🦸‍♂️
        ("Batman: The Killing Joke", "Alan Moore", "COM-001"),
        ("Spider-Man: Blue", "Jeph Loeb", "COM-002"),
        ("Watchmen", "Alan Moore", "COM-003"),
        ("The Dark Knight Returns", "Frank Miller", "COM-004"),
        ("Superman: Red Son", "Mark Millar", "COM-005"),
        ("Batman: Year One", "Frank Miller", "COM-006"),
        ("X-Men: Days of Future Past", "Chris Claremont", "COM-007"),
        ("The Infinity Gauntlet", "Jim Starlin", "COM-008"),
        ("Daredevil: Born Again", "Frank Miller", "COM-009"),
        ("Green Lantern: Secret Origin", "Geoff Johns", "COM-010"),

        # Manga 📚
        ("One Piece Vol. 1", "Eiichiro Oda", "COM-011"),
        ("Dragon Ball Vol. 1", "Akira Toriyama", "COM-012"),
        ("Naruto Vol. 1", "Masashi Kishimoto", "COM-013"),
        ("Attack on Titan Vol. 1", "Hajime Isayama", "COM-014"),
        ("Death Note Vol. 1", "Tsugumi Ohba", "COM-015"),
        ("Fullmetal Alchemist Vol. 1", "Hiromu Arakawa", "COM-016"),
        ("Berserk Vol. 1", "Kentaro Miura", "COM-017"),
        ("Demon Slayer Vol. 1", "Koyoharu Gotouge", "COM-018"),
        ("Jujutsu Kaisen Vol. 1", "Gege Akutami", "COM-019"),
        ("Tokyo Ghoul Vol. 1", "Sui Ishida", "COM-020"),

        # Indie & Alternative Comics 🎨
        ("Maus", "Art Spiegelman", "COM-021"),
        ("Saga Vol. 1", "Brian K. Vaughan", "COM-022"),
        ("Sandman Vol. 1: Preludes & Nocturnes", "Neil Gaiman", "COM-023"),
        ("Locke & Key Vol. 1", "Joe Hill", "COM-024"),
        ("Y: The Last Man Vol. 1", "Brian K. Vaughan", "COM-025"),
        ("Scott Pilgrim's Precious Little Life", "Bryan Lee O'Malley", "COM-026"),
        ("Hellboy Vol. 1: Seed of Destruction", "Mike Mignola", "COM-027"),
        ("The Umbrella Academy Vol. 1", "Gerard Way", "COM-028"),
        ("Fables Vol. 1: Legends in Exile", "Bill Willingham", "COM-029"),
        ("Sweet Tooth Vol. 1", "Jeff Lemire", "COM-030"),

        # Marvel Universe 🦸‍♂️
        ("Iron Man: Extremis", "Warren Ellis", "COM-031"),
        ("The Amazing Spider-Man: The Night Gwen Stacy Died", "Gerry Conway", "COM-032"),
        ("Thor: God of Thunder Vol. 1", "Jason Aaron", "COM-033"),
        ("Black Panther: A Nation Under Our Feet", "Ta-Nehisi Coates", "COM-034"),
        ("Captain America: The Winter Soldier", "Ed Brubaker", "COM-035"),
        ("Ms. Marvel Vol. 1: No Normal", "G. Willow Wilson", "COM-036"),
        ("Doctor Strange: The Oath", "Brian K. Vaughan", "COM-037"),
        ("The Wolverine", "Chris Claremont", "COM-038"),
        ("Hulk: Planet Hulk", "Greg Pak", "COM-039"),
        ("Deadpool: The Good, The Bad & The Ugly", "Brian Posehn", "COM-040"),

        # DC Universe 🦇
        ("Justice League: Origin", "Geoff Johns", "COM-041"),
        ("Flashpoint", "Geoff Johns", "COM-042"),
        ("Aquaman Vol. 1: The Trench", "Geoff Johns", "COM-043"),
        ("Wonder Woman: Blood", "Brian Azzarello", "COM-044"),
        ("Green Arrow: Year One", "Andy Diggle", "COM-045"),
        ("Superman: For All Seasons", "Jeph Loeb", "COM-046"),
        ("Batman: Hush", "Jeph Loeb", "COM-047"),
        ("Teen Titans: The Judas Contract", "Marv Wolfman", "COM-048"),
        ("The Flash: Rebirth", "Geoff Johns", "COM-049"),
        ("Batman: The Long Halloween", "Jeph Loeb", "COM-050")
    ],

    "notebooks-diaries": [
        # Premium Notebooks 🏆
        ("Moleskine Classic Notebook", "Moleskine", "NB-001"),
        ("Leuchtturm1917 Dotted Journal", "Leuchtturm", "NB-002"),
        ("Field Notes Memo Book", "Field Notes", "NB-003"),
        ("Rhodia Webnotebook", "Rhodia", "NB-004"),
        ("Paperblanks Hardcover Journal", "Paperblanks", "NB-005"),
        ("Baron Fig Confidant Notebook", "Baron Fig", "NB-006"),
        ("Midori MD Notebook", "Midori", "NB-007"),
        ("Traveler’s Notebook", "Traveler’s Company", "NB-008"),
        ("Blackwing Clutch Notebook", "Blackwing", "NB-009"),
        ("Write Notepads & Co. Ledger", "Write Notepads", "NB-010"),

        # Bullet Journals 📌
        ("Dingbats Earth Journal", "Dingbats", "NB-011"),
        ("Scrivwell Dotted Journal", "Scrivwell", "NB-012"),
        ("Northbooks A5 Dot Journal", "Northbooks", "NB-013"),
        ("Scribbles That Matter Notebook", "STM", "NB-014"),
        ("Minimalism Art Classic Journal", "Minimalism Art", "NB-015"),
        ("Nuuna Graphic Notebook", "Nuuna", "NB-016"),
        ("Lemome Thick Notebook", "Lemome", "NB-017"),
        ("The Clever Fox Planner", "Clever Fox", "NB-018"),
        ("Hobonichi Techo Planner", "Hobonichi", "NB-019"),
        ("Archer & Olive Dot Grid Journal", "Archer & Olive", "NB-020"),

        # Sketchbooks & Art Journals 🎨
        ("Strathmore 400 Series Sketchbook", "Strathmore", "NB-021"),
        ("Canson XL Mixed Media Notebook", "Canson", "NB-022"),
        ("Fabriano EcoQua Notebook", "Fabriano", "NB-023"),
        ("Moleskine Art Sketchbook", "Moleskine", "NB-024"),
        ("Stillman & Birn Alpha Series Sketchbook", "Stillman & Birn", "NB-025"),
        ("Hahnemühle Watercolor Journal", "Hahnemühle", "NB-026"),
        ("Pentalic Traveler’s Sketchbook", "Pentalic", "NB-027"),
        ("Handbook Journal Watercolor", "Global Art", "NB-028"),
        ("Royal & Langnickel Sketchbook", "Royal & Langnickel", "NB-029"),
        ("Shinhan Art Touch Sketchbook", "Shinhan Art", "NB-030"),

        # Specialty Notebooks & Diaries 📅
        ("Mead Five Star Notebook", "Mead", "NB-031"),
        ("Oxford Stone Paper Notebook", "Oxford", "NB-032"),
        ("Rocketbook Smart Reusable Notebook", "Rocketbook", "NB-033"),
        ("Panda Planner Daily", "Panda Planner", "NB-034"),
        ("Passion Planner", "Passion Planner", "NB-035"),
        ("BestSelf Co. Self Journal", "BestSelf Co.", "NB-036"),
        ("The Happy Planner", "Happy Planner", "NB-037"),
        ("Erin Condren LifePlanner", "Erin Condren", "NB-038"),
        ("Blue Sky Academic Planner", "Blue Sky", "NB-039"),
        ("Rekonect Magnetic Notebook", "Rekonect", "NB-040"),

        # Refillable & Eco-Friendly Notebooks 🌱
        ("Ecowriter Refillable Notebook", "Ecowriter", "NB-041"),
        ("Soothi Handmade Leather Journal", "Soothi", "NB-042"),
        ("Wanderings Leather Journal", "Wanderings", "NB-043"),
        ("Peter Pauper Press Leather Journal", "Peter Pauper Press", "NB-044"),
        ("PAPERCODE Luxury Journal", "PAPERCODE", "NB-045"),
        ("Intelligent Change The Five Minute Journal", "Intelligent Change", "NB-046"),
        ("Lemome Cork Cover Notebook", "Lemome", "NB-047"),
        ("Northbooks Recycled Notebook", "Northbooks", "NB-048"),
        ("Hamelin Ruled Notebook", "Hamelin", "NB-049"),
        ("Stone Paper Waterproof Notebook", "Karst", "NB-050")
    ],

    "pens-writing": [
        # Ballpoint Pens 🖊️
        ("Parker Jotter Ballpoint Pen", "Parker", "PW-001"),
        ("Pilot Acroball Ballpoint Pen", "Pilot", "PW-002"),
        ("Uni-Ball Jetstream Ballpoint Pen", "Uni-Ball", "PW-003"),
        ("BIC Cristal Original Ballpoint Pen", "BIC", "PW-004"),
        ("Paper Mate InkJoy Ballpoint Pen", "Paper Mate", "PW-005"),
        ("Cross Classic Century Ballpoint Pen", "Cross", "PW-006"),
        ("Fisher Space Pen Bullet", "Fisher Space Pen", "PW-007"),
        ("Sheaffer Sentinel Ballpoint Pen", "Sheaffer", "PW-008"),
        ("Parker IM Ballpoint Pen", "Parker", "PW-009"),
        ("Rotring Tikky Ballpoint Pen", "Rotring", "PW-010"),

        # Gel Pens 🖋️
        ("Pilot G2 Gel Pen", "Pilot", "PW-011"),
        ("Uni-Ball Signo 207 Gel Pen", "Uni-Ball", "PW-012"),
        ("Pentel EnerGel RTX Gel Pen", "Pentel", "PW-013"),
        ("Pilot Precise V5 RT Gel Pen", "Pilot", "PW-014"),
        ("BIC Gel-ocity Gel Pen", "BIC", "PW-015"),
        ("Zebra Sarasa Clip Gel Pen", "Zebra", "PW-016"),
        ("Muji Gel Ink Pen", "Muji", "PW-017"),
        ("TUL Retractable Gel Pen", "TUL", "PW-018"),
        ("Monami Plus Pen 3000", "Monami", "PW-019"),
        ("Arteza Rollerball Gel Pens", "Arteza", "PW-020"),

        # Fountain Pens 🏆
        ("Lamy Safari Fountain Pen", "Lamy", "PW-021"),
        ("Pilot Metropolitan Fountain Pen", "Pilot", "PW-022"),
        ("TWSBI Eco Fountain Pen", "TWSBI", "PW-023"),
        ("Kaweco Sport Fountain Pen", "Kaweco", "PW-024"),
        ("Platinum Preppy Fountain Pen", "Platinum", "PW-025"),
        ("Pelikan M200 Fountain Pen", "Pelikan", "PW-026"),
        ("Montblanc Meisterstück Fountain Pen", "Montblanc", "PW-027"),
        ("Faber-Castell Loom Fountain Pen", "Faber-Castell", "PW-028"),
        ("Aurora Ipsilon Fountain Pen", "Aurora", "PW-029"),
        ("Waterman Expert Fountain Pen", "Waterman", "PW-030"),

        # Rollerball Pens 🚀
        ("Uni-Ball Vision Elite Rollerball Pen", "Uni-Ball", "PW-031"),
        ("Parker IM Rollerball Pen", "Parker", "PW-032"),
        ("Cross Bailey Rollerball Pen", "Cross", "PW-033"),
        ("Pilot Precise V7 RT Rollerball Pen", "Pilot", "PW-034"),
        ("Schmidt Liquid Ink Rollerball", "Schmidt", "PW-035"),
        ("TWSBI Precision Rollerball Pen", "TWSBI", "PW-036"),
        ("Faber-Castell Basic Rollerball Pen", "Faber-Castell", "PW-037"),
        ("Pelikan Classic Rollerball Pen", "Pelikan", "PW-038"),
        ("Waterman Hemisphere Rollerball Pen", "Waterman", "PW-039"),
        ("Visconti Rembrandt Rollerball Pen", "Visconti", "PW-040"),

        # Calligraphy & Brush Pens 🎨
        ("Tombow Fudenosuke Brush Pen", "Tombow", "PW-041"),
        ("Pilot Parallel Calligraphy Pen", "Pilot", "PW-042"),
        ("Zebra Mildliner Brush Pen", "Zebra", "PW-043"),
        ("Pentel Arts Pocket Brush Pen", "Pentel", "PW-044"),
        ("Kuretake Zig Calligraphy Pen", "Kuretake", "PW-045"),
        ("Staedtler Calligraphy Pen Set", "Staedtler", "PW-046"),
        ("Sakura Pigma Micron Fineliner", "Sakura", "PW-047"),
        ("Faber-Castell Pitt Artist Pen", "Faber-Castell", "PW-048"),
        ("Winsor & Newton Calligraphy Pen", "Winsor & Newton", "PW-049"),
        ("Speedball Oblique Calligraphy Pen", "Speedball", "PW-050")
    ],

    "art-supplies": [
        # Colored Pencils & Crayons 🖍️
        ("Faber-Castell Polychromos Colored Pencils", "Faber-Castell", "ART-001"),
        ("Prismacolor Premier Colored Pencils", "Prismacolor", "ART-002"),
        ("Caran d'Ache Luminance Colored Pencils", "Caran d'Ache", "ART-003"),
        ("Derwent Coloursoft Pencils", "Derwent", "ART-004"),
        ("Staedtler Ergosoft Colored Pencils", "Staedtler", "ART-005"),
        ("Crayola Colored Pencils", "Crayola", "ART-006"),
        ("Lyra Rembrandt Polycolor Pencils", "Lyra", "ART-007"),
        ("Arteza Professional Colored Pencils", "Arteza", "ART-008"),
        ("Tombow Irojiten Colored Pencils", "Tombow", "ART-009"),
        ("Faber-Castell Albrecht Dürer Watercolor Pencils", "Faber-Castell", "ART-010"),

        # Markers & Pens ✒️
        ("Copic Sketch Markers", "Copic", "ART-011"),
        ("Prismacolor Premier Markers", "Prismacolor", "ART-012"),
        ("Winsor & Newton ProMarkers", "Winsor & Newton", "ART-013"),
        ("Sharpie Permanent Markers", "Sharpie", "ART-014"),
        ("Sakura Pigma Micron Pens", "Sakura", "ART-015"),
        ("Uni Posca Paint Markers", "Uni Posca", "ART-016"),
        ("Tombow Dual Brush Pens", "Tombow", "ART-017"),
        ("Zebra Mildliner Brush Pens", "Zebra", "ART-018"),
        ("Staedtler Triplus Fineliner", "Staedtler", "ART-019"),
        ("Faber-Castell Pitt Artist Pens", "Faber-Castell", "ART-020"),

        # Paints 🎨
        ("Winsor & Newton Watercolors", "Winsor & Newton", "ART-021"),
        ("Daniel Smith Extra Fine Watercolors", "Daniel Smith", "ART-022"),
        ("Holbein Artists' Watercolors", "Holbein", "ART-023"),
        ("Liquitex Professional Acrylic Paints", "Liquitex", "ART-024"),
        ("Golden Heavy Body Acrylic Paints", "Golden", "ART-025"),
        ("Amsterdam Standard Acrylic Paints", "Amsterdam", "ART-026"),
        ("Sennelier Oil Paints", "Sennelier", "ART-027"),
        ("Gamblin Artist Oil Colors", "Gamblin", "ART-028"),
        ("Reeves Gouache Paint Set", "Reeves", "ART-029"),
        ("Daler-Rowney Simply Acrylic Paints", "Daler-Rowney", "ART-030"),

        # Brushes & Palette Knives 🖌️
        ("Princeton Velvetouch Brushes", "Princeton", "ART-031"),
        ("Da Vinci Maestro Series Brushes", "Da Vinci", "ART-032"),
        ("Winsor & Newton Series 7 Brushes", "Winsor & Newton", "ART-033"),
        ("Silver Brush Limited Black Velvet Brushes", "Silver Brush Limited", "ART-034"),
        ("Escoda Versatil Synthetic Brushes", "Escoda", "ART-035"),
        ("Royal & Langnickel Zen Brushes", "Royal & Langnickel", "ART-036"),
        ("Bob Ross Landscape Brush Set", "Bob Ross", "ART-037"),
        ("Liquitex Freestyle Palette Knives", "Liquitex", "ART-038"),
        ("Micheal Harding Palette Knife Set", "Micheal Harding", "ART-039"),
        ("Masterson Sta-Wet Palette", "Masterson", "ART-040"),

        # Sketchbooks & Paper 📜
        ("Strathmore Sketch Pad", "Strathmore", "ART-041"),
        ("Canson XL Mixed Media Pad", "Canson", "ART-042"),
        ("Moleskine Art Sketchbook", "Moleskine", "ART-043"),
        ("Fabriano Artistico Watercolor Paper", "Fabriano", "ART-044"),
        ("Hahnemühle Toned Sketchbook", "Hahnemühle", "ART-045"),
        ("Arches Watercolor Paper Block", "Arches", "ART-046"),
        ("Legion Stonehenge Drawing Paper", "Legion", "ART-047"),
        ("Stillman & Birn Beta Sketchbook", "Stillman & Birn", "ART-048"),
        ("Bee Paper Super Deluxe Sketchbook", "Bee Paper", "ART-049"),
        ("Pentalic Traveler Pocket Journal", "Pentalic", "ART-050")
    ],

    "office-supplies": [
        # Basic Office Essentials 📎🖇️
        ("Stapler HD-10", "Max", "OS-001"),
        ("Swingline Heavy-Duty Stapler", "Swingline", "OS-002"),
        ("Bostitch No-Jam Stapler", "Bostitch", "OS-003"),
        ("Staples Standard Paper Clips", "Staples", "OS-004"),
        ("Binder Clips Assorted Sizes", "Officemate", "OS-005"),
        ("Rubber Bands Multi-Size Pack", "Alliance", "OS-006"),
        ("Push Pins Clear", "U Brands", "OS-007"),
        ("Magnetic Paper Clip Holder", "Officemate", "OS-008"),
        ("Deli Paper Punch", "Deli", "OS-009"),
        ("Fellowes Laminator", "Fellowes", "OS-010"),

        # Sticky Notes & Labels 📝
        ("Post-it Sticky Notes", "3M", "OS-011"),
        ("Post-it Super Sticky Notes", "3M", "OS-012"),
        ("Colored Adhesive Notes", "Officemate", "OS-013"),
        ("White Shipping Labels", "Avery", "OS-014"),
        ("Brother Label Maker", "Brother", "OS-015"),
        ("Dymo LabelWriter", "Dymo", "OS-016"),
        ("Sticky Flags & Page Markers", "3M", "OS-017"),
        ("Epson Label Printer", "Epson", "OS-018"),
        ("Magnetic Dry-Erase Labels", "Quartet", "OS-019"),
        ("Reusable Chalkboard Labels", "Kitchen Supreme", "OS-020"),

        # Writing & Correction Tools ✏️🖊️
        ("Pilot G2 Gel Pens", "Pilot", "OS-021"),
        ("Bic Cristal Ballpoint Pens", "Bic", "OS-022"),
        ("Sharpie Permanent Markers", "Sharpie", "OS-023"),
        ("Uni-Ball Vision Elite Rollerball Pens", "Uni-Ball", "OS-024"),
        ("Mechanical Pencils with Refill", "Pentel", "OS-025"),
        ("Correction Tape", "Tombow", "OS-026"),
        ("Erasable Pens", "Pilot FriXion", "OS-027"),
        ("Expo Dry Erase Markers", "Expo", "OS-028"),
        ("Whiteboard Cleaner Spray", "U Brands", "OS-029"),
        ("Highlighter Set (Multi-Color)", "Staedtler", "OS-030"),

        # Organization & Filing 📁📂
        ("Hanging File Folders", "Pendaflex", "OS-031"),
        ("Expanding File Folder Organizer", "Smead", "OS-032"),
        ("3-Ring Binders", "Avery", "OS-033"),
        ("Sheet Protectors (100-Pack)", "Amazon Basics", "OS-034"),
        ("Business Card Holder", "MaxGear", "OS-035"),
        ("Index Dividers", "Avery", "OS-036"),
        ("Manila File Folders", "Staples", "OS-037"),
        ("Letter Tray Desk Organizer", "SimpleHouseware", "OS-038"),
        ("Binder Clips with Stand", "Amazon Basics", "OS-039"),
        ("Clipboard with Storage", "Saunders", "OS-040"),

        # Miscellaneous Office Tools 🏢
        ("Scotch Transparent Tape Dispenser", "Scotch", "OS-041"),
        ("Double-Sided Tape", "Scotch", "OS-042"),
        ("Heavy-Duty Packing Tape", "Duck Brand", "OS-043"),
        ("Staple Remover", "Swingline", "OS-044"),
        ("Desk Tape Dispenser", "3M", "OS-045"),
        ("USB Desk Fan", "OPOLAR", "OS-046"),
        ("Wireless Keyboard & Mouse Combo", "Logitech", "OS-047"),
        ("Anti-Glare Screen Protector", "Vivo", "OS-048"),
        ("Under-Desk Cable Organizer", "Cable Clips", "OS-049"),
        ("Desk Pad & Mouse Mat", "YSAGi", "OS-050")
    ],

    "calculators": [
        # Scientific Calculators 📖🔬
        ("Casio FX-991EX", "Casio", "CALC-001"),
        ("Texas Instruments TI-36X Pro", "Texas Instruments", "CALC-002"),
        ("HP 35s Scientific Calculator", "HP", "CALC-003"),
        ("Sharp EL-W516T", "Sharp", "CALC-004"),
        ("Canon F-605G", "Canon", "CALC-005"),
        ("Casio FX-115ES PLUS", "Casio", "CALC-006"),
        ("TI-30XS MultiView", "Texas Instruments", "CALC-007"),
        ("HP SmartCalc 300s", "HP", "CALC-008"),
        ("Sharp EL-531TGBBW", "Sharp", "CALC-009"),
        ("Casio FX-300ES PLUS", "Casio", "CALC-010"),

        # Graphing Calculators 📉📈
        ("Texas Instruments TI-84 Plus", "Texas Instruments", "CALC-011"),
        ("Casio FX-CG50", "Casio", "CALC-012"),
        ("HP Prime Graphing Calculator", "HP", "CALC-013"),
        ("TI-Nspire CX II", "Texas Instruments", "CALC-014"),
        ("Casio FX-9750GII", "Casio", "CALC-015"),
        ("Sharp EL-9950", "Sharp", "CALC-016"),
        ("TI-89 Titanium", "Texas Instruments", "CALC-017"),
        ("Casio ClassPad II FX-CP400", "Casio", "CALC-018"),
        ("HP 50g Graphing Calculator", "HP", "CALC-019"),
        ("NumWorks Graphing Calculator", "NumWorks", "CALC-020"),

        # Financial Calculators 💰📊
        ("HP 12C Financial Calculator", "HP", "CALC-021"),
        ("Texas Instruments BA II Plus", "Texas Instruments", "CALC-022"),
        ("Casio FC-200V", "Casio", "CALC-023"),
        ("HP 17BII+ Financial Calculator", "HP", "CALC-024"),
        ("Sharp EL-738C", "Sharp", "CALC-025"),
        ("Canon LS-100TS Business Calculator", "Canon", "CALC-026"),
        ("Victor 6500 Financial Calculator", "Victor", "CALC-027"),
        ("Casio FC-100V", "Casio", "CALC-028"),
        ("HP 10BII+ Financial Calculator", "HP", "CALC-029"),
        ("TI BA II Plus Professional", "Texas Instruments", "CALC-030"),

        # Printing Calculators 🖨️
        ("Casio HR-100TM", "Casio", "CALC-031"),
        ("Sharp EL-1197PIII", "Sharp", "CALC-032"),
        ("Canon P23-DHV-3", "Canon", "CALC-033"),
        ("Victor 1310 Big Print Calculator", "Victor", "CALC-034"),
        ("Sharp EL-1801V", "Sharp", "CALC-035"),
        ("Casio HR-8TM", "Casio", "CALC-036"),
        ("Canon MP11DX", "Canon", "CALC-037"),
        ("Victor 1208-2", "Victor", "CALC-038"),
        ("HP OfficeCalc 200", "HP", "CALC-039"),
        ("Casio DR-270R", "Casio", "CALC-040"),

        # Basic & Pocket Calculators 🏫
        ("Casio SL-300SV", "Casio", "CALC-041"),
        ("Texas Instruments TI-503 SV", "Texas Instruments", "CALC-042"),
        ("Canon LS-82Z", "Canon", "CALC-043"),
        ("Sharp EL-233SB", "Sharp", "CALC-044"),
        ("HP SmartCalc 300s", "HP", "CALC-045"),
        ("Casio HS-8VA", "Casio", "CALC-046"),
        ("Texas Instruments TI-1795SV", "Texas Instruments", "CALC-047"),
        ("Sharp EL-240SAB", "Sharp", "CALC-048"),
        ("Canon TX-220TS", "Canon", "CALC-049"),
        ("Casio HL-820VA", "Casio", "CALC-050")
    ],

    "ehomes": [
        # eReaders 📖
        ("Kindle Paperwhite", "Amazon", "EH-001"),
        ("Kindle Oasis", "Amazon", "EH-002"),
        ("Kindle Scribe", "Amazon", "EH-003"),
        ("Kobo Clara HD", "Kobo", "EH-004"),
        ("Kobo Libra 2", "Kobo", "EH-005"),
        ("Kobo Elipsa", "Kobo", "EH-006"),
        ("Boox Note Air 2", "Boox", "EH-007"),
        ("Boox Nova Air C", "Boox", "EH-008"),
        ("Boox Tab Ultra", "Boox", "EH-009"),
        ("Sony DPT-RP1 Digital Paper", "Sony", "EH-010"),

        # Digital Notebooks & Tablets ✍️
        ("Remarkable 2 Digital Notebook", "Remarkable", "EH-011"),
        ("iPad Air with Apple Pencil", "Apple", "EH-012"),
        ("Samsung Galaxy Tab S9", "Samsung", "EH-013"),
        ("Microsoft Surface Pro 9", "Microsoft", "EH-014"),
        ("Boox Tab X", "Boox", "EH-015"),
        ("Lenovo Yoga Smart Tab", "Lenovo", "EH-016"),
        ("Amazon Fire HD 10", "Amazon", "EH-017"),
        ("Xiaomi Pad 6", "Xiaomi", "EH-018"),
        ("Huawei MatePad Pro", "Huawei", "EH-019"),
        ("Wacom One Drawing Tablet", "Wacom", "EH-020"),

        # Smart Home Hubs 🏡  
        ("Amazon Echo Show 10", "Amazon", "EH-021"),
        ("Amazon Echo Dot (5th Gen)", "Amazon", "EH-022"),
        ("Google Nest Hub Max", "Google", "EH-023"),
        ("Google Nest Mini", "Google", "EH-024"),
        ("Apple HomePod Mini", "Apple", "EH-025"),
        ("Samsung SmartThings Hub", "Samsung", "EH-026"),
        ("Lenovo Smart Clock 2", "Lenovo", "EH-027"),
        ("Sonos One (Smart Speaker)", "Sonos", "EH-028"),
        ("Facebook Portal+", "Meta", "EH-029"),
        ("Xiaomi Smart Speaker IR", "Xiaomi", "EH-030"),

        # Smart Displays & Assistants 📺  
        ("Amazon Fire TV Cube", "Amazon", "EH-031"),
        ("Google Chromecast with Google TV", "Google", "EH-032"),
        ("Roku Ultra", "Roku", "EH-033"),
        ("Apple TV 4K", "Apple", "EH-034"),
        ("Samsung The Frame Smart TV", "Samsung", "EH-035"),
        ("LG OLED evo Smart TV", "LG", "EH-036"),
        ("Sony Bravia XR Smart TV", "Sony", "EH-037"),
        ("Philips Hue Smart Bulbs", "Philips", "EH-038"),
        ("TP-Link Kasa Smart Plug", "TP-Link", "EH-039"),
        ("Nanoleaf Shapes Light Panels", "Nanoleaf", "EH-040"),

        # Home Automation & Security 🏠🔐  
        ("Ring Video Doorbell 4", "Ring", "EH-041"),
        ("Google Nest Doorbell", "Google", "EH-042"),
        ("Arlo Pro 4 Security Camera", "Arlo", "EH-043"),
        ("EufyCam 2C Pro", "Eufy", "EH-044"),
        ("Wyze Cam v3", "Wyze", "EH-045"),
        ("August Wi-Fi Smart Lock", "August", "EH-046"),
        ("Ecovacs Deebot T10 Plus (Robot Vacuum)", "Ecovacs", "EH-047"),
        ("iRobot Roomba j7+", "iRobot", "EH-048"),
        ("TP-Link Deco X20 Mesh WiFi", "TP-Link", "EH-049"),
        ("Amazon Blink Outdoor Camera", "Amazon", "EH-050")
    ]
}

descriptions = {
    "fiction": [
        "A gripping novel that immerses readers in a world of compelling characters, thrilling plot twists, and profound themes.",
        "An inspiring journey of self-discovery, set in a richly imagined world full of heart-pounding adventure.",
        "A timeless classic that delves into the complexities of human nature through memorable characters and vivid storytelling.",
        "A beautifully written tale of love, loss, and resilience that explores the depths of the human spirit.",
        "A fast-paced thriller that keeps readers on the edge of their seat from the first page to the last.",
        "A historical fiction novel that brings to life the past with vivid detail and unforgettable characters.",
        "A contemporary story of friendship and betrayal, set against a backdrop of ever-changing societal norms.",
        "A poetic exploration of the intricacies of human emotion and relationships through deeply personal narratives.",
        "A science fiction epic that stretches the limits of imagination and explores the future of humanity.",
        "A heartwarming and thought-provoking coming-of-age story about finding one's true path in life."
    ],

    "non-fiction": [
        "An insightful examination of contemporary issues, offering thought-provoking perspectives and solutions.",
        "A personal memoir that recounts the author's journey of overcoming obstacles and finding success.",
        "A deep dive into history, uncovering lesser-known facts and stories that shape the world we live in.",
        "A self-help book that provides practical strategies for achieving personal growth and well-being.",
        "A motivational guide that inspires readers to break free from their limitations and realize their full potential.",
        "An exploration of the art of mindfulness and how it can improve our mental and physical health.",
        "A comprehensive look at the science behind human behavior and the psychological factors that influence our decisions.",
        "A political analysis that sheds light on the power dynamics shaping today's global landscape.",
        "An exploration of leadership and the key principles that define great leaders in any field.",
        "A fascinating study of the natural world, detailing the mysteries and wonders of life on Earth."
    ],

    "educational": [
        "A comprehensive guide to mastering fundamental concepts in mathematics, designed for students of all levels.",
        "An essential textbook that introduces core principles of physics, with practical applications and problem-solving exercises.",
        "A deep dive into the world of chemistry, providing clear explanations and engaging activities to reinforce key concepts.",
        "A hands-on approach to learning computer science, with step-by-step tutorials and coding exercises.",
        "A structured overview of economics, offering practical insights into market dynamics and global finance.",
        "An advanced guide to organic chemistry, ideal for students pursuing higher education in the field.",
        "A beginner-friendly textbook that introduces the basics of artificial intelligence and machine learning.",
        "A detailed guide to learning a second language, with helpful tips, exercises, and real-world applications.",
        "An engaging introduction to literature, exploring major literary movements and influential works across the ages.",
        "A guide to mastering critical thinking and problem-solving skills, essential for academic and professional success."
    ],

    "comics": [
        "A superhero epic featuring dynamic action, complex characters, and thought-provoking themes.",
        "A graphic novel that combines humor and heart with stunning illustrations and a powerful message.",
        "An illustrated journey through a fantastical world, filled with magic, mystery, and adventure.",
        "A dark and gritty noir detective story, told through striking visuals and intense, atmospheric storytelling.",
        "A coming-of-age story set in a world of superheroes, exploring the challenges of growing up with extraordinary powers.",
        "A classic comic series that blends science fiction, political intrigue, and emotional depth.",
        "A satirical comic that takes on the absurdities of modern life, offering both humor and social commentary.",
        "A heroic saga set in a dystopian future, where the fate of the world rests on the shoulders of a few brave individuals.",
        "An action-packed adventure that combines epic battles with moments of heartfelt emotion and character development.",
        "A visually stunning graphic novel that explores the themes of identity, belonging, and personal growth."
    ],

    "notebooks-diaries": [
        "A beautifully crafted leather notebook, perfect for jotting down your thoughts, ideas, and daily musings.",
        "A stylish and functional planner that helps you stay organized and productive throughout the year.",
        "A luxurious diary with thick, acid-free paper that offers a smooth writing experience for all your creative endeavors.",
        "A minimalist journal designed for simplicity and elegance, ideal for sketching, writing, or planning.",
        "A practical and durable notebook, featuring a flexible cover and premium paper that can withstand daily use.",
        "A vibrant, colorful diary that makes writing a fun and inspiring experience, with motivational quotes on every page.",
        "A travel-sized notebook designed for on-the-go note-taking, with a compact size that fits easily in your bag or pocket.",
        "A functional bullet journal with dotted pages, perfect for organizing tasks, goals, and creative ideas.",
        "An eco-friendly journal made from recycled materials, offering a sustainable option for your writing needs.",
        "A hardcover notebook with a sleek design, featuring thick pages that are perfect for both writing and sketching."
    ],

    "pens-writing": [
        "A smooth-flowing ballpoint pen that offers a comfortable writing experience, ideal for everyday use.",
        "An elegant fountain pen with a classic design, providing a sophisticated writing experience with each stroke.",
        "A high-quality gel pen that glides effortlessly across the page, delivering bold, vibrant lines.",
        "A precision rollerball pen, designed for fine detail and consistent ink flow, perfect for professional use.",
        "An erasable pen that lets you write and revise easily, making it ideal for note-taking and drafting.",
        "A premium pen set that combines luxury and performance, perfect for gift-giving or personal use.",
        "A multi-purpose pen with built-in highlighter and stylus, perfect for multitasking in the office or classroom.",
        "A retractable pen with a sleek metal body, offering both style and durability for everyday writing.",
        "An eco-friendly pen made from recycled materials, combining sustainability with smooth performance.",
        "A colorful set of gel pens that adds fun and creativity to your notes, sketches, and designs."
    ],

    "art-supplies": [
        "A professional set of watercolor paints, offering a wide range of vibrant colors for both beginners and experts.",
        "A high-quality sketching pencil set, featuring various grades for all your drawing needs.",
        "An artist-grade acrylic paint set that provides rich, pigmented colors for canvas and mixed-media projects.",
        "A complete calligraphy kit with pens, nibs, and ink, perfect for learning and practicing the art of beautiful writing.",
        "A durable set of colored pencils, ideal for adding intricate details and vibrant hues to your artwork.",
        "A set of fine-tip markers that deliver precise lines and vibrant colors for detailed illustrations and designs.",
        "A heavy-duty easel that provides stability and versatility for artists working on large-scale projects.",
        "A professional-grade set of pastels, perfect for blending and creating expressive textures in your artwork.",
        "A high-quality sketchbook with thick, acid-free paper that can handle various art mediums.",
        "A set of oil paints with a rich selection of colors, perfect for creating beautiful landscapes, portraits, and still lifes."
    ],

    "office-supplies": [
        "A sturdy, heavy-duty stapler designed for high-volume use, with a comfortable grip for easy operation.",
        "A set of premium sticky notes in various sizes and colors, perfect for reminders and organization.",
        "An ergonomic office chair designed for maximum comfort and support during long work hours.",
        "A set of high-quality file folders for organizing and storing important documents and paperwork.",
        "A reliable paper shredder that ensures the security and confidentiality of your sensitive documents.",
        "A convenient desk organizer with compartments for pens, paper, and office essentials.",
        "A durable whiteboard with a smooth surface for easy writing and erasing, perfect for meetings and brainstorming sessions.",
        "A pack of colorful binders that keep your documents neat and organized in style.",
        "A multifunctional printer that offers high-quality printing, scanning, and copying capabilities.",
        "A sleek, wireless mouse and keyboard set designed for productivity and comfort in the office or home workspace."
    ],

    "calculators": [
        "A scientific calculator with advanced functions, perfect for students and professionals in math and science fields.",
        "A graphing calculator with a large display, ideal for plotting graphs and solving complex equations.",
        "A financial calculator designed for business and accounting professionals, with built-in functions for financial analysis.",
        "A simple, reliable basic calculator that provides accurate calculations for everyday use.",
        "A solar-powered calculator that never runs out of battery, making it a convenient choice for students and professionals.",
        "A multi-line scientific calculator with an intuitive interface and easy-to-read display.",
        "An engineering calculator with specialized functions for electrical, mechanical, and civil engineering tasks.",
        "A portable calculator with a sleek design, perfect for on-the-go use in the office or classroom.",
        "A large-display calculator that is easy to read, ideal for seniors or those with visual impairments.",
        "A programmable calculator that allows you to store and execute custom functions for advanced problem-solving."
    ],

    "ehomes": [
        "An Amazon Kindle with a crisp, high-resolution display, perfect for reading books, magazines, and more.",
        "A sleek digital notebook for jotting down your ideas and notes, with cloud synchronization for easy access across devices.",
        "A premium e-reader that supports multiple file formats, offering a versatile and enjoyable reading experience.",
        "A smart home assistant device that integrates with your home to provide voice-controlled services and entertainment.",
        "A high-definition tablet designed for reading eBooks, browsing, and media consumption, all in one portable device.",
        "A versatile smart notebook that syncs with your devices, making it easy to store and organize your notes digitally.",
        "A digital drawing tablet that offers precise control for artists and designers, with a variety of brushes and tools.",
        "A smart speaker with exceptional sound quality and built-in voice assistants for managing tasks hands-free.",
        "A portable digital recorder for capturing your ideas, lectures, or meetings, with excellent audio quality and easy sharing.",
        "A compact smart display that provides visual and voice-controlled access to a variety of apps and services."
    ]
}


features = {
        "Fiction": {
            "Plot": ["Gripping storylines", "Unexpected twists", "Complex characters", "Rich world-building", "Suspenseful pacing"],
            "Writing Style": ["Evocative prose", "Vivid descriptions", "Emotional depth", "Engaging dialogue", "Unique voice"],
            "Themes": ["Love, betrayal, and sacrifice", "Moral dilemmas", "Existential questions", "Hope and despair", "Human nature"],
            "Genre": ["Fantasy", "Mystery", "Historical fiction", "Romance", "Science fiction"],
            "Pacing": ["Fast-paced", "Slow burn", "Action-packed", "Character-driven", "Plot-driven"]
        },
        "Non-fiction": {
            "Content": ["Well-researched", "Fact-driven", "Evidence-backed", "Personal anecdotes", "Real-world examples"],
            "Writing Style": ["Clear and concise", "Accessible language", "In-depth analysis", "Engaging storytelling", "Thought-provoking"],
            "Subjects": ["Biography", "Self-help", "Science", "Philosophy", "Politics"],
            "Tone": ["Objective", "Personal", "Informative", "Inspirational", "Motivational"],
            "Audience": ["General readers", "Scholars", "Professionals", "Students", "Researchers"]
        },
        "Educational": {
            "Content": ["Comprehensive coverage", "Step-by-step explanations", "Clear examples", "Interactive exercises", "Visual aids"],
            "Subjects": ["Math", "Science", "History", "Geography", "Language arts"],
            "Pacing": ["Beginner level", "Intermediate level", "Advanced level", "Self-paced learning", "Classroom support"],
            "Format": ["Textbook-style", "Workbook", "Online resource", "Guided learning", "Practice tests"],
            "Audience": ["K-12 students", "University students", "Teachers", "Lifelong learners", "Homeschoolers"]
        },
        "Comics": {
            "Artwork": ["Vibrant illustrations", "High-quality print", "Dynamic action scenes", "Detailed backgrounds", "Stylized characters"],
            "Storytelling": ["Engaging plots", "Humor and wit", "Clever dialogue", "Superhero themes", "Fantasy settings"],
            "Genres": ["Superhero", "Fantasy", "Manga", "Graphic novels", "Science fiction"],
            "Target Audience": ["Teens", "Adults", "Children", "Collectors", "Pop culture enthusiasts"],
            "Series": ["Standalone issues", "Mini-series", "Graphic novels", "Ongoing series", "Limited editions"]
        },
        "Notebooks-Diaries": {
            "Cover": ["Leather-bound", "Hardcover", "Softcover", "Eco-friendly material", "Customizable"],
            "Pages": ["Acid-free", "Smooth texture", "Dotted lines", "Blank pages", "Grid pages"],
            "Features": ["Elastic closure", "Pen loop", "Bookmark ribbon", "Pocket at the back", "Durable binding"],
            "Size": ["A4", "A5", "Pocket-sized", "Travel-size", "Personalized size"],
            "Usage": ["Journaling", "Sketching", "Note-taking", "Bullet journaling", "Project planning"]
        },
        "Pens-Writing": {
            "Ink": ["Gel ink", "Ballpoint", "Fountain pen ink", "Quick-drying", "Smudge-resistant"],
            "Design": ["Ergonomic grip", "Sleek body", "Refillable", "Clip-on", "Comfortable writing experience"],
            "Tip Size": ["Fine", "Medium", "Bold", "Extra fine", "Broad"],
            "Color Options": ["Black", "Blue", "Red", "Multicolor", "Custom ink options"],
            "Use Case": ["Writing", "Drawing", "Signing", "Calligraphy", "Everyday use"]
        },
        "Art-Supplies": {
            "Materials": ["High-pigment paints", "Non-toxic markers", "Quality sketchbooks", "Charcoal", "Pastels"],
            "Tools": ["Brushes", "Pencils", "Canvas", "Palette knives", "Stencils"],
            "Surface": ["Canvas", "Watercolor paper", "Acrylic sheets", "Wooden boards", "Textured paper"],
            "Techniques": ["Oil painting", "Watercolor painting", "Sketching", "Calligraphy", "Mixed media"],
            "Brands": ["Winsor & Newton", "Faber-Castell", "Prismacolor", "Sennelier", "Arteza"]
        },
        "Office-Supplies": {
            "Stationery": ["Notepads", "Sticky notes", "Paper clips", "Staplers", "Folders"],
            "Storage": ["Drawer organizers", "File cabinets", "Binders", "Desktop organizers", "Storage boxes"],
            "Technology": ["Printers", "Label makers", "Scanners", "Shredders", "Projectors"],
            "Writing Instruments": ["Pens", "Highlighters", "Markers", "Whiteboard pens", "Pencils"],
            "Office Decor": ["Desk lamps", "Wall clocks", "Calendars", "Bulletin boards", "Photo frames"]
        },
        "Calculators": {
            "Types": ["Scientific", "Graphing", "Financial", "Basic", "Printing"],
            "Display": ["Large screen", "Color display", "Multi-line display", "Touchscreen", "Backlit display"],
            "Power": ["Solar-powered", "Battery-operated", "Dual power", "Rechargeable", "Manual"],
            "Functions": ["Advanced calculations", "Graph plotting", "Currency conversion", "Scientific functions", "Equation solving"],
            "Use Case": ["Students", "Professionals", "Engineers", "Mathematicians", "Accountants"]
        },
        "Ehomes": {
            "Features": ["Smart home connectivity", "Voice control", "Mobile app integration", "Remote monitoring", "Energy-efficient"],
            "Design": ["Compact", "Sleek", "User-friendly", "High-resolution", "Stylish"],
            "Functionality": ["Security cameras", "Smart speakers", "Smart thermostats", "Automated lighting", "Smart locks"],
            "Compatibility": ["Alexa", "Google Assistant", "Apple HomeKit", "IFTTT", "Z-Wave"],
            "Installation": ["Easy setup", "Wireless setup", "Plug-and-play", "DIY installation", "Professional installation available"],
            "Control": ["Mobile app", "Voice commands", "Touchscreen interface", "Remote control", "Automation"]
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
