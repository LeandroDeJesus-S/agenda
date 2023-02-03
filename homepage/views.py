from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Concat
from django.db.models import Q, Value
from django.http import Http404, HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from .edit_contact_form import AddContatctForm
from django.contrib import messages


@login_required(redirect_field_name='login')
def homepage(request):
    contacts = Contato.objects.order_by('Nome').filter(User=request.user)
    paginator = Paginator(contacts, 10)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page)
    return render(request, 'homepage.html', {'contacts': page})


@login_required(redirect_field_name='login')
def contact(request, contato_nome, contato_id):
    contct = get_object_or_404(
        Contato, Nome=contato_nome, id=contato_id, User=request.user
    )
    return render(request, 'contact.html', {'contact': contct})


@login_required(redirect_field_name='login')
def search(request):
    search = request.GET.get('fetch')
    if search is None:
        raise Http404()

    full_name = Concat('Nome', Value(' '), 'Sobrenome')
    contacts = Contato.objects.annotate(full_name=full_name).filter(
        Q(full_name__icontains=search)|Q(Telefone__icontains=search),
        User=request.user
    )
    paginator = Paginator(contacts, per_page=10)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page)
    return render(request, 'search.html', {'contacts': page})


@login_required(redirect_field_name='login')
def delete_contact(request, contact_name, contact_id):
    contact = get_object_or_404(
        Contato, Nome=contact_name, id=contact_id, User=request.user
    )
    if contact.User != request.user:
        raise PermissionDenied()
    
    messages.success(request, f'Contato; "{contact.Nome}" deletado.')
    contact.delete()
    return redirect('homepage')


@login_required(redirect_field_name='login')
def edit_contact(request, contact_name, contact_id):
    contact = get_object_or_404(
        Contato, Nome=contact_name, id=contact_id, User=request.user
    )
    form  = AddContatctForm(instance=contact)
    context = {'form': form, 'contact': contact}
    if request.user != contact.User:
        raise PermissionDenied()

    if request.method == 'GET':
        return render(request, 'edit_contact.html', context)
    
    form = AddContatctForm(request.POST, request.FILES, instance=contact)
    context.update({'form': form})
    if not form.is_valid():
        messages.error(request, 'Dados inválidos')
        return render(request, 'edit_contact.html', context)
    
    form.save()
    messages.success(request, 'Alterações salvas.')
    return redirect(
        'a_contact', contato_nome=contact_name, contato_id=contact_id
    )
