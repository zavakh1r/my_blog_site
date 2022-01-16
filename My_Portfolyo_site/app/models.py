from django.db import models
from ckeditor.fields import RichTextField

class Contact(models.Model):
          name=models.CharField(max_length=200)
          email=models.EmailField()
          subject=RichTextField()

          def __str__(self):
                    return self.email

class Article(models.Model):
    name=models.CharField(max_length=200)
    text=RichTextField()
    image=models.ImageField(upload_to='images/')
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


