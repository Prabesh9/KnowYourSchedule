from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from KYSProject.service.account_service import AccountService


def signin(request):
    signup_html_page = loader.get_template('../ui/login.html')
    context = {}
    if request.method == 'POST':
        email = request.POST["txtEmail"]
        password =  request.POST["txtPassword"]
        if not email:
            context["error_msg"] = "Invalid email or password."
        else:
            account_service = AccountService()
            user = account_service.signin(email, password)
            if user is None:
                context["error_msg"] = "Invalid email or password."
            else:
                request.session["login_user"] = user
                context["success_msg"] = "Login successful."
                return redirect("admindashboard")
    return HttpResponse(signup_html_page.render(context, request))


