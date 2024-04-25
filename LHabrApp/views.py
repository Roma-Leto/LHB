from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import PostForm
from .models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'LHabrApp/profile.html')


class LLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'LHabrApp/logout.html'


class LLoginView(LoginView):
    template_name = 'LHabrApp/login.html'


def good_morning(request):
    return render(request, 'for_my_baby.html', {'text': "Hello, my baby! I,m cool! =)"})


def index(request):
    return render(request, 'redirect.html')


def index_blog(request):
    articles = Post.objects.all()
    items_per_page = 4
    paginator = Paginator(articles, items_per_page)
    page_number = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_number)
    content = {
        'header': "Embedded World",
        'articles': articles,
        'page_objects': page_objects,
    }
    return render(request, 'LHabrApp/index_blog.html', content)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_pg')  # перенаправление на главную страницу
    else:
        form = PostForm()

    return render(request, 'LHabrApp/create_post.html', {'form': form})
