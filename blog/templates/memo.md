<!-- scssコンパイル(ローカル) -->
{% load sass_tags %}
<link href="{% sass_src 'css/app.scss' %}" rel="stylesheet" type="text/css">

<!-- css(heroku) -->
{% load static %}
<link href="{% static 'css/app.css' %}" rel="stylesheet" type="text/css">