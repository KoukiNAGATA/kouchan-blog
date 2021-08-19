from django.views.generic import DetailView, ListView
from blog.models import Post


class CommonListView(ListView):
    """ListViewのテンプレート"""

    def get_context_data(self, **kw):
        context = super().get_context_data(**kw)
        context['posts_all'] = Post.objects.all()
        return context


class PostListView(CommonListView):
    model = Post
    ordering = "-created_at"
    template_name = "post_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class BlogListView(CommonListView):
    model = Post
    ordering = "-created_at"
    template_name = "post_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category__name='blog')
        return context


class NewsListView(CommonListView):
    model = Post
    ordering = "-created_at"
    template_name = "post_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category__name='news')
        return context


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "post_detail.html"
    # post_idはこちらで持っておく
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_all'] = Post.objects.all()
        return context
