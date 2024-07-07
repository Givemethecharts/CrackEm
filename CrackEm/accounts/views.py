from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.views import View

from CrackEm.accounts.forms import AppUserCreationForm

OUR_USER = get_user_model()


# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = AppUserCreationForm
        return render(request, 'common/register-page.html', {'form': form})

    def post(self, request):
        form = AppUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            domain = '127.0.0.1:8000'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = f"http://{domain}{reverse('activate', kwargs={'uidb64': uid, 'token': token})}"
            print(activation_link)
            mail_subject = "Activate your account"
            message = render_to_string('common/acc_active_email.html',
                                       {'user': user,
                                        'domain': current_site.domain,
                                        'uid': uid,
                                        'token': token})
            to_email = form.cleaned_data.get('email')
            send_mail(mail_subject, message, 'cardamon6070@gmail.com', [to_email])
            return redirect('account_activation_sent')
        return render(request, 'common/register-page.html', {'form': form})


class Activate(View):
    def get(self, request, uidb64, token):

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = OUR_USER.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, OUR_USER.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('home-page')
        else:
            return render(request, 'common/activation_invalid.html')

