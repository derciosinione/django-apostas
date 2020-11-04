# Apostas-WebApp       
     Este é um sistema desenvolvido em Python utilizando a web Framework Django

<h2>Sistema de apostas</h2>
<p>A inspiração deste projecto vem de uma atividade muito comum em tempos de jogos de copa do mundo:
Apostar em um Bolão. Então implementaremos um sistema de apostas para os jogos da copa do mundo.
</p>

## Part 1 (voltada ao Admin):
<ol>
     <li>Cadastrar novos jogadores(Nome, Login (único), senha). Cada novo jogador recebe um crédito de R$ 10,00 automaticamente.</li>
     <li>Cadastrar Equipas</li>
     <li>Cadastrar Partidas</li>
     <li>Definir o resultados as partidas</li>
     <li>Adicionar crédito aos jogadores</li>
</ol>

## Part 2 (voltada ao publico):
<ol>
     <li>Permitir que um jogador faça login</li>
     <li>Depois de logar deve exibir o nome, o valor a sua disposição para apostar e a lista de todas partidas cadastradas.</li>
     <li>Permitir que um jogador selecione e aposta em uma partida (<b>Apenas uma aposta para cada jogador por partida.) cada aposta tem o valor fixo de R$ 5,00.</b></li>
     <li>Distribuir o prémio (total do montante de apostas) usando o seginte critério: 
          <ul>
               <li>
                    O vencedor será quem acertar o resultado, se mais de um jogador acertar o resultado, o prêmio será igualmente entre eles
               </li>
               <li>
               Se ninguém acertar o resultado, o dinheiro será devolvido para cada jogador. 
               </li>
          </ul>
     </li>
     <li>Listar o ranking dos jogadores cadastrados ordenados por valores ganhos.</li>
</ol>


## Tabelas nessesárias:
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


<p><img src="Screenshots/Captura%20de%20Tela%20(54).png" height="400" width="800"></p>
<p><img src="Screenshots/Captura%20de%20Tela%20(53).png" height="400" width="800"></p>
<p><img src="Screenshots/Captura%20de%20Tela%20(55).png" height="400" width="800"></p>
<p><img src="Screenshots/Captura%20de%20Tela%20(56).png" height="400" width="800"></p>
<p><img src="Screenshots/Captura%20de%20Tela%20(57).png" height="400" width="800"></p>
<p><img src="Screenshots/Captura%20de%20Tela%20(58).png" height="400" width="800"></p>
png" height="400" width="800">
<p><img src="Screenshots/Captura%20de%20Tela%20(61).png" height="400" width="800"></p>
<p><img src="Screenshots/Captura%20de%20Tela%20(62).png" height="400" width="800"></p>
<p><img src="Screenshots/Captura%20de%20Tela%20(63).png" height="400" width="800"></p>
<p><img src="Screenshots/Captura%20de%20Tela%20(64).png" height="400" width="800"></p>
<p><img src="Screenshots/Captura%20de%20Tela%20(65).png" height="400" width="800"></p>


# Suporte :
<p>Se achaste este projecto interessante ou aprendeste alguma coisa e queres agradacer-me, considera em ajudar-ne a pagar a minha conta da internet. Isso me motivará a criar mais projectos.
</p>

<ul>
    <li><a href="https://www.paypal.me/derciosinione"><b>PayPal</b></a></li>
</ul>