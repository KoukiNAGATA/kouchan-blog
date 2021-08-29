from django.views.generic import DetailView, ListView
from blog.models import Post


class CommonListView(ListView):
    """ListViewのテンプレート"""
    model = Post
    template_name = "post_list.html"
    paginate_by = 10

    def get_context_data(self, **kw):
        # 下書き以外で最新の10件を表示
        context = super().get_context_data(**kw)
        context['posts_all'] = Post.objects.order_by(
            '-created_at').exclude(category__name='Draft')
        return context


class PostListView(CommonListView):
    def get_context_data(self, **kw):
        # 下書き以外で最新の10件を表示
        context = super().get_context_data(**kw)
        context['posts'] = Post.objects.order_by(
            '-created_at').exclude(category__name='Draft')
        return context


class BlogListView(CommonListView):
    def get_context_data(self, **kw):
        context = super().get_context_data(**kw)
        context['posts'] = Post.objects.order_by(
            '-created_at').filter(category__name='Blog')
        return context


class NewsListView(CommonListView):
    def get_context_data(self, **kw):
        context = super().get_context_data(**kw)
        context['posts'] = Post.objects.order_by(
            '-created_at').filter(category__name='News')
        return context


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "post_detail.html"
    # postはこちらで持っておく
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        # 下書き以外で最新の10件を表示
        context = super().get_context_data(**kwargs)
        context['posts_all'] = Post.objects.order_by(
            '-created_at').exclude(category__name='Draft')
        return context


class AboutView(CommonListView):
    model = Post
    template_name = "about.html"
