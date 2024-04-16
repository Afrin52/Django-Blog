from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    # path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
    # path('<slug:slug>/', views.BlogListView.as_view(), name='blog_list_view'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('search/', views.search, name='search'),
]