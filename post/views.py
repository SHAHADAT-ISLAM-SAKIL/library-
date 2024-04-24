from django.shortcuts import render
from django.views.generic import DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PostModel
from transcation.models import BorrowedBookModel
from django.urls import reverse_lazy


#------------- show Details  view here now -------------------->
class Detailviews(DetailView):
    template_name = 'details.html'
    model = PostModel
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("home")


class returnBook(LoginRequiredMixin,ListView):
    template_name = 'profile.html'
    model = BorrowedBookModel
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['data']= BorrowedBookModel.objects.filter(user=self.request.user)
       
        return context
    
     