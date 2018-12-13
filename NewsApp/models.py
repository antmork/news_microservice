from django.db import models

class News(models.Model):
    author = models.CharField("Автор", max_length=50)
    title = models.CharField("Заголовок", max_length=100)
    body = models.TextField("Текст")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

def __str__(self):
    return '%s %s %s' % (self.author, self.title, self.body)