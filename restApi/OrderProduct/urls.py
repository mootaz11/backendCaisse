from django.conf.urls import url
from ..OrderProduct.views import getAllOrderProducts




urlpatterns=[
    url('getAll/',getAllOrderProducts,name='all_order_products'),
]


