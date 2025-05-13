from django.urls import path
from blog.views import BlogSimpleView, BlogDetailView, CommentsView, CommentDetailView, AuthorPostSerializer, \
    AuthorDetailView, AuthorPostView

urlpatterns = [
    path('blogs/', BlogSimpleView.as_view()),
    path('blogs/<uuid:pk>/', BlogDetailView.as_view()),
    path('comments/', CommentsView.as_view()),
    path('comments/<uuid:pk>/', CommentDetailView.as_view()),
    path('profile/me/', AuthorPostView.as_view()),
    path('profile/me/<uuid:pk>/', AuthorDetailView.as_view()),
]