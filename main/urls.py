from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.courses.views import (
    CategoryListView,
    CategoryDetailView,
    CourseDetailView,
    CourseListView,
    FAQListView,
    FeedbackMessageCreateView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="EPAM",
      default_version='v1',
      description="username:user / password:user",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


api_v1 = [
    path("categories/", CategoryListView.as_view()),
    path("category/<int:pk>", CategoryDetailView.as_view()),
    path("courses/", CourseListView.as_view()),
    path("course/<int:pk>", CourseDetailView.as_view()),
    path('faq/', FAQListView.as_view()),
    path('feedback/', FeedbackMessageCreateView.as_view()),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_v1)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
