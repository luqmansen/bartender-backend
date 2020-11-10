import string
from random import choice

from django.utils.text import slugify


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)[:20]
    Cls = instance.__class__
    qs_exist = Cls.objects.filter(slug=slug).exists()

    if qs_exist:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=10)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def random_string_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(choice(chars) for _ in range(size))
