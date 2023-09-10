import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='質問')
    pub_date = models.DateTimeField( verbose_name='発表日')

    def __str__(self):
        return self.question_text


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name = '質問'
        verbose_name_plural = '質問'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,verbose_name='質問')
    choice_text = models.CharField(max_length=200, verbose_name='選択理由')
    votes = models.IntegerField(default=0, verbose_name='投票数')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = '選択理由'
        verbose_name_plural = '選択理由'
