from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(
        max_length=50, verbose_name="Название", unique=True
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.FileField(upload_to='photos/', verbose_name="Картина")

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.os.path.basename(self.image.name)


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=255, verbose_name="Подзаголовок")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория",
        related_name="Courses"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name='Описание Курса'
    )
    photo = models.ForeignKey(
        Photo, on_delete=models.CASCADE, verbose_name="Картина",
        related_name="Courses"
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title
