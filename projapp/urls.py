from django.urls import path
from .import views
from .views import upload_image, image_list
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile_view, name="profile"),
    path('accounts/profile/', views.dashboard_view, name="profile"),
    path('trending/', views.trending_view, name="profile"),


    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.image_list, name='image_list'),
   
]