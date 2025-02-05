from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse
from .models import Post,table_peo,table_cam,table_duty_peo,table_user,table_sec
import time
import json
from django.template.loader import get_template




def camera_management(request):
    table_duty_peos = table_duty_peo.objects.all()
    table_cams = table_cam.objects.all()
    table_secs = table_sec.objects.all()

    template = get_template('camera_management.html')
    html = template.render(locals())   
    return HttpResponse(html)

def logManagement(request):
    table_duty_peos = table_duty_peo.objects.all()
    table_cams = table_cam.objects.all()
    table_secs = table_sec.objects.all()

    template = get_template('logManagement.html')
    html = template.render(locals())   
    return HttpResponse(html)

def userManagement(request):
    template = get_template('userManagement.html')
    html = template.render(locals())   
    return HttpResponse(html)

def work_management(request):
    table_duty_peos = table_duty_peo.objects.all()  
     
    template = get_template('work_management.html')
    html = template.render(locals())   
    return HttpResponse(html)

def run_management(request):
    template = get_template('run_management.html')
    html = template.render(locals())   
    return HttpResponse(html)



def security_management(request):
    template = get_template('security_management.html')
    html = template.render(locals())   
    return HttpResponse(html)

def ready_management(request):
    template = get_template('ready_management.html')
    html = template.render(locals())   
    return HttpResponse(html)

def standby_management(request):
    template = get_template('standby_management.html')
    html = template.render(locals())   
    return HttpResponse(html)


def index(request):    
    table_peos = table_peo.objects.all()
    table_cams = table_cam.objects.all()
    cam_1 = table_cams[0]
    peo_1 = table_peos[0]
   
    List=[]
    COO_x = []
    COO_y = []
    COO_warn = []
    
   
    for cam in table_cams:
        
        COO_x+=[cam.x]
        COO_y+=[cam.y]
        COO_warn += [cam.warn_num]
   
    for table in table_peos:
        
        List+=[table.num_p1,table.num_p2,table.num_p3]
#返回一系列的坐标点与坐标点的警告人数
    content = {
        'List': json.dumps(List),
        'COO_x':json.dumps(COO_x),
        'COO_y':json.dumps(COO_y),
        'COO_warn':json.dumps(COO_warn),
        'cam_1':cam_1,
        'peo_1':peo_1
        }
    return render(request, 'index.html',content)
   
def notfound(request):
        template = get_template('404.html')
        html = template.render(locals())
        return HttpResponse(html)

def basic_table(request):
        template = get_template('basic_table.html')
        html = template.render(locals())
        return HttpResponse(html)

def blank(request):
        template = get_template('blank.html')
        html = template.render(locals())
        return HttpResponse(html)

def chart_chartjs(request):
        template = get_template('chart-chartjs.html')
        html = template.render(locals())
        return HttpResponse(html)

def GaodeHeatMap(request):
        template = get_template('GaodeHeatMap.html')
        html = template.render(locals())
        return HttpResponse(html)

def login(request):
        template = get_template('login.html')
        html = template.render(locals())
        return HttpResponse(html)

def logManagement(request):
        template = get_template('logManagement.html')
        html = template.render(locals())
        return HttpResponse(html)

def swicthOn(request):
        template = get_template('swicthOn.html')
        html = template.render(locals())
        return HttpResponse(html)

def userManagement(request):
        template = get_template('userManagement.html')
        html = template.render(locals())
        return HttpResponse(html)

def videoDB(request):
        template = get_template('videoDB.html')
        html = template.render(locals())
        return HttpResponse(html)

def videoView(request):
        template = get_template('videoView.html')
        html = template.render(locals())
        return HttpResponse(html)

def warningVideoDB(request):
        template = get_template('warningVideoDB.html')
        html = template.render(locals())
        return HttpResponse(html)

def workCalendar(request):
        template = get_template('workCalendar.html')
        html = template.render(locals())
        return HttpResponse(html)

