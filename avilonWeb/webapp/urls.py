from django.urls import path, include
from .views import *
# from django.views.generic import TemplateView
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('', Index.as_view(), name = 'index'),

]
