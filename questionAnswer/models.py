from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="question_user")
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    tags = TaggableManager()
    created_at = models.TimeField(default=timezone.now())

    def __str__(self) -> str:
        return str(self.title)

class Answer(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    created_at = models.TimeField(default=timezone.now())

    def __str__(self) -> str:
        name = "answer of  " + str(self.question)
        return name
