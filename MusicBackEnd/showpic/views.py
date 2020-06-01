from django.shortcuts import render
from django.http.response import HttpResponse
import os
import time
# Create your views here.
from django.template import loader
from showpic.utils.music21tools import *
def UseMusic21(music_str):
    s = str2stream(music_str)
    filname = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    s.write('musicxml','./showpic/musicxml/%s.xml'%filname)
    command = 'MuseScore3 ./showpic/musicxml/{0}.xml -o ./showpic/static/musicpng/{0}.png'.format(filname)
    print(command)
    os.system(command)
    return filname

def ChangeMusic2Pic(request):
    if request.method == 'GET':
        music_str = request.GET.get('music_str')
        print(music_str)
        musicname = UseMusic21(music_str)

        return render(request, 'pic.html', {'musicname':musicname+'-1.png'})



def Showindex(request):
    return render(request, 'str2music.html', {})

def ShowPic(request):
    print('到这里')
    template = loader.get_template('showpic/pic.html')
    context = {}
    return HttpResponse(template.render(context, request))
