from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Post, Topic
from .forms import UserRegisterForm
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_posts(request):
    """Getting all post from DB"""
    if request.method == 'GET':
        dict_result = Post.objects.all()
        serializer = PostSerializer(dict_result, many=True)
        return Response(serializer.data)
    return Response({"message": "There is a problem with service!"})


class TopicListView(ListView):
    """Getting all posts which belongs to any topic"""
    model = Post
    template_name = 'blog/topic_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        topic_name = get_object_or_404(Topic, topic_name=self.kwargs.get('topic_name'))
        return Post.objects.filter(topic_name=topic_name).order_by('-date_posted')


class UserPostListView(ListView):
    """Getting all posts of a User"""
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'topic_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def search(request):
    return render(request, 'blog/search.html', {'title': 'Search here'})


def result(request):
    search = request.GET.get('search')
    status = Post.objects.filter(Q(title__icontains=search) | Q(content__icontains=search) | Q(topic_name__topic_name__contains=search) | Q(author__username__contains=search))
    return render(request, "blog/blog_result.html", {"posts": status})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    context = {
        'posts': Post.objects.filter(author=request.user)
    }
    return render(request, 'blog/profile.html', context)


