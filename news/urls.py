from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProblemsView

app_name = 'news'

urlpatterns = [
    path('problems/', ProblemsView.as_view(), name='problems-view')   
] 