# SUNFEST_EVENT-2020

## Tecnologias utilizadas nesse projeto:
- Framework de python para web Django 3 +
- Javascript + bootstrap +  css em alguns casos.
## Ferramentas que precisam ter na sua maquina:
* Python 3.7 + 

* Criar uma Virtual ENV 
    ```
    sudo apt-get install python3-venv
    ```
* Ativar Venv
    ```
    . venv/bin/activate ou source venv/bin/activate
    ```
* pip3
    ```
    sudo apt-get install python3-pip

    ```  
* Instalar Django  
    ```
    pip3 install Django

    ```
## Passo a passo para rodar o projeto : 
- Baixar todas as Dependencias:
    ```
    pip3 install -r requiriments.txt
    ```  
- Rodar as migrações:
    ```
    python3 manage.py migrate
    ```  
- Criar Usuarrio admin:
    ```
    python3 manage.py createsuperuser
    ```  
- Rodar:
    ```
    python3 manage.py runserver
    ```
E visualizar no navegador no http://127.0.0.1:8000/