from rest_framework.response import  Response
from rest_framework.decorators import  api_view,schema
import  rest_framework.status  as status
from ..models import Product
from .serializers import ProductSerializer

@api_view(['POST'])
def createProduct(request):
    serializer=ProductSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    else :
        return  Response(data=None,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def getAllProducts(request):
    serializer = ProductSerializer(Product.objects.all(),many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)



@api_view(['DELETE'])
def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response(data='Product deleted  ! ',status=status.HTTP_200_OK)

