from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.utils import timezone
from .forms import ContactForm, PostForm, PostForm2  # define in forms.py
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse


# Create your views here.


# "1" function base views
def indexView(request):
    """
    function base view
    """
    name = "Def"
    context = {"name": name}
    return render(request, "testurl.html", context)


"""
from django.shortcuts import redirect

def FBredirectToMaktab(request):
    return redirect('http://www.maktabkhooneh.com')
"""


# "3" class base views
class IndexView(TemplateView):
    """
    Class base view
    """

    template_name = "testurl.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Class"
        context["post"] = Post.objects.all()
        return context


# "6"
class RedirectToMaktab1(RedirectView):
    url = "http://www.maktabkhooneh.com"


# "7"
class RedirectToMaktab2(RedirectView):
    url = "http://www.maktabkhooneh.com"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


# 'post' # need template blog/post_list.html
class PostListView(PermissionRequiredMixin, ListView):
    permission_required = "blog.view_post"
    context_object_name = "posts"
    paginate_by = 10

    ordering = "-id"
    # model = Post #or
    queryset = Post.objects.all()

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


# 'post/<int:id>' # DetailView
class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


# 'post/create/' # FormView
class PostCreateView(FormView):
    template_name = "contact.html"
    # form_class = ContactForm # contact class LIKE models
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        # form.send_email()  #can send real email
        form.save()  # save in db
        return super().form_valid(form)


# 'post/create2/' # CreateView
class PostCreateView2(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date'] # form_class
    form_class = PostForm2  # define by me
    success_url = "/blog/post/"

    # check user has login or not
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# 'post/<int:pk>/edit/' # UpdateView
class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm2
    success_url = "/blog/post/"
    # template_name = "edit.html" # or blog/post_form.html (createview)


# 'post/<int:pk>/delete/' # DeleteView
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"
    # success_url = reverse_lazy("author-list")

class PostListApiView(TemplateView):
    template_name = "blog/post_list_api.html"