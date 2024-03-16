from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Shop

# Create your views here.


menu = [{
    'title': 'Главная страница', 'url_page': 'main_page'},
    {'title': 'Новости', 'url_page': 'news'},
    {'title': 'Форум', 'url_page': 'forum'},
    {'title': 'Войти', 'url_page': 'login'},
]


def index(request, product_slug=None):
    product = get_object_or_404(Shop, slug=product_slug)

    data = {
        'title': 'Главная страница',
        'menu': menu,
        'product': product,
    }

    return render(request, 'magazin/index.html', context=data)


def main_page(request):
    data = {'title': 'main_page'}
    return render(request, 'magazin/main_page.html', context=data)


def news(request):
    return HttpResponse('news')


def forum(request):
    return HttpResponse('forum')


def login_page(request):
    return HttpResponse('log_in')


def all_products(request):
    product = Shop.objects.all()
    data = {
        'products': product,
        'title': 'Products'
    }
    return render(request, 'magazin/all_products.html', context=data)
    # return HttpResponse(product)


def test_views(request):
    data = Shop.objects.all()
    data = {
        'title':data,
    }
    return render(request, 'magazin/test_views.html', context=data)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

from django.http import Http404
from django.shortcuts import render

from .models import Question


# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})