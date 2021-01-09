from rest_framework.response import  Response
from django.template.loader import  get_template
from rest_framework.decorators import api_view
from django.http import  HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from ..OrderApi.serializers import OrderSerializer
from ..OrderProduct.serializers import  OrderProductSerializer
from ..models import Ticket,Order,OrderProduct
from ..productApi.serializers import  ProductSerializer

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



@api_view(['GET'])
def passOrder(request,pk):
    template = get_template('ticketTemplate.html')
    html = template.render({})
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    filename = "YourPDF_Order.pdf"
    # t.pdf.save(filename,pdf)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None




@api_view(['GET'])
def getpassedOrders(request):
    print('passed orders')