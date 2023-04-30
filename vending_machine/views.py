from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

from .models import Beverage, Transaction


def index(request: HttpRequest):
    current_balance: float = request.session.get("balance", 0)

    beverages = Beverage.objects.all()
    context = {
        'balance': current_balance,
        'beverages': beverages
    }

    return render(request, 'vending_machine/index.html', context=context)


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


def purchase(request: HttpRequest):
    try: 
        assert request.method == "POST", "not a post request"
        item_id = request.POST['id']
        beverage = get_object_or_404(Beverage, pk=item_id)
        inserted_amount = request.session['balance']
        return_amount = inserted_amount - beverage.price
        assert return_amount >= 0, "insufficient amount"
        transaction = Transaction(beverage=beverage, inserted_amount=inserted_amount, return_amount=return_amount,
                                  trans_time = timezone.now())
        # print(f"Success: {beverage}, inserted: {inserted_amount}, time: {timezone.now()}")
        beverage.decrement_stock()
        # beverage.save()
        transaction.save()
        request.session['balance'] = return_amount
    except AssertionError as msg:
        print(msg)
    finally:
        return HttpResponseRedirect(reverse('vendingmachine:index'))
    

def history(request: HttpRequest):
    transactions = Transaction.objects.all()
    context = {
        'transactions' : transactions,
    }
    return render(request, 'vending_machine/history.html', context=context)
