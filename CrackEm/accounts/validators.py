import re


from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image


def validate_profile_picture(image):
    max_file_size = 5 * 1024 * 1024
    if image.size > max_file_size:
        raise ValidationError(_("File size should be less then 5 MB."))

    valid_file_types = ['image/jpeg', 'image/png']
    file_type = image.file.content_type
    if file_type not in valid_file_types:
        raise ValidationError(_('Unsupported file type. File should be JPEG or PNG.'))

    min_width, min_height = 300, 300
    with Image.open(image) as img:
        width, height = img.size
        if width < min_width or height < min_height:
            raise ValidationError(_('Minimum resolution for the image is 300x300.'))


def username_validator(value):
    min_length = 3
    max_length = 50
    if len(value) < min_length or len(value) > max_length:
        raise ValidationError(f"Username should be between {min_length} and {max_length} letters")

    if not re.match(r'^\w+$', value):
        raise ValidationError(_('Username can only contain letters, numbers and underscore.'))




