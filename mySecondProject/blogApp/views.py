from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,CreateView,
                                    ListView,DetailView,
                                    UpdateView,DeleteView)
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.urls import reverse_lazy
import requests
# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PostCreateView(LoginRequiredMixin,CreateView):

    template_name = "blogapp/create.html"
    form_class = PostForm
    model = Post
    success_url = reverse_lazy("draft_list")
    
class DraftListView(ListView):

    template_name = "blogapp/draft_blog.html"
    context_object_name = 'drafts'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')

class PostListView(ListView):

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

        template_name = "blogapp/post_list.html"
        # context_object_name = 'posts'
        model = Post

class PostDetailView(DetailView):
    template_name = "blogapp/blog_single.html"
    context_object_name = 'post_detail'
    model = Post
    
class PostUpdate(LoginRequiredMixin,UpdateView):
    template_name = "blogapp/update.html"
    fields = ('title','text','featured_image')
    model = Post
    # form_class = PostForm

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


def publish_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.published_post()

    return redirect('post_detail',pk=post.pk)


class AddCommentView(CreateView):
    model = Comment
    template_name = "blogapp/comment_form.html"
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('post_list')

# def addCommentView(request,pk):
#     post = get_object_or_404(Post,pk=pk)

#     if request.method == 'POST':
#         form = CommentForm(request.POST)

#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail',pk=post.pk)
#         else:

#             form = CommentForm()
#             post_rec = post
#             data = {'form':form, 'post':post_rec}
#             return render(request,'blogapp/comment_form.html',{'data':data})

class CovidListView(TemplateView):
    
    template_name = 'blogapp/outbreak-news.html'

class PreventCovid(TemplateView):
    template_name = 'blogapp/covid19.html'

def CovidNaija(request):
    overview = requests.get('https://covidnigeria.herokuapp.com/api').json()
    cases = overview['data']['states']
    confirmed = overview['data']['totalConfirmedCases']
    death = overview['data']['death']
    discharged = overview['data']['discharged']
    active = overview['data']['totalActiveCases']
    context = {
        'covids':cases,
        'confirmed':confirmed,
        'death':death,
        'discharged':discharged,
        'active':active
    }
    return render(request,'blogapp/covid9ja.html',context)




    




    