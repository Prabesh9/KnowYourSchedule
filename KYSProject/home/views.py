from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    index_html_page = loader.get_template('../UI/index.html')
    context = {"Welcome to NCCS forum site!"}
    return HttpResponse(index_html_page.render())


def admin(request):
    adminDash = loader.get_template('../UI/AdminDash.html')
    return HttpResponse(adminDash.render())


def adminEdit(request):
    adminEditor = loader.get_template('../UI/AdminEdit.html')
    return HttpResponse(adminEditor.render())


def adminAdd(request):
    adminAddView = loader.get_template('../UI/AddViewer.html')
    return HttpResponse(adminAddView.render())
