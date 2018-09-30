from django.conf.urls import url, include

from wallet import views


urlpatterns = [
    url(
        r'^deposit/(?P<option_id>\d+)/return/(?P<invoice_id>\d+)/$',
        views.deposit_return,
        name='deposit_return',
    ),
    url(
        r'^deposit/(?P<option_id>\d+)/return/(?P<invoice_id>\d+)/cancel/$',
        views.deposit_cancel,
        name='deposit_cancel',
    ),
    url(
        r'^report/$', views.wallet_report, name='wallet_report',
    ),
]
