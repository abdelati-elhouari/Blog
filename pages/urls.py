from django.urls  import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('newPost',views.newPost,name='newPost'),
    path('aboutPost',views.aboutPost,name='aboutPost'),
]
