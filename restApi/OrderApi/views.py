from datetime import date

from rest_framework.response import  Response
from django.template.loader import  get_template
from rest_framework.decorators import api_view
from django.http import  HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from ..OrderApi.serializers import OrderSerializer
from ..OrderProduct.serializers import  OrderProductSerializer
from ..models import Ticket,Order,OrderProduct,Product
from ..productApi.serializers import  ProductSerializer
from datetime import datetime
from django.core.files import File
from .utils import render_to_pdf

@api_view(['GET'])
def getOrder(request,pk):
    order = Order.objects.get(id=pk)
    serializedOrder = OrderSerializer(order,many=False)
    Orderproducts=order.orderProducts.all()
    products=[{'product':ProductSerializer(p.product,many=False).data,
               'orderProduct':OrderProductSerializer({'quantity':p.quantity,'order':p.order,'product':p.product}).data}
              for p  in Orderproducts]
    return Response({'products':products,'order':serializedOrder.data})


@api_view(['PATCH'])
def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    serializer = OrderProductSerializer(data={
        'product': request.data['product']['id'],
        'quantity': request.data['quantity'],
        'order': int(pk)})

    if serializer.is_valid():
        if request.data['product']['id'] in [i.id for i in OrderProduct.objects.filter(order=pk)]:
            orderProduct=OrderProduct.objects.get(id=request.data['product']['id'])
            orderProduct.quantity+=1
            orderProduct.save()
        else:
            serializer.save()
        order.total = request.data['product']['price']*(OrderProductSerializer(orderProduct,many=False).data['quantity'])
        if (request.data['product']['offer'] == True):
            print(OrderProductSerializer(orderProduct,many=False).data['quantity']//3)
            order.total-=(request.data['product']['price']*(OrderProductSerializer(orderProduct,many=False).data['quantity']//3))
        order.save()

    serializedOrder = OrderSerializer(order, many=False)

    return Response(serializedOrder.data,status=200)


@api_view(['POST'])
def createOrder(request):
    order=Order()
    order.save()
    if(order.id):
        serializer = OrderProductSerializer(data={
            'product':request.data['product']['id'],
            'quantity':request.data['quantity'],
            'order':order.id})

        if serializer.is_valid():
            serializer.save()
            order.total=request.data['product']['price']
            order.save()
        serializedOrder=OrderSerializer(order,many=False)

    return Response(serializedOrder.data,status=200)



@api_view(['POST'])
def passOrder(request,pk):
        order = Order.objects.get(id=pk)
        serializedOrder = OrderSerializer(order,many=False)
        Orderproducts=order.orderProducts.all()
        _products=[]
        for i in Orderproducts:
            product=Product.objects.get(pk=i.product.id)
            product.stock-=i.quantity
            product.save()
            _products.append({'name':product.name,'price':product.price,'quantity':i.quantity,'total':i.quantity*product.price})
        order.passed=True
        order.save()
        pdf = render_to_pdf('ticketTemplate.html',  {'products':_products,
                                                        'GrandTotal':order.total
                                                        ,'DateTicket':str(order.date),'ticket_id':str(order.id)})

        ticket = Ticket(order=order)
        filename = "ticket_{date}.pdf".format(date=str(datetime.now()))
        ticket.pdf.save(filename, File(BytesIO(pdf.content)))
        ticket.save()

        return Response("order passed done !",status=200)


@api_view(['GET'])
def getpassedOrders(request):
    orders=Order.objects.filter(passed=True)
    print(orders)
    return Response("")