from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    user_data = {
        "name": "Md Rakibul Hasan Naym",
        "designation": "Head of Artificial Intelligence",
        "company": "HawkEyes Digital Monitoring Ltd",
        "bio": "AI Engineer with expertise in asynchronous programming, image processing, NLP, and deep learning. Passionate about optimizing AI systems for high performance and scalability.",
        "profile_image": "/static/images/profile_3.jpeg",
        "contact": {
            "email": "naym.mj@gmail.com",
            "linkedin": "https://www.linkedin.com/in/md-rakibul-hasan-naym-625263229/",
            "github": "https://github.com/RH-NAYM",
            "huggingface": "https://huggingface.co/rakib72642",
            "twitter": "https://twitter.com/rakib72642",
            "website": "https://rakibnaym.com"
        },
        "skills": [
            "Python", "FastAPI", "Django", "AI & Machine Learning", "Deep Learning", "Computer Vision", "NLP", "Asynchronous Programming", "GPU Acceleration"
        ],
        "projects": [
            {
                "title": "Moiré Pattern Detection",
                "description": "Detecting Moiré patterns in facial images using advanced image processing techniques.",
                "image": "/static/images/miorie_pattern.png",
                "link": "https://github.com/RH-NAYM/morie-pattern-detection"
            },
            {
                "title": "Text Data Cleaning",
                "description": "Processing text data to remove specific phrases using regex and Python.",
                "image": "/static/images/data_cleaning.png",
                "link": "https://github.com/RH-NAYM/text-cleaning"
            },
            {
                "title": "Object Detection Pipeline",
                "description": "Detect and crop objects from images using YOLO models.",
                "image": "/static/images/object_detection.jpg",
                "link": "https://github.com/RH-NAYM/object-detection"
            },
            {
                "title": "Django AI Server",
                "description": "AI server with YOLO models, object detection, and optimized multitasking.",
                "image": "/static/images/django_ai.png",
                "link": "https://github.com/RH-NAYM/django-ai-server"
            },
            {
                "title": "FastAPI Portfolio",
                "description": "A beautifully designed portfolio using FastAPI and Jinja2 templates.",
                "image": "/static/images/portfolio.jpg",
                "link": "https://github.com/RH-NAYM/fastapi-portfolio"
            }
        ],
        "testimonials": [
            {"name": "John Doe", "feedback": "Rakibul is an exceptional AI engineer with deep expertise in computer vision and NLP!"},
            {"name": "Jane Smith", "feedback": "Working with Rakibul was amazing. His knowledge of FastAPI and AI optimization is top-notch!"}
        ],
        "certifications": [
            "Deep Learning Specialization - Coursera",
            "FastAPI Mastery - Udemy",
            "Computer Vision Expert - OpenCV AI"
        ]
    }
    return templates.TemplateResponse("index.html", {"request": request, **user_data})

# Directory Structure
# - main.py
# - templates/
#    - index.html
# - static/
#    - style.css
#    - images/
#       - profile.jpg
#       - miorie_pattern.png
#       - data_cleaning.png
#       - object_detection.jpg
#       - django_ai.png
#       - portfolio.jpg
