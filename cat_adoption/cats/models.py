import uuid
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
from datetime import datetime

def video_upload_path(instance, filename):
    """동영상 파일을 S3에 업로드할 때 고유한 경로 생성"""
    extension = filename.split('.')[-1]
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    new_filename = f"{instance.id}_{timestamp}_{uuid.uuid4().hex[:8]}.{extension}"
    return f"cats/videos/{new_filename}"

class Cat(models.Model):
    """고양이 정보를 저장하는 모델"""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    video = models.FileField(upload_to=video_upload_path, storage=S3Boto3Storage(), null=True, blank=True)
    shelter = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class HealthRecord(models.Model):
    """고양이 건강 기록을 저장하는 모델"""
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    diagnosis_date = models.DateField()
    disease = models.CharField(max_length=100)
    treatment = models.TextField()

    def __str__(self):
        return f"{self.cat.name} - {self.disease}"