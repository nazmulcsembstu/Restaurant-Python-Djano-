from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="Index"),
    path('About/', views.About, name="About"),
    path('Menu/', views.Menu, name="Menu"),
    path('BanFacility/', views.BanFacility, name="BanFacility"),
    path('RecVendors/', views.RecVendors, name="RecVendors"),
    path('Gallery/', views.Gallery, name="Gallery"),
    path('Catering/', views.Catering, name="Catering"),
    path('Events/', views.Events, name="Events"),
    path('Contact/', views.Contact, name="Contact"),
    path('BanBook/', views.BanBook, name="BanBook"),
]