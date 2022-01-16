from django.db import models
from django.db.models import CASCADE
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField("Service", max_length=150)
    description = models.TextField("Description")
    image = models.ImageField(null=True, blank=True, upload_to='servicephoto')

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=150, null=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='trainerphoto')

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    plan = models.ManyToManyField(Plan, null=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    name = models.CharField("Schedule", max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    meeting = models.DateTimeField()
    image = models.ImageField(null=True, blank=True, upload_to='schedulephoto')
    trainer_image = models.ImageField(null=True, blank=True, upload_to='trainerphoto')

    def __str__(self):
        return self.name


class Pose(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posephoto')


class Application(models.Model):
    name = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=True)
    subject = models.CharField(max_length=150, null=True)
    message = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=150, null=True)
    date = models.DateTimeField(auto_now_add=True)
    url = models.SlugField(max_length=160, unique=True)
    service = models.ForeignKey(Category, verbose_name="category", on_delete=models.CASCADE)
    text = models.TextField(null=True)
    image = models.ImageField(null=True, blank=True, upload_to='blogphoto')

    def __str__(self):
        return self.name

    def get_comments(self):
        return self.comment.all()




class Social(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()