from django.conf.urls import url
from ..productApi.views import createProduct,getAllProducts,deleteProduct




urlpatterns=[
    url('create/',createProduct,name='create_product'),
    url('getAll/',getAllProducts,name='all_products'),
    url('delete/<str:pk>/',deleteProduct,name="delete_product")
]


