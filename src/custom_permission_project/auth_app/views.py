from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response


class UserAPI(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)
    
    def get(self,request):    
        users = User.objects.all()
        serializer = self.get_serializer(users, many=True)
        return Response(data=serializer.data, status=200)