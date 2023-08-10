from rest_framework import routers

from api.views import BookListView, BookViewSet, LikeBook
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
     path('books/<int:pk>/like/', LikeBook.as_view(), name='like-book'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)