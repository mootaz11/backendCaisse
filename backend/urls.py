"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
"""
in this file we define the routes that we are going to use in the whole rest api  defined in urlpatterns

    url('admin/', admin.site.urls),
    url('api/order/',include('restApi.OrderApi.urls')), :  the bridge to the order api
    url('api/product/', include('restApi.productApi.urls')), : the route that connects us to product api 
    url('api/ticket/', include('restApi.ticketApi.urls')), : the route that connects us to ticket api
    url('api/productOrder/', include('restApi.OrderProduct.urls')), : the route that connects us to productOrder api 
            ]
            
            
            +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  : this instruction helps us to see the files stored in the media file 

"""

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/order/',include('restApi.OrderApi.urls')),
    url('api/product/', include('restApi.productApi.urls')),
    url('api/ticket/', include('restApi.ticketApi.urls')),
    url('api/productOrder/', include('restApi.OrderProduct.urls')),
            ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)