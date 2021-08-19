from django.views.generic import DetailView, ListView
from blog.models import Post


class CommonListView(ListView):
    """ListViewのテンプレート"""
    model = Post
    template_name = "post_list.html"
    paginate_by = 10

    def get_context_data(self, **kw):
        context = super().get_context_data(**kw)
        context['posts_all'] = Post.objects.order_by('-created_at').all()
        return context


class PostListView(CommonListView):
    def get_context_data(self, **kw):
        context = super().get_context_data(**kw)
        context['posts'] = Post.objects.order_by('-created_at').all()
        return context


class BlogListView(CommonListView):
    def get_context_data(self, **kw):
        context = super().get_context_data(**kw)
        context['posts'] = Post.objects.order_by(
            '-created_at').filter(category__name='blog')
        return context


class NewsListView(CommonListView):
    def get_context_data(self, **kw):
        context = super().get_context_data(**kw)
        context['posts'] = Post.objects.order_by(
            '-created_at').filter(category__name='news')
        return context


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "post_detail.html"
    # post_idはこちらで持っておく
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_all'] = Post.objects.order_by('-created_at').all()
        return context
