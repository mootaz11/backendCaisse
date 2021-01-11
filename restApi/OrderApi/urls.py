from django.conf.urls import url
from ..OrderApi.views import passOrder,createOrder,getpassedOrders,updateOrder,getOrder
from django.urls import path

"""
in this file we define the routes that we are going to use in order api  defined in urlpatterns

    url('passed/', getpassedOrders, name="passed_orders") : get all passed orders 
    url('create/',createOrder,name="create_order") :  create an order
    path('pass/<str:pk>/',passOrder,name='pass_order') : pass the order and generate the order ticket 
    path('update/<str:pk>/',updateOrder,name="update_order") :  update the order by adding products and update the total with making a consideration to the offers
    path('<str:pk>/',getOrder, name="get_order") :  get the order by the given id 


"""


urlpatterns=[

    url('passed/', getpassedOrders, name="passed_orders"),
    url('create/',createOrder,name="create_order"),
    path('pass/<str:pk>/',passOrder,name='pass_order'),
    path('update/<str:pk>/',updateOrder,name="update_order"),
    path('<str:pk>/',getOrder, name="get_order"),

]



