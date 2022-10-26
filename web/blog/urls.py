from django.urls import path
from rest_framework.routers import DefaultRouter

from main.views import TemplateAPIView

from . import views

app_name = 'blog'

router = DefaultRouter()
router.register('posts', views.ArticleViewSet, basename='post')

urlpatterns = [
    path('blog/', TemplateAPIView.as_view(template_name='blog/post_list.html'), name='blog-list'),
]

urlpatterns += router.urls
