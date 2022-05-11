# from wsgiref.simple_server import demo_app
# from users.models import User
# from django.shortcuts import get_object_or_404
# from users.serializers import UserSerializer
# from rest_framework.decorators import action
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import permissions

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = [(permissions.IsAuthenticated)]
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user, context={'request': request})
#         return Response(serializer.data)

# user_list = UserViewSet.as_view({'get': 'list'})
# user_retrieve = UserViewSet.as_view({'get': 'retrieve'})