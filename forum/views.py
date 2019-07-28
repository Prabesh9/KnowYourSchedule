from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

from model.forum import Forum
from service.forum_service import ForumService

import os


def delete_forum(request):
    if request.POST and "login_user" in request.session:
        forum_id = request.POST["txtForumId"]
        forum_service = ForumService()
        forum_service.delete(forum_id)
    return redirect("index")

def index(request):
    index_page = loader.get_template("../ui/forum.html")
    context = {}
    if "login_user" in request.session:
        context["login_user"] = request.session["login_user"]
        if request.POST:
            title = request.POST["txtTitle"]
            tag = request.POST["txtTags"]
            body = request.POST["txtBody"]
            forum = Forum()
            if request.FILES and "forumImage" in request.FILES:
                forum_image = request.FILES["forumImage"]
                fs = FileSystemStorage()
                path = os.path.join("static/uploads", forum_image.name)
                saved_file = fs.save(path, forum_image)
                file_path = fs.url(saved_file)
                forum.forum_image = file_path
            forum.title = title
            forum.tag = tag
            forum.body = body
            forum.user = request.session["login_user"]
            context["forum"] = forum
            if not title:
                context["error_msg"] = "Invalid title"
            elif not tag:
                context["error_msg"] = "Invalid tag"
            elif not body:
                context["error_msg"] = "Forum body can't be empty."
            else:
                forum_service = ForumService()
                result = forum_service.save(forum)
                if result is None:
                    context["error_msg"] = "Could not save forum."
                else:
                    del context["forum"]
                    context["success_msg"] = "Forum saved successfully."
    else:
        return redirect("signin")
    return HttpResponse(index_page.render(context, request))