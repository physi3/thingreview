from django.db.models import Count, Q
from django.shortcuts import redirect, render

from random import randint

from . import models
from . import forms


def index(request):
    return render(request, 'things/index.html')


def search(request, **kwargs):
    search = None
    try:
        search = request.GET['search']
    except:
        return render(request, 'things/search.html')

    results = models.Thing.objects.filter(
        Q(name__icontains=search) |
        Q(nickname__icontains=search),
    ).order_by('name')

    context = {
        'search': search,
        'results': results,
    }

    return render(request, 'things/search.html', context)


def thing(request, **kwargs):
    if _thing := models.Thing.objects.filter(id=kwargs['id']).first():
        context = {
            'thing': _thing,
            'reviews': _thing.review_set.all(),
        }
        return render(request, 'things/thing.html', context)
    else:
        return redirect('things:index')


def make_thing(request):
    form = forms.ThingForm
    if request.method == 'POST':
        form = forms.ThingForm(request.POST)
        if form.is_valid():
            # Create new thing.
            _thing = models.Thing()
            _thing.name = form.cleaned_data['name']
            _thing.nickname = form.cleaned_data['nickname']
            _thing.description = form.cleaned_data['description']
            _thing.website = form.cleaned_data['website']
            _thing.save()
            return redirect('things:thing', _thing.id)
    context = {
        'form': form,
    }
    return render(request, 'things/make_thing.html', context)


def things(request):
    context = {
        'things': models.Thing.objects.all().order_by('name'),
    }
    return render(request, 'things/things.html', context)


def review(request, **kwargs):
    form = forms.ReviewForm
    if _thing := models.Thing.objects.filter(id=kwargs['id']).first():
        if request.method == 'POST':
            form = forms.ReviewForm(request.POST)
            if form.is_valid():
                # Create new review.
                # Is rating 0-5?
                _review = models.Review()
                _review.thing = _thing
                _review.content = form.cleaned_data['content']
                _review.rating = form.cleaned_data['rating']
                _review.author = form.cleaned_data['author']
                _review.save()
                return redirect('things:thing', _thing.id)
        context = {
            'thing': _thing,
            'form': form
        }
        return render(request, 'things/review.html', context)
    else:
        return redirect('things:index')


def random(request):
    count = models.Thing.objects.count()
    if count:
        _thing = models.Thing.objects.all()[randint(0, count-1)].id
        return redirect('things:thing', _thing)
    else:
        return redirect('things:index')

def latest(request):
    count = models.Thing.objects.count()
    if count:
        _thing = models.Thing.objects.order_by('-date').first()
        return redirect('things:thing', _thing.id)
    else:
        return redirect('things:index')

def least_reviewed(request):
    count = models.Thing.objects.count()
    if count:
        _thing = models.Thing.objects.annotate(num_reviews=Count('review')).order_by('num_reviews').first()
        return redirect('things:thing', _thing.id)
    else:
        return redirect('things:index')
