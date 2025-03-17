from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI(title="Subscription Service")

# Mount static files for serving CSS, JS, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 template engine
templates = Jinja2Templates(directory="templates")

# SMTP Email setup (adjust with your email credentials)
EMAIL = "naym.mj@gmail.com"
PASSWORD = "qwpi okax czji hvkt"  # App password if 2FA enabled
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    try:
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error rendering index.html: {e}")


@app.post("/subscribe", response_class=HTMLResponse)
async def subscribe(request: Request, email: str = Form(...)):
    try:
        # Send confirmation email
        send_email(email)

        # You can add logic here to store the email in a database or file
        return templates.TemplateResponse("subscribe-success.html", {"request": request, "email": email})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error handling subscription: {e}")


def send_email(receiver_email: str):
    try:
        # Setup the MIME
        message = MIMEMultipart()
        message["From"] = EMAIL
        message["To"] = receiver_email
        message["Subject"] = "Subscription Confirmation"

        # Email body
        body = "Thank you for subscribing to our newsletter!"
        message.attach(MIMEText(body, "plain"))

        # Connect to Gmail SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL, PASSWORD)  # Login to the SMTP server
            server.sendmail(EMAIL, receiver_email, message.as_string())  # Send email
        print(f"Confirmation email sent to {receiver_email}")

    except Exception as e:
        print(f"Error sending email: {e}")
        raise HTTPException(status_code=500, detail="Failed to send confirmation email")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
