@echo off
REM cmd /k "cd /d C:\Users\Admin\Desktop\venv\Scripts & activate & cd /d    C:\Users\Admin\Desktop\helloworld & python manage.py runserver"
cmd /k "cd C:\Users\Partage\PycharmProjects\FeuilleTravail\venv\Scripts & activate & cd /d %~dp0 & python Importation.py && exit"


