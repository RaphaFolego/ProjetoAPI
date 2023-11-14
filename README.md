# ProjetoAPI

<h1>API para cadastro e manutenção de usuários</h1>

<p>O desafio foi desenvolvido usando o framework FastAPI, do Python</p>
<p>O framework escolhido foi o FastAPI por conta da sua agilidade na hora de subir uma API, além do fato de ser um framework mais recente quando comparado com Django e Flask, por exemplo.</p>

<h1>Passos iniciais para o funcionamento da API</h1>
<p>Para que a API funcione, será necessário ter, no mínimo, a versão 3.10+ do Python instalado, juntamente com o VSCode instalado.</p>

<p>Para verificar qual a versão do Python está instalada no seu computador, basta digitar o comando 'python -V' no terminal</p>
<>

<p>Após verificar a versão do python, basta criar uma pasta na área de trabalho, abrir o VSCode e abrir o folder dentro dele.</p>
<>

<h1>Criação do ambiente virtual</h1>
<p>Ao abrir o folder, pressione Ctrl+J para abrir o terminal e criar o ambiente virtual para rodar a API.</p>
<p>No terminal, digite o comando 'python -m venv nome_do_ambiente'</p>
<>

<p>Após criar o ambiente virutal, digite no terminal o comando '.\nome_do_ambiente\Scripts' e logo em seguida digite.\Activate.ps1\ (caso esteja no powershell)</p>
<p>Caso o PowerShell não tenha permissão para acessar a pasta Scripts (por padrão,ele não permite acesso), basta abrir o PowerShell no windows e digitar o comando "Set-ExecutionPolicy Unrestricted", e depois digitar um "S" para confirmar a alteração.</p>

<p>Caso esteja no cmd, basta digitar .\Activate.bat\</p>

<p>Após a criação do ambiente virtual, digite cd ..\.. para retornar à pasta da API</p>

<h1>Importando as bibliotecas</h1>
<p>O Python possui um instalado de pacotes próprio, o "pip", ou seja, ele será usado para instalar todas as dependências necessárias para poder rodas a aplicação.</p>

<p>As bibliotecas necessárias para que a aplicação funcione estão localizadas no arquivo "requirements.txt".</p>
<p>Para a instalação da biblioteca, usaremos o comando pip install nome_da_biblioteca dentro do terminal do nosso ambiente virtual.</p>

<p>As principais bibliotecas que usaremos são:</p>
<li>FastAPI</li>
<li>Uvicorn</li>
<li>SQLAlchemy</li>
<li>Pydantic</li>

<h1>Executando a API</h1>
<p>Após a criação do ambiente virtual e da instalação de todas as bibliotecas necessárias, já podemos rodar a aplicação</p>
<p>Para rodá-la, basta abrir o terminal (Ctrl+J) e digitar o comando "uvicorn main:app"</p>
<p>Isso irá gerar um link no terminal, basta dar um click+c para entrar no link, e uma página como a abaixo irá abrir no seu navegador.</p>

<p>Ao abrir o navegador, coloque no final do URL "/docs" para acessar as funcionalidades da API, e então, só testar as funcionalidades!</p>

<h1>Métodos do recurso /users</h1>
<p>O recurso /users possui 4 métodos, sendo eles:</p>
<li>Get -> Lê a tabela de dados</li>
<li>Post -> Cria um usuário novo</li>
<li>Put -> Altera os dados de um usuário já existente</li>
<li>Delete -> Deleta todos os dados de um usuário</li>
<br>
<p>Cada um possui especificações para que eles possam ser executados</p>
