from django.urls import path,include

from . import views
urlpatterns = [
   path('', views.home.as_view(),name='home'),
   path('brandFitering/<slug:brand_slug>/', views.brandFitering,name='brand_slug'),
]
