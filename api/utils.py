import string
from io import BytesIO
from random import choice
import qrcode

from django.utils.text import slugify
from django.core.files.base import ContentFile


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = f"{slugify(instance.title)}-{random_string_generator(size=10)}"

    Cls = instance.__class__
    qs_exist = Cls.objects.filter(slug=slug).exists()

    if qs_exist:
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def generate_qr(slug):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(slug)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img_io = BytesIO()
    img.save(img_io, format='JPEG', quality=100)
    img_content = ContentFile(img_io.getvalue(), slug.split('/')[-1])
    return img_content


def random_string_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(choice(chars) for _ in range(size))
