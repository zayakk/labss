from django.db import connection
from django.shortcuts import get_object_or_404, render
from salbar.models import Product, Category

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'products': products,
        'category': categories   # ← энэ нэрийг template-тайгаа тааруул
    })
def cart(request):
    return render(request, 'cart.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def order_complete(request):
    return render(request, 'order_complete.html')
def place_order(request):
    return render(request, 'place_order.html')
def product_detail(request):
    return render(request, 'product-detail.html')
def register(request):
    return render(request, 'register.html')
def search_result(request):
    return render(request, 'search-result.html')
def signin(request):
    return render(request, 'signin.html')
def home(request):
    products = Product.objects.all().filter(is_available =True)
    context = {
        'products': products
    }
    return render(request, 'home.html', context)
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)
        
    count = products.count()
    context = {
        'products': products,
        'count': count,
    }
    return render(request, 'store/store.html', context)

