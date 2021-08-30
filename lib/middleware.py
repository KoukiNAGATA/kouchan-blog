from django.http import HttpResponsePermanentRedirect
from django.conf import settings


class RedirectCorrectHostname(object):
    """
    redirects to correct hostname if requested hostname and settings.CORRECT_HOST does not match
    (at heroku domain redirects to custom domain)
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # settingsにCORRECT_HOSTがあるか
        if not getattr(settings, 'CORRECT_HOST', None):
            return None
        # settings.CORRECT_HOSTとアクセスしているhostが一致するか
        if request.get_host() == settings.CORRECT_HOST:
            return None

        # 一致しなかった場合、settings.CORRECT_HOSTにリダイレクト
        return HttpResponsePermanentRedirect(
            '{scheme}://{host}{path}'.format(scheme=request.scheme,
                                             host=settings.CORRECT_HOST,
                                             path=request.get_full_path()))
