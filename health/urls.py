from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('price/', views.PriceView.as_view(), name='price'),
    path('class/', views.ScheduleView.as_view(), name='schedule'),
    path('trainer/', views.TrainerView.as_view(), name='trainer'),
    path('pose/', views.PoseView.as_view(), name='pose'),

    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<slug:id>/', views.SinglePageView.as_view(), name='single_page'),


    path('contact/', views.ContactView.as_view(), name='contact'),

]