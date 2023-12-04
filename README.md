### Команды для запуска виртуального окружения env
- py -m venv env - добавить окружение в локальную папку
- .\env\Scripts\Activate.ps1 - активировать окружение
- deactivate - деактивация окружения

### Команды для установки необходимых модулей
- pip install pytest
- pip install selenium
- pip install allure-pytest
- pip instal faker

### Команды для работы с requirements.txt
- pip freeze > requirements.txt - замораживает все зависимости в файл.txt
- pip install -r requirements.txt - устанавливает все зависимости в окружение

### Команды для пуша в удаленный репозиторий Github
- git add . - добавить изменения
- git commit -m "Название коммита" - закомитить файлы
- git push -u origin "Название ветки"(без кавычек) - запушить изменения в ветку 

### Команды для запуска автотестов и открытие их в Allure
- Set-Alias allure C:\Users\kimma\Documents\my_projects\allure-2.19.0\bin\allure.bat - задать путь до папки с Allure
- pytest --alluredir=tests\allure_results .\tests\elements_test.py::TestElements:: -запускает автотесты в опред. папке с сохранением результатов в папку results
- allure serve .\tests\allure_results - выводит результаты прогона в Allure

### Вспомогательные аргументы:
- '-tb=line' позволяет вывести только одну строку из упавшего теста
- '-x' позволяет завершить сессию автотестов при первом неудачном результате
- '-v' включает детализацию, отображаему в терминале
- '-s' позволяет отобразить в терминале результат методов print()
- '-m' позволяет запустить тесты с определеным маркером
- '-rx' позволяет увидеть сообщение ошибки(reason) провал. теста в консоли
- '-xvsm' данные аргументы можно группировать