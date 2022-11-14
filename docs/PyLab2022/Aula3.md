
# PYLAB 2022 | AULA 3
# Acessando uma vaga
# Crie uma nova URL para vaga
path('vaga/<int:id>', views.vaga, name="vaga"),

# Crie a views vaga:
def vaga(request, id):
    vaga = get_object_or_404(Vagas, id=id)
    return render(request, 'vaga.html', {'vaga': vaga})

# Crie o HTML vaga.html
{% extends 'base.html' %}
{% load static %}

{% block 'head' %}
    <link rel="stylesheet" href="{% static 'vaga/css/vaga.css' %}"> 
{% endblock %}

{% block 'body' %}
    <div class="container">
        {% if messages %}
            {% for message in messages %}
            <br>
                <section class="alert {{message.tags}}">
                    {{message}}
                </section>
            {% endfor %}
        {% endif %}
        <br>
        <h3 class="titulo">{{vaga.titulo}}</h3>
        <p class="titulo2">{{vaga.empresa}}</p>
        <p>Progresso atual</p>
        
        <div style="width: 40%" class="progress">
            <div class="progress-bar progress-bar-striped bg-success" role="progressbar" style="width: 80%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
    </div>

    <div class="bg2">
        <div class="container">
            <div class="row">
                <div class="col-md">
                    <p class="titulo2">Crie uma tarefa</p>
                    <p>Lembre-se de realizar todas suas tarefas com antecedência</p>


                    <form>
                        <label>Título:</label>
                        <input name="titulo" type="text" class="form-control input-tarefa" placeholder="Digite o título da tarefa..."> 
                        <br>
                        <label>Prioridade:</label>
                        <select name="prioridade" class="form-select input-tarefa">
                            <option value="U">Urgente</option>
                            <option value="A">Alta</option>
                            <option value="B">Baixa</option>
                        </select>
                        <br>
                        <label>Data:</label>
                        <input name="data" type="date" class="form-control input-tarefa" placeholder=""> 
                        <br>
                        <input type="submit" value="Nova tarefa" class="btn btn-orange">

                    </form>

                </div>

                <div class="col-md">
                    
                        <div class="li-tarefa">
                            <label>Título</label>
                            <label class="prioridade-bloco">
                                <svg class="prioridade-vermelho" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-triangle-fill" viewBox="0 0 16 16">
                                    <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                                </svg>
                            </label>
                            <label class="prioridade-bloco">
                                Data
                            </label>
                            <label class="prioridade-bloco">
                                <a href="#" class="btn btn-success">Finalizado</a>
                            </label>

                        </div>
                </div>

            </div>
        </div>

    </div>

    <div class="container bg3">
        <div class="row">

            <div class="col-md">
                <p class="titulo2">Enviar E-mail</p>
                <p>Envie e-mails para essa vaga por aqui.</p>
            </div>

            <div class="col-md">
                <form>
                    <label>Assunto:</label>
                    <input name="assunto" type="text" class="form-control" placeholder="assunto">
                    <br>
                    <label>Corpo do email:</label>
                    <textarea name="corpo" class="form-control"></textarea>
                    <br>
                    <input type="submit" class="btn btn-orange" value="Enviar">
                </form>
            </div>
        </div>

    </div>


    <div class="bg2">
        <div class="container">
            <div class="row"> 
                <h3 class="titulo">Histórico de e-mails</h3>
                
                    <div class="col-md">

                        <div class="box-email">
                            <div class="header-email">
                                Assunto
                            </div>

                            <div class="body-email">
                                Corpo do email
                            </div>
                            
                        </div>
            
                    </div>
                
                
                  
            </div> 
            
                    
        </div>
    </div>

    <div class="container bg3">
        <div class="row">
            <div class="col-md">
                <p class="titulo2">Tecnologias que domino</p>

                <div class="li-tech">
                    Python

                    <svg class="arrow-right" xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
                    </svg>
                </div>

            </div>

            <div class="col-md">
                <p class="titulo2">Preciso estudar</p>

                <div class="li-tech">
                    <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
                    </svg>
                    Python
                </div>
            </div>
        </div>
    </div>
{% endblock %}

# Crie o CSS de vaga
.titulo{

    color: #7D2948;
    font-weight: bold;
    font-size: 35px;

}

.titulo2{

    font-weight: bold;
    font-size: 30px;

}

.bg2{

    background-color: #EDE6E6;
    margin-top: 40px;
    padding-top: 30px;
    padding-bottom: 30px;

}


.input-tarefa{

    width: 60%;

}

.btn-orange{

    background-color: #ED8554;
    color: white;
}

.list-tarefa{
    list-style: none;
}

.li-tarefa{
    background-color: #3B0032;
    padding: 10px;
    color:white;
    border-radius: 10px;
    margin-top: 10px;
}

.li-tech{
    background-color: #3B0032;
    padding: 10px;
    color:white;
    border-radius: 10px;
    margin-top: 10px;
    width: 60%;
}

.arrow-right{
    float: right;
    
}

.prioridade-bloco{
    margin-left: 20px;
}

.prioridade-vermelho{
    color: red;
}

.prioridade-amarelo{
    color: yellow;
}

.prioridade-verde{
    color: green;
}

.bg3{

    padding-top: 30px;
    padding-bottom: 30px;
}

.box-email{

    width: 400px;
    margin-top: 60px;
    background-color: #C9C3C3;
    box-shadow: 2px 2px 2px 2px rgba(0,0,0,.5);
}

.header-email{
    background-color: #7D2948;
    padding: 15px;
    color: white
}

.body-email{
    padding: 15px;
}

.paragrafo-orange{
    color: #ED8554;
}

# Barra de progresso
# Na model vagas crie o seguinte método:

def progresso(self):
        x = [((i+1)*20,j[0]) for i, j in enumerate(self.choices_status)]
        x = list(filter(lambda x: x[1] == self.status, x))[0][0]
        return x


# Altere o preenchimento da barra dinamicamente:

{{vaga.progresso}}

# Tarefas
# Crie a model tarefas

class Tarefa(models.Model):
    choices_prioridade = (
        ('B', 'Baixa'),
        ('A', 'Alta'),
        ('U', 'Urgente')
    )
    vaga = models.ForeignKey(Vagas, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    prioridade = models.CharField(max_length=1, choices=choices_prioridade)
    data = models.DateField()
    realizada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


# Execute as migrações!

# Crie a url nova_tarefa:

path('nova_tarefa/<int:id_vaga>', views.nova_tarefa, name='nova_tarefa'),


# Crie a views nova_tarefa:

def nova_tarefa(request, id_vaga):
    titulo = request.POST.get('titulo')
    prioridade = request.POST.get("prioridade")
    data = request.POST.get('data')
    
    tarefa = Tarefa(vaga_id=id_vaga,
                    titulo=titulo,
                    prioridade=prioridade,
                    data=data)
    tarefa.save()
    messages.add_message(request, constants.SUCCESS, 'Tarefa criada com sucesso')
    return redirect(f'/vagas/vaga/{id_vaga}')

# Adicione os dados no <form>:

action="{% url 'nova_tarefa' vaga.id %}" method="POST"


# Agora precisamos listar as tarefas, para isso busque os dados na view vaga:

def vaga(request, id):
    vaga = get_object_or_404(Vagas, id=id)
    tarefas = Tarefa.objects.filter(vaga=vaga).filter(realizada=False)
    return render(request, 'vaga.html', {'vaga': vaga,
                                         'tarefas': tarefas,})

# Liste as tarefas no HTML:

{% for tarefa in tarefas %}
    <div class="li-tarefa">
        <label>{{tarefa.titulo}}</label>
        <label class="prioridade-bloco">
            <svg class="prioridade-vermelho" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-triangle-fill" viewBox="0 0 16 16">
                <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
            </svg>
        </label>
        <label class="prioridade-bloco">
            {{tarefa.data}}
        </label>
        <label class="prioridade-bloco">
            <a href="#" class="btn btn-success">Finalizado</a>
        </label>

    </div>
{% endfor %}


# Agora precisamos exibir o ícone dinamicamente, e para isso crie o método icon na models tarefas:

from django.utils.safestring import mark_safe
def icon(self):
        if self.prioridade == "U":
            classe = 'prioridade-vermelho'
        elif self.prioridade == "A":
            classe = 'prioridade-amarelo'
        elif self.prioridade == "B":
            classe = 'prioridade-verde'

        icon = f'''<svg  class="{classe}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-triangle-fill" viewBox="0 0 16 16">
                                    <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                    </svg>'''

        return mark_safe(icon)

# Nos templates é só adicionar:

{{tarefa.icon}}

# Vamos criar uma URL para marcar a tarefa como finalizada:

path('realizar_tarefa/<int:id>', views.realizar_tarefa, name='realizar_tarefa'),

# Crie a view realizar_tarefa:

def realizar_tarefa(request, id):
    tarefas_list = Tarefa.objects.filter(id=id).filter(realizada=False)

    if not tarefas_list.exists():
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema!')
        return redirect(f'/home/empresas/')

    tarefa = tarefas_list.first()
    tarefa.realizada = True
    tarefa.save()    
    messages.add_message(request, constants.SUCCESS, 'Tarefa realizada com sucesso, parabéns!')
    return redirect(f'/vagas/vaga/{tarefa.vaga.id}')

# No botão realizado redireciona para a URL criada:

{% url 'realizar_tarefa' tarefa.id %}


# Emails
# Faça as configurações em settings.py


# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_USER = "seu_email@email.com.br"


# Crie a URL para o envio de E-mails:

path('envia_email/<int:id_vaga>', views.envia_email, name="envia_email")


# Crie um template HTML para os emails:

<html>
    <head>
        
    </head>

    <body>
        
        {{corpo}}
        <footer>
            E-mail enviado por SELETIVE.
        </footer>
    </body>

</html>


# Crie a view envia_email:


from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

def envia_email(request, id_vaga):
    vaga = Vagas.objects.get(id=id_vaga)
    assunto = request.POST.get('assunto')
    corpo = request.POST.get('corpo')

    html_content = render_to_string('emails/template_email.html', {'corpo': corpo})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(assunto, text_content, settings.EMAIL_HOST_USER, [vaga.email,])
    email.attach_alternative(html_content, "text/html")
    if email.send():  
        messages.add_message(request, constants.SUCCESS, 'Email enviado com sucesso.')
        return redirect(f'/vagas/vaga/{id_vaga}')
    else:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema!')
        return redirect(f'/vagas/vaga/{id_vaga}')


# No formulário de envio de e-mail adicione:

action="{% url 'envia_email' vaga.id%}" method="POST"


# Agora vamos salvar os E-mails no banco.

# Crie uma model Email:

class Emails(models.Model):
    vaga = models.ForeignKey(Vagas, on_delete=models.DO_NOTHING)
    assunto = models.CharField(max_length=100)
    corpo = models.TextField()
    enviado = models.BooleanField()

    def __str__(self):
        return self.assunto


# Faça as migrações!

Quando o E-mail for enviado, salve no banco:

if email.send():
    mail = Emails(
        vaga=vaga,
        assunto=assunto,
        corpo=corpo,
        enviado=True
    )
    mail.save()
    messages.add_message(request, constants.SUCCESS, 'Email enviado com sucesso.')
    return redirect(f'/vagas/vaga/{id_vaga}')
else:
    mail = Emails(
        vaga=vaga,
        assunto=assunto,
        corpo=corpo,
        enviado=False
    )
    mail.save()
    messages.add_message(request, constants.ERROR, 'Erro interno do sistema!')
    return redirect(f'/vagas/vaga/{id_vaga}')


# Para listar os e-mails vamos buscar eles no banco:

emails = Emails.objects.filter(vaga=vaga)


# Exiba os e-mails no template:

{% for email in emails%}
    <div class="col-md">

        <div class="box-email">
            <div class="header-email">
                {{email.assunto}}
            </div>

            <div class="body-email">
                {{email.corpo}}
            </div>
            
        </div>

    </div>
{% endfor %}


# Materiais complementares

Assista apenas após a conclusão da AULA 2 DA PYLAB 2022

[https://www.youtube.com/watch?v=JSwofXOC4OY](https://www.youtube.com/watch?v=JSwofXOC4OY)

Gerar credenciais do GMAIL:

[https://medium.com/@heltonteixeira92/enviando-e-mail-com-django-e-uma-conta-gmail-atualizado-2022-bc2f186811ec](https://medium.com/@heltonteixeira92/enviando-e-mail-com-django-e-uma-conta-gmail-atualizado-2022-bc2f186811ec)

# Desafios

Para treinar suas habilidades cada vez mais vou deixar 2 desafios.

→ Permitir alteração do status de uma vaga

→ Desenvolver funcionalidades das tecnologias que domina ou não.