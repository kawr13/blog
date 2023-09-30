from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import PostForm, CommentsForm
from django.urls import reverse
from django.views.generic.list import ListView
from .models import Post, Comments

# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = 'blogapp/index.html'
    context_object_name = 'posts'
    ordering = '-created_at'








def blog(request):
    return render(request, 'blogapp/post.html')


def creat_post(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # Устанавливаем значение is_published на основе значения из формы
            post.is_published = form.cleaned_data['is_published']
            post.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = PostForm()

    context = {
        'form': form,
        'title': 'Создание поста',
    }

    return render(request, 'blogapp/creat_post.html', context=context)


def post(request, pk):
    if request.method == 'POST':
        form = CommentsForm(data=request.POST)
        if form.is_valid():
            post = Post.objects.get(pk=pk)
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('blogapp:post', args=[pk]))
    else:
        form = CommentsForm()
    posts = Post.objects.filter(pk=pk)
    comments = Comments.objects.filter(post=pk)
    context = {
        'title': 'Пост',
        'posts': posts,
        'form': form,
        'comments': comments,
    }
    return render(request, 'blogapp/post.html', context)


# class DetailedView(ListView):
#     model = Post
#     template_name = 'blogapp/post.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(DetailedView, self).get_context_data()
#         context['title'] = 'Пост'
#         context['posts'] = Post.objects.filter(id=self.request.GET.get('pk'))
#         return context



