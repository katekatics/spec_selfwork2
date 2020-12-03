from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item


class ItemsListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "list_items.html"
    context_object_name = "items"
    login_url = 'login'


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "detail_item.html"
    context_object_name = "item"
    login_url = 'login'


class ItemEditView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "edit_item.html"
    fields = ("title", "price", "amount")
    context_object_name = "item"
    login_url = 'login'


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "delete_item.html"
    success_url = reverse_lazy("list_items")
    login_url = 'login'


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "new_item.html"
    fields = ("title", "price", "amount")
    login_url = 'login'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
