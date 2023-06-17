from django.contrib import admin

from apps.courses.models import Category, Photo, Course, Faq


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    pass
