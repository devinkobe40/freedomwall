from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Thread(models.Model):
    title = models.CharField(
            max_length = 200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")])
    text = models.TextField()

    #Images
    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()

    #Images
    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')

    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
