from django.urls import path
from .views import HomePageView, SobrePageView

urlpatterns = [
    path('', HomePageView.as_view(), name= 'home'),
     path('sobre', SobrePageView.as_view(), name= 'sobre'), 
]