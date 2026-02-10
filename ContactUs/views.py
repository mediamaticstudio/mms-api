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
