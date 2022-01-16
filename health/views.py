from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, CreateView, ListView
from rest_framework import generics
from rest_framework.response import Response

from .forms import *
from rest_framework.views import APIView
from .serializers import CategoryListSerializer, CategoryDetailSerializer,\
    CategoryCreateSerializer, TrainerListSerializer, TrainerDetailSerializer


from .models import *


class HomeView(TemplateView):

    def get(self, request):

        return render(
            request,
            'base.html',
            {
                'services': Service.objects.all(),
                'trainers': Trainer.objects.all().select_related(),
                'schedules': Schedule.objects.all(),
                'prices': Price.objects.all(),

            }
        )


class ServiceView(TemplateView):

    def get(self, request):
        services = Service.objects.all()
        return render(
            request,
            'health/service.html',
            {
                'services': services
            }
        )


class AboutView(TemplateView):

    def get(self, request):
        trainers = Trainer.objects.all()
        return render(
            self.request,
            'health/about.html',
            {
                'trainers': trainers
            }
        )


class PriceView(TemplateView):

    def get(self, request):
        return render(
            request,
            'health/price.html',
            {
                'prices': Price.objects.all()
            }
        )


class ScheduleView(TemplateView):
    def get(self, request):
        return render(
            request,
            'health/class.html',
            {'schedules': Schedule.objects.all()}
        )


class TrainerView(TemplateView):
    def get(self, request):
        return render(
            request,
            'health/trainer.html',
            {'trainers': Trainer.objects.all()}
        )


class PoseView(TemplateView):
    def get(self, request):
        return render(
            request,
            'health/pose.html',
            {'poses': Pose.objects.all()}
        )


class ContactView(TemplateView):

    def get(self, request):
        form = ApplicationForm()
        return render(
            request,
            'health/contact.html',
            {
                'form': form
            }
        )

    def post(self, request):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(
            request,
            'health/contact.html',
            {
                'form': form
            }
        )


class BlogView(TemplateView):
    def get(self, request):
        return render(request, 'health/blog.html', {'posts': Blog.objects.all()})


class SinglePageView(DetailView):
    model = Blog
    template_name = 'health/single_page.html'
    slug_url_kwarg = 'id'
    context_object_name = 'post'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Blog, id=id_)


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)


class CategoryCreateView(APIView):
    def post(self, request):
        category = CategoryCreateSerializer(data=request.data)
        if category.is_valid():
            category.save()
        return Response(status=201)


class TrainersListView(generics.ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerListSerializer


class TrainersDetailView(generics.RetrieveAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerDetailSerializer