from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views



urlpatterns = [
    path("save/", views.save_product, name="save_product"),
    path("save-json/", views.save_product_json, name="save_product_json"),
    path('contact/', views.contact_view, name='contact'),
    path('upload/', views.upload_profile, name='upload-profile'),
    path('profiles/', views.profile_list, name='profile-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

