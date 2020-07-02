from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document

# Create your views here.

def upload_image(request):
    message = 'Upload as many files as you want!'
    #Handle file upload
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('list')    
    else:
        form = DocumentForm()
    
    #load data for list page
    documents = Document.objects.all()

    #render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)