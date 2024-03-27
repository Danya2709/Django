
## Иструкция

В любом терминале прописываем:

```
python3 -m venv venv
```

## После этого ее нужно активировать:
# (это нужно для Linux)
 ```
source venv/bin/activate
```
# (для Windows)
```
venv\Scripts\activate 
```
## Приступаем к скачивание всех необходимых библиотек (зависимости)

## Чтобы запустить проект прописываем:
```
pip install -r  requirements.\prod.txt
```
## Чтобы протестировать проект прописываем:
```
pip install -r  requirements\test.txt
```
## Для разроботки проекта прописываем:
```
pip install -r  requirements\dev.txt
```

## Чтобы запустить сервер в dev-режиме:
```
cd lyceum
python manage.py runserver
```

## Если вам нужно сделать Fixture /data.json прописываем:
```
python manage.py dumpdata catalog > fixtures/data.json
```
После этого нужно прописать:
```
python manage.py dumpdata catalog --indent=3 > fixtures/data.json
```
