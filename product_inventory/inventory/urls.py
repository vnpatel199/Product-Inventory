from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',  views.index, name='index'),
    path('search/',views.search, name='search'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('home/', views.home, name='home'),
    path('home/<pk>/', views.detail, name='detail'),
    path('home/update/<pk>/', views.update, name='update')
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)