from django.db import connection
from django.shortcuts import get_object_or_404, render
from salbar.models import Product, Category
import sqlite3 as sql

def home(request):
    con = sql.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute(
        '''
        SELECT * FROM tbl_products
        WHERE is_available=1
        ORDER BY id DESC
        LIMIT 5
    '''
    )
    products = cur.fetchall()
    product_count = len(products)
    con.close()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'home.html', context)

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'products': products,
        'category': categories,  
    })
def cart(request):
    return render(request, 'cart.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def order_complete(request):
    return render(request, 'order_complete.html')
def place_order(request):
    return render(request, 'place_order.html')
def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(
        Product,
        category__slug=category_slug,
        slug=product_slug,
        is_available=True
    )
    return render(request, 'product-detail.html', {'product': product})
def register(request):
    return render(request, 'register.html')
def search_result(request):
    return render(request, 'search-result.html')
def signin(request):
    return render(request, 'signin.html')   


def store(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()

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
    return render(request, 'store.html', context)

