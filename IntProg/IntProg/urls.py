from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home, name='home'),
    path('<int:idCloth>/', views.clothes_detail, name='clothes_detail'),
    path('clothes/<str:type>', views.clothesCart, name='clothesCart'),
    path('item/new', views.itemAdd.as_view(), name="item.new"),
    path('list', views.itemList.as_view(), name="list"),

    path('list/<int:pk>/', views.itemDetail.as_view(), name='item.detail'),

    path('list/<int:pk>/edit', views.itemUpdate.as_view(), name="item.update"),
    path('login', views.LoginInterfaceView.as_view(), name="login"),
    path('logout',views.LogoutInterfaceView.as_view(), name= 'logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('search', views.searchView, name='search'),


]
