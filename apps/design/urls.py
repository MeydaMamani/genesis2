from django.urls import path,include
from . import views
from .views import *

app_name="design"

urlpatterns = [
    path('', (views.HomeView.as_view()), name='home'),
]
