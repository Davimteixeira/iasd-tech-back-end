# 💌 PROCESSO SELETIVO IATEC - Desafio: Sistema de Cadastro, Login e Produtos

## 🚀 Backend

### ✨ **Tecnologias Utilizadas:**

- Python 3.13.1
- Django + Django REST Framework (DRF) + PostgreSQL
- Autenticação: JWT (com djangorestframework-simplejwt)
- ORM: Django ORM
- Comunicação: API REST usando Django REST Framework
- Banco de Dados: PostgreSQL
- Documentação da API: Swagger

---

## 📄 **Arquivo .env (Exemplo)**

```env
# Chave secreta (deve ser alterada em produção para uma chave única e segura)
SECRET_KEY=""

# Configuração de Debug (True para desenvolvimento, False para produção)
DEBUG=

# Modo de Teste "True para ativar o CORS livre para qualquer rota (APENAS TESTE recomendado deixar False) "
TEST_MODE=

# Hosts permitidos (separados por vírgula)
ALLOWED_HOSTS=

# CSRF Trusted Origins (separados por vírgula)
CSRF_TRUSTED_ORIGINS=

# Configuração do banco de dados PostgreSQL
POSTGRES_USER=
POSTGRES_PASS=
POSTGRES_PORT=
POSTGRES_DB_NAME=
POSTGRES_HOST=

# Configuração de módulo Django
DJANGO_SETTINGS_MODULE=core.settings
CORS_ORIGIN_ALLOW_ALL=True
```

---

## 📅 **Passo a Passo de Instalação**

### 1️⃣ **Clonar o Repositório**

```sh
$ git clone https://github.com/Davimteixeira/iasd-tech-back-end
$ cd iasd-tech-back-end
```

### 2️⃣ **Criar e Ativar um Ambiente Virtual**

```sh
# Criar ambiente virtual
$ python -m venv venv

# Ativar no Windows
$ venv\Scripts\activate

# Ativar no Linux/macOS
$ source venv/bin/activate
```

### 3️⃣ **Instalar Dependências**

```sh
$ pip install -r requirements.txt
```

### 4️⃣ **Rodar Migrações do Banco de Dados**

```sh
$ python manage.py migrate
```

### 5️⃣ **Criar Superusuário**

```sh
$ python manage.py createsuperuser
```

### 6️⃣ **Rodar o Servidor**

```sh
$ python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`.

---

## 🔄 **Rodando os Testes**

### 📊 **Executar Todos os Testes**

Para rodar todos os testes do projeto, execute:

```sh
$ python manage.py test
```

### 🔍 **Executar Testes de um Aplicativo Específico**

Para rodar apenas os testes de um app, use:

```sh
$ python manage.py test nome_do_app
```

Por exemplo, para testar apenas o app `products`:

```sh
$ python manage.py test apps.products
```

### 🏋️ **Evitar Recriação do Banco de Testes**

Para rodar os testes sem recriar o banco de testes a cada execução, utilize:

```sh
$ python manage.py test --keepdb
```

---

## 📚 **Endpoints da API Django**

| Método | Rota             | Descrição                  |
| ------ | ---------------- | -------------------------- |
| POST   | /api/register/   | Registrar usuário          |
| POST   | /api/login/      | Login e geração de token   |
| GET    | /api/products/   | Listar produtos do usuário |
| POST   | /api/products/   | Criar novo produto         |
| GET    | /api/categories/ | Listar categorias          |

---

## 📖 **Documentação da API**

A documentação da API está disponível via **Swagger**.
Para acessar, execute o projeto e abra no navegador:

```
# A documentação está na rota principal
http://127.0.0.1:8000/
```

---

## 🛠️ **Dependências e Justificativas**

```txt
asgiref==3.8.1                  # Suporte para ASGI (necessário para Django)
certifi==2025.1.31              # Certificados SSL/TLS confiáveis para requisições HTTP seguras
charset-normalizer==3.4.1       # Normalização de encoding de caracteres em requisições
python-decouple==3.8            # Gerenciamento de variáveis de ambiente (utilizado no .env)
Django==5.1.6                   # Framework principal para desenvolvimento web
Django REST Framework==3.15.2   # Framework para construção de APIs REST
Django REST Framework SimpleJWT==5.4.0  # Autenticação baseada em JWT
idna==3.10                      # Suporte a internacionalização de domínios e URLs
psycopg2==2.9.10 (Windows)      # Driver PostgreSQL para Django no Windows
psycopg2-binary==2.9.10 (Linux/Mac)  # Driver PostgreSQL para Django no Linux/Mac
PyJWT==2.10.1                   # Manipulação de tokens JWT
requests==2.32.3                # Biblioteca para fazer requisições HTTP
sqlparse==0.5.3                 # Analisador SQL para Django ORM
urllib3==2.3.0                   # Gerenciador de conexões HTTP
Django CORS Headers==4.6.0      # Suporte para CORS em Django
Django Dotenv==1.4.2            # Carregamento de variáveis de ambiente em Django
Django Guardian==2.4.0          # Controle de permissões baseadas em objetos
```
