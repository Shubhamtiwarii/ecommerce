import json
from django.http import JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib import messages
from ecommerce.settings import razor_pay_key_id,key_secret
import razorpay
from .forms import CustomerSignUpForm,CustomerLoginForm
from django.contrib.auth import login as dj_login,authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def store(request):
    Products=Product.objects.all()
    #for p in Products:
        #print(p.image.url)
    return render(request,"store.html",{'products':Products})

@login_required
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        cart,created=Cart.objects.get_or_create(customer=customer,completed=False)
        cartitems=cart.cartitems_set.all()
        
        #hipaddress=ShippingAddress.objects.get(customer=customer)
        #print(shipaddress.state)
    else:
        cartitems=[]
        cart={"get_cart_toal":0,"get_itemtotal":0}
    
    return render(request,"cart.html",{'cartitems':cartitems,'cart':cart})  
    #return render(request,"cart.html",{'cartitems':cartitems,'cart':cart,'ship':shipaddress})


def updateCart(request):
    data=json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    product=Product.objects.get(id=productId)
    customer=request.user.customer
    cart,created=Cart.objects.get_or_create(customer=customer,completed=False)
    cartitem,created=Cartitems.objects.get_or_create(cart=cart,product=product)
    if action == "add":
        cartitem.quantity+=1
        cartitem.save()

    return JsonResponse("Cart Updated",safe=False)

def updateQuantity(request):
    data=json.loads(request.body)
    quantityFieldValue=data['qfv']
    # if quantityFieldValue <= str(0):
    #     messages.error(request,'product can not below zero')
    #     return redirect('cart')
    # else:
    quantityFieldProduct=data["qfp"]
    product=Cartitems.objects.filter(product__name=quantityFieldProduct).last()
    product.quantity=quantityFieldValue
    product.save()
    return JsonResponse("Quantity update",safe=False)
    
def deleteProduct(request):
    data=json.loads(request.body)
    product_id=data["product_id"]
    print("hello",product_id)
    cart_item=Cartitems.objects.filter(product__id=product_id)
    cart_item.delete()
    return render(request,"cart.html")

def address_and_payment(request):
    customer=request.user.customer
    print(customer)
    #cart=request.cart
    #print(cart)
    if request.method=="POST":
        state=request.POST.get("state")
        city=request.POST.get("city")
        address=request.POST.get("address")
        zip=request.POST.get("zipcode")
        cart_id=request.POST.get("cart_id")
        #cart_id=Cart.objects.filter(id=cart_id)
        print(state,city,address,zip,cart_id)
        s=ShippingAddress(customer=customer,cart=cart_id,state=state,city=city,address=address,zipcode=zip)
        s.save()
        #client = razorpay.Client(auth=(razor_pay_key_id,key_secret))
        p=Cart.objects.get(id=cart_id)
        print(p)
        p.completed=True
        p.save()
        o=Order(cartt=p,status=0)
        o.save()
        return redirect('cart')

def signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            customer = Customer.objects.create(user=user, name=name, email=email)
            customer.save()
            # login(request, user)
            return redirect('store')  # Redirect to home page after signup
    else:
        form = CustomerSignUpForm()
    return render(request, 'signup.html', {'form': form})   
    

def login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                dj_login(request, user)
                return redirect('store')  # Redirect to home page after login
            else:
                error_message = "Invalid username or password"
    else:
        form = CustomerLoginForm()
        error_message = None
    return render(request, 'login.html', {'form': form, 'error_message': error_message})

@login_required
def logout_view(request):
    logout(request)
    return redirect("signup")

def order(request):
    customer=request.user.customer
    print(customer)
    
    orders= Order.objects.filter(cartt__customer=customer)

    cart_item=[]
    order_detail=[]
    for order in orders:
        #print(order.cartt)
        cart_item.extend(Cartitems.objects.filter(cart=order.cartt).all())
        #print(cart_item)
        order_detail.append({
            'order': order,
            'status': order.status,
            'cart':order.cartt.cart_id,
        })
    print(order_detail)
    
    
    
    return render(request,"order.html",{'order':order_detail,'cart_item':cart_item})
    