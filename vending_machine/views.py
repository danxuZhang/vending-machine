from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.urls import reverse

from . import models


def index(request: HttpRequest):
    current_balance: float = request.session.get("balance", 0)

    beverages = models.Beverage.objects.all()
    context = {
        'balance': current_balance,
        'beverages': beverages
    }

    return render(request, 'vending_machine/index.html', context=context)


def purchase(request: HttpRequest):
    return render(request, 'vending_machine/index.html')


def top_up(request: HttpRequest):
    balance: float = request.session.get("balance", 0)
    try:
        amount = float(request.POST['amount'])
        balance = balance + amount
    except KeyError:
        print(request.POST)
        return HttpResponse(f"cannot handle input!")

    request.session['balance'] = balance
    return HttpResponseRedirect(reverse('vendingmachine:index'))


def flush(request: HttpRequest):
    try:
        assert request.method == "POST", "not a post request"
        assert bool(request.POST['flush'])
        del request.session['balance']
    except AssertionError as msg:
        print(msg)
    finally:
        return HttpResponseRedirect(reverse('vendingmachine:index'))
