from django.shortcuts import render

# Create your views here.


from django.views import generic
from .models import BlogAuthor, Blog, BlogComment
from django.contrib.auth.models import User #Blog author or commenter


def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html
    return render(
        request,
        'index.html',
    )
    

class BlogListView(generic.ListView):
    """
    Generic class-based view for a list of all blogs.
    """
    model = Blog
    paginate_by = 5

class BloggerListView(generic.ListView):
    """
    Generic class-based view for a list of bloggers.
    """
    model = BlogAuthor
    paginate_by = 5

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


class BlogDetailView(CreateView):
    """
    Form for adding a blog comment. Requires login. 
    """
    model = BlogComment
    fields = ['description',]
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        if not self.request.user.is_authenticated:
            return HttpResponse('Unauthorized', status=401)
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog=get_object_or_404(Blog, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(BlogDetailView, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})
