from django.shortcuts import render , redirect
from django.views import generic
from .forms import ReviewForm
from .models import Product , ProductImages , Brand,Review
from django.db.models import Q ,F ,Value , Func
from django.db.models.aggregates import Count,Avg,Sum,Min,Max

from django.http import JsonResponse
from django.template.loader import render_to_string

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator




@cache_page(60 * 1)
def post_list_debug(request):
    
    
    
 
    
    
    data = Product.objects.all()
    
    
    
    
    return render(request,'products/debug.html' ,{'data':data})
   
    #send email 1m user

@method_decorator(cache_page(60 * 5), name='dispatch')
class ProductList(generic.ListView):
    model = Product
    paginate_by=100
    
    
    
class ProductDetail(generic.DetailView):
    model = Product  
    
    
def add_review(request,slug):
    product = Product.objects.get(slug=slug)
    form = ReviewForm(request.POST)
    if form.is_valid():
        myform = form.save(commit=False)
        myform.user = request.user
        myform.product = product
        myform.save()
        
        
        reviews = Review.objects.filter(product=product)
        html = render_to_string('include/all_reviews.html',{'reviews':reviews , request:request})
        return JsonResponse({'result':html})
        
        #return redirect(f'/products/{product.slug}')
    
    
class BrandList(generic.ListView):
    model = Brand
    paginate_by=50
    def get_queryset(self):
        object_list = Brand.objects.annotate(posts_count=Count('product_brand'))
        return object_list
    
    
    
    
class BrandDetail(generic.ListView):
    model = Product
    template_name = 'products/brand_detail.html'
    
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(posts_count=Count('product_brand'))[0]
        return context
    
    
    
    
    
    
    
    
    
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
    
    #data = Product.objects.filter(price__gt=50,flag='Sale')
    
    

    #data = Product.objects.filter(
    #    Q(price__gt=95),
    #   Q(flag='Sale')
    # )
    
    #data = Product.objects.filter(
    #    Q(price__gt=95) &
    #  Q(flag='Sale')
    #)
    
    
    #data = Product.objects.filter(
    #   Q(price__gt=95) |
    #   ~Q(flag='Sale')
    #)
    
    #data = Product.objects.filter(
    #  Q(price__gt=95) &
    # Q(flag='Sale')
    #)
    
    #data = Product.objects.filter(sku=F('price'))
    #data = Product.objects.filter(sku=F('brand__id'))
    #data = Product.objects.all().order_by('name')   #ASC
    #data = Product.objects.all().order_by('-name')   #DES
    #data = Product.objects.order_by('-name')    
    #data = Product.objects.filter(brand__id=1).order_by('name')
    #data = Product.objects.order_by('flag','name')   
    #data = Product.objects.order_by('flag','name')[0]
    #data = Product.objects.earliest('flag','name')
    #data = Product.objects.last()
    #data = Product.objects.all()[:5]
    #data = Product.objects.all()[5:10]
    #data = Product.objects.values('name','price','flag','brand__name')
    #data = Product.objects.values_list('name','price','flag','brand__name')
    #data = Product.objects.values_list('name','price','flag','brand__name').distinct()
    #data = Product.objects.only('name','price','flag','brand__name')
    #data = Product.objects.defer('tags')
    #data = Product.objects.defer('description')
    #data = Product.objects.all()
    
    # data = Product.objects.select_related('brand').all()    #select_related : one-to-one , one-to-many
    #data = Product.objects.prefetch_related('brand').all()    #prefetch_related : many-to-many
    
    #data = Product.objects.prefetch_related('brand').all() 
    #data = Product.objects.aggregate(Count('id')) 
    #data = Product.objects.aggregate(Sum('price')) 
    #data = Product.objects.aggregate(Max('price')) 
    #data = Product.objects.aggregate(Min('price'))
    #data = Product.objects.aggregate(mymin = Min('price'))
    #data = Product.objects.aggregate(mymin = Min('price'),mycount=Count('id'))
    
    #data = Product.objects.annotate(is_new=Value(True))
    #data = Product.objects.annotate(pric_with_tax=F('price')*1.2)
    #data = Brand.objects.annotate(posts=Count('product_brand'))