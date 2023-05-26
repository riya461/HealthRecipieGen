
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    # path('profilec/', include('profilec.urls')),
    path('', include('addpost.urls')),
    path('',include('search.urls'))
]
