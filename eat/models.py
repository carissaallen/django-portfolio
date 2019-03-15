from django.db import models

class Eat(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # display food titles in admin page
    def __str__(self):
        return self.title
