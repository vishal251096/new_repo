from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('about_us/', views.AboutView.as_view(), name='about'),
    path('combo_offers/', views.ComboListView.as_view(), name='combo_list'),
    path('combo_offers/<slug:slug>/', views.ComboDetailView.as_view(), name='combo_detail'),
]