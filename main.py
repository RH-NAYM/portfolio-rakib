from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="AI Engineer Portfolio API", description="API for showcasing AI Engineer's portfolio.")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Skill(BaseModel):
    name: str
    proficiency: str

class Project(BaseModel):
    title: str
    description: str
    technologies: List[str]
    github_url: Optional[str] = None
    demo_url: Optional[str] = None
    image: Optional[str] = None  # Added image field

class Experience(BaseModel):
    company: str
    position: str
    start_date: str
    end_date: Optional[str] = None
    description: str
    technologies: List[str]

class Contact(BaseModel):
    email: str
    linkedin: Optional[str] = None
    github: Optional[str] = None
    website: Optional[str] = None

class About(BaseModel):
    name: str
    title: str
    summary: str
    profile_image: Optional[str] = None  # Added profile image

# Data (Replace with your own data!)
skills = [
    # Programming Languages
    Skill(name="Python", proficiency="Expert"),
    Skill(name="JavaScript", proficiency="Intermediate"),
    Skill(name="C++", proficiency="Intermediate"),

    # Web Frameworks
    Skill(name="Django", proficiency="Expert"),
    Skill(name="FastAPI", proficiency="Expert"),
    Skill(name="Flask", proficiency="Advanced"),

    # Machine Learning & Deep Learning
    Skill(name="TensorFlow", proficiency="Expert"),
    Skill(name="PyTorch", proficiency="Advanced"),
    Skill(name="Scikit-learn", proficiency="Expert"),
    Skill(name="XGBoost", proficiency="Advanced"),
    Skill(name="LightGBM", proficiency="Advanced"),

    # Computer Vision
    Skill(name="OpenCV", proficiency="Expert"),
    Skill(name="YOLO (Object Detection)", proficiency="Expert"),
    Skill(name="MediaPipe", proficiency="Advanced"),
    Skill(name="OCR (Tesseract, EasyOCR)", proficiency="Expert"),

    # Natural Language Processing (NLP)
    Skill(name="spaCy", proficiency="Expert"),
    Skill(name="Transformers (Hugging Face)", proficiency="Advanced"),
    Skill(name="BERT", proficiency="Advanced"),
    Skill(name="GPT Models", proficiency="Advanced"),
    Skill(name="NLTK", proficiency="Expert"),

    # Neural Network Architectures
    Skill(name="CNN (Convolutional Neural Networks)", proficiency="Expert"),
    Skill(name="RNN (Recurrent Neural Networks)", proficiency="Advanced"),
    Skill(name="LSTM (Long Short-Term Memory)", proficiency="Advanced"),
    Skill(name="GRU (Gated Recurrent Unit)", proficiency="Advanced"),
    Skill(name="DNN (Deep Neural Networks)", proficiency="Expert"),

    # AI Model Deployment & Optimization
    Skill(name="ONNX", proficiency="Advanced"),
    Skill(name="TensorRT", proficiency="Advanced"),
    Skill(name="TF Serving", proficiency="Expert"),
    Skill(name="Docker", proficiency="Expert"),
    Skill(name="Kubernetes", proficiency="Intermediate"),
    Skill(name="AWS SageMaker", proficiency="Advanced"),

    # Asynchronous & Parallel Computing
    Skill(name="AsyncIO", proficiency="Expert"),
    Skill(name="Multiprocessing", proficiency="Expert"),
    Skill(name="CUDA (GPU Programming)", proficiency="Advanced"),

    # Databases
    Skill(name="PostgreSQL", proficiency="Expert"),
    Skill(name="MySQL", proficiency="Advanced"),
    Skill(name="MongoDB", proficiency="Advanced"),
    Skill(name="Redis", proficiency="Advanced"),

    # DevOps & CI/CD
    Skill(name="Git", proficiency="Expert"),
    Skill(name="GitHub Actions", proficiency="Intermediate"),
    Skill(name="CI/CD Pipelines", proficiency="Advanced"),

    # Others
    Skill(name="Tkinter (GUI Development)", proficiency="Advanced"),
    Skill(name="FastAPI WebSockets", proficiency="Advanced"),
    Skill(name="RESTful API Design", proficiency="Expert"),
    Skill(name="GraphQL", proficiency="Intermediate"),
]

projects = [
    Project(
        title="Sentiment Analysis Model",
        description="A model to analyze sentiment of text",
        technologies=["Python", "TensorFlow", "NLP"],
        github_url="https://github.com/yourusername/sentiment-analysis",
        image="/static/images/data_cleaning.png"
    ),
    Project(
        title="Image Classification System",
        description="Classify images using CNNs",
        technologies=["Python", "PyTorch", "Computer Vision"],
        github_url="https://github.com/yourusername/image-classification",
        image="/static/images/object_detection.jpg"
    ),
    # Add other projects as needed
]

experience = [
    Experience(
        company="Tech Company Inc.",
        position="AI Engineer",
        start_date="2020-01-01",
        end_date="2023-12-31",
        description="Worked on AI-driven projects using ML/DL techniques.",
        technologies=["Python", "TensorFlow", "AWS"]
    ),
    # Add other experience as needed
]

contact = Contact(
    email="naym.mj@gmail.com",
    linkedin="https://www.linkedin.com/in/yourprofile/",
    github="https://github.com/yourusername",
    website="https://yourwebsite.com"
)

about = About(
    name="MD Rakibul Hasan Naym",
    title="Manager AI",
    summary="Experienced AI Engineer with a passion for building innovative machine learning solutions.",
    profile_image="/static/images/profile_1.jpg"
)

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "about": about})

@app.get("/skills", response_class=HTMLResponse)
async def read_skills(request: Request):
    print("Skills:", skills)  # Debug line
    return templates.TemplateResponse("skills.html", {"request": request, "skills": skills})

@app.get("/projects", response_class=HTMLResponse)
async def read_projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request, "projects": projects})

@app.get("/experience", response_class=HTMLResponse)
async def read_experience(request: Request):
    return templates.TemplateResponse("experience.html", {"request": request, "experience": experience})

@app.get("/contact", response_class=HTMLResponse)
async def read_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "contact": contact})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
