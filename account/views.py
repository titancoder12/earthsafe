from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dlogin, logout as dlogout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        # Get details
        username = request.user.username
        email = request.user.email
        first_name = request.user.first_name
        last_name = request.user.last_name

        return render(request, "account/index.html", {
            "username": username,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
        })
    else:
        return HttpResponseRedirect(reverse("login"))

def viewaccount(request):
    pass

def register(request):
    if request.method == "POST":

        # Get details
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Check if username exists already
        if User.objects.filter(username=username).exists():
            return render(request, "account/register.html", {
                "alert": 'Error: Username already exists'
            })

        # Register user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()

        # Authenticate user
        user = authenticate(username=username, password=password)

        # Login user
        dlogin(request, user)

        # Return a redirect to main page after created account TODO
        return HttpResponseRedirect(reverse("index"))

    # Render registration page
    return render(request, "account/register.html")

def login(request):
    print("LOGIN!")
    if request.method == "POST":

        # Get details
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        # Login user if credentials are valid
        if user is not None:
            # Login user
            dlogin(request, user)

            # Redirect to main page
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "account/login.html", {
                "message": "Invalid Credentials."
            })

    # Render login page
    return render(request, "account/login.html")

def logout(request):
    dlogout(request)
    return HttpResponseRedirect(reverse("login"))
    