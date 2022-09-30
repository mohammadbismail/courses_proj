from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages


def index(request):
    context = {
        "courses": Course.objects.all(),
    }
    return render(request, "index.html", context)


def remove_page(request, course_id):
    context = {
        "courses": Course.objects.all(),
        "course": Course.objects.get(id=course_id),
    }
    return render(request, "delete_course.html", context)


def add_course(request):

    errors = Course.objects.validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
    else:
        Course.objects.create(
            name=request.POST["name"],
            description=request.POST["desc"],
        )
    return redirect("/")


def remove_course(reuqest, course_id):
    course_to_remove = Course.objects.get(id=course_id)
    course_to_remove.delete()

    return redirect("/")
