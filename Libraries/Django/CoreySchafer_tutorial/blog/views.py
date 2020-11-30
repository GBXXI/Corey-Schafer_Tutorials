
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from blog.models import \
    Post  # Importing this module in order to query our database
          # and pass the values that we want, to be rendered.

# Excplicity returning our requests.
# def home(request):
#     return HttpResponse("<h1>Blog Home</h1>")

# def about(request):
#     return HttpResponse("<h1>Blog About</h1>")

# Dummy data.
posts = [
    {
        'author': 'LuckyBrake',
        'title': 'Post 1',
        'content': 'First comment, to be deleted!',
        'date_posted': '12/10/2020'
    },

    {
        'author': 'BurmaSan',
        'title': 'Post 2',
        'content': 'Second comment to be deleted!',
        'date_posted': '13/10/2020'
    }
]

# Rendering our templates.


def home(request):
    context = {
        # 'posts': posts  # Quering our dummy data.
        'posts': Post.objects.all()  # Quering from our database.
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 7

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False


def about(request):
    return render(request, 'blog/about.html')
