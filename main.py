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
        subs(email)

        # You can add logic here to store the email in a database or file
        return templates.TemplateResponse("subscribe-success.html", {"request": request, "email": email})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error handling subscription: {e}")


def subs(receiver_email: str):
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
        
        
        
@app.post("/now-appointment", response_class=HTMLResponse)
async def now_appointment_post(request: Request, name: str = Form(...), email: str = Form(...), phone: str = Form(...), date: str = Form(...), time: str = Form(...), message: str = Form(...)):
    try:
        # Send confirmation email (optional)
        send_email(email, name, date, time, message)

        # Logic for storing appointment details (optional)
        # You can store them in a database, or log them, etc.

        return templates.TemplateResponse("appointment-success.html", {"request": request, "name": name, "email": email, "date": date, "time": time, "message": message})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error handling appointment: {e}")

@app.get("/schedule-appointment", response_class=HTMLResponse)
async def schedule_appointment(request: Request):
    try:
        return templates.TemplateResponse("appointment.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error rendering appointment.html: {e}")

@app.post("/schedule-appointment", response_class=HTMLResponse)
async def schedule_appointment_post(request: Request, name: str = Form(...), email: str = Form(...), phone: str = Form(...), date: str = Form(...), time: str = Form(...), message: str = Form(...)):
    try:
        # Send confirmation email (optional)
        send_email(email, name, date, time, message)

        # Logic for storing appointment details (optional)

        return templates.TemplateResponse("appointment-success.html", {"request": request, "name": name, "email": email, "date": date, "time": time})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error handling appointment: {e}")

def send_email(receiver_email: str, name: str, date: str, time: str, message: str):
    try:
        # Setup the MIME
        message_mime = MIMEMultipart()
        message_mime["From"] = EMAIL
        message_mime["To"] = receiver_email
        message_mime["Subject"] = "Your Appointment Confirmation"

        # Create a beautiful HTML body for the email
        html_body = f"""
        <html>
        <body>
            <h2>Appointment Confirmation</h2>
            <p>Dear {name},</p>
            <p>We are pleased to confirm your appointment. Below are the details:</p>
            <table style="width: 100%; border: 1px solid #ddd; border-collapse: collapse;">
                <tr>
                    <th style="padding: 10px; text-align: left;">Date</th>
                    <td style="padding: 10px;">{date}</td>
                </tr>
                <tr>
                    <th style="padding: 10px; text-align: left;">Time</th>
                    <td style="padding: 10px;">{time}</td>
                </tr>
                <tr>
                    <th style="padding: 10px; text-align: left;">Message</th>
                    <td style="padding: 10px;">{message}</td>
                </tr>
            </table>
            <p>If you have any questions, feel free to reply to this email.</p>
            <p>Looking forward to meeting with you!</p>
            <p>Best regards,</p>
            <p><strong>Your Company Name</strong></p>
        </body>
        </html>
        """

        # Attach the HTML content to the email
        message_mime.attach(MIMEText(html_body, "html"))

        # Connect to Gmail SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL, PASSWORD)  # Login to the SMTP server
            server.sendmail(EMAIL, receiver_email, message_mime.as_string())  # Send email
        print(f"Confirmation email sent to {receiver_email}")

    except Exception as e:
        print(f"Error sending email: {e}")
        raise HTTPException(status_code=500, detail="Failed to send confirmation email")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
