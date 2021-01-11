from rest_framework.response import  Response
from rest_framework.decorators import  api_view,schema
import  rest_framework.status  as status
from ..models import Product
from .serializers import ProductSerializer

"""
function name : createProduct

http-method: POST

Description :
this function returns a specific created product 

parameters : 
request : the request coming from the front side in this parameter we find the body that the user sends to the server side ,
the request contains the product that we want to create and add to our database


what the function Returns :Response(serializer.data,status=status.HTTP_201_CREATED)
 the function returns a json response that contains the the product created and status=201  which is the status of the server response 
"""


@api_view(['POST'])
def createProduct(request):
    serializer=ProductSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else :
        return  Response(data=None,status=status.HTTP_400_BAD_REQUEST)


"""
function name : getAllProducts

http-method: GET

Description :
this function returns a set of products 

parameters : 
request : the request coming from the front side in this parameter we find the body that the user sends to the server side,the request body can be empty


what the function Returns :Response(serializer.data,status=status.HTTP_201_CREATED)
 the function returns a json response that contains the products  and status=200  which is the status of the server response 
"""


@api_view(['GET'])
def getAllProducts(request):
    serializer = ProductSerializer(Product.objects.all(),many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)

"""
function name : getAllProducts

http-method: DELETE

Description :
this function returns a string message "Product deleted  !" when the product is deleted

parameters : 
request : the request coming from the front side in this parameter we find the body that the user sends to the server side,the request body can be empty
pk : is the param that we send in the route which presents the id of such product


what the function Returns :Response(data='Product deleted  ! ',status=status.HTTP_200_OK)
 the function returns a json response that contains a success message when the product is deleted  and status=200  which is the status of the server response 
"""


@api_view(['DELETE'])
def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response(data='Product deleted  ! ',status=status.HTTP_200_OK)

