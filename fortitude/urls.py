from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import include, path


def redirect_to_login_or_collections(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('collections-list')

    return redirect('login')


def login(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(request, 'login.html')


urlpatterns = [
    path('', redirect_to_login_or_collections, name='index'),
    path('collections/', include('apps.collections.urls')),
    path('login/', login, name='login'),
    path('admin/', admin.site.urls),
]
