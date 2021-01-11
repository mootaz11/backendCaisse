from rest_framework.response import  Response
from rest_framework.decorators import api_view
from io import BytesIO
from ..OrderApi.serializers import OrderSerializer
from ..OrderProduct.serializers import  OrderProductSerializer
from ..models import Ticket,Order,OrderProduct,Product
from ..productApi.serializers import  ProductSerializer
from ..ticketApi.serializers import  TicketSerializer

from datetime import datetime
from django.core.files import File
from .utils import render_to_pdf

"""
function name : getOrder

http-method: GET

Description :
this function returns a specific order 

parameters : 
request : the request coming from the front side in this parameter we find the body that the user sends to the server side
pk : is the param that we send in the route which presents the id of such order


what the function Returns :
 the function returns a json response that contains the order and the products of this order 

"""
@api_view(['GET'])
def getOrder(request,pk):
    order = Order.objects.get(id=pk)
    serializedOrder = OrderSerializer(order,many=False)
    Orderproducts=order.orderProducts.all()
    products=[{'product':ProductSerializer(p.product,many=False).data,
               'orderProduct':OrderProductSerializer({'quantity':p.quantity,'order':p.order,'product':p.product}).data}
              for p  in Orderproducts]
    return Response({'products':products,'order':serializedOrder.data})


"""
function name : updateOrder

http-method: PATCH

Description :
this function returns a specific order 

parameters : 
request : the request coming from the front side in this parameter we find the body that the user sends to the server side,
the request contains the product that we want to add to our order and the quantity
pk : is the param that we send in the route which presents the id of such order


what the function Returns :
 the function returns a json response that contains the order by updating the orderProducts and update the total of a given order  
 and a 200 status which is the status of the server response
"""



@api_view(['PATCH'])
def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    serializer = OrderProductSerializer(data={
        'product': request.data['product']['id'],
        'quantity': request.data['quantity'],
        'order': int(pk)})
    if serializer.is_valid():
        if request.data['product']['id'] in [i.product.id for i in OrderProduct.objects.filter(order=pk)]:
            orderProduct=OrderProduct.objects.get(product=request.data['product']['id'])
            orderProduct.quantity+=1
            orderProduct.save()

        else:
            orderProduct=serializer.save()

        _total=order.total
        if (request.data['product']['offer'] == True):
            _total-=((request.data['product']['price'])*(OrderProductSerializer(orderProduct,many=False).data['quantity']-1))-\
                    (request.data['product']['price']*((OrderProductSerializer(orderProduct,many=False).data['quantity']-1)//3))

            orderProductTotal=((request.data['product']['price'])*(OrderProductSerializer(orderProduct,many=False).data['quantity']))-\
                              (request.data['product']['price']*(OrderProductSerializer(orderProduct,many=False).data['quantity']//3))

            _total+=orderProductTotal

        else:
            _total=_total-(request.data['product']['price'])*(OrderProductSerializer(orderProduct,many=False).data['quantity']-1)
            _total=_total+(request.data['product']['price'])*(OrderProductSerializer(orderProduct,many=False).data['quantity'])
    order.total=_total
    order.save()
    serializedOrder = OrderSerializer(order, many=False)

    return Response(serializedOrder.data,status=200)

"""
function name : createOrder

http-method: POST

Description :
this function returns a specific order 

parameters : 
request : the request coming from the front side in this parameter we find the body that the user sends to the server side ,
the request contains the product that we want to add to our new order and the quantity


what the function Returns : Response(serializedOrder.data,status=201)
 the function returns a json response that contains the order by updating the orderProducts and update the total of a given order and a 201 status 
 which is the status of the server response 
"""



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

    return Response(serializedOrder.data,status=201)

"""
function name : passOrder

http-method: POST

Description :
this function returns the ticket generated of the passed order , the ticket contains the date and 
the path of the pdf file stored in media/pdfs 

parameters : 
request : the request coming from the front side in this parameter we find the body that the user sends to the server side ,
the request contains the product that we want to add to our new order and the quantity
pk : is the param that we send in the route which presents the id of such order


what the function Returns : Response(ticket_serializer.data,status=200)
 the function returns a json response that contains the ticket by of a given order and a 200 status 
 which is the status of the server response 
"""



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
            i.delete()
            print(product.discount)
            if(product.offer and not product.discount):
                _products.append({'name':product.name,'price':product.price,'quantity':i.quantity,'total':(i.quantity*product.price),'reduction':"2 products = 1 free :"+str((i.quantity*product.price)-((i.quantity//3)*product.price))})
            if(product.discount and not product.offer):
                _products.append({'name':product.name,'price':product.price,'quantity':i.quantity,'total':(i.quantity*product.price),'reduction':"50% remise"+str((i.quantity*(product.price*0.5)))})
            if(product.discount and product.offer):
                _products.append({'name':product.name,'price':product.price,'quantity':i.quantity,'total':(i.quantity*product.price),'reduction':"50% remise + 2products= 1 free :"+str((i.quantity*product.price*0.5)-((i.quantity//3)*(product.price*0.5)))})
            if(not product.discount and not product.offer):
                _products.append({'name':product.name,'price':product.price,'quantity':i.quantity,'total':(i.quantity*product.price),'reduction':'no offers '+str((i.quantity*product.price))})




        order.passed=True
        order.save()
        pdf = render_to_pdf('ticketTemplate.html',  {'products':_products,
                                                        'GrandTotal':order.total
                                                        ,'DateTicket':str(order.date),'ticket_id':str(order.id)})

        ticket = Ticket(order=order)
        filename = "ticket_{date}.pdf".format(date=str(datetime.now()))
        ticket.pdf.save(filename, File(BytesIO(pdf.content)))
        ticket.save()
        ticket_serializer=TicketSerializer(ticket,many=False)


        return Response(ticket_serializer.data,status=200)

"""
function name : getpassedOrders

http-method: GET

Description :
this function returns a passed orders 

parameters : 
request : the request coming from the front side in this parameter we find the body that the user sends to the server side


what the function Returns :
 the function returns a json response that contains a set of passed orders { passed=True }

"""



@api_view(['GET'])
def getpassedOrders(request):
    orders=Order.objects.filter(passed=True)
    _orders=[]
    for order in orders:
        _orders.append({'order':OrderSerializer(order,many=False).data,'Ticket':str(order.ticket.pdf)})
    return Response(_orders)