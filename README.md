# Como rodar a aplicação

Antes de prosseguir certifique-se de que você tem instalado na sua máquina o node (https://nodejs.org/en/), o yarn (https://yarnpkg.com/getting-started/install) e o python (https://www.python.org/downloads/)

## Back End

Abra um terminal na pasta desafio-ada-back. Começando pelo nosso servidor, para rodá-lo é necessário um ambiente virtual do python. Para criá-lo basta rodar o comando

```
python -m venv venv
```

Em seguida é necessário ativá-lo:

```
source venv/bin/activate
```

E então instalar as libs do projeto (que podem ser encontradas no arquivo requirements.txt) com o comando seguinte: 

```
pip install -r requirements.txt
```

Também é necessário rodar as migrações. Isso criará um arquivo db.sqlite3 que funcionará como banco de dados de ambiente de desenvolvimento:

```
python manage.py migrate
```

Por fim, basta rodar o servidor com:

```
python manage.py runserver
```

Um link aparecerá com a porta em que o servidor está rodando ("Starting development server at..."). Acessar esse link dará acesso aos templates do Django Rest Framework, onde é possível ter um retorno visual do banco de dados. É importante notar que é necessário adicionar o final da URL ao link fornecido, já que não existe rota '/' no projeto. Portanto, para visualizar os dados das contas registradas o link deve ser "{link fornecido no terminal}api/contas/".

Pronto! O servidor está rodando.

## Front End

Abra um terminal na pasta desafio-ada-front. Para instalar as dependências do projeto, rode o comando:

```
yarn
```

Com as dependências instaladas, basta rodar a aplicação com o comando:

```
yarn start
```

Pronto! A página de front da aplicação deve ser carregada automaticamente no seu localhost!
