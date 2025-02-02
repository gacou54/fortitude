from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse

from apps.collections.models import Collection


def collections(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(request, 'collections/list.html', {'collections': Collection.objects.all()})
