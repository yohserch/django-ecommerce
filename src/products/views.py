from django.shortcuts import render
from django.views.generic import ListView, DetailView


from .models import Product

class ProductFeaturedListView(ListView):
    queryset = Product.objects.featured()
    template_name = "products/list.html"


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = "products/featured-detail.html"

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"
