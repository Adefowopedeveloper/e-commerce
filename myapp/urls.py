from django.urls import path
from . import views 
from django.conf.urls.static import static 
from torillo import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('booking/', views.booking, name="booking"),
    path('contact/', views.contact, name="contact"),
    path('menu/', views.menu, name="menu"), 
    path('team/', views.team, name="team"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('service/', views.service, name="service"),
    path('register/', views.register, name="register"), 
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('order/<int:pk>/', views.OrderProduct, name="order"), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
