from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


app_name = "blog"  # related to path "5"

urlpatterns = [
    # # function base views
    path("1", views.indexView, name="function base view"),  # def
    # # class base views
    path(
        "2",
        TemplateView.as_view(
            template_name="testurl.html", extra_context={"name": "Class"}
        ),
        name="TemplateView",
    ),  # no views
    path("3", views.IndexView.as_view(), name="class base view"),  # TemplateView
    path(
        "4",
        RedirectView.as_view(url="https://www.google.com/"),
        name="RedirectView go to url",
    ),  # no views defined
    path(
        "5",
        RedirectView.as_view(pattern_name="blog:function base view"),
        name="edirectView go to pattern",
    ),  # no views defined
    path(
        "6",
        views.RedirectToMaktab1.as_view(),
        name="redirect-to-maktabkhooneh 1",
    ),  # RedirectView
    path(
        "7/<int:pk>",
        views.RedirectToMaktab2.as_view(),
        name="redirect-to-maktabkhooneh-with-pk",
    ),  # RedirectView
    path(
        "post/", views.PostListView.as_view(), name="post-list"
    ),  # in ListView for addressing need "/" and template is in templateS/blog/post_list.html base on ListView calss
    path(
        "post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail-view"
    ),  # class with DetailView - work with pk - close address with "/"
    path(
        "post/create/", views.PostCreateView.as_view(), name="post-create-view"
    ),  # FormView
    path(
        "post/create2/", views.PostCreateView2.as_view(), name="post-createview"
    ),  # CreateView
    path(
        "post/<int:pk>/edit/", views.PostEditView.as_view(), name="post-Edit-UpdateView"
    ),  # UpdateView
    path(
        "post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-DeleteView"
    ),  # DeleteView
    # API file address
    path("api/v1/", include("blog.api.v1.urls")),  # api address blog/api/v1
    
    path("post/api/", views.PostListApiView.as_view(), name="post-list-api"),
]
