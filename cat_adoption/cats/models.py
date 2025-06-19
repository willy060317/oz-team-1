from django.db import models
from django.contrib.auth.models import User

def video_upload_path(instance, filename):
    return f"videos/{instance.id}/{filename}"

class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    shelter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cats')
    video = models.FileField(upload_to=video_upload_path, blank=True, null=True)
    # video_url = models.URLField(blank=True, null=True)  # 필요 시 유지

    def __str__(self):
        return self.name

class HealthRecord(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='health_records')
    record = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cat.name} - {self.record[:20]}"