from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pubdate = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # display blog titles in admin page
    def __str__(self):
        return self.title
    
    # shortens body of blog post on blog home page
    def summary(self):
        return self.body[:200]+'...'

    # see strftime.org for date customization 
    def date(self):
        return self.pubdate.strftime('%b %e %Y')
