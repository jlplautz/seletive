from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect
from django.http import Http404
from srcprg.empresa.models import Vagas


def nova_vaga(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        email = request.POST.get('email')
        tecnologias_domina = request.POST.getlist('tecnologias_domina')
        tecnologias_nao_domina = request.POST.getlist('tecnologias_nao_domina')
        experiencia = request.POST.get('experiencia')
        data_final = request.POST.get('data_final')
        empresa = request.POST.get('empresa')
        status = request.POST.get('status')

        # strip retira os espaços em branco
        if (len(titulo.strip()) == 0 or len(email.strip()) == 0 or len(experiencia.strip()) == 0 or
            len(data_final.strip()) == 0 or len(empresa.strip()) == 0 or len(status.strip()) == 0): # noqa
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/home/nova_empresa')

        vaga = Vagas(
            titulo=titulo,
            email=email,
            nivel_experiencia=experiencia,
            data_final=data_final,
            empresa_id=empresa,
            status=status,
        )
        vaga.save()

        vaga.tecnologias_estudar.add(*tecnologias_nao_domina)
        vaga.tecnologias_dominadas.add(*tecnologias_domina)

        vaga.save()
        messages.add_message(request, constants.SUCCESS, 'Vaga criada com sucesso.')
        return redirect(f'/home/empresa/{empresa}')

    elif request.method == "GET":
        raise Http404()
