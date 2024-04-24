from django.urls import path,include

from . import views
urlpatterns = [
  path('details/<int:id>/', views.Detailviews.as_view(), name='detail'),
  path('profile/', views.returnBook.as_view(), name='profile'),
]
