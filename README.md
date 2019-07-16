# Enreda
Repositorio para enreda

Componentes utilizados:

 - python 3.7
 - django 2.2
   - djangorestframework
   - django-cors-headers
 - virtualenv
 - npm: - vue.js (CLI) - axios - vue-form-generator - vue-bootstrap - sweetalert

Despliegue:

 - en ../
   - python manage.py migrate
   - python manage.py runserver
 - en otro terminal ../frontend
   - (Es posible que haga falta realizar un "vue init webpack frontend" para cargar la carpeta "/node_modules")
   - npm run dev
 - acceder a un navegador web y poner http://localhost:8080/
