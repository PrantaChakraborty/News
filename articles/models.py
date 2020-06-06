from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    # when user create an article and click on the button it will redirect to 'article detail' page
    # (every time it will redirect to the page).

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


# creating a table named 'comments' for user to leave comment on article, One article can have many comments


class Comment(models.Model):
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='comments'# renaming FOO_set
                                )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')
