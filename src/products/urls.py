from django.conf.urls import url

from .views import ProductListView, ProductDetailView, ProductFeaturedListView, ProductFeaturedDetailView


urlpatterns = [
    url(r'^$', ProductListView.as_view(), name="products-list"),
    url(r'^featured/$', ProductFeaturedListView.as_view(), name="products-featured-list"),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name="product-detail"),
    url(r'^featured/(?P<slug>[\w-]+)/$', ProductFeaturedDetailView.as_view(), name="product-featured-detail"),
]