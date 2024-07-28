from django.urls import path
from profiles_api import views

# this will convert helloapiview to view, and if get request is made then  get() will be called in HelloApiView
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
