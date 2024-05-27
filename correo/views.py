from django.shortcuts import render
from django.conf import settings
import zipfile
import io
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse
from .models import Email


def home(request):
    emails = Email.objects.all()
    return render(request, 'home.html',{'emails': emails})


def download_zip(request, email_id):
    email = Email.objects.get(pk=email_id)
    zip_path = email.zip_file.path
    with open(zip_path, 'rb') as zip_file:
        response = HttpResponse(zip_file.read(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="archivo.zip"'
        return response


def view_pdf(request, email_id):
    email = get_object_or_404(Email, pk=email_id)
    zip_path = email.zip_file.path
    
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        for file_name in zip_file.namelist():
            if file_name.endswith('.pdf'):
                pdf_file = zip_file.open(file_name)
                response = FileResponse(pdf_file, content_type='application/pdf')
                response['Content-Disposition'] = f'inline; filename="{file_name}"'
                return response

    return HttpResponse("No PDF found in the ZIP file.")


