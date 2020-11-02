# Apostas-WebApp       

<h2>Sistema de apostas</h2>
A inspiração deste projecto vem de uma atividade muito comum em tempos de jogos de copa do mundo:
Apostar em um Bolão. Então implementaremos um sistema de apostas para os jogos da copa do mundo.


<h4>Part 1 (voltada ao Admin):</h4>
<ol>
     <li>Cadastrar novos jogadores(Nome, Login (único), senha). Cada novo jogador recebe um crédito de R$ 10,00 automaticamente.</li>
     <li>Cadastrar Equipas</li>
     <li>Cadastrar Partidas</li>
     <li>Definir o resultados as partidas</li>
     <li>Adicionar crédito aos jogadores</li>
</ol>

<h4>Part 2 (voltada ao publico):</h4>
<ol>
     <li>...</li>
     <li>...</li>
     <li>...</li>
     <li>...</li>
</ol>


<h4>Tabelas nessesárias:</h4>
<ol>
     <li>Usuários</li>
     <li>Crédito</li>
     <li>Equipas</li>
     <li>Partidas</li>
     <li>Apostas</li>
     <li>Ranking</li>
</ol>

    
<h2>Tecnologias usadas:</h2>
<ul>
    <li>Python</li>
    <li>Django</li>
    <li>Bootstrap</li>
    <li>JavaScript</li>
</ul>
    
<h2>Python modulos necessários:</h2>
<ul>
    <li>Django==2.2.4</li>
</ul>
  

<h2>Usuablidade :</h2>
    <h3>Em ordem de ver o projecto execute os comandos abaixos</h3>

    python manage.py makemigrations

    python manage.py migrate

    python manage.py createsuperuser

    python manage.py runserver
    
   In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/


