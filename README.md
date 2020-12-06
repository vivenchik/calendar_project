# calendar_project

```
docker-compose up --build -d
```

Не забудте создать суперпользователя в системе.

http://0.0.0.0:8000/event/ - GET, POST  
  GET - список всех событий  
  POST - добавление события  
    Пример:  
```
{  
    "name": "event",  
    "begin_date": "2020-12-06T13:21Z",  
    "end_date": "2020-12-06T19:25Z"  
}  
```

http://0.0.0.0:8000/event/{id}/ - GET, DELETE, PUT  
  GET - одно событие с заданным id  
  DELETE - удаление события с заданным id  
  PUT - изменение события с заданным id (можно частично)  
