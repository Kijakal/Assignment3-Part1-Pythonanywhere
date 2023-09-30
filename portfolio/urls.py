"""
URL configuration for investments project - portfolio app.
"""
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from portfolio import views

urlpatterns = [
    path('', views.customer_list),
    path('api/customers/', views.customer_list),
    path('api/mycustomers/', views.my_customer_list),
    path('api/customers/<int:pk>', views.getCustomer),
    path('api/investments/', views.investment_list),
    path('api/investments/<int:pk>', views.getInvestment),
    path('api/stocks/', views.stock_list),
    path('api/stocks/<int:pk>', views.getStock),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':
settings.MEDIA_ROOT}), #serve media files when deployed
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':
settings.STATIC_ROOT}), #serve static files when deployed
]

