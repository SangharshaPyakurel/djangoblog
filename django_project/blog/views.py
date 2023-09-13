from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse

from users.forms import CommentForm
from .models import Post, Comment
from django.views.generic import (ListView, 
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string


# posts = [
#     {
#         'author': 'Sangharsha',
#         'title': 'Blog Post 1',
#         'content': 'First Post Content',
#         'date_posted': 'Sep 8 , 2023'
#     },
#     {
#         'author': 'Pyakurel',
#         'title': 'Blog Post 2',
#         'content': 'Second post Content',
#         'date_posted': 'Sep 8, 2022'
#     }
# ]

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def LikeView(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, id = request.POST.get('oid'))
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
        context = {
            # 'post': post,
            'liked': liked,
            'total_likes': post.total_likes()
        }
    return JsonResponse({
        'message': context
    })
    
    # if request.po():
    #     html = render_to_string('blog/like_section.html', context, request=request)
    # # return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))




class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'   #<app>/<model>_<viewtype>.html  
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    def get_context_data(self,**kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        
        stuff = get_object_or_404(Post, id= self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    # to override the valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    # fields = '__all__'
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    success_url = reverse_lazy('home')
    # to override the valid method
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ['title','content']
    # to override the valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        # which object we want to update
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        # which object we want to delete
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

