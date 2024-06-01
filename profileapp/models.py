from django.db import models

class userprofile(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=100)
    address=models.TextField()
    pincode=models.IntegerField()
    skill1=models.CharField(max_length=100)
    skill2=models.CharField(max_length=100)
    skill3=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    whatsapp=models.IntegerField()
    education_course=models.CharField(max_length=100)
    education_school=models.CharField(max_length=100)
    education_start_date=models.DateField()
    education_end_date=models.DateField()
    certificate_course=models.CharField(max_length=100)
    certificate_school=models.CharField(max_length=150)
    certificate_images=models.ImageField()
    project_name=models.CharField(max_length=150)
    project_summary=models.TextField()
    project_link=models.URLField()
    project_image=models.ImageField(max_length=200)

    def __str__(self):
        return self.firstname

