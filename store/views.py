from django.shortcuts import render

# Create your views here.
def store(request):
    context = {}
    return render(request, "store/store.html", context)


def cart(request):
    context = {}
    return render(request, "store/cart.html", context)


def checkout(request):
    context = {"test1": "test1", "test2": "test1"}
    return render(request, "store/checkout.html", context)
