from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        cover = request.data['cover']
        title = request.data['title']
        description=request.data['description']
        Book.objects.create(title=title,description=description, cover=cover)
        return HttpResponse({'message': 'Book created'}, status=200)

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Delete the book's cover image file and description file from the server filesystem
        instance.cover.delete()
        instance.delete_description_file()  # Custom method to delete the associated description file

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
class LikeBook(APIView):
    def post(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            book.like_count += 1
            book.save()
            return Response({'message': 'Liked successfully', 'like_count': book.like_count})
        except Book.DoesNotExist:
            return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        book = self.get_object()
        book.like_count += 1
        book.save()
        return Response({'message': 'Liked successfully', 'like_count': book.like_count})
