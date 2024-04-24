from django.urls import path,include

from user_account.views import UserSingUpView,UserLoginView,UserLogoutView,UserUpdate
urlpatterns = [
   path('singup/', UserSingUpView.as_view(),name='singup'),
   path('login/', UserLoginView.as_view(),name='login'),
   path('logout/', UserLogoutView.as_view(),name='logout'),
   path('update/' , UserUpdate.as_view(), name='update'),
]
