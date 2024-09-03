from django.db import models

# Create your models here.
class Feedback(models.Model):

    name = models.CharField(max_length=200, null=False)
    comment = models.TextField(null=False)
    is_accepted = models.BooleanField(default=False, help_text='Designates whether this feedback is displayed in index', verbose_name='active')

    def __str__(self):
        return f"name: {self.name}, comment: {self.comment}"