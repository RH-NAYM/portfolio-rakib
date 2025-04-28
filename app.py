from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from en import MYINFO
from mangum import Mangum  # For Vercel serverless handling
import os

# Initialize FastAPI app
app = FastAPI(title="Subscription Service")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Load email settings
items = MYINFO()

# SMTP Email setup
EMAIL = os.getenv("EMAIL", "your_default_email@gmail.com")
cred = os.getenv("EMAIL_PASSWORD", items.get_data())
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
        subs(email)
        return templates.TemplateResponse("subscribe-success.html", {"request": request, "email": email})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error handling subscription: {e}")

def subs(receiver_email: str):
    try:
        message = MIMEMultipart()
        message["From"] = EMAIL
        message["To"] = receiver_email
        message["Subject"] = "Subscription Confirmation 📨"

        body = "Thank you for subscribing to our newsletter! 🎉 We are thrilled to have you on board."
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, cred)
            server.sendmail(EMAIL, receiver_email, message.as_string())

        print(f"Confirmation email sent to {receiver_email}")

    except Exception as e:
        print(f"Error sending email: {e}")
        raise HTTPException(status_code=500, detail="Failed to send subscription confirmation email")

@app.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    try:
        return templates.TemplateResponse("contact.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error rendering contact.html: {e}")

@app.get("/schedule-appointment", response_class=HTMLResponse)
async def schedule_appointment(request: Request):
    try:
        return templates.TemplateResponse("appointment.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error rendering appointment.html: {e}")

@app.post("/schedule-appointment", response_class=HTMLResponse)
async def schedule_appointment_post(request: Request, name: str = Form(...), email: str = Form(...), phone: str = Form(...), date: str = Form(...), time: str = Form(...), message: str = Form(...)):
    try:
        send_email(email, name, date, time, message)
        return templates.TemplateResponse("appointment-success.html", {"request": request, "name": name, "email": email, "date": date, "time": time})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error handling appointment: {e}")

@app.post("/now-appointment", response_class=HTMLResponse)
async def now_appointment_post(request: Request, name: str = Form(...), email: str = Form(...), phone: str = Form(...), date: str = Form(...), time: str = Form(...), message: str = Form(...)):
    try:
        send_email(email, name, date, time, message)
        return templates.TemplateResponse("appointment-success.html", {"request": request, "name": name, "email": email, "date": date, "time": time, "message": message})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error handling appointment: {e}")

def send_email(receiver_email: str, name: str, date: str, time: str, message: str):
    try:
        message_mime = MIMEMultipart()
        message_mime["From"] = EMAIL
        message_mime["To"] = receiver_email
        message_mime["Subject"] = "Your Appointment Confirmation 🎉"

        html_body = f"""
        <html>
        <body>
            <h2 style="color: #4CAF50;">Appointment Confirmation 📅</h2>
            <p>Dear <strong>{name}</strong>,</p>
            <p>We are pleased to confirm your appointment! 😊 Below are your details:</p>
            <table style="width: 100%; border: 1px solid #ddd; border-collapse: collapse; padding: 10px;">
                <tr>
                    <th style="padding: 10px; background-color: #f2f2f2;">Date</th>
                    <td style="padding: 10px;">{date}</td>
                </tr>
                <tr>
                    <th style="padding: 10px; background-color: #f2f2f2;">Time</th>
                    <td style="padding: 10px;">{time}</td>
                </tr>
                <tr>
                    <th style="padding: 10px; background-color: #f2f2f2;">Message</th>
                    <td style="padding: 10px;">{message}</td>
                </tr>
            </table>
            <p>If you need any further assistance, feel free to reply to this email! ✨</p>
            <p>We look forward to meeting you soon! 😊</p>
            <p><strong>Best regards,</strong><br>Your Company Name 🌟</p>
        </body>
        </html>
        """

        message_mime.attach(MIMEText(html_body, "html"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, cred)
            server.sendmail(EMAIL, receiver_email, message_mime.as_string())

        print(f"Appointment confirmation email sent to {receiver_email}")

    except Exception as e:
        print(f"Error sending appointment email: {e}")
        raise HTTPException(status_code=500, detail="Failed to send appointment confirmation email")

# Serverless handler for Vercel
handler = Mangum(app)
