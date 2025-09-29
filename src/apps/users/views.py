from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, SignInForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/sign_up.html"
    success_url = reverse_lazy("users:sign_in")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Sign up completed successfully! Please sign in to continue."
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_action"] = reverse_lazy("users:sign_up")
        return context


class SignInView(LoginView):
    template_name = 'users/sign_in.html'
    form_class = SignInForm

    def form_valid(self, form):
        messages.success(self.request, 'Sign in successful!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid email or password.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_action"] = reverse_lazy("users:sign_in")
        return context
