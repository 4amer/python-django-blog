from django.db import models

class Article(models.Model):
    article_username = models.CharField('Имя', max_length=255, null=True)
    article_content = models.TextField('Контент')
    article_date = models.DateTimeField('Дата')
