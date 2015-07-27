from concertina import concertina
from django import template

register = template.Library()


@register.filter()
def concertina_pagination(page_object):
    return concertina(page_object.number, page_object.paginator.num_pages)
