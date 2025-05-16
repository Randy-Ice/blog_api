from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.request import Request

#* Sorting, filtering, pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
#*end

from .models import Blog, Comment, Author, Category, Tag
from .permissions import IsAuthorOrReadOnly, IsAuthorOrReadOnlyProfile
from .serializers import SimpleBlogSerializer, DetailBlogSerializer, CommentCRUDSerializer, \
    CommentPostSerializer, AuthorPostSerializer, CategoryPostSerializer, TagPostSerializer


# Create your views here.

class BlogSimpleView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = SimpleBlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'tags']
    search_fields = ['title__istartswith', 'body']
    ordering_fields = ['created_at', 'updated_at', ]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = DetailBlogSerializer
    permission_classes = [IsAuthorOrReadOnly]


class CommentsView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentPostSerializer
    permission_classes = [IsAuthenticated]

class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCRUDSerializer
    permission_classes = [IsAuthenticated ,IsAuthorOrReadOnly]

class AuthorPostView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorPostSerializer
    permission_classes = [IsAuthenticated]

class AuthorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorPostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnlyProfile]
    @action(detail=False)
    def me(self, request):
        return Request(request.user.id)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryPostSerializer
    permission_classes = [IsAdminUser]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagPostSerializer
    permission_classes = [IsAdminUser]