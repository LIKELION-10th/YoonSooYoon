from django.db import models

class Geust(models.Model): # 방명록 객체
    nickname = models.CharField(max_length=15)
    body = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nickname