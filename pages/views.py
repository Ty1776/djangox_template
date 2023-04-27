from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Thing
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class ThingListView(ListView):
    template_name = 'list.html'
    model = Thing
    context_object_name = 'list_view'


class ThingDetailView(DetailView):
    template_name = 'detail.html'
    model = Thing


class ThingCreateView(CreateView):
    template_name = 'create.html'
    model = Thing
    fields = ['name', 'description', 'owner']


class ThingUpdateView(UpdateView):
    template_name = 'update.html'
    model = Thing
    fields = ['name', 'description', 'owner']


class ThingDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Thing
    success_url = reverse_lazy('list_view')
