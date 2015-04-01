from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    content = models.TextField(null=True)
    time = models.DateTimeField()

    def get_absolute_url(self):
        path = reverse('detail',kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-time']

class Myself(models.Model):
    aboutme = models.TextField()
