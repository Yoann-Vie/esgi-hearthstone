from django.shortcuts import render, redirect, get_object_or_404


def home(request):
    title = 'Home'
    context = {
        'title': title
    }

    return render(request, 'hearthstone/index.html', context)
