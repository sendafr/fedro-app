from django.urls import path
from .views import video_home


urlpatterns=[
    path(" ", video_home, name="video_home")
]