from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_page/", views.new_page, name="new_page"),
    path("random_page/",views.random_page, name="random_page"),

    path("<str:question_id>/",views.detail,name="detail"),
    path("<str:question_id>/edit_page/",views.edit_page,name="edit_page"),

]
