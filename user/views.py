from django.shortcuts import render, reverse, redirect
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

# Create your views here.


@login_required
def profile_view(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "profile updated")
            return redirect("user:profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    # print(request.user.username, "ddddd")
    return render(request, "user/profile.html", context)


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            Profile.objects.create(user=new_user)
            messages.success(request, "User created Successfully")
            return HttpResponseRedirect(reverse("user:login"))
    else:
        user_form = UserRegistrationForm()

    return render(request, "user/register.html", {"user_form": user_form})
