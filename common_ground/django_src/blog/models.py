from django.db import models
# Create your models here.
from django.utils import timezone
from django import forms

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('Input more than 3 characters.')

class Post(models.Model):
    # 작성자
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 제목
    title = models.CharField(max_length=200, validators=[min_length_3_validator])
    # 내용
    text = models.TextField()
    # 작성일자
    created_date = models.DateTimeField(default=timezone.now) # 얜 걍 호출이라 괄호없
    # 겟일자
    published_date = models.DateTimeField(blank=True, null=True)

    # 필드 추가 - 삭제할 예정
    # test = models.TextField()


    # 게시일자에 현재 날짜&시간을 대입해주는 함수
    def publish(self):
        self.published_date = timezone.now() # 얜 함수라 괄호있
        self.save()

    # 게시글 제목을 객체 주소 대신에 입력받은대로 반환해주는 함수
    # 자바로 치면 toString()이라고 한다
    def __str__(self):
        return self.title

# Post Comment class
class Comment(models.Model):
    # post information
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    # commenter
    author = models.CharField(max_length=100)
    # contents
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)