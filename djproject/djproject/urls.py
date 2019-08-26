from django.contrib import admin
from django.urls import path
from djproject import views as local_views
from posts import views as posts_views

import djproject.views

urlpatterns = [
    path('numbers-get', local_views.numbers),
    path('age-path/<str:name>/<int:age>', local_views.agePath),
    path('admin/', admin.site.urls),
    path('posts', posts_views.list_posts)
]
