from django import forms
from .models import Post, Comment

# Validator 함수 정의
# title 입력필드의 길이 체크 <3
# def min_length_3_validator(value):
#     if len(value) < 3:
#         raise forms.ValidationError('Input more than 3 characters.')

# PostForm 클래스 선언
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
    # title = forms.CharField()
    # title = forms.CharField(validators=[min_length_3_validator])
    # text = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
