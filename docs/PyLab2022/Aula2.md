PYLAB 2022 - AULA 2
# Listagem das empresas
# Vamos começar a aula adicionando a quantidade de vagas que cada empresa possui.
# Para isso, crie um método qtd_vagas em models.py:

def qtd_vagas(self):
        return Vagas.objects.filter(empresa__id=self.id).count()

# Agora no template vamos exibir a quantidade de vagas e uma bandeira:
{% if empresa.qtd_vagas > 0 %}
    <img src="{% static 'empresa/img/flag_green.png' %}">
{% else %}
    <img src="{% static 'empresa/img/flag_red.png' %}">
{% endif %}
&nbsp&nbsp{{empresa.qtd_vagas}}

# Adicione os ícones abaixo em seus arquivos estáticos:


# Filtrando empresas
# Adicione as seguintes propriedades no form:
action="{% url 'empresa' %}" method="GET"

# Agora preencha o select com todas as tecnologias:
{% for tech in tecnologias%}
    <option value="{{tech.id}}">{{tech}}</option>
{% endfor %}

# Faça os filtros na view empresas:
def empresas(request):
    technologias_filtrar = request.GET.get('tecnologias')
    nome_filtrar = request.GET.get('nome')
    empresas = Empresa.objects.all()

    if technologias_filtrar:
        empresas = empresas.filter(tecnologias = technologias_filtrar)
    
    if nome_filtrar:
        empresas = empresas.filter(nome__icontains = nome_filtrar)

    tecnologias = Tecnologias.objects.all()
    return render(request, 'empresa.html', {'empresas': empresas, 'tecnologias': tecnologias})


# Acessando uma única empresa
# Crie uma URL para empresa:
path('empresa/<int:id>', views.empresa, name="empresa_unica"),

# Agora vamos para view empresa:
def empresa(request, id):
    empresa_unica = get_object_or_404(Empresa, id=id)
    return render(request, 'empresa_unica.html', {'empresa': empresa_unica})

# Crie o empresa.html
{% extends 'base.html' %}
{% load static %}

{% block 'head' %}
    <link href="{% static 'empresa/css/empresa.css' %}" rel="stylesheet">
{% endblock%}


{% block 'body' %}

    
    <br>
    <div class="container">
        {% if messages %}
            {% for message in messages %}
                <br>
                <section class="alert {{message.tags}}">
                    {{message}}
                </section>
            {% endfor %}
        {% endif %}    
        <div class="row">
            <div class="col-md-3">
                <img width="100%" src="{{empresa.logo.url}}">
            </div>

            <div class="col-md">
                <h1 class="titulo">{{empresa.nome}}</h1>
                <p class="paragrafo">{{empresa.endereco}}</p>
            </div>



        </div>
        <br>
        <div class="row">
            <div class="col-md-6">
                <label>Nicho de mercado:</label>
                <input disabled type="text" class="form-control" value="Nicho">
            </div>

            <div class="col-md-3">
                <label>Tecnologias usadas:</label>
                <select class="form-select">   
                       <option>---</option>

                </select>
                
            </div>
        </div>
        <br>
        <div class="row">
            <div class="col-md-7">
                <label>Características da empresa:</label>
                <textarea disabled class="form-control">{{empresa.caracteristica_empresa}}</textarea>
            </div>

            <div class="col-md-3">
                
                
            </div>
        </div>

        <hr>

        <a class="btn btn-lg btn-orange">Nova vaga</a>

        <div class="row">
            vagas
        </div>

    </div>
    <br>
    <br>

{% endblock %}


# Crie a url para os arquivos de media:
from django.conf import settings
from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Preencha os campos com os dados da empresa:
#Nicho
<input disabled type="text" class="form-control" value="{{empresa.get_nicho_mercado_display}}">

#Tecnologias
{% for tech in empresa.tecnologias.all %}
    <option>{{tech}}</option>

{% endfor %}

#Caracteristicas
<textarea disabled class="form-control">{{empresa.caracteristica_empresa}}</textarea>


# Nova vaga
# Crie o modal com o formulário para nova vaga:
<div class="modal fade modal-lg" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 style="font-size: 30px" class="modal-title titulo" id="exampleModalLabel">Nova vaga</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form action="" method="POST">
                    <div class="row">
                        <div class="col-md">
                            <label>Título:</label>
                            <input type="text" name="titulo" class="form-control" placeholder="Digite o título da vaga...">
                        </div>

                        <div class="col-md">
                            <label>Email:</label>
                            <input type="email" name="email" class="form-control" placeholder="email@email.com.br">
                        </div>
                        
                    </div>
                    <br>
                    <div class="row">
                        <div class="col-md">
                            <label>Tecnologias que já domino:</label>
                            <select name="tecnologias_domina" class="form-select" multiple>
                                {% for tech in tecnologias %}
                                    <option value="{{tech.id}}">{{tech}}</option>
                                {% endfor %}

                            </select>
                        </div>

                        <div class="col-md">
                            <label>Tecnologias que não domino:</label>
                            <select name="tecnologias_nao_domina" class="form-select" multiple>
                                {% for tech in tecnologias %}
                                    <option value="{{tech.id}}">{{tech}}</option>
                                {% endfor %}

                            </select>
                        </div>
                        
                    </div>
                    <br>
                    <div class="row">
                        <div class="col-md">
                            <label>Nível de experiência:</label>
                            <select name="experiencia" class="form-select">
                                <option value="J">Júnior</option>
                                <option value="P">Pleno</option>
                                <option value="S">Sênior</option>
                            </select>
                        </div>

                        <div class="col-md">
                            <label>Data final:</label>
                            <input type="date" class="form-control" name="data_final"> 
                            
                        </div>
                        
                    </div>
                    <br>
                    <div class="row">
                        <div class="col-md">
                            <label>Empresa:</label>
                            <select name="empresa" class="form-select">
                                                                                                                                 
                            </select>
                        </div>
       
                    </div>

                    <br>
                    <div class="row">
                        <div class="col-md">
                            <label>Status:</label>
                            <select name="status" class="form-select">     
                                <option value="I">Interesse</option>
                                <option value="C">Currículo enviado</option>    
                                <option value="E">Entrevista</option>    
                                <option value="D">Desafio técnico</option>    
                                <option value="F">Finalizado</option>          
                            </select>
                        </div>
       
                    </div>
                    <br>
                    <input type="submit" value="Nova empresa" class="btn btn-lg btn-orange">

                </form>
            </div>
           
            </div>
        </div>
    </div>


# Chame o modal através do botão nova empresa:
<a data-bs-toggle="modal" data-bs-target="#exampleModal" class="btn btn-lg btn-orange">Nova vaga</a>


# Adicione no empresa.css
.titulo{

    color: #7D2948;
    font-weight: bold;

}

.paragrafo{
    font-size: 25px;
}

.btn-orange{

    background-color: #ED8554;
    color: white;
}

label{
    font-weight: bold;
}

.box-vagas{

    width: 400px;
    margin-top: 60px;
    background-color: #EDE6E6;
}

.header-vagas{
    background-color: #7D2948;
    padding: 15px;
    color: white
}

.body-vagas{
    padding: 15px;
}

.paragrafo-orange{
    color: #ED8554;
}

# Busque os dados necessário na view empresa:
def empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    empresas = Empresa.objects.all()
    tecnologias = Tecnologias.objects.all()
    vagas = Vagas.objects.filter(empresa_id=id)
    return render(request, 'empresa_unica.html', {'empresa': empresa,
                                            'tecnologias': tecnologias,
                                            'empresas': empresas,
                                            'vagas': vagas})

# Liste as empresas a propeidade select no option permite selecionarmos a opção correta:
{% for empresa_iter in empresas %}
    <option {% if empresa_iter.id == empresa.id %}selected{%endif%}  value="{{empresa_iter.id}}">{{empresa_iter}}</option>
{% endfor %}

# Crie o app vagas:
python3 manage.py startapp vagas

# Instale o app!!
# Crie uma URL para o app criado:
path('vagas/', include('vagas.urls'))

# Crie o urls.py:
from django.urls import path
from . import views

urlpatterns = [
    path('nova_vaga/', views.nova_vaga, name="nova_vaga")
]

# Vamos para views nova_vaga:
def nova_vaga(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        email = request.POST.get('email')
        <!-- usar o getlist para coletar todos os valores selecionados-->
        tecnologias_domina = request.POST.getlist('tecnologias_domina')
        tecnologias_nao_domina = request.POST.getlist('tecnologias_nao_domina')
        experiencia = request.POST.get('experiencia')
        data_final = request.POST.get('data_final')
        empresa = request.POST.get('empresa')
        status = request.POST.get('status')

        # TODO: validations

        vaga = Vagas(
                    titulo=titulo,
                    email=email,
                    nivel_experiencia=experiencia,
                    data_final=data_final,
                    empresa_id=empresa,
                    status=status,
        )


        vaga.save()

        <!-- * significa que precisamos descompactar pois vem em uma lista  -->
        vaga.tecnologias_estudar.add(*tecnologias_nao_domina)
        vaga.tecnologias_dominadas.add(*tecnologias_domina)

        vaga.save()
        messages.add_message(request, constants.SUCCESS, 'Vaga criada com sucesso.')
        return redirect(f'/home/empresa/{empresa}')
    elif request.method == "GET":
        raise Http404()

# Adicione o campo E-mail em vagas:
email = models.EmailField(null=True)

# Faça as migrações:
python manage.py makemigrations
python manage.py migrate

# Agora é só listar as vagas de cada empresa:
{% for vaga in vagas %}
    <div class="col-md">

    <div class="box-vagas">
        <div class="header-vagas">
            {{vaga.titulo}}
        </div>

        <div class="body-vagas">
            <div class="row">
                <div class="col-md">
                    <label class="paragrafo">Nível:</label>
                    <br>        
                    <label class="paragrafo paragrafo-orange">{{vaga.get_nivel_experiencia_display}}</label>                           
                </div>

                <div class="col-md">
                    <label class="paragrafo">Status <img src="{% static 'empresa/img/flag_green.png' %}"></label>
                    <br>        
                    <label class="paragrafo paragrafo-orange">{{vaga.get_status_display}}</label>                           
                </div>

            </div>
        </div>
        
    </div>
        
    </div>
{% endfor %}
