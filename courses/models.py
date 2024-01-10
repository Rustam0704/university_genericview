from django.db import models

class Speciality(models.Model):
    name = models.CharField(max_length=28)
    code = models.CharField(max_length=10, unique=True)
    start_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}-{self.start_date}'

    class Meta:
        verbose_name_plural = "yo’nalishlar"
        verbose_name = "yo’nalish"

class Teacher(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    degree = models.CharField(max_length=10, blank=True, null=True)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.first_name}-{self.speciality}-{self.degree}'

    class Meta:
        verbose_name_plural = "o’qituvchilar"
        verbose_name = "o’qituvchi"


