from django import template

from ..models import Terms

register = template.Library()


@register.inclusion_tag('kgterms/terms.html')
def terms_for_person(person):
    terms = Terms.objects.exclude(users_agreed__person=person)
    return {'terms': terms}
