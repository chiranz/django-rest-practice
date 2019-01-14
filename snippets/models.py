from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=120, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.TextField(
        max_length=100, choices=LANGUAGE_CHOICES, default='python')
    style = models.CharField(
        max_length=100, choices=STYLE_CHOICES, default='friendly')

    class Meta:
        ordering = ('created',)
