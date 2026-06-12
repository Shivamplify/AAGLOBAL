"""Seed script: create admin + demo articles non-interactively."""
import os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from app import create_app
from app.extensions import db
from app.models import Admin, Category, Article, Tag
from app.utils import slugify, reading_time
from datetime import datetime, timedelta, UTC

app = create_app()

with app.app_context():
    # Create admin if not exists
    admin = Admin.query.first()
    if not admin:
        admin = Admin(email="admin@axisandatoms.com", name="Editor")
        admin.set_password("admin1234")
        db.session.add(admin)
        db.session.commit()
        print(f"Created admin: admin@axisandatoms.com / admin1234")
    else:
        print(f"Admin already exists: {admin.email}")

    # Ensure categories
    cat_names = {
        "Science": "Discoveries that reshape what we know",
        "Technology": "Innovation at the speed of thought",
        "Space": "Beyond the atmosphere, into the cosmos",
        "Health": "Body, mind, and the science in between",
        "Environment": "Earth systems, climate, and conservation",
    }
    cats = {}
    for name, desc in cat_names.items():
        cat = Category.query.filter_by(slug=slugify(name)).first()
        if not cat:
            cat = Category(name=name, slug=slugify(name), description=desc)
            db.session.add(cat)
            db.session.flush()
        cats[name] = cat
    db.session.commit()

    # Demo articles
    articles_data = [
        {
            "title": "CRISPR 3.0: Gene Editing Enters the Precision Era",
            "excerpt": "A new generation of CRISPR tools can rewrite DNA with single-letter accuracy — opening doors to cures once considered impossible.",
            "content": "<p>The third generation of CRISPR technology represents a quantum leap in precision medicine. Unlike its predecessors, CRISPR 3.0 can make edits at the single-nucleotide level without introducing double-strand breaks in DNA.</p><h2>How It Works</h2><p>Traditional CRISPR-Cas9 acts like molecular scissors, cutting DNA at specific locations. CRISPR 3.0, however, uses base editors and prime editors that chemically convert one DNA letter to another, or insert and delete sequences with surgical precision.</p><p>Researchers at the Broad Institute have demonstrated that prime editing can correct up to 89% of known pathogenic human genetic variants. This includes the mutations responsible for sickle cell disease, cystic fibrosis, and Tay-Sachs disease.</p><h2>Clinical Trials</h2><p>Phase I trials are already underway for several conditions. Early results show remarkable efficacy with minimal off-target effects — a persistent concern with earlier CRISPR approaches.</p><blockquote>We're not just editing genes anymore. We're rewriting the source code of life with spell-check turned on. — Dr. David Liu, Broad Institute</blockquote><p>The implications extend beyond medicine. Agricultural applications could yield drought-resistant crops, while environmental scientists envision gene drives that could help combat invasive species.</p>",
            "category": "Science",
            "is_featured": True,
            "is_trending": True,
            "tags": ["CRISPR", "Genetics", "Medicine"],
        },
        {
            "title": "Quantum Computers Just Solved a Problem That Would Take Classical Machines 10,000 Years",
            "excerpt": "Google's latest quantum processor achieves computational supremacy on a real-world optimization problem for the first time.",
            "content": "<p>In a landmark demonstration of practical quantum advantage, Google's Willow quantum processor has solved a complex molecular simulation in under four minutes — a task estimated to take the world's fastest classical supercomputer approximately 10,000 years.</p><h2>The Breakthrough</h2><p>The computation involved simulating the behavior of a lithium-ion battery electrolyte at the quantum mechanical level. Understanding these interactions is crucial for developing next-generation batteries with higher energy density and longer lifespan.</p><p>Willow uses 1,121 superconducting qubits arranged in a novel error-correction topology that dramatically reduces decoherence — the nemesis of quantum computation.</p><h2>What This Means</h2><p>While previous quantum supremacy claims involved artificial benchmark problems, this result addresses a real engineering challenge. Battery manufacturers have already expressed interest in licensing the simulation data.</p><p>The achievement also validates the approach of scaling quantum processors through better error correction rather than simply adding more qubits.</p>",
            "category": "Technology",
            "is_featured": True,
            "is_trending": False,
            "tags": ["Quantum Computing", "Google", "Physics"],
        },
        {
            "title": "NASA's DRAGONFLY Mission: Exploring Titan's Methane Seas",
            "excerpt": "The rotorcraft lander will touch down on Saturn's largest moon in 2034, searching for prebiotic chemistry in an alien ocean world.",
            "content": "<p>NASA's Dragonfly mission represents the most ambitious planetary exploration endeavor since the Mars rovers. The nuclear-powered rotorcraft will fly through Titan's thick nitrogen atmosphere, hopping between dozens of sites across the moon's surface.</p><h2>Why Titan?</h2><p>Saturn's largest moon is the only body in our solar system besides Earth with stable liquid on its surface. But instead of water, Titan's lakes and seas are filled with liquid methane and ethane. Beneath its icy crust lies a subsurface ocean of water.</p><p>This makes Titan a natural laboratory for studying prebiotic chemistry — the complex organic reactions that may have preceded the origin of life on Earth billions of years ago.</p><h2>The Technology</h2><p>Dragonfly is an octocopter — a dual-quadcopter design that provides redundancy. It will be powered by a Multi-Mission Radioisotope Thermoelectric Generator (MMRTG), the same type of power source used by the Curiosity and Perseverance Mars rovers.</p><p>Each flight will cover roughly 8 kilometers, with the craft spending most of its time on the surface conducting science experiments between hops.</p>",
            "category": "Space",
            "is_featured": False,
            "is_trending": True,
            "tags": ["NASA", "Titan", "Space Exploration"],
        },
        {
            "title": "The Gut-Brain Highway: How Microbiome Science Is Revolutionizing Mental Health",
            "excerpt": "New research reveals that the bacteria in your gut may influence everything from anxiety to memory — and treatment is closer than you think.",
            "content": "<p>The human gut contains approximately 39 trillion microorganisms — more than the total number of human cells in the body. Collectively known as the gut microbiome, these bacteria, fungi, and viruses are increasingly recognized as a second brain.</p><h2>The Vagus Nerve Connection</h2><p>The gut communicates with the brain through the vagus nerve, a superhighway of neural signals. Research has shown that certain gut bacteria produce neurotransmitters like serotonin, dopamine, and GABA — chemicals traditionally associated with brain function.</p><p>In fact, approximately 95% of the body's serotonin is produced in the gut, not the brain. This finding has profound implications for understanding and treating depression.</p><h2>Psychobiotics</h2><p>A new class of treatments called psychobiotics — probiotics specifically designed to influence brain function — are showing promise in clinical trials. Early results suggest they may be effective for reducing anxiety, improving sleep quality, and enhancing cognitive performance.</p><blockquote>The microbiome is the organ we forgot we had. Now it's telling us things we never expected to hear. — Dr. John Cryan, University College Cork</blockquote>",
            "category": "Health",
            "is_featured": False,
            "is_trending": True,
            "tags": ["Microbiome", "Mental Health", "Neuroscience"],
        },
        {
            "title": "Carbon Capture Gets a Boost: New Material Absorbs CO₂ 100x Faster Than Trees",
            "excerpt": "Engineers at MIT unveil a porous polymer that could make direct air capture economically viable for the first time.",
            "content": "<p>A team of chemical engineers at MIT has developed a novel porous polymer material that can absorb carbon dioxide from ambient air approximately 100 times more efficiently than natural photosynthesis in trees.</p><h2>The Material</h2><p>The polymer, dubbed 'CarbonSponge,' uses a hierarchical pore structure inspired by the alveoli in human lungs. When air passes through the material, CO₂ molecules are selectively captured through a chemical reaction with amine groups embedded in the polymer matrix.</p><p>What sets CarbonSponge apart from existing direct air capture (DAC) technologies is its remarkably low energy requirement for regeneration. The captured CO₂ can be released by heating the material to just 85°C — compared to 900°C for conventional calcium-based approaches.</p><h2>Scale and Economics</h2><p>Current DAC technologies cost between $400–600 per ton of CO₂ removed. The MIT team estimates that CarbonSponge could reduce this to under $100 per ton at scale — a threshold widely considered necessary for DAC to become economically competitive.</p><p>A pilot plant using the technology is expected to begin operations in 2027, with the capacity to remove 1,000 tons of CO₂ per year.</p>",
            "category": "Environment",
            "is_featured": True,
            "is_trending": False,
            "tags": ["Climate", "Carbon Capture", "Engineering"],
        },
        {
            "title": "The Race to Map Every Neuron: Brain Connectomics Enters Its Golden Age",
            "excerpt": "After mapping the fruit fly's brain, scientists set their sights on the mouse — and eventually the human connectome.",
            "content": "<p>In 2024, researchers completed the first full connectome of an adult fruit fly brain — mapping all 139,255 neurons and their 54.5 million synaptic connections. Now, the field of connectomics is scaling up dramatically.</p><h2>From Flies to Mice</h2><p>The Allen Institute for Brain Science has launched a $500 million initiative to map the complete mouse brain connectome. At roughly 70 million neurons, it represents a 500-fold increase in complexity over the fruit fly.</p><p>The project relies on serial electron microscopy, slicing preserved brain tissue into 30-nanometer sections and imaging each one. The resulting dataset is expected to exceed 2 exabytes — roughly equivalent to all the data generated by CERN's Large Hadron Collider over its entire operational history.</p><h2>AI-Powered Analysis</h2><p>Machine learning algorithms are essential for tracing neural pathways through the massive image stacks. Google DeepMind has developed specialized neural network architectures that can automatically identify and classify synaptic connections with 97% accuracy.</p><p>Understanding the complete wiring diagram of a brain could revolutionize our understanding of consciousness, learning, and neurological diseases.</p>",
            "category": "Science",
            "is_featured": False,
            "is_trending": False,
            "tags": ["Neuroscience", "AI", "Brain"],
        },
        {
            "title": "Solid-State Batteries Are Finally Here — And They Change Everything",
            "excerpt": "Toyota announces mass production of solid-state batteries for EVs by 2028, promising 1,200 km range and 10-minute charging.",
            "content": "<p>After decades of research, solid-state batteries are transitioning from laboratory curiosities to commercial reality. Toyota has announced that it will begin mass production of solid-state batteries for its electric vehicles by 2028.</p><h2>The Advantages</h2><p>Solid-state batteries replace the liquid electrolyte found in conventional lithium-ion cells with a solid ceramic or polymer material. This change offers several transformative advantages:</p><p><strong>Energy Density:</strong> Solid-state cells can achieve energy densities of 500 Wh/kg — roughly double that of current lithium-ion batteries. This translates to EVs with ranges exceeding 1,200 km on a single charge.</p><p><strong>Charging Speed:</strong> Without the risk of dendrite formation that plagues liquid electrolytes, solid-state batteries can be charged at much higher rates. Toyota claims an 80% charge in under 10 minutes.</p><p><strong>Safety:</strong> Eliminating flammable liquid electrolytes dramatically reduces the risk of thermal runaway and fires.</p><h2>Remaining Challenges</h2><p>Manufacturing costs remain the primary barrier. Current solid-state cells cost approximately 3–5 times more to produce than equivalent lithium-ion cells. Toyota expects costs to reach parity by 2030 through economies of scale.</p>",
            "category": "Technology",
            "is_featured": False,
            "is_trending": True,
            "tags": ["Batteries", "EV", "Toyota"],
        },
        {
            "title": "Deep Ocean Mining: Promise and Peril on the Seafloor",
            "excerpt": "As demand for rare earth minerals surges, companies eye the deep ocean floor — but marine biologists warn of irreversible damage.",
            "content": "<p>Miles beneath the ocean surface, scattered across vast abyssal plains, lie trillions of potato-sized mineral nodules containing manganese, nickel, cobalt, and rare earth elements. These polymetallic nodules have become the center of a heated debate about the future of mining.</p><h2>The Case For</h2><p>The global transition to clean energy requires enormous quantities of critical minerals. A single electric vehicle battery contains roughly 8 kg of lithium, 35 kg of nickel, and 14 kg of cobalt. Current terrestrial mining operations cannot keep pace with projected demand.</p><p>Deep-sea nodules contain these minerals in concentrations far higher than most land-based deposits, and harvesting them avoids the deforestation, water pollution, and human rights concerns associated with traditional mining.</p><h2>The Case Against</h2><p>Marine biologists warn that the abyssal plains, long considered biological deserts, are actually home to complex ecosystems. Many species found near nodule fields are entirely new to science. Mining operations would destroy these habitats, which may take millions of years to recover.</p><blockquote>We are talking about industrializing the last pristine wilderness on Earth before we even understand what lives there. — Dr. Diva Amon, Marine Biologist</blockquote>",
            "category": "Environment",
            "is_featured": False,
            "is_trending": False,
            "tags": ["Ocean", "Mining", "Conservation"],
        },
    ]

    for i, data in enumerate(articles_data):
        slug = slugify(data["title"])
        if Article.query.filter_by(slug=slug).first():
            print(f"  Skipping (exists): {data['title'][:50]}...")
            continue
        
        cat = cats.get(data["category"])
        
        # Create tags
        tag_objs = []
        for tag_name in data.get("tags", []):
            tag_slug = slugify(tag_name)
            tag = Tag.query.filter_by(slug=tag_slug).first()
            if not tag:
                tag = Tag(name=tag_name, slug=tag_slug)
                db.session.add(tag)
                db.session.flush()
            tag_objs.append(tag)
        
        pub_date = datetime.now(UTC).replace(tzinfo=None) - timedelta(hours=i * 6)
        article = Article(
            title=data["title"],
            slug=slug,
            excerpt=data["excerpt"],
            content=data["content"],
            reading_minutes=reading_time(data["content"]),
            status="published",
            is_featured=data.get("is_featured", False),
            is_trending=data.get("is_trending", False),
            category_id=cat.id if cat else None,
            author_id=admin.id,
            published_at=pub_date,
            seo_title=data["title"],
            seo_description=data["excerpt"],
        )
        article.tags = tag_objs
        db.session.add(article)
        print(f"  Added: {data['title'][:60]}...")

    db.session.commit()
    print("\nDone! Demo content seeded.")
    print(f"Admin login: admin@axisandatoms.com / admin1234")
    print(f"Site: http://127.0.0.1:5000")
