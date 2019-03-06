"""abianji URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from abianji.admin_site import admin_site

handler404 = 'blog.views.page_not_found_view'
handler500 = 'blog.views.server_error_view'
handler403 = 'blog.views.permission_denied_view'

urlpatterns = [
    url(r'^admin/', admin_site.urls),
    url('', include('blog.urls', namespace='blog'))
]
