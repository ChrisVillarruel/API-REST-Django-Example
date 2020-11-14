from django.urls import path
from profilesApi.views import *

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
]
