from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from service.forum_service import ForumService


def index(request):
    index_html_page = loader.get_template('../ui/index.html')
    context = {"title": "Welcome to NCCS forum site!"}
    if "login_user" in request.session:
        context["login_user"] = request.session["login_user"]
    forum_service = ForumService()
    context["forums"] = forum_service.get_all_forums()
    return HttpResponse(index_html_page.render(context, request))


def about(request):
    return HttpResponse("This is about page.")
