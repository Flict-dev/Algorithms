# Инструменты
## 1. pdb [docs](https://docs-python.ru/standart-library/modul-pdb-python/)
1. Способы применения
   ![image](https://github.com/Flict-dev/Handbook/assets/76905733/0e4784a5-8749-4364-86fa-67ace60267de)
2. Пример
   ```python
   import pdb
   pdb.set_trace()
  
   def calculate_rps(requests, seconds):
       return requests / seconds
  
  
   if __name__ == '__main__':
       req = float(input('Requests: '))
       seq = float(input('Seconds: '))
       res = calculate_rps(req, seq)
       print(f"Rps: {res}")
   ```
3. Команды
   - help <название команды> - база
   - quit - Выход из pdb
   - next - Построчно будет выполнять код
   - step - Проваливается в вызов функции
   - continue - Выпллнение программы
   - where - Выведет стек трейс
   - list - Укажет на текущую строчку
   - args - Выведет аргументы с которыми была вызвана функция
   ![image](https://github.com/Flict-dev/Handbook/assets/76905733/81fe2049-c222-43cd-a39d-388ed9344ae1)
## 2. cProfile [docs](https://digitology.tech/docs/python_3/library/profile.html)
![image](https://github.com/Flict-dev/Handbook/assets/76905733/5e59abe3-b0cb-43d4-b2c8-aba29f35123b)
## 3. snakeviz [docs](https://pypi.org/project/snakeviz/)
![image](https://github.com/Flict-dev/Handbook/assets/76905733/886d5fd1-9992-48fc-b770-9ac016442119)
## 4. vmprof [docs](https://github.com/vmprof/vmprof-python)
![image](https://github.com/Flict-dev/Handbook/assets/76905733/4c1f9955-2059-445a-81f5-f5483922378e)
## 5. tracemalloc [docs](https://docs-python.ru/standart-library/modul-tracemalloc-python/)
`Утилита для профилирования памяти`

---

# База логирования
`Разобпаться с kibana и elasticsearch для логов`
![image](https://github.com/Flict-dev/Handbook/assets/76905733/f21452d7-34f4-4463-9cb5-339ee2f8a02f)
![image](https://github.com/Flict-dev/Handbook/assets/76905733/a2c4267f-8c22-4fb6-a3b9-365ef782a5a6)
![image](https://github.com/Flict-dev/Handbook/assets/76905733/970deb69-6b96-48a1-bf6d-f3ef397d3165)
![image](https://github.com/Flict-dev/Handbook/assets/76905733/935cd582-78ee-4254-afa2-5619f28e174b)
![image](https://github.com/Flict-dev/Handbook/assets/76905733/98897bda-044e-4a6a-b009-2767c41d4790)
![image](https://github.com/Flict-dev/Handbook/assets/76905733/c1fb3fe4-04a0-4b6b-8d6e-4340ee7bb29a)

---

# Лекция
## Про процессы
![image](https://github.com/Flict-dev/Handbook/assets/76905733/36cc78ef-c834-4f6f-a1a9-0ea89855d838)
**`Создание просцесса в python`**
![image](https://github.com/Flict-dev/Handbook/assets/76905733/5052e078-16f6-40d3-bffe-365e11586676)
```python
import os

def main():
    print(f"{os.getpid()}: Давайте создадим процесс")
    res = os.fork()
    if res:
        print(f"Новый процесс с pid={res} создан")
    else:
        print(f"    {os.getpid()}: Я дочерний процесс")
        print(f"    {os.getpid()}: pid родительского процесса (ppid) = {os.getppid()}")
        input()


if __name__ == "__main__":
    main()

```
---

## Про сигналы
![image](https://github.com/Flict-dev/Handbook/assets/76905733/f33febff-6e9c-4b97-97f8-f76715abd762)
В python есть модуль `signal` при помощи него можно переписывать обработчики сигналов
```python
import signal
import time


def on_sigint(signo, stack_frame):
    print(f"Поймал сигнал {signo}")


signal.signal(signal.SIGINT, on_sigint)
while True:
    time.sleep(1)
```
---
 
## Про exit code
![image](https://github.com/Flict-dev/Handbook/assets/76905733/e95ffaa2-01b8-4f02-a46d-275ed390c50a)

---

## Про просмотр сетевого трафика
`Неплохой способ, но wireshark лучше`
![image](https://github.com/Flict-dev/Handbook/assets/76905733/6bdf2c9a-3d3a-4975-8e1d-d50912610578)
- [Тутор по wireshark](https://youtu.be/Kfnoy9TziNg) с 17 минут самое полезное
- [Немного про tcpdump](https://youtu.be/uOvHITxYXM8)

---





