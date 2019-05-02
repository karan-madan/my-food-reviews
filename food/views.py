from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (Post, Post1,
                     Post2, Post3, Post4, Post5, Post6, Post7,
                     Post8, Post9, Post10, Post11, Post12, Post13,
                     Post14, Post15, Post16, Post17, Post18, Post19
                     )
from .forms import (Postform, Post1form,
                    Post2form, Post3form, Post4form, Post5form, Post6form, Post7form,
                    Post8form, Post9form, Post10form, Post11form, Post12form, Post13form,
                    Post14form, Post15form, Post16form, Post17form, Post18form, Post19form
                    )


def home(request):
    return render(request, 'food/home.html')


def about(request):
    return render(request, 'food/about.html')


def contactus(request):
    return render(request, 'food/contactus.html')


def butterchicken(request):
    context = {
        'posts': Post.objects.all(),
        'form': Postform
    }
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            Post.author = request.user
            form.save()
            return redirect('food-butterchicken')

    else:
        context = {
            'posts': Post.objects.all(),
            'form': Postform
        }
    return render(request, 'food/butterchicken.html', context)


def chickencurry(request):
    context = {
        'posts': Post1.objects.all(),
        'form': Post1form
    }
    if request.method == 'POST':
        form = Post1form(request.POST)
        if form.is_valid():
            Post1.author = request.user
            form.save()
            return redirect('food-chickencurry')

    else:
        context = {
            'posts': Post1.objects.all(),
            'form': Post1form
        }
    return render(request, 'food/chickencurry.html', context)


def keema(request):
    context = {
        'posts': Post2.objects.all(),
        'form': Post2form
    }
    if request.method == 'POST':
        form = Post2form(request.POST)
        if form.is_valid():
            Post2.author = request.user
            form.save()
            return redirect('food-keema')

    else:
        context = {
            'posts': Post2.objects.all(),
            'form': Post2form
        }
    return render(request, 'food/keema.html', context)


def shahipaneer(request):
    context = {
        'posts': Post3.objects.all(),
        'form': Post3form
    }
    if request.method == 'POST':
        form = Post3form(request.POST)
        if form.is_valid():
            Post3.author = request.user
            form.save()
            return redirect('food-shahipaneer')

    else:
        context = {
            'posts': Post3.objects.all(),
            'form': Post3form
        }
    return render(request, 'food/shahipaneer.html', context)


def kadhaipaneer(request):
    context = {
        'posts': Post4.objects.all(),
        'form': Post4form
    }
    if request.method == 'POST':
        form = Post4form(request.POST)
        if form.is_valid():
            Post4.author = request.user
            form.save()
            return redirect('food-kadhaipaneer')

    else:
        context = {
            'posts': Post4.objects.all(),
            'form': Post4form
        }
    return render(request, 'food/kadhaipaneer.html', context)


def masaladosa(request):
    context = {
        'posts': Post5.objects.all(),
        'form': Post5form
    }
    if request.method == 'POST':
        form = Post5form(request.POST)
        if form.is_valid():
            Post5.author = request.user
            form.save()
            return redirect('food-masaladosa')

    else:
        context = {
            'posts': Post5.objects.all(),
            'form': Post5form
        }
    return render(request, 'food/masaladosa.html', context)


def pasta(request):
    context = {
        'posts': Post6.objects.all(),
        'form': Post6form
    }
    if request.method == 'POST':
        form = Post6form(request.POST)
        if form.is_valid():
            Post6.author = request.user
            form.save()
            return redirect('food-pasta')

    else:
        context = {
            'posts': Post6.objects.all(),
            'form': Post6form
        }
    return render(request, 'food/pasta.html', context)


def burger(request):
    context = {
        'posts': Post7.objects.all(),
        'form': Post7form
    }
    if request.method == 'POST':
        form = Post7form(request.POST)
        if form.is_valid():
            Post7.author = request.user
            form.save()
            return redirect('food-burger')

    else:
        context = {
            'posts': Post7.objects.all(),
            'form': Post7form
        }
    return render(request, 'food/burger.html', context)


def pizza(request):
    context = {
        'posts': Post8.objects.all(),
        'form': Post8form
    }
    if request.method == 'POST':
        form = Post8form(request.POST)
        if form.is_valid():
            Post8.author = request.user
            form.save()
            return redirect('food-pizza')

    else:
        context = {
            'posts': Post8.objects.all(),
            'form': Post8form
        }
    return render(request, 'food/pizza.html', context)


def rolls(request):
    context = {
        'posts': Post9.objects.all(),
        'form': Post9form
    }
    if request.method == 'POST':
        form = Post9form(request.POST)
        if form.is_valid():
            Post9.author = request.user
            form.save()
            return redirect('food-rolls')

    else:
        context = {
            'posts': Post9.objects.all(),
            'form': Post9form
        }
    return render(request, 'food/rolls.html', context)


def naanza(request):
    context = {
        'posts': Post10.objects.all(),
        'form': Post10form
    }
    if request.method == 'POST':
        form = Post10form(request.POST)
        if form.is_valid():
            Post10.author = request.user
            form.save()
            return redirect('food-naanza')

    else:
        context = {
            'posts': Post10.objects.all(),
            'form': Post10form
        }
    return render(request, 'food/naanza.html', context)


def coffee(request):
    context = {
        'posts': Post11.objects.all(),
        'form': Post11form
    }
    if request.method == 'POST':
        form = Post11form(request.POST)
        if form.is_valid():
            Post11.author = request.user
            form.save()
            return redirect('food-coffee')

    else:
        context = {
            'posts': Post11.objects.all(),
            'form': Post11form
        }
    return render(request, 'food/coffee.html', context)


def lassi(request):
    context = {
        'posts': Post12.objects.all(),
        'form': Post12form
    }
    if request.method == 'POST':
        form = Post12form(request.POST)
        if form.is_valid():
            Post12.author = request.user
            form.save()
            return redirect('food-lassi')

    else:
        context = {
            'posts': Post12.objects.all(),
            'form': Post12form
        }
    return render(request, 'food/lassi.html', context)


def shawarma(request):
    context = {
        'posts': Post13.objects.all(),
        'form': Post13form
    }
    if request.method == 'POST':
        form = Post13form(request.POST)
        if form.is_valid():
            Post13.author = request.user
            form.save()
            return redirect('food-shawarma')

    else:
        context = {
            'posts': Post13.objects.all(),
            'form': Post13form
        }
    return render(request, 'food/shawarma.html', context)


def biryani(request):
    context = {
        'posts': Post14.objects.all(),
        'form': Post14form
    }
    if request.method == 'POST':
        form = Post14form(request.POST)
        if form.is_valid():
            Post14.author = request.user
            form.save()
            return redirect('food-biryani')

    else:
        context = {
            'posts': Post14.objects.all(),
            'form': Post14form
        }
    return render(request, 'food/biryani.html', context)


def roastedchicken(request):
    context = {
        'posts': Post15.objects.all(),
        'form': Post15form
    }
    if request.method == 'POST':
        form = Post15form(request.POST)
        if form.is_valid():
            Post15.author = request.user
            form.save()
            return redirect('food-roastedchicken')

    else:
        context = {
            'posts': Post15.objects.all(),
            'form': Post15form
        }
    return render(request, 'food/roastedchicken.html', context)


def tandoorichicken(request):
    context = {
        'posts': Post16.objects.all(),
        'form': Post16form
    }
    if request.method == 'POST':
        form = Post16form(request.POST)
        if form.is_valid():
            Post16.author = request.user
            form.save()
            return redirect('food-tandoorichicken')

    else:
        context = {
            'posts': Post16.objects.all(),
            'form': Post16form
        }
    return render(request, 'food/tandoorichicken.html', context)


def afghanichicken(request):
    context = {
        'posts': Post17.objects.all(),
        'form': Post17form
    }
    if request.method == 'POST':
        form = Post17form(request.POST)
        if form.is_valid():
            Post17.author = request.user
            form.save()
            return redirect('food-afghanichicken')

    else:
        context = {
            'posts': Post17.objects.all(),
            'form': Post17form
        }
    return render(request, 'food/afghanichicken.html', context)


def paneertikka(request):
    context = {
        'posts': Post18.objects.all(),
        'form': Post18form
    }
    if request.method == 'POST':
        form = Post18form(request.POST)
        if form.is_valid():
            Post18.author = request.user
            form.save()
            return redirect('food-paneertikka')

    else:
        context = {
            'posts': Post18.objects.all(),
            'form': Post18form
        }
    return render(request, 'food/paneertikka.html', context)


def mushroomtikka(request):
    context = {
        'posts': Post19.objects.all(),
        'form': Post19form
    }
    if request.method == 'POST':
        form = Post19form(request.POST)
        if form.is_valid():
            Post19.author = request.user
            form.save()
            return redirect('food-mushroomtikka')

    else:
        context = {
            'posts': Post19.objects.all(),
            'form': Post19form
        }
    return render(request, 'food/mushroomtikka.html', context)




