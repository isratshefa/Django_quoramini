from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Question(models.Model):
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question_title = models.TextField()
    asked_date = models.DateTimeField(auto_now_add=True)


    def get_best_answer(self):
        answers = self.answer_set.all()
        if answers:
            answers = self.answer_set.order_by('-answered_date')
            return answers[0]
        else:
            return answers


    def __str__(self):
        return self.asked_by.username + " - " + self.question_title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField()
    answered_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)


    def __str__(self):
        return self.answered_by.username + " - " + self.answer

