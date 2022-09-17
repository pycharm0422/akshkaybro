from django.db import models

class News(models.Model):
    headline = models.CharField(max_length=200)
    main = models.TextField()

    def __str__(self):
        return self.headline