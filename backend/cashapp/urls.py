
from django.urls import path
from cashapp import views

urlpatterns = [
    path('make-order/', views.MakeOrderView.as_view(), name='make_order'),
    path('make-qr/<str:event_id>/', views.MakeQr.as_view(), name='make_qr'),
]
