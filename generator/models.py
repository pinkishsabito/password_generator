from django.db import models


class GeneratedPassword(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=30)
    objects = models.Manager()

    def __init__(self, new_password):
        super().__init__()
        self.password = new_password
