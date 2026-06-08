from django.db import models

class Mahsulot(models.Model):
    KATEGORIYA_CHOICES = [
        ('oziq-ovqat', 'Oziq-ovqat'),
        ('kiyim', 'Kiyim'),
        ('texnika', 'Texnika'),
    ]

    nomi = models.CharField(max_length=150)
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    kategoriya = models.CharField(max_length=50, choices=KATEGORIYA_CHOICES)
    soni = models.PositiveIntegerField()
    faol = models.BooleanField(default=True)
    tavsif = models.TextField(blank=True)
    qoshilgan_sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi