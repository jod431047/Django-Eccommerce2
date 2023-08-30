from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializers 
from .models import Product



@api_view(['GET'])
def product_list_api(request):
    queryset = Product.objects.all()[:10]
    data = ProductSerializers(queryset,many=True).data
    return Response({'data':data})