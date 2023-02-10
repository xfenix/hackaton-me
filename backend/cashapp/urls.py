from django.urls import path

from cashapp import views


urlpatterns = [
    path('make-order/', views.MakeOrderView.as_view(), name='make_order'),
    path('make-qr/<str:alias>/', views.MakeQr.as_view(), name='make_qr'),
    path('fetch-event-info/<str:alias>/', views.FetchEventView.as_view(), name='fetch_event_info'),
    path('pdf417-code/<str:uuid>/', views.Pdf417CodeView.as_view(), name='pdf417_code'),
]
