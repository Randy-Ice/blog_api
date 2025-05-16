from django.contrib import admin
from .models import Blog, Category, Tag, Comment, Author
# Register your models here.

#customize admin interface
admin.site.site_header = "Blog Admin"
admin.site.site_title = "Heyoo"
admin.site.index_title = "Blog data is here ohyeah"

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

   list_display = ['title', 'body','category' ,'author',
                   'created_at', 'important', 'number_of_comments', 'number_of_tags']
   list_editable = ['category' ,'important']
   list_per_page=10
   list_select_related = ['author']
   list_prefetch_related = ['tags']
   search_fields = ['title__istartswith', 'body__istartswith']
   #istartswith, icontains, iendswith
   list_filter = ['important', 'created_at', 'category', 'tags']
   prepopulated_fields = {
       'slug': ['title']
   }
   autocomplete_fields = ['category', 'tags']


   @admin.display(ordering='body')
   def snippet(self, obj):
       return obj.body[:25] + "..."

   @admin.display(ordering='comments')
   def number_of_comments(self, obj):
       return obj.comments.count()

   @admin.display(ordering='tags')
   def number_of_tags(self, obj):
       return obj.tags.count()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id', 'title']
    list_editable=['title']
    search_fields=['title']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['id', 'name']
    list_editable=['name']
    search_fields=['name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['id', 'author','blog', 'title']
    list_editable=['title']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=[
        'id',

        'birth_date',
        'bio'
    ]
    list_editable=['birth_date', 'bio']


