#### System packages
* Python 3.5 +
 
#### Установка
После того как скачан архив, в папке с проектом создаем вирутальное окружение
 
    virtualenv --no-site-packages env
   
запускаем окружение с помощью
 
    source env/bin/activate
 
устанавливаем необходимые компоненты
 
    pip3 install -r requirements.txt
 
запускаем проект
 
    python3 manage.py runsever
