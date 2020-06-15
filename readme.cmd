site funcionando: http://simplemooc.wesleymends.com.br/

meu site funcionando:  https://simplemooc-psbp.herokuapp.com/

django-3.0.x: https://github.com/django/django/blob/stable/3.0.x/django/contrib/auth/models.py

versao: django - 3.0.6
		python   3.8.3 64bits
		
ewave: niane

# fazendo deploy de aplicação no servidor gratuito: heroku
existem outros google open engine, appfog,  etc.

# aula 73:
Heroku:

1. instalar o heroku toolbelt

2. heroku login

3. heroku keys:add (somente a primeira vez que for subir pro heroku os outro projetos nao precisa mais)

4. instala o pacote do heroku na aplicação do django
 (.venv) C:\code\SimpleMooc>pip install django-toolbelt
 
5. criar arquivo: runtime.txt, com o conteudo:
  python-3.8.3  --> a verso do python que precisa rodar no heroku a versao que foi desenvolvida o projeto
  
6. criar o arquivo Procfile: com o conteudo:
	web: gunicorn SimpleMooc.wsgi
	
7. gerar o arquivo requirements.txt 
(.venv) C:\code\SimpleMooc>pip freeze > requirements.txt  

8.  gerar o git .gitignore
*.pyc
staticfiles

9. iniciar o git
(.venv) C:\code\SimpleMooc>git init

10. adicionar os arquivos
(.venv) C:\code\SimpleMooc>git add .     

11. gravar os arquivos
(.venv) C:\code\SimpleMooc>git commit -m "PRIMEIRO COMMIT"


12. criar projeto no heroku
(.venv) C:\code\SimpleMooc>heroku create

no final o local da aplicacao: To https://git.heroku.com/fathomless-harbor-49389.git

 https://fathomless-harbor-49389.herokuapp.com/
 
 
13. apo renomar a aplicação no heroku: https://simplemooc-psbp.herokuapp.com/, para atualizar a maquina local seguir os passos.
# aula 74
passos:   
    1. verificar como esta
	(.venv) C:\code\SimpleMooc>git remote -v 
	
	2. remover do heroku
	(.venv) C:\code\SimpleMooc>git remote rm heroku
	
	3. adiciona com o nome alterado
	(.venv) C:\code\SimpleMooc>git remote add heroku git.heroku.com/simplemooc-paulobernardo.git
	
    1. verificar como ficou
	(.venv) C:\code\SimpleMooc>git remote -v 
	
	git: https://git.heroku.com/simplemooc-paulobernardo.git
	url: https://simplemooc-paulobernardo.herokuapp.com/
	
	
	 https://git.heroku.com/simplemooc-paulobernardo.gi
	
	
 
 ***** QUANDO PERDER A CONEXAO DO HEROKU COM O GIT 
 ### https://adamatti.github.io/blog/git/2017/06/04/heroku.html
 
 (.venv) C:\code\SimpleMooc>heroku git:remote -a simplemooc-paulobernardo
 #depois fazer o deploy
 (.venv) C:\code\SimpleMooc>git push heroku master
 
 
# Verificar as alterações realidas nos commit por usuario 
    git shortlog


video 10 de python: https://www.youtube.com/watch?v=K0pVZmw_pJU
video explicacao de url: https://www.youtube.com/watch?v=QvTyqta3OJo

$ pip install -r requirements.txt

##### procedimento inicial GIT
git init

git add .

git commit -m 'Proejto inicial'

git remote add origin https://github.com/paulosergiobp69/SimpleMooc.git

git push -u origin master

##### procedimento inicial GIT


Simplemooc
# executando a aplicação: python manage.py runserver


# cria banco de dados inicial projeto simplemooc
# o comando syncdb foi retirado do django o
(versao 1.6)
(.venv) C:\code\simplemooc>python manage.py syncdb
(versao 3.0)

(.venv) C:\code\SimpleMooc>python manage.py makemigrations

(.venv) C:\code\simplemooc>python manage.py migrate
ou 
(.venv) C:\code\simplemooc>python manage.py migrate --run-syncdb

#crias usuario
python manage.py createsuperuser
# usuario criado: paulo.bernardo senha: 123456

#criar uma aplicacao padrao
(.venv) C:\code\simplemooc>python manage.py startapp core

mv core simplemooc  // movendo a pasta para o projeto principal
# configurar settings app
	INSTALLED_APPS = [  
	...,
    'simplemooc.core'
	
# facilidade do django estudar melhor
--->11. URL's (include e namespace)

# para criacao de tabelas courses houve problemas, para tanto foi rodado:
(.venv) C:\code\simplemooc>python manage.py  makemigrations

# e depois 
(.venv) C:\code\simplemooc>python manage.py migrate

# validacoes e querys django: (.venv) C:\code\simplemooc>python manage.py shell

>>> from simplemooc.courses.models import Course
>>> django = Course(name='Python com Django', slug='Django')
>>> django.save()
>>> django.id    --> consulta o registro inserido e/ou instanciado
1
# manual com comandos existentes: https://docs.djangoproject.com/en/3.0/ref/models/querysets/

# outros comandos
courses = Course.objects.all()
for course in courses:
    print(course.name)
	

# atualizando o manager: aula 15 Course manager
>>> from simplemooc.courses.models import Course
>>> Course.objects.search('python')
<QuerySet [<Course: Course object (1)>]>


# secão 2: 17 model admin: definicoes para as telas de crud
__str__ : traducao de nomes de classes

  class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name'] ou ['-name'] ordem ascendente
		
# secao 2: 18
    # adicionado - para o campo slug automaticamente, 
	# nao esquecer da virgula apos o ultimo campo
    prepopulated_fields = {'slug':('name',)} 



# seção 3: 20 
  {{ course.description|linebreaks }}     
  
#para imagens staticas de teste use site: http://placehold.it
# com link: http://placehold.it/400x250
	 
# secao 3 : 27
# form renderizado pelo django se,m fazer nada na pagina exempplo: arquivo courses -> details.html
                    <table>
                    <tbody>
                        {{ form }}
                    </tbody>
                </table>

# para alterar a tabela usuarios foi realizado um adicao na aula: 36


#aula 55 usando templatetgs:

--> muito util: trocar register.assignment_tag por @register.simple_tag

#aula 59: traz forma de trazer comentarios sem fazer escrever nada, apenas com um comando no model, "muito bom".
- traz tbem um exemplo de pluralize



#aula 62: quando nao tem todos os dados na tela e é preciso complementar com parametros com os dados da view
 course -> views -> show_announcement
 course -> forms -> CommentForm
 

#aula 63: utilizacao de signals: mensagens enviadas automaticamente apos a gravacao de um comentarios, 
			sistema disponibilizado pelo django nativo
			

#aula 65: esta tem uma tela de cadastro com aula e material juntas, tipo uma tela cabecalho: aula, detalhe: os materiais das aulas.

#secao 6: aulas de tests apartir de aula:69:
	- para testas models, facilita se instalar o: 
	   Successfully installed model-mommy-X.X.X


# fazendo deploy de aplicação no servidor gratuito: heroku
	   

# aula: 79 paginação e detalhes de forum




