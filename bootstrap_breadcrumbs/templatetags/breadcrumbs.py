import re
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django import template

register = template.Library()

def url_breadcrumbs(context, divider='/', home='Dashboard'):
    """
    Display breadcrumbs using bootstrap CSS, based on URL decomposition.

    Requires Twitter Bootstrap 2.

    Usage:

    {% load breadcrumbs %}

    {% url_breadcrumbs %}

    Options:

    divider: default = '/'
    home: default='Home'

    eg: {% url_breadcrumbs divider='&gt;' home='Dashboard' %}
    """
    request = context['request']
    home = ['<ul class="breadcrumb"><li><a href="/" title="%s">%s</a> <span class="divider">%s</span></li>' % (home, home, divider),]
    links = request.path_info.strip('/').split('/')
    bread = []
    total = len(links)-1
    for i, link in enumerate(links):
        if not link == '':
            bread.append(link)
            this_url = "/".join(bread)
            sub_link = re.sub('-', ' ', link)
            if not i == total:
                tlink = '<li><a href="/%s/" title="%s">%s</a> <span class="divider">%s</span></li>' % (this_url, sub_link, sub_link, divider)
            else:
                tlink = '<li>%s</li>' % sub_link
            home.append(tlink)
    bcrumb = "".join(home)
    return mark_safe(bcrumb + '</ul>')

register.simple_tag(takes_context=True)(url_breadcrumbs)
