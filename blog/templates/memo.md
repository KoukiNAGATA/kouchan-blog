# メモ
デプロイ周りのメモ書きをする場所

## css
heroku上でscssコンパイルができないので、ローカルでコンパイル、herokuには静的ファイルを置くという方法で一旦対応。

### scssコンパイル(ローカル)
文頭
```
{% load sass_tags %}
```
headタグ
```
<link rel="stylesheet" href="{% sass_src 'css/app.scss' %}" type="text/css">
```

### css(heroku)
headタグ
```
<link rel="stylesheet" href="{% static 'css/app.css' %}" type="text/css">
```

## Migration
データベースに変更があれば、ローカルでmigrationファイルを作成し、migrate
```
python3 manage.py makemigrations
python3 manage.py migrate
```

herokuを変更したら、そちらのデータベースもmigrate
```
heroku run python3 manage.py migrate
```
djangoはデフォルトでSQLiteを使うが、herokuはpostgreSQLなので注意
自分の環境でmigrationの静的ファイル作って、herokuでmigrateすることでpostgresに適用する
一旦仮ファイルを作って解決した例
参考:https://stackoverflow.com/questions/61464113/django-db-utils-programmingerror-cannot-cast-type-uuid-to-integer