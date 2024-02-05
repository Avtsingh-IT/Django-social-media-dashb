from django.db import models

class UploadedImage(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='uploaded_images/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Image-{self.id}"