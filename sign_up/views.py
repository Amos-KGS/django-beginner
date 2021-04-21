from django.shortcuts import render, redirect
from .forms import SignupForm
# Create your views here.
def sign_up(response):
    if response.method == "POST":
        form = SignupForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")    
    else:
        form = SignupForm() 
               
    return render(response, "sign_up/signup.html", {"form": form})
    
    