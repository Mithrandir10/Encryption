from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.utils import timezone

from caesarapp.CaesarCipher import CaesarCipher, HillCipher
from .models import UserInput
from .forms import UserInputForm, UserInputForm2

# Create your views here.

def index(request):
    
    return render(request, 'caesarapp/index.html', {})


def encryptcaesar(request):
    if request.method == "POST":
        form = UserInputForm(request.POST)
        if (form.is_valid()):
            userInput = form.save(commit=False)
            userInput.pub_date = timezone.now()
            userInput.save()
            return HttpResponseRedirect(reverse('encrypted', args=(userInput.id, )))
    else:
        form = UserInputForm()
    return render(request, 'caesarapp/encrypt.html', {'form': form})

def encrypthill(request):
    if request.method == "POST":
        form = UserInputForm2(request.POST)
        if (form.is_valid()):
            userInput = form.save(commit=False)
            userInput.pub_date = timezone.now()
            userInput.save()
            return HttpResponseRedirect(reverse('encryptedhill', args=(userInput.id, )))
    else:
        form = UserInputForm2()
    return render(request, 'caesarapp/encrypthill.html', {'form': form})

def encrypted(request, userInput_id):
    userInput = get_object_or_404(UserInput, pk=userInput_id)
    caesarCipher = CaesarCipher(userInput.encryption_key)
    encryptedText = caesarCipher.encrypt(userInput.plain_text)
    return render(request, 'caesarapp/encrypted.html', {'userInputkey': userInput.encryption_key,'userInputtext':userInput.plain_text, 'encrypted': encryptedText})

def encryptedhill(request, userInput_id):
    userInput = get_object_or_404(UserInput, pk=userInput_id)
    caesarCipher = HillCipher(userInput.hill_key)
    encryptedText = caesarCipher.encryptscytale(userInput.plain_text)
    return render(request, 'caesarapp/encrypted.html', {'userInputkey': userInput.hill_key,'userInputtext':userInput.plain_text, 'encrypted': encryptedText})

def about(request):
    return HttpResponse("Hello Universe")

def history(request):
    latest_userInput_list = UserInput.objects.order_by('pub_date')
    template = loader.get_template('caesarapp/history.html')
    context = {
        'latest_userInput_list': latest_userInput_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'caesarapp/history.html', context)