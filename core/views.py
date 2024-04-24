from django.shortcuts import render
from django.views.generic import TemplateView 
from books_brand.models import BrandModels
from post.models import PostModel
# Create your views here.
class home(TemplateView):
    template_name = 'home.html'
   
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = BrandModels.objects.all()
        context['post'] = PostModel.objects.all()
        return context

def brandFitering(request,brand_slug=None):
    post = PostModel.objects.all()


    if brand_slug is not None:
        brand = BrandModels.objects.get(slug = brand_slug)
        post = PostModel.objects.filter(brand=brand)

    brand = BrandModels.objects.all()
    return render(request,'home.html',{"post":post,"brand":brand})
