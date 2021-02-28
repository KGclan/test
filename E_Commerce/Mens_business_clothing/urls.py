from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseView.as_view(),name='index'),
    path('<slug:slug>/',views.ProductDetailView.as_view(),name = 'ProductDetail'),
    path('category/<slug:slug>/',views.CategoryView.as_view(),name = 'Category'),
    path('subcategory/<slug:slug>/',views.SubcategoryView.as_view(),name = 'Subcategory'),
    path('basket/<str:username>/',views.ShopBasket.as_view(), name = 'Basket'),
    path('basketdel/<int:id>/',views.ShopBasketDelete.as_view(), name = 'BasketDel'),
    path('order/<str:username>/',views.Order.as_view(), name = 'order'),
]