from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login, name='accounts'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadaster/', views.cadaster, name='cadaster'),
    path('new-contact/', views.add_contact, name='new_contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
