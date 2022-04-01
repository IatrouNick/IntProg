from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<int:idCloth>/', views.clothes_detail, name='clothes_detail'),
    path('<str:type>', views.clothesCart, name='clothesCart'),
    path('itemadd/new', views.itemAdd.as_view(), name="itemadd.new"),
]
