from django.http import HttpResponse
from django.shortcuts import render
from .models import Learn
from django.core.paginator import Paginator
from django.apps import apps
Portfolio = apps.get_model('portfolio','Portfolio')


def competitive_programming(request):
    learns=Learn.objects.filter(learn_category="Competitive Programming").order_by('-learn_id')[::1]
    total=len(Learn.objects.filter(learn_category="Competitive Programming").order_by('-learn_id')[::1])
    paginator = Paginator(learns,6)
    page = request.GET.get('page')
    learns = paginator.get_page(page)

    result=total/6

    if page:
        start=int(page)*6-5
        end=int(page)*6
        if end>total:
            end = total
    else:
        start = 1
        end=6
        if total<6:
            end=total

    params={"learn":learns,"competitive_category":True,"total":total,"start":start,"end":end}

    return render(request, 'learn/competitive-programming.html',params)

def pattern_programs(request):
    learns=Learn.objects.filter(learn_category__contains="Pattern Programs").order_by('-learn_id')[::1]
    total=len(Learn.objects.filter(learn_category__contains="Pattern Programs").order_by('-learn_id')[::1])
    paginator = Paginator(learns, 6)
    page = request.GET.get('page')
    learns = paginator.get_page(page)

    result = total / 6

    if page:
        start = int(page) * 6 - 5
        end = int(page) * 6
        if end > total:
            end = total
    else:
        start = 1
        end = 6
        if total < 6:
            end = total

    params = {"learn": learns, "pattern_category": True, "total": total, "start": start, "end": end}

    return render(request, 'learn/competitive-programming.html',params)

def basic_programming(request):
    learns=Learn.objects.filter(learn_category="Basic Programming").order_by('-learn_id')[::1]
    total=len(Learn.objects.filter(learn_category="Basic Programming").order_by('-learn_id')[::1])
    paginator = Paginator(learns, 6)
    page = request.GET.get('page')
    learns = paginator.get_page(page)

    result = total / 6

    if page:
        start = int(page) * 6 - 5
        end = int(page) * 6
        if end > total:
            end = total
    else:
        start = 1
        end = 6
        if total < 6:
            end = total

    params = {"learn": learns, "basic_category": True, "total": total, "start": start, "end": end}

    return render(request, 'learn/competitive-programming.html',params)


def view_competitive_programming(request,learn_url):
    learns = Learn.objects.filter(learn_url=learn_url)
    latest_learns = Learn.objects.all().order_by('-learn_id')[:5:1]
    portfolios = Portfolio.objects.all().order_by('-portfolio_id')[:9:1]

    if learns[0].learn_category=="Competitive Programming":
        last_url="competitive-programming"
        params = {"learn": learns,"latest_learn":latest_learns, "last_url": last_url,"competitive_category":True,"portfolio":portfolios}
    elif learns[0].learn_category=="Pattern Programs":
        last_url="pattern-programs"
        params = {"learn": learns,"latest_learn":latest_learns,"last_url": last_url,"pattern_category":True,"portfolio":portfolios}
    elif learns[0].learn_category=="Basic Programming":
        last_url="basic-programming"
        params = {"learn": learns,"latest_learn":latest_learns, "last_url": last_url,"basic_category":True,"portfolio":portfolios}
    return render(request, 'learn/view-competitive-programming.html',params)

# Create your views here.



def python(request):
    latest_learns = Learn.objects.all().order_by('-learn_id')[:5:1]
    portfolios = Portfolio.objects.all().order_by('-portfolio_id')[:9:1]
    params = {"latest_learn": latest_learns,"portfolio": portfolios}
    return render(request, 'learn/python.html',params)

def face_detection(request):
    latest_learns = Learn.objects.all().order_by('-learn_id')[:5:1]
    portfolios = Portfolio.objects.all().order_by('-portfolio_id')[:9:1]
    params = {"latest_learn": latest_learns,"portfolio": portfolios}
    return render(request, 'learn/face-detection.html',params)

