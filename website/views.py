from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
def home(request):
    # Check if logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect("home")
        else:
            messages.success(
                request, "There Was an Error Logging In Please Try Again ..."
            )
            return redirect("home")
    else:
        return render(request, "home.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out ... 'BYE'")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, "You've successfully registered — great to have you with us!"
            )
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})
