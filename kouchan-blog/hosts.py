from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'', settings.ROOT_URLCONF, name='kouchan-blog'),
    host(r'admin', 'kouchan-blog.admin_urls', name='admin'),
)
