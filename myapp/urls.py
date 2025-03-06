from django.urls import path
from .views import contact_view,save_product, save_product_json


urlpatterns = [
    path("save/", save_product, name="save_product"),
    path("save-json/", save_product_json, name="save_product_json"),
    path('contact/', contact_view, name='contact'),
]