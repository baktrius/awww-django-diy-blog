from django.shortcuts import render

# Create your views here.


from django.views import generic
from .models import BlogAuthor  #, Blog, BlogComment
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
    

# TODO: Create Views for BlogList, BlogDetailView
    
class BloggerListView(generic.ListView):
    """
    Generic class-based view for a list of bloggers.
    """
    model = BlogAuthor
    paginate_by = 5