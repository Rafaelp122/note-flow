from django.shortcuts import render

from .forms import CustomUserCreationForm


def sign_up_view(request):
    form = CustomUserCreationForm
    context = {
        'form': form,
    }

    return render(request, "users/sign_up.html", context)


def sign_in_view(request):
    return render(request, "users/sign_in.html")
