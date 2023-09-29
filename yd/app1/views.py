from django.shortcuts import render
from django.http import HttpResponse

# importing all the required modules
from django.shortcuts import render, redirect
from pytube import *
from django.http import JsonResponse
import json


# defining function
def youtube(request):
    return render(request, 'home.html')



def get_resolution(request, **kwargs):
    options = []
    data = json.loads(str(request.body, encoding='utf-8'))
    link = data['link']
    print(request.POST)
    print(link)
    if link is None:
        return JsonResponse({'error': 'Link is required.'})
    try :
        video = YouTube(link)
    except:
        return JsonResponse({'error': 'Invalid Link.'})
    stream = video.streams.filter( file_extension='mp4').order_by('resolution').desc()
    for i in stream:
        if i.resolution not in options:
            options.append(i.resolution)
    #return render(request, 'options.html', options)
    return JsonResponse(options, safe=False)

def download(request):
    print(request.POST)
    print('download')
    data = json.loads(str(request.body, encoding='utf-8'))
    link = data['link']
    resolution = data['resolution']
    print(link,resolution)
    video = YouTube(link)
    stream = video.streams.filter( file_extension='mp4', resolution=resolution).first()
    stream.download()
    return JsonResponse({'success': 'Video downloaded successfully.'})