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
