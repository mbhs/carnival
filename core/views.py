from django.shortcuts import render
from googleapiclient.http import MediaFileUpload
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
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
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = Image()
            image.picture = form.cleaned_data["picture"]
            image.save()
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
            file_metadata = {'name': image.picture.name,'parents': [folder_id]}
            media = MediaFileUpload(image.picture.path,mimetype='image/jpeg')
            service.files().create(body=file_metadata,media_body=media,fields='id').execute()


    else:
        form = ImageForm()

    return render(request, "core/dayof.html", {'form': form, 'navbar': ''})