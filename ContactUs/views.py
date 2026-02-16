from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
from django.conf import settings


class ContactMailView(APIView):
    """
    POST → Send contact form details to company email
    """
    def post(self, request):
        name = request.data.get("name")
        email = request.data.get("email")
        phone = request.data.get("phone")
        message = request.data.get("message")

        if not name or not email or not message:
            return Response(
                {"status": "error", "message": "All fields required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # -------------------------------
        # 1 Email to Admin
        # -------------------------------
        admin_subject = f"New Contact Message from {name}"
        admin_body = f"""
            Name: {name}
            Email: {email}
            Phone No: {phone}

            Message:
            {message}
            """

        admin_mail = EmailMessage(
            subject=admin_subject,
            body=admin_body,
            from_email='support@mediamaticstudio.com',
            to=['support@mediamaticstudio.com'],
        )
        admin_mail.send(fail_silently=False)

        # -------------------------------
        # 2 Auto-reply Email to User
        # -------------------------------
        user_subject = "Thank you for contacting us"
        user_body = f"""
            Hi {name},

            Thank you for reaching out to us.

            We have received your message and our team will get back to you shortly.

            Your message:
            "{message}"

            Best regards,
            Support Team
            """

        user_mail = EmailMessage(
            subject=user_subject,
            body=user_body,
            from_email='support@mediamaticstudio.com',
            to=[email],
        )
        user_mail.send(fail_silently=False)

        return Response(
            {"status": "success", "message": "Message sent and reply email delivered"},
            status=status.HTTP_200_OK
        )


class GetQuoteMailView(APIView):
    """
    POST → Send get quote form details to company email
    """
    def post(self, request):
        first_name = request.data.get("firstName")
        last_name = request.data.get("lastName")
        email = request.data.get("email")
        phone = request.data.get("phone")
        dial_code = request.data.get("dialCode")
        country_code = request.data.get("countryCode")
        start_date = request.data.get("startDate")
        selected_service = request.data.get("selectedService")
        message = request.data.get("message")

        # Validation
        if not first_name or not email or not selected_service or not message:
            return Response(
                {"status": "error", "message": "Required fields: First Name, Email, Service, Message"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Format full name
        full_name = f"{first_name} {last_name}".strip()
        
        # Format phone number with dial code
        full_phone = f"{dial_code} {phone}".strip() if phone else "Not provided"

        # -------------------------------
        # 1 Email to Admin
        # -------------------------------
        admin_subject = f"New Quote Request from {full_name}"
        admin_body = f"""
New Quote Request Received

Client Information:
-------------------
Name: {full_name}
Email: {email}
Phone: {full_phone}
Country Code: {country_code}

Project Details:
----------------
Service Requested: {selected_service}
Preferred Start Date: {start_date if start_date else 'Not specified'}

Message:
{message}

---
This is an automated notification from MediaMatic Studio Quote Form.
            """

        admin_mail = EmailMessage(
            subject=admin_subject,
            body=admin_body,
            from_email='support@mediamaticstudio.com',
            to=['support@mediamaticstudio.com'],
        )
        admin_mail.send(fail_silently=False)

        # -------------------------------
        # 2 Auto-reply Email to User
        # -------------------------------
        user_subject = "Thank you for requesting a quote - MediaMatic Studio"
        user_body = f"""
Hi {first_name},

Thank you for your interest in our services!

We have received your quote request for "{selected_service}" and our team is reviewing your requirements.

Project Summary:
• Service: {selected_service}
• Preferred Start Date: {start_date if start_date else 'Not specified'}

One of our representatives will get back to you within 24-48 hours with a detailed quote and next steps.

If you have any urgent questions, please feel free to reach out to us at:
📞 +91 96295 93615
📧 support@mediamaticstudio.com

Best regards,
MediaMatic Studio Team
www.mediamaticstudio.com
            """

        user_mail = EmailMessage(
            subject=user_subject,
            body=user_body,
            from_email='support@mediamaticstudio.com',
            to=[email],
        )
        user_mail.send(fail_silently=False)

        return Response(
            {"status": "success", "message": "Quote request sent successfully"},
            status=status.HTTP_200_OK
        )
