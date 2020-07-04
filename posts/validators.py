import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    print(value)
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    # valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    valid_extensions = ['.pdf',]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
