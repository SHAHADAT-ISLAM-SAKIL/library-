from django.urls import path
from . import views
urlpatterns = [
    path('deposite/', views.DepositMoneyView.as_view(),name='deposit'),
    path('borrow/<int:id>/', views.BorrowBook, name='borrow'),
    path('return/<int:id>/', views.returnBook,name='return'),
    path('borrowReport/', views.TransacationReport.as_view(), name='transation'),
   
]
