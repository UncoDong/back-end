from django.shortcuts import render
from django.http.response import HttpResponse
import os
import time
# Create your views here.
from django.template import loader
from covert2musicscore.utils.music21tools import *


def UseMusic21(music_str):
    s = str2stream(music_str)
    filname = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    s.write('musicxml','./covert2musicscore/musicxml/%s.xml'%filname)
    command = 'MuseScore3 ./covert2musicscore/musicxml/{0}.xml -o ./covert2musicscore/static/musicpng/{0}.png'.format(filname)
    print(command)
    os.system(command)
    return filname


'''
Summary:
    将音乐字符串转换成图片
Return:
    返回转换后的结果
'''
def ConvertMusicStr2Pic(request):
    if request.method == 'GET':
        music_str = request.GET.get('music_str')
        print(music_str)
        musicname = UseMusic21(music_str)
        # 将字符串放入上下文，以后用
        return render(request, 'test_show_musicscore_pic.html', {'musicname':musicname+'-1.png'})


'''
Summary:
    展示字符串上传的首页
Return:
    首页的html
'''
def ShowUnploadstrIndex(request):
    return render(request, 'str2music.html', {})

'''
Summary:
    展示图片(测试用)
Return:
    含有图片的html(测试用)
'''
def Test_ShowPic(request):
    print('到这里')
    template = loader.get_template('covert2musicscore/test_show_musicscore_pic.html')
    context = {}
    return HttpResponse(template.render(context, request))
