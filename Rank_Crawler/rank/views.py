

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render



def rank_page(request):
    # 기본 템플릿 폴더(admin\templates)
    # 1. admin 앱은 기본설치됨
    # 2. 각 앱의 폴더에 있는 templates 폴더
    # 3. 직접 설정한 폴더


    return render(request, 'rank_page.html')


