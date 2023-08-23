from django.shortcuts import render , redirect
from django.views.generic import ListView
from .models import Order , Cart , CartDetail
from products.models import Product


class OrderList(ListView):
    model = Order
   
   
def add_to_cart(request):
    
    # get data frontend
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = request.POST['quantity']  
    
    #get cart
    cart = Cart.objects.get(user=request.user,completed=False) 
    
    #cart detail
    cart_detail , created = CartDetail.objects.get_or_create(cart=cart , product=product)
    cart_detail.quantity = quantity
    cart_detail.price = product.price
    cart_detail.total = round(int(quantity) * product.price,2)
    cart_detail.save()
    
    return redirect(f'/products/{product.slug}')
        #cart detail
    #cart_detail , created = CartDetail.objects.get_or_create(cart=cart , product=product)
    #if created :
        #cart_detail.quantity = quantity
    #else:
        #cart_detail.quantity += quantity
        
    #cart_detail.price = product.price
    #cart_detail.total = int(quantity) * product.price
    #cart_detail.save()