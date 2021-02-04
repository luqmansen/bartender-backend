from django.db import models
from django.utils.timezone import now


class Cage(models.Model):
    number = models.IntegerField()
    CAGE_POS = [
        ('L', 'Kiri'),
        ('R', 'Kanan'),
    ]
    position = models.CharField(choices=CAGE_POS, max_length=1)
    is_empty = models.BooleanField(default=False)

    def __str__(self):
        return str(self.number)


class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(default=now)
    cage_num = models.ForeignKey(
        to=Cage,
        on_delete=models.CASCADE
    )
    egg = models.IntegerField()

    def __str__(self):
        return str(self.date)
