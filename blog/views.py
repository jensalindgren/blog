from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostForm
from django.contrib import messages
from django.utils.text import slugify


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    """ Get post to be added and render a form to add comments """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
            },
        )


class AddPost(View):
    """ Get post to be added and render a add form """

    def get(self, request):

        post_form = PostForm()

        return render(
            request,
            'add_post.html',
            {
                'post_form': post_form,
            }
        )

    def post(self, request):
        """ Add new post """
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.slug = slugify(post_form.instance.title)
            post_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your post has been Added.'
            )

        else:
            post_form = PostForm()
            messages.add_message(
                request,
                messages.ERROR,
                'There was an error submitting your Post. '
                'Please try again!'
            )

        return HttpResponseRedirect(reverse('home'))


class DeletePost(View):

    def get(self, request, slug, *args, **kwargs):
        """ Get post to be deleted and render a delete form """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'delete_post.html',
            {
                'post': post,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ Delete existing post """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        post.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Your post has been deleted.'
        )

        return HttpResponseRedirect(reverse('home'))


class EditPost(View):
    """ Get post to be edited and render a edit form """
    def get(self, request, id, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=id)

        data = {'title': post.title, 'content': post.content}
        edit_form = PostForm(initial=data)

        return render(
            request,
            'edit_post.html',
            {
                'post': post,
                'edit_form': edit_form
            },
        )

    def post(self, request, id, *args, **kwargs):
        """ Edit existing post """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=id)
        edit_form = PostForm(request.POST, request.FILES, instance=post)
        if edit_form.is_valid():
            edit_form.instance.author = request.user
            edit_form.instance.slug = slugify(edit_form.instance.title)
            edit_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your post has been edited.'
            )

        else:
            edit_form = PostForm()
            messages.add_message(
                request,
                messages.ERROR,
                'There was an error submitting your Post. '
                'Please try again!'
            )

        return HttpResponseRedirect(reverse('home'))


class AddComment(View):

    def get(self, request, post_id, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=post_id)
        comment_form = CommentForm()
        return render(
            request,
            'add_comment.html',
            {
                'comment_form': comment_form,
                'post': post,
            },
        )

    def post(self, request, post_id, *args, **kwargs):
        ''' Add new comment '''
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=post_id)
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your Comment has been added. '
            )
        else:
            comment_form = CommentForm()
            messages.add_message(
                request,
                messages.ERROR,
                'There was an error submitting your comment. '
                'Please try again!'
            )

        return HttpResponseRedirect(reverse('question_detail', args=[slug]))


class DeleteComment(View):

    def get(self, request, id, *args, **kwargs):
        """ Let user delete comment """
        queryset = Post.objects.filter(status=1)
        comment = get_object_or_404(queryset, id=id)
        return render(
            request,
            'delete_comment.html',
            {
                'comment': comment,
            }
        )

    def post(self, request, id, *args, **kwargs):
        """ Delete existing comment """
        queryset = Post.objects.filter(status=1)
        comment = get_object_or_404(queryset, id=id)
        slug = comment.post.slug
        comment.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Your comment has been deleted.'
        )

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class EditComment(View):
    """ Get post to be edited and render a edit form """
    def get(self, request, id, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        comment = get_object_or_404(queryset, id=id)
        comment.post = post

        return render(
            request,
            'edit_post.html',
        )

    # 'commented': False,
    # 'liked': liked,
    # 'comment_form': CommentForm()
    # def post(self, request, slug, *args, **kwargs):
    #     queryset = Post.objects.filter(status=1)
    #     post = get_object_or_404(queryset, slug=slug)
    #     comments = post.comments.filter(approved=True).order_by(
        # '-created_on')
    #     liked = False
    #     if post.likes.filter(id=self.request.user.id).exists():
    #         liked = True

    #     comment_form = CommentForm(request.POST)

    #     if comment_form.is_valid():
    #         comment_form.instance.email = request.user.email
    #         comment_form.instance.name = request.user.username
    #         comment = comment_form.save(commit=False)
    #         comment.post = post
    #         comment.save()
    #         messages.add_message(
    #             request,
    #             messages.SUCCESS,
    #             'Your comment has been added. '
    #         )

    #     else:
    #         comment_form = CommentForm()
    #         messages.add_message(
    #             request,
    #             messages.ERROR,
    #             'There was an error submitting your Comment. '
    #             'Please try again!'
    #         )

    #     return render(
    #         request,
    #         'post_detail.html',
    #         {
    #             'post': post,
    #             'comments': comments,
    #             'commented': True,
    #             'liked': liked,
    #             'comment_form': CommentForm()
    #         },
    #     )
