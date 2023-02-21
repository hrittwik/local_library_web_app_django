from django.shortcuts import render
from .models import Book, Author, BookInstance
# Create your views here.


def index(request):
    """View function for home page of site."""
    
    #Generate counts of some of the main object
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.object.count()

    context={
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)