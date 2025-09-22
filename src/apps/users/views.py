from django.shortcuts import render


def sign_up_view(request):
    return render(request, "users/sign_up.html")


def sign_in_view(request):
    return render(request, "users/sign_in.html")
