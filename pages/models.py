from django.db import models

class Post(models.Model):
    topic = models.CharField(max_length=101)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/')  # 'upload_to' specifies the directory where the images will be uploaded

    def __str__(self):
        return self.title
