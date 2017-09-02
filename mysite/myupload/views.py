from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from django.template import loader
from .models import file

# based on https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/
from .forms import UploadFileForm

def index(req):
    # return HttpResponse('Hi, this is the upload page to be built.')
    template = loader.get_template('myupload/index.html')

    if req.method=='POST':
        # add new file (a new record in table myupload_file)
        # https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.create
        new_file = file.objects.create(
            file_name       = req.POST['file_name'],
            upload_datetime = req.POST['upload_datetime'],
            comment         = req.POST['comment'],
        )

    number_of_files = len(file.objects.all())
    context = {
        'number_of_files': number_of_files,
    }
    return HttpResponse(template.render(context, req))

def list(req):
    # response = 'There are {} records of uploads.'
    # return HttpResponse(response.format('999'))

    latest_files = file.objects.order_by('-upload_datetime')[:10]
    # output = ' & '.join([x.file_name for x in latest_files])

    template = loader.get_template('myupload/list.html')

    context = {
        'latest_files': latest_files
    }
    return HttpResponse(template.render(context, req))

def detail(req, file_id):

    try:
        x = file.objects.get(pk=file_id)
    except file.DoesNotExist:
        raise Http404('File {} does not exist.'.format(file_id))
        
    template = loader.get_template('myupload/detail.html')
    context = {'file': x}
    return HttpResponse(template.render(context, req))


def test(req, something):
    # a view that receives something thru a GET request.
    response = 'I got {} passed by GET request!'
    return HttpResponse(response.format(something))


def upload_file(req):

    # template = loader.get_template('myupload/upload_file.html')

    if req.method=='POST':
        form = UploadFileForm(req.POST, req.FILES)
        # so, looks like I just pass FILES object to the class form.
        # Looks like I'm creating a form populating user input...
        if form.is_valid():

            # if form is valid, do something to data given
            new_file = file.objects.create(
                file_name       = req.FILES['file'].name,
                upload_datetime = req.POST['upload_datetime'],
                comment         = req.POST['comment'],
            )

            form = UploadFileForm()
            context = {'form': form}
            return render(req, 'myupload/upload_file.html', context)

        else:
            return HttpResponse(req.FILES['file'].name)

    else:
        # if this is not a POST method, just show empty form
        # .... is my understanding
        form = UploadFileForm()

        context = {'form': form}

        # so I have to pass this form to 'upload_file.html'
        # return HttpResponse(template.render(context, req))
        # return render(req, template, context)
        return render(req, 'myupload/upload_file.html', context)
