from rest_framework import serializers
from .models import Blog, Comment, Author, Tag, Category


class SimpleBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title', 'body', 'category', 'created_at']



class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','blog', 'author', 'title', 'created_at', 'updated_at']

class DetailBlogSerializer(serializers.ModelSerializer):
    comments = CommentPostSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title','body', 'author', 'category', 'tags', 'important','comments', 'created_at', 'updated_at']




class CommentCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'blog', 'author', 'title', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'blog', 'author']


class AuthorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'user_id', 'birth_date', 'bio']


class CategoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class TagPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at', 'updated_at']
