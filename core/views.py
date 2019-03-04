from django.core.files.storage import default_storage
from django.shortcuts import render
from googleapiclient.http import MediaFileUpload
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from carnival import settings
from .forms import ImageForm
from .models import Image

def index(request):
    context = {
        'navbar': 'home'
    }
    return render(request, 'core/index.html', context)


def about(request):
    context = {
        'navbar': 'about'
    }
    return render(request, 'core/about.html', context)


def espanol(request):
    context = {
        'navbar': 'espanol'
    }
    return render(request, 'core/espanol.html', context)


def contact(request):
    return


def dayof(request):
    if request.method == 'POST':
        #form = ImageForm(request.POST,request.FILES)
        #if form.is_valid():
        #image = Image()
        files = request.FILES.getlist('picture')
        #image.picture = form.cleaned_data["picture"]
        #image.save()
        creds = None
        SCOPES = ['https://www.googleapis.com/auth/drive']
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server()
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        service = build('drive', 'v3', credentials=creds)
        folder_id = '1dOy-chl03stjflrlu4jl6nxyWhvAZNmR'
        for f in files:
            #print(f)
            #image.pics.append(f)
            save_path = os.path.join(settings.MEDIA_ROOT, str(f))
            default_storage.save(str(f), f)
            file_metadata = {'name': str(f),'parents': [folder_id]}
            media = MediaFileUpload(save_path,mimetype='image/jpeg')
            service.files().create(body=file_metadata,media_body=media,fields='id').execute()
            default_storage.delete(str(f))
        #image.delete()

    else:
        form = ImageForm()

    return render(request, "core/dayof.html", {'navbar': ''})