from .models import *
from salbar.models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links= links)