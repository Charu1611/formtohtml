from django.db import models
# import uuid

class UploadTemplate(models.Model):
    # name=models.CharField(max_length=20)
    template_choices =[
    ('t1','t1️'),
    ('t2','t2️'),
    ('t3','t3️'),
    ]
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    dob=models.DateField(max_length=8)
    education=models.CharField(max_length=50)
    photo=models.ImageField(upload_to="img/%y")
    user=models.CharField(max_length=30,default='myname',null=True)
    template = models.CharField(max_length=2 , choices=template_choices)
    # uniqueID = models.UUIDField(max_length=255, default = uuid.uuid4)

    def __str__(self):
        return self.user
