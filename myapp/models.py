from django.db import models

class Image(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="myimage")
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Image {self.id} - {self.likes} likes"
