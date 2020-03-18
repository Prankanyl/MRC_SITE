from django.db import models


class Article(models.Model):
    article_title = models.CharField(
        verbose_name='Название статьи',
        max_length=100,
    )
    article_text = models.TextField(
        verbose_name='Текст статьи',
    )
    date_release = models.DateTimeField(
        verbose_name='Дата создания статьи'
    )

    def __str__(self):
        return f'{self.article_title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField(
        verbose_name='Имя автора комментария',
        max_length=10,
    )
    comment_text = models.TextField(
        verbose_name='Текст комментария',
    )

    def __str__(self):
        return f'{self.author_name}:\n{self.comment_text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
