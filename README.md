Hillel Support web application
# https://gitmoji.dev/
# pip install django==4.2.11
# pip freeze
# pip install -r requirements.txt
# pip install pipenv
# pip install pipx
# pip list packages
# pipenv check 
# pipenv shell - создает виртуальную среду
# exit - выход с pipenv shell
# pipfile - в нем прописываешь те библиотеки, которые нужны для твоего проэкта
# pipenv install isort - установка через pipenv

pipenv lock - Команда pipenv lock в Pipenv выполняет следующие действия:
Обновление файла Pipfile.lock: Создает или обновляет файл Pipfile.lock в вашем проекте. Этот файл содержит точные версии всех зависимостей вашего проекта, включая их подзависимости.
Фиксация версий зависимостей: Закрепляет версии всех пакетов, указанных в вашем Pipfile, а также их подзависимостей. Это важно для обеспечения воспроизводимости вашего окружения при установке зависимостей.
Создание файлов блокировки для виртуального окружения: Если виртуальное окружение не существует или было изменено, pipenv lock также создает или обновляет файлы блокировки в директории виртуального окружения (Pipfile.lock, Pipfile.lock.local).
В результате выполнения этой команды, ваши зависимости будут фиксированы с конкретными версиями, что делает проект более надежным и воспроизводимым в будущем.

pipenv sync - Команда pipenv sync в Pipenv выполняет следующие действия:
Установка зависимостей из файла Pipfile.lock: Она использует информацию из файла Pipfile.lock для установки конкретных версий зависимостей вашего проекта. Это гарантирует, что у вас будет точно такое же окружение, как и в момент создания или обновления Pipfile.lock.
Создание виртуального окружения, если оно не существует: Если виртуальное окружение для проекта ещё не было создано, pipenv sync создаст его.
Активация виртуального окружения: После установки зависимостей команда активирует виртуальное окружение, чтобы вы могли сразу начать использовать его.
Эта команда обеспечивает точное воспроизведение окружения, определенного в файле Pipfile.lock. Она полезна, например, при передаче проекта другим разработчикам или при развертывании проекта на других системах, чтобы убедиться, что все зависимости 

pipenv graph-Команда pipenv graph в Pipenv используется для вывода графа зависимостей проекта. Она показывает связи между различными пакетами и их версии, основываясь на информации из файлов Pipfile и Pipfile.lock.
Когда вы выполняете pipenv graph, вы получите структурированный вывод, который представляет собой древовидный граф зависимостей, где каждый пакет отображается вместе с его подзависимостями и версиями. Это полезно для понимания, какие библиотеки используются в вашем проекте и как они связаны друг с другом.

django-admin --help :
[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
django-admin startproject support 
Команда django-admin startproject support используется для создания нового проекта Django с именем "support". После выполнения этой команды будет создан каталог с именем "support", который будет содержать структуру проекта Django, включая файлы настройки, файлы URL-адресов и другие необходимые файлы и каталоги для запуска Django-проекта.

python support\manage.py --help
python support\manage.py runserver
http://127.0.0.1:8000/admin/
MVT django
python manage.py startapp user
python manage.py makemigrations
python manage.py migrate
python manage.py shell
pipenv install django-stubs~=4.2.7
pipenv sync --dev