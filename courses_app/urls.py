from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("add_course/", views.add_course),
    path("courses/destroy/<int:course_id>/", views.remove_page), # id coming from db at index page
    path("remove_course/<int:course_id>/", views.remove_course),
    # path("courses/<int:course_id>/",views.index),
]
