from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from model.user import User
from model.user_register import UserRegister
from service.account_service import AccountService


def signout(request):
    request.session.flush()
    return redirect("signin")

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
                return redirect("index")
    return HttpResponse(signup_html_page.render(context, request))


def signup(request):
    signup_html_page = loader.get_template('../ui/signup.html')
    context = {}
    if request.method == 'POST':
        full_name = request.POST["txtFullname"]
        email = request.POST["txtEmail"]
        password =  request.POST["txtPassword"]
        cpassword = request.POST["txtCPassword"]
        user = User()
        user.full_name = full_name
        user.email = email
        user_register = UserRegister()
        user_register.user = user
        user_register.password = password
        user_register.cpassword = cpassword
        context["user_register"] = user_register
        if not full_name or len(str(full_name).strip(' ')) <= 4:
            context["error_msg"] = "Invalid full name."
        elif not email:
            context["error_msg"] = "Invalid email."
        elif not password or len(str(password).strip(' ')) <= 7:
            context["error_msg"] = "Password must be 8 character long."
        elif not cpassword or cpassword != password:
            context["error_msg"] = "Password don't match."
        else:
            account_service = AccountService()
            service_response = account_service.signup(user_register)
            if service_response is None:
                context["error_msg"] = "Could not save user."
            else:
                context["success_msg"] = "User saved successfully."

    return HttpResponse(signup_html_page.render(context, request))
