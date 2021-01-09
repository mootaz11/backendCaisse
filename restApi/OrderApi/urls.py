from django.conf.urls import url
from ..OrderApi.views import passOrder,createOrder,getpassedOrders,updateOrder,getOrder
from django.urls import path

urlpatterns=[
    url('create/',createOrder,name="create_order"),
    url('pass/<str:pk>',passOrder,name='pass_order'),
    url('getHistorical/',getpassedOrders,name="passed_orders"),
    path('update/<str:pk>/',updateOrder,name="update_order"),
    path('<str:pk>/',getOrder, name="get_order")
]


