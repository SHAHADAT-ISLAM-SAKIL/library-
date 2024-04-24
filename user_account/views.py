from django.shortcuts import render , redirect
from django.views.generic import FormView,UpdateView
from django.contrib.auth.views import LoginView , LogoutView
from .forms import UserSingUpForm,UpdateUser
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

#-------------------email function------------------------------------->

def send_email(user,template,subject):
    message = render_to_string(template,{
        'user':user,
    })
    send_mail = EmailMultiAlternatives(subject,"",to=[user.email])
    send_mail.attach_alternative(message,'text/html')
    send_mail.send()






#---------------------- UsersingUpView create Here ----------------------->

class UserSingUpView(FormView):
    template_name = 'user_auth.html'
    form_class  = UserSingUpForm
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        user = form.save()
        messages.success(self.request,'Register Successfully !')
        login(self.request,user)
        send_email(self.request.user,'sing.html','Register Book Shop Now ')
        return super().form_valid(form)
    




#---------------------- UserLoginView create Here ----------------------->

class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        messages.success(self.request,'LogIn Successfully !')
        # send_email(self.request.user,'sing.html','Register Book Shop Now ')
        return reverse_lazy('home')

    


#---------------------- UserLoginView create Here ----------------------->
    
class UserLogoutView(LogoutView):
    def get_success_url(self):
        messages.success(self.request,'Logout Successfully !')
        return reverse_lazy('home')

    
#-------------------- update data------------------------>
class UserUpdate(UpdateView):
    template_name = "update.html"
    form_class = UpdateUser

    def get_success_url(self):
        messages.success(self.request, "You Data Update Succefully!")
        send_email(self.request.user,'u.html','Update profile Book Shop')
        return reverse_lazy("home")

    def get_object(self, queryset=None):
        return self.request.user 



