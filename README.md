# ProjetoAPI
Desafio parte do processo seletivo para vaga de Estágio no banco Itaú

<h1>API para cadastro e manutenção de usuários</h1>

<p>Esse projeto faz parte do processo seletivo para a vaga de estágio do Itaú que consiste no desenvolvimento de uma API para cadastro e manutenção de funcionários</p>

<p>O desafio foi desenvolvido usando o framework FastAPI, do Python</p>

<p>Para que a API funcione, será necessário ter, no mínimo, a versão 3.10+ do Python instalado, juntamente com o VSCode instalado.</p>

<p>Para verificar qual a versão do Python está instalada no seu computador, basta digitar o comando 'python -V' no terminal</p>
<link= >

<p>Após verificar a versão do python, basta criar uma pasta na área de trabalho, abrir o VSCode e abrir o folder dentro dele.</p>
<link= >

<h1>Criação do ambiente virtual</h1>
<p>Ao abrir o folder, pressione Ctrl+J para abrir o terminal e criar o ambiente virtual para rodar a API.</p>
<p>No terminal, digite o comando 'python -m venv nome_do_ambiente'</p>
<link= >

<p>Após criar o ambiente virutal, digite no terminal o comando '.\nome_do_ambiente\Scripts' e logo em seguida digite.\Activate.ps1\ (caso esteja no powershell)</p>

<p>Caso esteja no cmd, basta digitar .\Activate.bat\</p>

<p>Após a criação do ambiente virtual, digite cd ..\.. para retornar à pasta da API</p>

<h1>Importando as bibliotecas</h1>
<p>O Python possui um instalado de pacotes próprio, o "pip", ou seja, ele será usado para instalar todas as dependências necessárias para poder rodas a aplicação.</p>

<p>As bibliotecas necessárias para que a aplicação funcione estão localizadas no arquivo "requirements.txt".</p>
<p>Para a instalação da biblioteca, usaremos o comando pip install nome_da_biblioteca dentro do terminal do nosso ambiente virtual.</p>

<p>As principais bibliotecas que usaremos são:</p>
<li>fastapi</li>
<li>uvicorn</li>
<li>sqlalchemy</li>
<li>pydantic</li>
