from django.conf.urls import url
from ..OrderProduct.views import getAllOrderProducts



"""
in this file we define the routes that we are going to use in orderProduct api  defined in urlpatterns
    url('getAll/',getAllOrderProducts,name='all_order_products') : get all order products
"""

urlpatterns=[
    url('getAll/',getAllOrderProducts,name='all_order_products'),
]


