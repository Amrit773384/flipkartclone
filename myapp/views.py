from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from myapp.models import ProductDetails,ReviewDetails

# Create your views here.

def product_view(request,product_id):

    if request.method == "POST":

        review_obj = ReviewDetails(
            review=request.POST.get('review'),
            product_id=ProductDetails.objects.get(product_id=request.POST.get('product_id')) ,
            user=request.POST.get('user')
            )
        review_obj.save()

        reviews = ReviewDetails.objects.filter(product_id=request.POST.get('product_id'))[::-1]
        return render(request,'productview.html',{'message':'Review Successfully added.',                 'product':ProductDetails.objects.get(product_id=request.POST.get('product_id')),
            'reviews':reviews})

    product = ProductDetails.objects.get(product_id=product_id)
    reviews = ReviewDetails.objects.filter(product_id=product_id)[::-1]
    return render(request,'productview.html',{'request':request,'product':product,
    'star':range(product.units),
    'notstar':range(5-product.units),
    'reviews':reviews
    })


def addproduct_view(request):
    if request.method == "POST" and request.user.is_authenticated:
        try:
            product_obj = ProductDetails(product_name=request.POST.get('product_name'),
                title=request.POST.get('title'),
                product_prophile = request.FILES.get('product_prophile'),
                brand = request.POST.get('brand'),
                price = request.POST.get('price'),
                stars = request.POST.get('stars'),
                units = request.POST.get('units'),
                )
            product_obj.save()
        except Exception as e:
            print(e)
            return render(request,'addproduct.html',{'request':request,
                                                    'error':'Something Went wrong ! '})
        return render(request,'addproduct.html',{'request':request,'status':'OK'})
    elif request.user.is_authenticated:
        return render(request,'addproduct.html',{'request':request})
    else:
        return redirect('/')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        print(user)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('/')
        else:
            return render(request,'login.html',context={'error':'User not Fount !'})
    return render(request,'login.html',context={})

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    if request.user.is_authenticated:
        all_products = ProductDetails.objects.all()
        return render(request,'home.html',context={'request':request,'product_list':all_products})
        print('user is authenticated')
    return redirect('/login/')