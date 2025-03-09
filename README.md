give me all the files by updating <link rel="stylesheet" href="/static/css/style.css">

templates/about.hmtl
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ about.name }} | AI Engineer Portfolio</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <nav>
            <div class="container">
                <a href="/" class="logo">AI Engineer Portfolio</a>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/skills">Skills</a></li>
                    <li><a href="/projects">Projects</a></li>
                    <li><a href="/experience">Experience</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </div>
        </nav>
    </header>
    
    <section class="about">
        <div class="container">
            <div class="profile">
                <img src="{{ about.profile_image }}" alt="{{ about.name }}">
                <h1>{{ about.name }}</h1>
                <h2>{{ about.title }}</h2>
                <p>{{ about.summary }}</p>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2025 AI Engineer Portfolio | All Rights Reserved</p>
        </div>
    </footer>
</body>
</html>





templates/base.html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="AI Engineer Portfolio showcasing skills, projects, and experience.">
    <meta name="author" content="AI Engineer">
    
    <!-- Open Graph Meta Tags for Social Media Integration -->
    <meta property="og:title" content="AI Engineer Portfolio">
    <meta property="og:description" content="AI Engineer Portfolio showcasing skills, projects, and experience.">
    <meta property="og:image" content="/static/images/portfolio-image.jpg"> <!-- Replace with your portfolio image -->
    <meta property="og:url" content="https://www.yourportfolio.com">
    
    <!-- Twitter Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@yourusername">
    <meta name="twitter:title" content="AI Engineer Portfolio">
    <meta name="twitter:description" content="AI Engineer Portfolio showcasing skills, projects, and experience.">
    <meta name="twitter:image" content="/static/images/portfolio-image.jpg"> <!-- Replace with your image -->

    <!-- Page Title -->
    <title>{% block title %}AI Engineer Portfolio{% endblock %}</title>
    
    <!-- Google Font (Roboto) -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    
    <!-- Link to Custom CSS -->
    <link rel="stylesheet" href="/static/css/style.css">
    
    <!-- AOS (Animate on Scroll) CSS -->
    <link rel="stylesheet" href="https://unpkg.com/aos@2.3.1/dist/aos.css">
    
    <!-- Optional Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-XXXXXXXXX-X"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'UA-XXXXXXXXX-X'); // Replace with your own Google Analytics ID
    </script>
</head>

<body>
    <header>
        <nav>
            <a href="/">About</a>
            <a href="/skills">Skills</a>
            <a href="/projects">Projects</a>
            <a href="/experience">Experience</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>

    <main class="content">
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>&copy; {{ about.name if about is defined else 'AI Engineer Portfolio' }}</p>
    </footer>

    <!-- AOS JS for Scroll Animations -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({
            duration: 1200, // Duration for the animation
            easing: 'ease-in-out', // Easing function for animation
            once: true // Ensures the animation only happens once
        });
    </script>
</body>




templates/contract.html
{% extends "base.html" %}


{% block content %}
    <section class="contact-section" data-aos="fade-up">
        <h1>Contact</h1>
        <div class="contact-details">
            <p><strong>Email:</strong> <a href="mailto:{{ contact.email }}">{{ contact.email }}</a></p>
            
            {% if contact.linkedin %}
                <p><strong>LinkedIn:</strong> 
                    <a href="{{ contact.linkedin }}" target="_blank">
                        <i class="fab fa-linkedin"></i> LinkedIn Profile
                    </a>
                </p>
            {% endif %}
            
            {% if contact.github %}
                <p><strong>GitHub:</strong> 
                    <a href="{{ contact.github }}" target="_blank">
                        <i class="fab fa-github"></i> GitHub Profile
                    </a>
                </p>
            {% endif %}
            
            {% if contact.website %}
                <p><strong>Website:</strong> 
                    <a href="{{ contact.website }}" target="_blank">
                        <i class="fas fa-globe"></i> Visit Website
                    </a>
                </p>
            {% endif %}
        </div>
    </section>
{% endblock %}



templates/experience.html
{% extends "base.html" %}

{% block content %}
    <section class="experience-section" data-aos="fade-up">
        <h1>Experience</h1>
        <div class="experience-list">
            {% for exp in experience %}
                <div class="experience-item" data-aos="zoom-in">
                    <h2>{{ exp.position }} at {{ exp.company }}</h2>
                    <p><strong>Duration:</strong> {{ exp.start_date }} - {{ exp.end_date or "Present" }}</p>
                    <p><strong>Description:</strong> {{ exp.description }}</p>
                    <p><strong>Technologies:</strong> {{ ", ".join(exp.technologies) }}</p>
                </div>
            {% endfor %}
        </div>
    </section>
{% endblock %}




templates/projects.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projects | AI Engineer Portfolio</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <nav>
            <div class="container">
                <a href="/" class="logo">AI Engineer Portfolio</a>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/skills">Skills</a></li>
                    <li><a href="/projects">Projects</a></li>
                    <li><a href="/experience">Experience</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </div>
        </nav>
    </header>

    <section class="projects">
        <div class="container">
            <h1>Projects</h1>
            <div class="projects-grid">
                {% for project in projects %}
                <div class="project-card">
                    <img src="{{ project.image }}" alt="{{ project.title }}">
                    <h3>{{ project.title }}</h3>
                    <p>{{ project.description }}</p>
                    <a href="{{ project.github_url }}" target="_blank">View on GitHub</a>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2025 AI Engineer Portfolio | All Rights Reserved</p>
        </div>
    </footer>
</body>
</html>




templates/skills.html
{% extends "base.html" %}

{% block content %}
    <section class="skills-section" data-aos="fade-up">
        <h1>Skills</h1>
        <ul class="skills-list">
            {% for skill in skills %}
                <li data-aos="zoom-in">
                    <strong>{{ skill.name }}:</strong> {{ skill.proficiency }}
                </li>
            {% endfor %}
        </ul>
    </section>
{% endblock %}

