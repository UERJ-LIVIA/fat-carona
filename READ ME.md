 Instruções básicas para acessar andpoints do rest_api:
 1- instale a biblioteca django, usando o comando no terminal: ' pip install django';
 2- instale a biblioteca djangorestframework no terminal,
  usando o comando : 'pip install djangorestframework';
 3- entre no terminal do projeto e digite o comando : ' python manage.py runserver';
 4- o terminal irá retornar um enedereço http,clique nele ('http://127.0.0.1:8000');
 5- neste endpoint, coloque a seguinte sequencia apos a porta 8000 :
    'api/v1/rides' : para acessar a versão 1 da Api de caronas listadas;
    'api/v1/profiles: para acessar a versão 1 da Api que traz os perfis relacionados a cada carona;
    'api/v2/rides : segunda versão do Api de caronas configurado usando ViewSets e Routers;
    'api/v2/profiles : segunda versão do Api de profiles .