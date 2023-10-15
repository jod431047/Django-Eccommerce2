from django.shortcuts import render , redirect
from django.views.generic import ListView
from .models import Order , Cart , CartDetail
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from settings.models import DeliveryFee


class OrderList(LoginRequiredMixin, ListView):
    model = Order
    paginate_by = 1
    def get_queryset(self):
        queryset = super().get_queryset()    # return all orders
        queryset = queryset.filter(user=self.request.user) # filter the current user
        return queryset
    
    
   
def checkout_page(request):
    cart = Cart.objects.get(user=request.user ,completed=False)
    cart_detail =   CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last()
    
    sub_total = cart.cart_total()
    print(sub_total)
    discount = 0
    total = sub_total + delivery_fee.fee
    
    
    return render(request,'orders/checkout.html',{
        'cart_detail':cart_detail ,
        'delivery_fee' : delivery_fee ,
        'sub_total' : sub_total ,
        'total' : total , 
        'discount' : discount
        })
   
   
   
   
   
   
 
def add_to_cart(request):
    # get data from frontend
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = request.POST['quantity']
    # get cart data
    cart = Cart.objects.get(user=request.user,completed=False)
    cart_detail , created = CartDetail.objects.get_or_create(cart=cart , product=product)
    cart_detail.quantity = quantity
    cart_detail.price = product.price
    cart_detail.total = round(int(quantity) * product.price,2)
    cart_detail.save()
    return redirect(f'/products/{product.slug}')