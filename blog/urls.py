from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.list_post, name = 'list_url'),
    path('<str:slug>/<int:id>/',views.post, name = 'post_url'),
    path('create/',views.create_post,name = 'create_url')
]
