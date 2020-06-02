from django.shortcuts import render
from django.http.response import HttpResponse
import os
import time
# Create your views here.
from django.template import loader
from Myapp_covert2musicscore.utils.music21tools import *


def use_music21(music_str):
    pan = False
    print('准备预测')
    for each in music_str:
        if each.isupper() == True:
            pan = True
            break
    # 如果没有大写字母，也就是纯数字
    if pan == False:
        print('纯数字')
        s = musicstr_to_stream(music_str)
    else:
        print('大写字母')
        s = musicstr_char_to_stream(music_str)
    filname = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    s.write('musicxml','./Myapp_covert2musicscore/musicxml/%s.xml'%filname)
    #command = '/usr/bin/musescore ./showpic/musicxml/{0}.xml -o ./showpic/static/musicpng/{0}.png'.format(filname)
    command = 'MuseScore3 ./Myapp_covert2musicscore/musicxml/{0}.xml -o ./Myapp_covert2musicscore/static/musicpng/{0}.png'.format(filname)
    print(command)
    os.system(command)
    return filname


'''
Summary:
    将音乐字符串转换成图片
Return:
    返回转换后的结果
'''
def convert_musicstr_2_pic(request):
    if request.method == 'GET':
        print(request.GET)
        music_str = request.GET.get('music_str')

        print(music_str)
    elif request.method == 'POST':
        music_str = request.POST.get('str-container')
        print(request.POST)
        print(music_str)
    musicname = use_music21(music_str)

    # 将字符串放入上下文，以后用
    return render(request, 'test_show_musicscore_pic.html', {'musicname':musicname+'-1.png'})


'''
Summary:
    展示字符串上传的首页
Return:
    首页的html
'''
def show_uploads_index(request):
    return render(request, 'str2music.html', {})

'''
Summary:
    展示图片(测试用)
Return:
    含有图片的html(测试用)
'''
def test_show_pic(request):
    print('到这里')
    template = loader.get_template('Myapp_covert2musicscore/test_show_musicscore_pic.html')
    context = {}
    return HttpResponse(template.render(context, request))
