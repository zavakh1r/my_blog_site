from django.urls import path
from .views import index, Blog_View, Blog_Detail_View

urlpatterns=[
    path('', index, name='index'),
    path('blog/', Blog_View.as_view(),name="blog"),
    path('blog/<int:pk>/', Blog_Detail_View.as_view(), name='blog_detail'),
]