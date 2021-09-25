from django.urls import path
from .import views
from .views import PostEdit, PostList,  TemplateView, PostDetail, PostCreate, PostDelete

urlpatterns=[
  path('', views.index, name='home'),
  path('index/', PostList.as_view(), name='index'),
  path('index/index_home/', TemplateView.as_view(), name='index_home'),
  path('index/index_home/<int:pk>/', PostDetail.as_view(), name='post_detail'),
  path('index/index_home/new/', PostCreate.as_view(), name='post_create'),
  path('input/input_home/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
  path('input/input_home/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

  

]