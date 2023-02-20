"""versat_clinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from core.views import front
from django.views.generic import TemplateView
from apps.users.views import Login, Logout

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path("", front, name="front"),
  
#     path("", TemplateView.as_view(template_name='index.html')),
#     # TemplateView.as_view(template_name='frontend/index.html'))
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", front, name="front"),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}), # only test not production
    re_path(r"^.*$",TemplateView.as_view (template_name="base.html")),
    path('user/', include('apps.users.api.urls')),
    path('', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('trabajador/', include('apps.trabajador.api.urls')),
    path('paciente/', include('apps.paciente.api.urls')),
]
