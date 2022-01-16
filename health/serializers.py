from rest_framework import serializers

from .models import Category, Trainer


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("name",)


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TrainerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"


class TrainerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"