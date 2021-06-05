from django.views.generic import DetailView, ListView
from blog.models import Post


class PostListView(ListView):
    model = Post
    ordering = "-created_at"
    template_name = "post_list.html"
    context_object_name = "posts"
    paginate_by = 10


class BlogListView(ListView):
    model = Post
    ordering = "-created_at"
    template_name = "post_list.html"
    context_object_name = "posts"
    paginate_by = 10
    queryset = Post.objects.filter(category__name='blog')


class NewsListView(ListView):
    model = Post
    ordering = "-created_at"
    template_name = "post_list.html"
    context_object_name = "posts"
    paginate_by = 10
    queryset = Post.objects.filter(category__name='news')


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "post_detail.html"
    context_object_name = "post"
