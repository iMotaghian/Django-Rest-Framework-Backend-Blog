from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    GenericAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .paginations import DefaultPagination
from .serializers import PostSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly
from ...models import Post, Category  # ech '.' is back folder


############### model view set ############
class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["category", "author", "status"]
    search_fields = ["title", "content"]  # search_fields = ['=username', '=email']
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination

    # @action(methods=["get"],detail=False) # default method is get // detail=False: no need to pk (id or ...)
    # def get_ok(self,request): # http://127.0.0.1:8000/blog/api/v1/post/get_ok/
    #     return Response({'detail':'ok'})


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


################ viewset (post-list & post-detail) ################
"""
class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    
    def list(self, request):
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request,pk=None):
        post_object = get_object_or_404(self.queryset,pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
"""
############### class API view [Generic views] #################


class PostList(ListCreateAPIView):
    """getting a list of post and creating new post"""

    permission_classes = [IsAuthenticatedOrReadOnly]  # permissions for authenticated
    serializer_class = PostSerializer  # convert json to from for POST method
    queryset = Post.objects.filter(
        status=True
    )  # posts = Post.objects.filter(status=True) # jay in queryset migire


class PostDetail(RetrieveUpdateDestroyAPIView):
    """getting details of a post and edit or remove a post"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


# with APIView
'''
class PostList(APIView):
    """getting a list of post and creating new post"""
    permission_classes = [IsAuthenticatedOrReadOnly] # permissions for authenticated
    serializer_class = PostSerializer # convert json to from for POST method
    
    def get(self, request):
        """send a list of post"""
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True) # by default many is false (for more than one object need true many)
        return Response(serializer.data)
    
    def post(self, request):
        """create a new post"""
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''

'''
class PostDetail(APIView):
    """getting details of a post and edit or remove a post"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    def get(self, request, id):
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post) # serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, id):
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
'''

# with mixins class
'''
class PostDetail(GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    """getting details of a post and edit or remove a post"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    # lookup_field = "id" #### in urls use pk: path('post/<int:pk>/',views.PostDetail.as_view(), name="post-detail"),
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''
############################## function base view #################
"""
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated]) # important: NEED set after api_view ### [IsAuthenticatedOrReadOnly] [IsAdminUser]
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True) # by default many is false (for more than one object need true many)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
"""

"""
@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request,id):
    post = get_object_or_404(Post,pk=id,status=True) # 404
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
"""
############################## 404 (try & except) #############################
"""
@api_view()
def postDetail(request,id):
    try:
        post = Post.objects.get(pk=id)
        #print(post.__dict__)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({"detail":"Post does not exist"},status=status.HTTP_404_NOT_FOUND) 
"""
