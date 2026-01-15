import os
import resend
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, Field

resend.api_key = os.getenv("RESEND_API_KEY")
MAIL_TO = os.getenv("MAIL_TO")
SENDER_NAME = "Michael Schlosser"

router = APIRouter()

class ContactFormRequest(BaseModel):
    name: str = Field(..., max_length=100)
    email: EmailStr = Field(..., max_length=100)
    message: str = Field(..., min_length=10, max_length=2000)

@router.post("/submit-contact", status_code=status.HTTP_200_OK)
async def submit_contact(request: ContactFormRequest):
    if not resend.api_key or not MAIL_TO:
        raise HTTPException(
            status_code=500,
            detail="Email service configuration is missing."
        )

    try:
        # 1. Send Email to YOU (the Owner)
        owner_params = {
            "from": f"{SENDER_NAME} <onboarding@resend.dev>",
            "to": [MAIL_TO],
            "subject": f"Portfolio Inquiry from {request.name}",
            "reply_to": request.email,
            "text": f"Name: {request.name}\nEmail: {request.email}\n\nMessage:\n{request.message}"
        }
        resend.Emails.send(owner_params)

        return {"message": "Inquiry sent successfully"}

    except Exception as e:
        print(f"ERROR SENDING EMAIL: {e}")
        raise HTTPException(
            status_code=500,
            detail="Failed to send message. Please try again later."
        )