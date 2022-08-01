from django.db import models


class Article(models.Model):
    feed = models.ForeignKey(on_delete=models.deletion.CASCADE, to='news.Feed')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title