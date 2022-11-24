from django.db import models

class Article(models.Model):
    article_text = models.CharField('Название', max_length=100)
    article_content = models.TextField('Контент')
    article_date = models.DateTimeField('Дата')

    def __str__(self):
        return self.article_text
