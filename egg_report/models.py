from django.db import models


class CageNum(models.Model):
    number = models.IntegerField(unique=True)
    is_empty = models.BooleanField(default=False)

    def __str__(self):
        return str(self.number)


class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cage_num = models.ForeignKey(
        to=CageNum,
        to_field='number',
        on_delete=models.CASCADE
    )
    is_lay_egg = models.BooleanField(default=False)
