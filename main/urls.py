from django.contrib import admin
from django.urls import path, include

from apps.courses.views import CategoryListView, CategoryDetailView

api_v1 = [
    path("categories/", CategoryListView.as_view()),
    path("category/<int:pk>", CategoryDetailView.as_view())
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/", include(api_v1))
]

