from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Livre
from .forms import SignUpForm, LivreForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('liste_livres')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def livre_create(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            livre = form.save(commit=False)
            livre.ajout_par = request.user
            livre.save()
            return redirect('liste_livres')
    else:
        form = LivreForm()
    return render(request, 'bibliotheque/livre_form.html', {'form': form})

def liste_livres(request):
    query= request.GET.get('q')
    if query:
        livres = Livre.objects.filter(Q(titre__icontains=query)).order_by('-date_ajout')
    else:
     livres = Livre.objects.all().order_by('-date_ajout')
    return render(request,'bibliotheque/liste_livres.html',{'livres':livres})

def Livre_detail(request,pk):
    livre = get_object_or_404(Livre,pk=pk)
    return render(request,'bibliotheque/livre_detail.html',{'livre':livre})
@login_required
def Livre_update(request,pk):
    livre = get_object_or_404(Livre,pk=pk)
    if request.user != livre.ajout_par:
        return redirect('liste_livres')
    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livre modifié avec succès')
            return redirect('liste_livres')
        else:
            messages.error(request,"Erreur dans le formulaire.")
    else:
        form = LivreForm(instance=livre)
        return render(request,'bibliotheque/livre_form.html',{'form':form})
@login_required
def Livre_delete(request,pk):
    livre = get_object_or_404(Livre,pk=pk)
    if request.user != livre.ajout_par:
        return redirect('liste_livres')
    if request.user != livre.ajout_par:
        return redirect('liste_livres')
    if request.method == 'POST':
        livre.delete()
        messages.success(request,"Livre supprimé avec succès !")
        return redirect ('liste_etudiants')
    return render(request,'bibliotheque/Livre_confirm_delete.html',{'livre': livre})

