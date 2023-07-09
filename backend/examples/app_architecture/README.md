# Лекция

## `Резюме`
![image](https://github.com/Flict-dev/Handbook/assets/76905733/fc5b773e-3286-40e9-8570-58b67853afc9)

---

## Про хедеры
В приципе тут всё понятно. Основаная суть заключается в том, что на них нельзя забивать.
Пишем:
- Content-type: application/json (что отдаем)
- Accept: application/json (что принимаем)
- User-Agent: <product> (важен в основном, если бэкенд используется мобилкой)
- Authorization: <тип> <данные пользователя>
- Accept-Language: * (оповещение сервера о текущем языке приложения)
- Retry-After: <http-data или delay-seconds> (Для поллинга, например проверки статуса операции)
- Cache-Control <type> (управление кешированием) 
---

## Про коды ответов сервера
![image](https://github.com/Flict-dev/Handbook/assets/76905733/7c87e457-eacf-4523-8ff4-97971cb69463)
![image](https://github.com/Flict-dev/Handbook/assets/76905733/9dd07020-798f-40d5-ab40-1a309984b8ee)
![image](https://github.com/Flict-dev/Handbook/assets/76905733/107671ad-ed69-4aa8-a701-19e60f2f31f1)
![image](https://github.com/Flict-dev/Handbook/assets/76905733/52db388a-35a2-4ef9-ab65-a0624338f499)

---
## Про идемпотентность
К примеру у клиента отвалился интернет после отправки POST на сервер.
Сервер обработал POST, но не смог вернуть ответ. 
Когда пользователь нажмет ещё раз на кнопку так-как явно не получил ответ,
мы должны использовать идемпотентность и не создавать ещё одну запись
![image](https://github.com/Flict-dev/Handbook/assets/76905733/f540b86a-8e15-48f1-9f03-2bae59288e12)
![image](https://github.com/Flict-dev/Handbook/assets/76905733/148c2071-7732-4d9b-9276-0895f5c184a3)

---
## Про API composer
Идея заключается в том, чтобы замутить master сервис, который бы собирал данные из нескольких slave сервисов.
В мастер сервис приходит один запрос, который он разбивает на несколько
![image](https://github.com/Flict-dev/Handbook/assets/76905733/b8318782-ca81-4dd0-afd8-4f9111fba2c8)
![image](https://github.com/Flict-dev/Handbook/assets/76905733/1e642cc7-93bd-4157-a21a-5bc3513512d6)
