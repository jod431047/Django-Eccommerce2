from django.shortcuts import render
from django.views import generic
from .models import Product , ProductImages , Brand,Review


def post_list_debug(request):
    
    
    
    # data = Product.objects.all()
    #data = Product.objects.filter(price=20)
    #data = Product.objects.filter(price__gt=80)
    #data = Product.objects.filter(price__gte=80)
    #data = Product.objects.filter(price__lt=80)
    #data = Product.objects.filter(price__lte=80)
    #data = Product.objects.filter(price__range=(24,25))
    
    
    #data = Product.objects.filter(brand__name='Apple')
    
    
    #data = Product.objects.filter(brand__id=1)
    #data = Product.objects.filter(brand__id__gt=30)
    #data = Product.objects.filter(name__contains='Sara')
    #data = Product.objects.filter(name__startswith='Sara')
    #data = Product.objects.filter(name__endswith='Snyder')
    #data = Product.objects.filter(video__isnull=True)
     
    #data = Review.objects.filter(create_date__year=2023)
    #data = Review.objects.filter(create_date__month=8)
    
    data = Product.objects.filter(price__gt=50,flag='Sale')
    data = Product.objects.filter(price__gt=50).filter(flag='Sale')
    
    
    return render(request,'products/debug.html' ,{'data':data})


class ProductList(generic.ListView):
    model = Product
    paginate_by=100
    
    
    
class ProductDetail(generic.DetailView):
    model = Product  
    
    
class BrandList(generic.ListView):
    model = Brand
    paginate_by=50
    
    
class BrandDetail(generic.ListView):
    model = Product  
    template_name= 'products/brand_detail.html'   

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context