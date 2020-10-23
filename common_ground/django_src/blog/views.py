from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# 우리가 만든걸 import하는건지 Django가 제공해주는걸 하는건지 구분하자

from .models import Post
from .forms import PostForm, CommentForm


# Post 상세조회
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# Post 목록
def post_list(request):
#     # name = 'Django'
#     return HttpResponse('''<h2>Post List</h2>
#         <p>Welcome {name}!</p><p>{content}</p>'''\
#                         # .format(name=name, content=request.content_type))
# #                         이거 하면 text/plain 뜨고
#                         .format(name=name, content=request.user))
# #                         이거 하면 django 뜨고

    # QuerySet을 이용해서 DB에서 Post 목록 가져오기
    posts = Post.objects.filter(published_date__lte=timezone.now())\
        .order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


# Post 등록
@login_required
def post_new(request):
    if request.method == "POST":
        # Form 데이터를 입력하고 등록요청을 했을 때
        form = PostForm(request.POST)
        # Form 데이터가 clean한 상태
        if form.is_valid():
            print(form.cleaned_data)
            post = Post.objects.create\
                   (author=User.objects.get(username=request.user.username),
                    published_date=timezone.now(),
                    title=form.cleaned_data['title'],
                    text=form.cleaned_data['text'])
            # # title, text field의 값이 저장된다
            # post = form.save(commit=False) # 아직 DB에 반영은 안시키겠다는 뜻
            # # 현재 로그인 된 유저 ID값을 집어넣겠다는 뜻
            # post.author = User.objects.get(username=request.user.username)
            # post.published_date = timezone.now()
            # post.save() # 이때 DB에 저장을 시키겠다는 뜻
            return redirect('post_detail', pk=post.pk) # 그담에 바로 상세페이지로ㄱㄱ
    else:
        # 등록 Form을 보여줌
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# Post 삭제
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


# Post 수정
@login_required
def post_edit(request, pk):
    # DB에서 해당 pk와 매칭되는 Post 객체를 가져온다.
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # 수정처리하는 부분
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username=request.user.username)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # 수정 전에 수정하려는 데이터를 읽어오는 부분
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delet()
    return redirect('post_detail', pk=post_pk)




