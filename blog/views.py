from django.views.generic import DetailView, ListView
from django.template.response import TemplateResponse
from blog.models import Post


class PostListView(ListView):
    model = Post
    ordering = "-created_at"
    template_name = "post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "post_detail.html"
    context_object_name = "post"


def post_list(request):
    return TemplateResponse(
        request,
        "post_list.html",
        {"posts": Post.objects.all()},
    )
