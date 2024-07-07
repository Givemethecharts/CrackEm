from django.urls import path
from django.views.generic import TemplateView

from CrackEm.accounts.views import RegisterView, Activate

urlpatterns = (path('register/', RegisterView.as_view(), name='register-page'),
               path('account_activation_sent/', TemplateView.as_view(template_name='common/account_activation_sent.html'),
                    name='account_activation_sent'),
               path('activate/<uidb64>/<token>/', Activate.as_view(), name='activate'))
