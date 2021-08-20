# from django.http import JsonResponse
# from django.db import transaction
# from rest_framework.generics import GenericAPIView

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class UsersView(GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         users = self.get_queryset()
#         serializer = self.serializer_class(users, many=True)
#         data = serializer.data
#         return JsonResponse(data, safe=False)

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         try:
#             serializer = self.serializer_class(data=data)
#             serializer.is_valid(raise_exception=True)
#             with transaction.atomic():
#                 serializer.save()
#             data = serializer.data
#         except Exception as e:
#             data = {'error': str(e)}
#         return JsonResponse(data)