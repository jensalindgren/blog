from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.postgres.search import SearchVector


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetailView(View):
    """ Get post to be added and render a form to add comments """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by('-created_on')
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


class AddPostView(View):
    """ Get post to be added and render a add form """

    def get(self, request):

        post_form = PostForm()

        return render(
            request,
            'post_post.html',
            {
                'post_form': post_form,
            }
        )

    def post(self, request):
        """ Add new post """
        post_form = PostForm(data=request.POST)
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


class DeletePostView(View):
    """ Get post to be deleted and render a delete form """
    def get(self, request, id, *args, **kwargs):
        """ Get post to be deleted and render a delete form """

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=id)

        return render(
            request,
            'delete_post.html',
            {
                'post': post,
            },
        )

    def post(self, request, id, *args, **kwargs):
        """ Delete existing post """

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=id)

        post.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Your post has been deleted.'
        )

        return HttpResponseRedirect(reverse('home'))


class EditPostView(View):
    """ Get post to be edited and render a edit form """
    def get(self, request, id, *args, **kwargs):

        queryset = Post.objects.all()
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

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=id)

        edit_form = PostForm(instance=post, data=request.POST,)
        if edit_form.is_valid():
            post.title = edit_form.cleaned_data.get('title')
            post.content = edit_form.cleaned_data.get('content')
            post.slug = slugify(edit_form.cleaned_data.get('title'))
            post.save()
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


class CommentPostView(View):
    """View to allow user to create a new comment"""

    def get(self, request, post_id):
        """ Get comment form and related post and render data """

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=post_id)

        comment_form = CommentForm()

        return render(
            request,
            'post_comment.html',
            {
                'comment_form': comment_form,
                'post': post,
            }
        )

    def post(self, request, post_id):
        """ Create new comment using the form data and returns to home page """

        queryset = Post.objects.all()
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

        return HttpResponseRedirect(
            reverse(
                'post_detail',
                args=[post.slug]
            )
        )


class CommentEditView(View):
    """ View to allow user to edit a specific comment"""

    def get(self, request, id):
        """ Get comment data and return a prefilled form """

        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, id=id)

        data = {'body': comment.body}
        edit_form = CommentForm(initial=data)

        return render(
            request,
            'edit_comment.html',
            {
                'comment': comment,
                'edit_form': edit_form
            }
        )

    def post(self, request, id):
        """ Update existing comment using the form data"""

        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, id=id)

        edit_form = CommentForm(instance=comment, data=request.POST)

        if edit_form.is_valid():
            comment.body = edit_form.cleaned_data.get('body')
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'You edited your comment successfully.'
            )

        else:
            edit_form = CommentForm()
            messages.add_message(
                request,
                messages.WARNING,
                'Your comment has not been edited.'
            )

        return HttpResponseRedirect(
            reverse(
                'post_detail',
                args=[comment.post.slug]
            )
        )