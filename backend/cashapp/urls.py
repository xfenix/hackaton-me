from django.conf import settings
from django.contrib import admin
from django.urls import path

from cashapp import views


admin.site.site_header = settings.APP_TITLE
urlpatterns = [
    path('make-order/', views.MakeOrderView.as_view(), name='make_order'),
    path('make-qr/<str:alias>/', views.MakeQr.as_view(), name='make_qr'),
    path('fetch-event-info/<str:alias>/', views.FetchEventView.as_view(), name='fetch_event_info'),
    path('pdf417-code/<str:uuid>/', views.Pdf417CodeView.as_view(), name='pdf417_code'),
    path('finish-order/<str:uuid>/', views.FinishOrderView.as_view(), name='finish_order'),
    path('sbp-webhook/', views.SBPWebhookView.as_view(), name='sbp_webhook'),
]
