from django.views import generic
from django.shortcuts import reverse
from .forms import CustomSignupForm


class SignupView(generic.CreateView):
    """
    User signup view
    """
    template_name = "registration/signup.html"
    form_class = CustomSignupForm

    def get_success_url(self):
        """
        Success URL
        :return:
        """
        return reverse("login")
