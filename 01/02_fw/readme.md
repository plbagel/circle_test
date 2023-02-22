Для запуска файла `test_circle_area.py`  
используйте следующую команду
```bash
python3 -m unittest test-circle_area.py
```
или такую
```bash
python3 -m unittest
```

```-m``` означает, что unittest запускается как модуль  
Если не писать имя файла, то будут выполнены все файлы  
из проекта, которые начинаются на ```test-```

Для детального просмотра тестов используйте ключ -v
```bash
python3 -m unittest -v test-circle_area.py
```

Если нужно, чтобы при запуске теста экран очищался,  
то используйте вызов двух команд за раз - очистка и тесты:
```bash
clear && python3 -m unittest test-circle_area.py
```
