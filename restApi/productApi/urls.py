from django.conf.urls import url
from ..productApi.views import createProduct,getAllProducts,deleteProduct



"""
in this file we define the routes that we are going to use in product api  defined in urlpatterns

    url('create/',createProduct,name='create_product'), : create a product 
    url('getAll/',getAllProducts,name='all_products'), : get all products in the database
    url('delete/<str:pk>/',deleteProduct,name="delete_product") : delete a product by a given id passed in params

"""

urlpatterns=[
    url('create/',createProduct,name='create_product'),
    url('getAll/',getAllProducts,name='all_products'),
    url('delete/<str:pk>/',deleteProduct,name="delete_product")
]


