from rest_framework.response import  Response
from rest_framework.decorators import  api_view,schema
import  rest_framework.status  as status
from ..models import OrderProduct
from .serializers import OrderProductSerializer





@api_view(['GET'])
def getAllOrderProducts(request):
    serializer = OrderProductSerializer(OrderProduct.objects.all(),many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)



