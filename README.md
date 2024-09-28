# Sprint_7
  Финальный проект 7-го спринта

  Тема проекта: "Учебный сервис "Яндекс.Самокат".
  Это сервис, на котором можно заказать самокат на прокат в удобный день и время.

  Содержание проекта:

  задание выполнено в отдельной ветке разработки -develop-;
  в директории allurt_results - сгенерированы Allure;  
  в директории tests - содержатся файлы с тестами; 
  в файле .gitignore содержатся локальные файлы;
  в файле README.md текстовая часть о проделанной работе;
  в файлу requirements.txt - список внешних зависимостей.

  Список реализованных тестов:

  test_courier_login.py - проверяет, что:
    курьер может авторизоваться;
    для авторизации нужно передать все обязательные поля;
    система вернёт ошибку, если неправильно указать логин или пароль;
    если какого-то поля нет, запрос возвращает ошибку;
    если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;
    успешный запрос возвращает id.;
  
  test_creating_a_courier.py - проверяет, что: 
    курьера можно создать;
    нельзя создать двух одинаковых курьеров;
    чтобы создать курьера, нужно передать в ручку все обязательные поля;
    запрос возвращает правильный код ответа;
    успешный запрос возвращает {"ok":true};
    если одного из полей нет, запрос возвращает ошибку;
    если создать пользователя с логином, который уже есть, возвращается ошибка.

  test_creating_an_order.py - проверяет, что, когда создаешь заказ:
    можно указать один из цветов — BLACK или GREY;
    можно указать оба цвета;
    можно совсем не указывать цвет;
    тело ответа содержит track.
  
  test_list_of_orders.py - проверяет, что  в тело ответа возвращается список заказов.

  Тесты для вывода из терминала - проверены командой: pytest -v.
  Команда для запуска с записью отчета в allure_results: `pytest --alluredir=allure_results`.
