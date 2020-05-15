"""jwcnpj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include  # v2 coloquei o include
from django.conf.urls import handler404, handler500  # na view get_object_or_404

# v1 from django.urls import path

# v1 from core.views import index, contato

from core import views  # para aparecer o views.error404

urlpatterns = [
    path('admin/', admin.site.urls),
    # v1 path('', index),
    # v1 path('contato',contato),
    path('', include('core.urls')),  # v2 criou arquivo de urls dentro do core para cada applicação
]

handler404 = views.error404
handler500 = views.error500
