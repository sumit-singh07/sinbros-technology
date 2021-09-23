from django.http import HttpResponse
from django.shortcuts import render
from .models import Portfolio
from django.core.paginator import Paginator

def index(request):
    portfolios = Portfolio.objects.all().order_by('-portfolio_id')
    # paginator = Paginator(portfolios, 9)
    # page = request.GET.get('page')
    # portfolios= paginator.get_page(page)

    portfolios_logo = Portfolio.objects.filter(portfolio_category="Logo").order_by('-portfolio_id')
    # paginator = Paginator(portfolios_logo, 9)
    # page = request.GET.get('page')
    # portfolios_logo = paginator.get_page(page)

    portfolios_social = Portfolio.objects.filter(portfolio_category="Social Media").order_by('-portfolio_id')
    # paginator = Paginator(portfolios_social, 9)
    # page = request.GET.get('page')
    # portfolios_social = paginator.get_page(page)

    portfolios_website = Portfolio.objects.filter(portfolio_category="Website").order_by('-portfolio_id')
    portfolio_instagram= Portfolio.objects.filter(portfolio_category="Instagram").order_by('-portfolio_id')

    params={"portfolio":portfolios,"portfolio_logo":portfolios_logo,"portfolio_social":portfolios_social,"portfolio_website":portfolios_website,"portfolio_instagram":portfolio_instagram}
    return render(request, 'portfolio/portfolio.html',params)
