from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, View
from django.urls import reverse_lazy

from blog.models import Blog
from blog.forms import BlogForm
# Create your views here.


class Index(ListView):
    model = Blog


class Home(View):
    def get(self, request):
        return render(request, "blog/home.html")


class Detail(DetailView):
    model = Blog


class Create(CreateView):
    model = Blog
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:all')


class Update(UpdateView):
    model = Blog
    # fields = ['title', 'content']
    template = 'blog/blog_update.html'
    success_url = reverse_lazy('blog:all')

    def get(self, request, pk):
        blog = get_object_or_404(self.model, pk=pk)
        # try:
        #     blog = request.POST.get(pk, 0)
        # except e:
        #     raise

        # print(blog.title)
        ctx = {'title': blog.title, 'content': blog.content}
        # print(ctx)
        return render(request, self.template, ctx)

    def post(self, request, pk):
        blog = get_object_or_404(self.model, pk=pk)
        form = BlogForm(request.POST, instance=blog)
        if not form.is_valid():
            ctx = {'title': blog.title, 'content': blog.content}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)


class Delete(DeleteView):
    model = Blog
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:all')

    # model = Blog
    # success_url = reverse_lazy('blog:all')
    # template = 'blog/blog_confirm_delete.html'

    # def get(self, request, pk):
    #     blog = get_object_or_404(self.model, pk=pk)
    #     form = BlogForm(instance=blog)
    #     ctx = {'blog': blog}
    #     return render(request, self.template, ctx)

    # def post(self, request, pk):
    #     make = get_object_or_404(self.model, pk=pk)
    #     make.delete()
    #     return redirect(self.success_url)


# def home(request):
#     return render(request, 'home.html')


# def post_page(request, post_id):
#     # print(post_id)
#     post = Blog.objects.get(pk=post_id)
#     return render(request, "post.html", {"post": post})


# def all_posts(request):
#     all_posts = Blog.objects.all()
#     return render(request, "allposts.html", {"posts": all_posts})


# def create_post(request):
#     if request.method == "POST":
#         # print(request.POST)
#         title = request.POST["title"]
#         content = request.POST["content"]

#         new_post = Blog.objects.create(title=title, content=content)

#         return redirect("/allposts/")
#     return render(request, "create_post.html")


# def delete_post(request, post_id):
#     post = Blog.objects.get(pk=post_id)
#     post.delete()
#     return redirect("/allposts/")


# def edit_post(request, post_id):
#     post = Blog.objects.get(pk=post_id)
#     if request.method == "POST":
#         title = request.POST["title"]
#         content = request.POST["content"]

#         post.title = title
#         post.content = content

#         post.save()

#         return redirect(f'/post/{post.id}')
#     return render(request, "edit_post.html", {"post": post})
