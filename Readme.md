(Meu nome é Ivano Gabriel(@i.gabriel13_) e esse é meu primeiro projeto, ainda em desenvolvimento e não concluído 100%)
(Para agendar, não consolidei nenhum Popup de notificação, porem vai agendar se você atualizar a página. Se tiver com atraso para iniciar o servidor, provavelmente é o Render.com que no plano grátis entra em modo hibernar...aguarde uns 30s na primeira vez e tudo vai dar certo, sinta-se em casa ^_^ )

# 💈 Projeto Barbearia Django API 💈
Este é um projeto web desenvolvido com Django e Django REST Framework para gerenciar agendamentos de uma barbearia, oferecendo uma API robusta para o backend e uma interface simples para os clientes.

## 🚀 Funcionalidades Atuais

* **Agendamento de Serviços:** Permite que clientes agendem horários para cortes, barba e outros serviços.
* **Visualização de Agendamentos:** Clientes podem visualizar seus agendamentos.
* **Filtragem de Agendamentos:** Capacidade de filtrar agendamentos (ainda em desenvolvimento/ajustes para produção).
* **API RESTful:** Backend com endpoints REST para integração com outras aplicações.

## 🛠️ Tecnologias Utilizadas

* **Backend:**
    * [Python](https://www.python.org/)
    * [Django](https://www.djangoproject.com/)
    * [Django REST Framework](https://www.django-rest-framework.org/)
    * [Gunicorn](https://gunicorn.org/) (Servidor WSGI para produção)
    * [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) (Adaptador PostgreSQL)
    * [dj-database-url](https://pypi.org/project/dj-database-url/) (Configuração de URL de banco de dados)
    * [Pillow](https://pypi.org/project/Pillow/) (Processamento de imagem para Django)
    * [django-filter](https://django-filter.readthedocs.io/en/stable/) (Filtros avançados para consultas)
* **Frontend:**
    * HTML, CSS, JavaScript (puro)
* **Banco de Dados:**
    * PostgreSQL (em produção)
    * SQLite (em desenvolvimento)
* **Controle de Versão:**
    * [Git](https://git-scm.com/)
    * [GitHub](https://github.com/)
* **Hospedagem (Cloud Hosting):**
    * [Render.com](https://render.com/)

## 🌐 Acesso ao Projeto Online

O projeto está atualmente hospedado no Render.com e pode ser acessado através da seguinte URL:

* **URL do Site:** [https://barbearia-ivano-api.onrender.com](https://barbearia-ivano-api.onrender.com)

## 💻 Como Rodar Localmente (Desenvolvimento)

Para configurar e rodar este projeto em sua máquina local, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/](https://github.com/)<SeuNomeDeUsuarioNoGitHub>/<NomeDoSeuRepositorioNoGitHub>.git
    cd <NomeDoSeuRepositorioNoGitHub>
    ```
    *(Substitua `<SeuNomeDeUsuarioNoGitHub>` e `<NomeDoSeuRepositorioNoGitHub>` pelo seu nome de usuário e nome do repositório, ex: `BarbeariaDjango`)*

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # No Windows
    # source venv/bin/activate # No Linux/macOS
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o banco de dados (SQLite para desenvolvimento):**
    * Certifique-se de que seu `settings.py` está configurado para usar SQLite em desenvolvimento (geralmente é o padrão).
    * Execute as migrações:
        ```bash
        python manage.py migrate
        ```
    * Crie um superusuário (opcional, para acessar o admin):
        ```bash
        python manage.py createsuperuser
        ```

5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

    O site estará disponível em `http://127.0.0.1:8000/`.

## 🤝 Contribuições

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request. Sou novo na área e preciso de conselhos, indicações e experiência.Estou aberto a tudo.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.

É isto. ^_^ i.gabriel13_