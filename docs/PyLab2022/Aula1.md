PYLAB 2022 - AULA 1
Conceitos
Cliente servidor:
Fluxo de dados no Django:
A aplicação:
Configurações iniciais:


# Primeiro devemos criar o ambiente virtual:
# Criar Linux
python3 -m venv venv
# Windows
python -m venv venv


# Após a criação do venv vamos ativa-lo:
#Ativar Linux
source venv/bin/activate
# Windows
venv\Scripts\Activate

# Caso algum comando retorne um erro de permissão execute o código e tente novamente:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Agora vamos fazer a instalação do Django e as demais bibliotecas:
pip install django
pip install pillow

# Vamos criar o nosso projeto em Django:
django-admin startproject seletive .

# Vamos criar um app para lidar com as Empresas
python3 manage.py startapp empresa

# LEMBRE-SE de cadastrar o app em settings.INSTALLED_APPS

## Criar nova empresa

# Crie uma URL que aponte para o app empresa:
path('home/', include('empresa.urls'))

# Crie um arquivo urls.py no app empresa :
from django.urls import path
from . import views
urlpatterns = [
    path('nova_empresa/', views.nova_empresa, name="nova_empresa"),
]

# Agora é necessário criar a função nova_empresa que chamamos na URL acima:
def nova_empresa(request):
    return HttpResponse('Estou aqui')

# Configure os templates em settings.py:
os.path.join(BASE_DIR, 'templates')

# Em templates crie um arquivo chamado base.html:
<!doctype html>
<html lang="pt-BR">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block 'title' %}{% endblock%}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet">
    {% block 'head' %}{% endblock%}
</head>

<body>

    <nav class="navbar navbar-expand-lg navbar-dark bg-nav">
        <a class="navbar-brand" href="#">SELETI.VE</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

    </nav>

    {% block 'body' %}{% endblock%}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>

# Vamos criar o html de nova_empresa, em plataforma/templates crie um arquivo chamado nova_empresa.html:
{% extends "base.html" %}

{% block 'body' %}

<div class="wrapper">
    <div class="box">
        <div class="header">
            <h3 class="titulo">Nova empresa</h3>
        </div>

        <div class="body-box">
            <form action="" method="" enctype="multipart/form-data">
                <div class="row">
                    <div class="col-md">
                        <label>Nome:</label>
                        <input type="text" class="form-control" name="nome" placeholder="Digite seu nome...">
                    </div>

                    <div class="col-md">
                        <label>E-mail:</label>
                        <input type="email" class="form-control" name="email" placeholder="email@gmail.com">
                    </div>

                </div>
                <br>
                <div class="row">
                    <div class="col-md">
                        <label>Cidade:</label>
                        <input type="text" class="form-control" name="cidade"
                            placeholder="Digite a cidade da empresa...">
                    </div>

                    <div class="col-md">
                        <label>Endereço:</label>
                        <input type="text" class="form-control" name="endereco" placeholder="Rua...">
                    </div>

                </div>
                <br>
                <div class="row">
                    <div class="col-md">
                        <label>Nicho de mercado:</label>
                        <select class="form-control" name="nicho">
                            <option value="M">Marketing</option>
                            <option value="N">Nutrição</option>
                            <option value="D">Design</option>
                        </select>
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-md">
                        <label>Tecnologias usadas:</label>
                        <select class="form-control" name="tecnologias" multiple>
                            <option value=""></option>

                        </select>
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-md">
                        <label>Característica da empresa:</label>
                        <textarea name="caracteristicas" class="form-control"></textarea>
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-md">
                        <label>Logo:</label>
                        <input type="file" class="form-control" name="logo">
                    </div>
                </div>
                <br>
                <input type="submit" value="Nova empresa" class="btn btn-lg btn-orange">
            </form>

        </div>
    </div>
</div>


{% endblock%}

# Agora é necessário adicionar um CSS para deixar as páginas visualmente mais agradáveis, e para isso precisamos
# configurar os arquivos estáticos em settings.py:
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join('static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Com os arquivos estáticos configurados podemos criar uma pasta static dentro de templates para adicionar o CSS.
# Em base.css adicione:
body{

background-color: #C6C6C6;

}

.bg-nav{
background-color: #3B0032 !important;
padding: 10px;
}

# No HTML vamos importar o arquivo css criado anteriormente:
<link href="{% static 'base/css/base.css' %}" rel="stylesheet">

# Vamos agora para o css de nova_empresa.css:
.wrapper {
    margin-top: 3%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.box {
    padding: 30px;
    width: 40vw;
    background: #fff;
    box-shadow: 4px 4px 10px rgba(0,0,0,.3);
}

.header{
    border-bottom: 1px solid black;
}

.titulo{

    color: #7D2948;
}

.body-box{
    margin-top: 20px;
}

.btn-orange{

    background-color: #ED8554;
    color: white;
}

.btn-orange:hover{

background-color: #be6136;
    color: white;
}

@media (max-width: 1000px)
{
    .box{
        width: 80vw;
    }
}

# Vamos começar a criar o banco de dados:
from django.db import models

class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia

class Empresa(models.Model):
    choices_nicho_mercado = (
        ('M', 'Marketing'),
        ('N', 'Nutrição'),
        ('D', 'Design')
    )
    logo = models.ImageField(upload_to="logo_empresa")
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    tecnologias = models.ManyToManyField(Tecnologias)
    endereco = models.CharField(max_length=60)
    nicho_mercado = models.CharField(max_length=3, choices=choices_nicho_mercado)
    caracteristica_empresa = models.TextField()

    def __str__(self) -> str:
        return self.nome

class Vagas(models.Model):
    choices_experiencia = (
        ('J', 'Júnior'),
        ('P', 'Pleno'),
(       'S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado')
        )

    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=30)
    nivel_experiencia = models.CharField(max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologias)
    tecnologias_estudar = models.ManyToManyField(Tecnologias, related_name='estudar')


    def __str__(self):
        return self.titulo

# Execute as migrações:
python manage.py makemigrations
python manage.py migrate

# Cadastre as models no admin.py:
from .models import Tecnologias, Empresa, Vagas

admin.site.register(Tecnologias)
admin.site.register(Empresa)
admin.site.register(Vagas)

# Agora precisamos preencher o campo tecnologias dinamicamente, para isso vamos buscar todas as tecnologias salvas do
# banco:
def nova_empresa(request):
    techs = Tecnologias.objects.all()
    return render(request, 'nova_empresa.html', {'techs': techs})

# Vamos inserir os dados no HTML:
{% for tech in techs %}
    <option value="{{tech.id}}">{{tech.tecnologia}}</option>
{% endfor %}

# Adicione os seguintes parâmetros na tag form:
action="{% url 'nova_empresa' %}" method="POST" enctype="multipart/form-data"

# Receba os dados enviados do formulário em sua view:
def nova_empresa(request):
    if request.method == "GET":
        techs = Tecnologias.objects.all()
        return render(request, 'nova_empresa.html', {'techs': techs})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        caracteristicas = request.POST.get('caracteristicas')
        tecnologias = request.POST.getlist('tecnologias')
        logo = request.FILES.get('logo')

# Faça as validações:
if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cidade.strip()) == 0 or len(endereco.strip()) == 0 or
    len(nicho.strip()) == 0 or len(caracteristicas.strip()) == 0 or (not logo)):
    messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
    return redirect('/home/nova_empresa')

if logo.size > 100_000_000:
    messages.add_message(request, constants.ERROR, 'A logo da empresa deve ter menos de 10MB')
    return redirect('/home/nova_empresa')

if nicho not in [i[0] for i in Empresa.choices_nicho_mercado]:
    messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
    return redirect('/home/nova_empresa')

# Em settings.py configure as mensagens:
from django.contrib.messages import constants

MESSAGE_TAGS = {
    constants.DEBUG: 'alert-primary',
    constants.ERROR: 'alert-danger',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info',
    constants.WARNING: 'alert-warning',
}
Exiba no HTML as mensagens de erro:
{% if messages %}
    {% for message in messages %}
        <section class="alert {{message.tags}}">
            {{message}}
        </section>
    {% endfor %}
{% endif %}

# Agora é só salvar os dados no banco:
def nova_empresa(request):
    if request.method == "GET":
        techs = Tecnologias.objects.all()
        return render(request, 'nova_empresa.html', {'techs': techs})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        caracteristicas = request.POST.get('caracteristicas')
        tecnologias = request.POST.getlist('tecnologias')
        logo = request.FILES.get('logo')

        if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cidade.strip()) == 0 or len(endereco.strip()) == 0 or
        len(nicho.strip()) == 0 or len(caracteristicas.strip()) == 0 or (not logo)):
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('/home/nova_empresa')

        if logo.size > 100_000_000:
        messages.add_message(request, constants.ERROR, 'A logo da empresa deve ter menos de 10MB')
        return redirect('/home/nova_empresa')

        if nicho not in [i[0] for i in Empresa.choices_nicho_mercado]:
        messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
        return redirect('/home/nova_empresa')

        empresa = Empresa(logo=logo,
                        nome=nome,
                        email=email,
                        cidade=cidade,
                        endereco=endereco,
                        nicho_mercado=nicho,
                        caracteristica_empresa=caracteristicas)
    empresa.save()
    empresa.tecnologias.add(*tecnologias)
    empresa.save()
    messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
    return redirect('/home/empresas')

# Listar empresas
# Com o cadastro de empresas finalizado agora podemos partir para a listagem.
# Vamos começar criando a URL para listagem:
path('empresas/', views.empresas, name="empresa"),

# Defina a view empresas:
def empresas(request):
    empresas = Empresa.objects.all()
    tecnologias = Tecnologias.objects.all()
    return render(request, 'empresa.html', {'empresas': empresas, 'tecnologias': tecnologias})


# Crie o arquivo empresa.html:
{% extends 'base.html' %}

{% block 'body' %}
<div class="wrapper">
    <div class="box">
        <div class="header-box">
            {% if messages %}
            {% for message in messages %}
            <section class="alert {{message.tags}}">
                {{message}}
            </section>
            {% endfor %}
            {% endif %}
            <h2 class="titulo">Gerenciar empresas</h2>
            <a class="btn-nova-empresa">Nova empresa</a>
        </div>
        <div class="borda-box"></div>
        <div class="body-box">

            <form>
                <div class="row">

                    <div class="col-md-5">
                        <input type="text" placeholder="Busque pelo nome" class="form-control" name="nome">
                    </div>

                    <div class="col-md-4">
                        <select class="form-select" name="tecnologias">
                            <option value="">--------</option>
                        </select>
                    </div>

                    <div class="col-md-3">
                        <input type="submit" value="FILTRAR" class="btn btn-lg btn-orange">
                    </div>
                </div>
            </form>

            <table class="tabela" cellpadding="20">
                <tr>
                    <th>Nome</th>
                    <th>Endereço</th>
                    <th>Tecnologias usadas</th>
                    <th>Quantidade de vagas</th>
                    <th>Ação</th>
                </tr>


                <tr class="tabela-linha">
                    <td>Nome da empresa</td>
                    <td>Endereço da empresa</td>
                    <td>
                        <select class="form-select">
                            <option></option>
                        </select>
                    </td>
                    <td>
                        Quantidade de vagas
                    </td>
                    <td>
                        <a class="btn-excluir">Excluir empresa</a>
                    </td>
                </tr>

            </table>
        </div>




    </div>
</div>

{% endblock%}

# Crie o empresas.css:
.wrapper {
    margin-top: 3%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.box {

    width: 80vw;
    background: #fff;
    box-shadow: 4px 4px 10px rgba(0,0,0,.3);
}


.titulo{
    display: inline;
    }

.btn-nova-empresa{
    float: right;
    text-decoration: none;
    color: white;
    background-color: #7D2948;
    padding: 10px;
    border-radius: 10px;
    font-weight: bold;
}

.btn-nova-empresa:hover{
    color: white;
    text-decoration: none;
    background-color: #631f38;
}

.btn-excluir:hover{
    color: white;
    text-decoration: none;
    background-color: #631f38;
}

.header-box{

    padding: 30px;

}

.borda-box{
    border-top: 1px solid black;
}

.body-box{
    padding: 30px;
}

.btn-orange{

    background-color: #ED8554;
    color: white;
}


.tabela{
    width: 100%;
    margin-top: 20px;
}

.tabela-linha{
    background-color: #EDE6E6;
}

.btn-excluir{
    text-decoration: none;
    color: white;
    background-color: #7D2948;
    padding: 10px;
    border-radius: 10px;
    font-weight: bold;
}

# Importe o css em empresas.html:
{% load static %}

{% block 'head' %}
    <link href="{% static 'empresa/css/empresas.css' %}" rel="stylesheet">
{% endblock%}

# Liste as empresas dinamicamente:
{% for empresa in empresas%}
<tr class="tabela-linha">
    <td>{{empresa.nome}}</td>
    <td>{{empresa.endereco}}</td>
    <td>
        <select class="form-select">
            <option></option>
        </select>
    </td>
    <td>
        Quantidade de vagas
    </td>
    <td>
        <a class="btn-excluir">Excluir empresa</a>
    </td>
</tr>
{% endfor %}

# Exiba as tecnologias de cada empresa:
{% for tech in empresa.tecnologias.all %}
    <option>{{tech}}</option>
{% endfor %}

# Por fim, vamos colorir a linha da tabela uma sim e uma não
# Adicione na linha:
{% if not forloop.counter|is_par %} class="tabela-linha" {% endif %}

# Crie o filtro is_par:
from django import template

register = template.Library()

@register.filter(name='is_par')
def is_par(valor):
return True if valor % 2 == 0 else False
Registre os filtros na livraria:
'libraries': {
'filtro': 'empresa.templatetags.filtro',
}
Carregue os filtros:
{% load filtro %}
Deletar empresa