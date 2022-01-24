from django.urls import path
from mainapp import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.ProductsListView.as_view(), name='products'),
    path('category/<int:pk>/', mainapp.ProductsListView.as_view(), name='category'),
    # path('category/<int:pk>/<page>/', mainapp.products, name='category_page'),
    path('product/<int:pk>/', mainapp.product, name='product'),

]

