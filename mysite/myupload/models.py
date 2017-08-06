from django.db import models

# Create your models here.


class file(models.Model):
    file_name       = models.CharField(max_length=200)
    upload_datetime = models.DateTimeField('Date uploaded.')
    comment         = models.CharField(max_length=5000)

    def __str__(self):
        return '{} / {}'.format(
            self.file_name,
            self.upload_datetime,
        )
