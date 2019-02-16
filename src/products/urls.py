from django.conf.urls import url

from .views import ProductListView


urlpatterns = [
    url(r'^$', ProductListView.as_view(), name="products_list"),
]