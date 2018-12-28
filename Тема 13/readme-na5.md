# Задание на 5 
<br>

<b>Ссылка на код в GitHub</b> - https://github.com/TradesMark/Programirovanie-5/blob/master/%D0%A2%D0%B5%D0%BC%D0%B0%2013/main.py

<b>Ссылка на repl</b> - https://repl.it/@AntonGalkin/demo1 

Задача посмотреть какая из функций работает быстрее при подаче большого массива данных со случайными числами


<b>РЕАЛИЗАЦИЯ</b>


from random import randint

ls = [randint(0, 50000) for i in range(9000)]

Пример работы программы (Пара пробныз запусков программы с массивом в 9000 значений)


<b>Пример 1</b>

<img src="https://nuqbbw.am.files.1drv.com/y4mYNoZOvNUEZL1-S38yGzKB3aYnfi24M9qyqSkmSUAQZtFU-bE3glB5piA4us0wMjUputY7HIx7m1nvmE8l2YJYLbd-3NZeZuD8hlENj-0fCmdiak_6GwBue9vZ7qMtSEzCM2AxXEamCmxYVqMjyZNRBxkt2jJYvrGJCVHk7M9zmwa7hcsZ99DAFLeJL6r4puBVVfqpT1Q4doiys90pP2_QA?width=582&height=71&cropmode=none" width="582" height="71" />


<b>Пример 2</b>

<img src="https://ptyhnq.am.files.1drv.com/y4mYTHXw2PCvxQqEc0Py4C-C7ZI_c3hXk6xrCI0krFJF1N76GAB8VnyuyvJe17CuakrCJfkRw2iBXHDhVgMeWQbw7spsZbvnQLSgrhd9_QIcyWoQvZGu7dMqlKIkw5NvldAyt_EGlXz4iXHT0fURrYwY-1hxhRppXl5390CJt6B3dwJ8UbYfLdc80MAYyJNyt234JknzwSzi0f1HYf-ZvwQCA?width=506&height=75&cropmode=none" width="506" height="75" />



<b>Вывод: </b>

Первая функция при запуске с большим массивом начала заметно тормозить, что видно по скриншотам, а вторая напротив выполняется все так же быстро и не загружает сильно ПК
