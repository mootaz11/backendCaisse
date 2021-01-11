from rest_framework.response import  Response
from rest_framework.decorators import  api_view,schema
import  rest_framework.status  as status
from ..models import OrderProduct
from .serializers import OrderProductSerializer




"""
function name : getAllOrderProducts

http-method: GET

Description :
this function returns a set of all orderProducts

parameters : 
request : the request coming from the front side in this parameter we find the body that the user sends to the server side


what the function Returns : Response(data=serializer.data,status=status.HTTP_200_OK)
 
 the function returns a json response that contains a set of orderProducts and a 200 status for the response 
"""


@api_view(['GET'])
def getAllOrderProducts(request):
    serializer = OrderProductSerializer(OrderProduct.objects.all(),many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)



