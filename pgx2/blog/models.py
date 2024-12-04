from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']


class Category(models.Model):
    name = models.CharField(max_length=255)
    blog_post = models.ManyToManyField(BlogPost)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_category'


class Media(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="title")
    size = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="file size")
    description = models.TextField(
        verbose_name="description")
    age_limited = models.BooleanField(
        default=False,
        verbose_name="18+")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_media'


class Docs(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="title")
    size = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="file size")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_docs'
