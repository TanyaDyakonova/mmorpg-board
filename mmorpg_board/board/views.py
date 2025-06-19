from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Reply, Category
from .forms import PostForm, ReplyForm
from django.contrib.auth.decorators import login_required


class PostListView(ListView):
    model = Post
    template_name = 'board/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_at')
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category__name=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'board/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReplyForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = self.object
            reply.user = request.user
            reply.save()
            messages.success(request, 'Отклик отправлен!')
            return redirect('post_detail', pk=self.object.pk)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'board/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'board/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'board/post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class MyRepliesView(LoginRequiredMixin, ListView):
    model = Reply
    template_name = 'board/my_replies.html'
    context_object_name = 'replies'

    def get_queryset(self):
        user_posts = Post.objects.filter(author=self.request.user)
        selected_post_id = self.request.GET.get('post')
        if selected_post_id:
            return Reply.objects.filter(post_id=selected_post_id, post__author=self.request.user)
        return Reply.objects.filter(post__in=user_posts)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_posts'] = Post.objects.filter(author=self.request.user)
        context['selected_post_id'] = self.request.GET.get('post')
        return context


@login_required
def accept_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id, post__author=request.user)
    reply.accepted = True
    reply.save()
    messages.success(request, 'Отклик принят.')
    return redirect('my_replies')


@login_required
def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id, post__author=request.user)
    reply.delete()
    messages.success(request, 'Отклик удалён.')
    return redirect('my_replies')








