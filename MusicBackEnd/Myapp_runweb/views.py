from django.shortcuts import render

# Create your views here.
'''
Summary:
    展示主页
Return:
    首页的html
'''
def home(request):
    return render(request, 'home.html', {})

'''
Summary:
    展示字符串上传的首页
Return:
    首页的html
'''
def str_to_musicscore(request):
    return render(request, 'str2musicscore.html', {})

'''
Summary:
    展示声波图
Return:
    首页的html
'''
def wave_scope(request):
    return render(request, 'wavescope.html', {})

'''
Summary:
    展示在线钢琴
Return:
    首页的html
'''
def piano_online(request):
    return render(request, 'pianoOnLine.html', {})

'''
Summary:
    展示节拍器
Return:
    首页的html
'''
def metronome(request):
    return render(request, 'metronome.html', {})

'''
Summary:
    上传文件
Return:
    首页的html
'''
def file_to_musicscore(request):
    return render(request, 'file2musicscore.html', {})

