# agenda

#### Uma agenda de contatos basica onde você pode adicionar, editar, deletar contatos

### Tecnologias
- Python 🐍
- Django

### Dependências
   - Antes de tudo, é preciso ter o Python instalado. Você pode instalá-lo [aqui](https://www.python.org/downloads/).
   - Para instalar as dependências, use o comando ```pip install -r requirements.txt```.

   - Definir as configurações de desenvolvimento das variáveis ```DEBUG``` e ```SECRET_KEY```
      - Para definir as configurações de desenvolvimento, siga os seguintes passos:

         1. Crie um arquivo chamado ".env" na raiz do projeto.
         1. Dentro do arquivo .env, atribua o valor ```True``` à variável DEBUG.
         1. Para configurar a variável SECRET_KEY, execute o seguinte comando no terminal: ```python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"```. <br>
         Copie o valor de saída e, no arquivo .env, atribua o valor à variável SECRET_KEY. Por exemplo: ```SECRET_KEY="valor do comando"```.

   Seu arquivo .env deve ser assim:
   ```
  DEBUG=True
  SECRET_KEY="valor do comando"
   ```
### Executar o servidor
Se tudo ocorrer bem, execute o comando ```python manage.py runserver``` ou ```python3 manage.py runserver``` (no Linux) para iniciar o servidor do projeto.

