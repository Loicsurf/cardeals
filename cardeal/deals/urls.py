from django.contrib import admin
from django.urls import path
from deals import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('cars/', views.cars, name='cars'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('detail/', views.detail, name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)