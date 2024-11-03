from django.shortcuts import render, redirect, reverse
from noivos.models import Presentes, Convidados

# Create your views here.
def convidados(request):
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    presente = Presentes.objects.filter(reservado=False).order_by('-importancia')
    return render(request, 'convidado.html', {'convidado':convidado, 'presentes':presente})

def responder_presenca(request):
    resposta = request.GET.get('resposta')
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    if resposta not in ['C', 'R']:
        messages.add_message(request, constants.ERROR, 'Você deve confirmar ou recusar')
        return redirect(f'{reverse('convidados')}?token={token}')
    
    convidado.status = resposta
    convidado.save()

    return redirect(f'{reverse('convidados')}?token={token}')

def reservar_presente(request, id):
    token = request.GET.get('token')

    convidado = Convidados.objects.get(token=token)
    presente = Presentes.objects.get(id=id)

    presente.reservado=True
    presente.reservado_por = convidado
    presente.save()
    return redirect(f'{reverse('convidados')}?token={token}')