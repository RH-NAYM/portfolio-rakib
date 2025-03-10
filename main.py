from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Static HTML Server")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    try:
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error rendering index.html: {e}")

@app.get("/contact", response_class=HTMLResponse)
async def read_contact(request: Request):
    try:
        return templates.TemplateResponse("contact.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error rendering contact.html: {e}")

@app.get("/404", response_class=HTMLResponse)
async def read_404(request: Request):
    try:
        return templates.TemplateResponse("404.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error rendering 404.html: {e}")

@app.get("/blog-single", response_class=HTMLResponse)
async def read_blog_single(request: Request):
    try:
        return templates.TemplateResponse("blog-single.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error rendering blog-single.html: {e}")

@app.get("/portfolio-details", response_class=HTMLResponse)
async def read_portfolio_details(request: Request):
    try:
        return templates.TemplateResponse("portfolio-details.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error rendering portfolio-details.html: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)