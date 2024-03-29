from django.urls import path
from .views import ProductViewSet, UserAPIView

# add extra parameters: get points to list func etc
urlpatterns = [
    path("products", ProductViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "products/<str:pk>",
        ProductViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path("user", UserAPIView.as_view()),
]
