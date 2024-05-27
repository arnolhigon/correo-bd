
from django.urls import path


from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('download/<int:email_id>/', download_zip, name='download_zip'),
    path('emails/<int:email_id>/view_pdf/', view_pdf, name='view_pdf'),
]
