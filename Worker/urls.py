
from django.contrib import admin
from django.urls import include, path
from salbar.views import (
    index, register, cart, dashboard, order_complete, product_detail, search_result, store, signin, place_order
)
import Worker.settings as settings
from django.conf.urls.static import static
from salbar import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('store', include('salbar.urls') ),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

