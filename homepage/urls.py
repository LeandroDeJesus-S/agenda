from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<str:contato_nome>/<int:contato_id>', views.contact, name='a_contact'),
    path("search/", views.search, name="search"),
    path('delete/<str:contact_name>/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('edit/<str:contact_name>/<int:contact_id>/', views.edit_contact, name='edit_contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
