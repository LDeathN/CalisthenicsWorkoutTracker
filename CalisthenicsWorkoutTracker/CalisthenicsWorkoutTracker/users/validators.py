from django.core.exceptions import ValidationError


def validate_email(email):
    if not all(ch.isalnum() or ch == "@" or ch == "." for ch in email) or "@" not in email:
        raise ValidationError("Invalid email!")

