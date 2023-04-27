from django.urls import path

from .views import HomePageView, AboutPageView, ThingListView, ThingDetailView, ThingCreateView, ThingUpdateView, ThingDeleteView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path('list/', ThingListView.as_view(), name='list_view'),
    path('<int:pk>/', ThingDetailView.as_view(), name='detail_view'),
    path('create/', ThingCreateView.as_view(), name='create_view'),
    path('<int:pk>/update', ThingUpdateView.as_view(), name='update_view'),
    path('<int:pk>/delete', ThingDeleteView.as_view(), name='delete_view'),
]
