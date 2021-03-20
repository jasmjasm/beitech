import os
from django.core.exceptions import ValidationError


def valida_pdf(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf']
    if not ext in valid_extensions:
        raise ValidationError('Solo se permiten archivos .pdf')
