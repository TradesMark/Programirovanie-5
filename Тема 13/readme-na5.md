# Задание на 5 
<br>

<b>Ссылка на код в GitHub</b> - https://github.com/TradesMark/Programirovanie-5/blob/master/%D0%A2%D0%B5%D0%BC%D0%B0%2013/main.py

<b>Ссылка на repl</b> - https://repl.it/@AntonGalkin/demo1 

<h2>Задача </h2>

Посмотреть какая из функций работает быстрее при подаче большого массива данных со случайными числами


<h2>РЕАЛИЗАЦИЯ</h2>


from random import randint

ls = [randint(0, 50000) for i in range(9000)]


<h2>Код программы</h2>

    from random import randint
    class Solution:

    def deco(func):
        import functools
        import time

        @functools.wraps(func)
        def inner(*args, **kwargs):
            start_time = time.time()  # начало таймера
            result = func(*args, **kwargs)
            end_time = time.time()  # завершение таймера
            time_delta = end_time - start_time
            print(f'Время выполнения кода {func.__name__} заняло: {time_delta}')
            return result

        return inner

    @staticmethod
    @deco
    def two_sum_brute(nums, target):  # staticmethod(deco(two_sum_brute))
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """

        length = len(nums)
        for i in range(length):
            for j in range(length):
                if nums[j] == target - nums[i]:
                    return [i, j]

    @staticmethod
    @deco
    def two_sum(nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """
        length = len(nums)
        nums_map = dict()
        for i in range(length):
            nums_map[nums[i]] = i

        for i in range(length):
            diff = target - nums[i]

            if (diff in nums_map.keys()) and (nums_map.get(diff, -1) != i):
                return [i, nums_map.get(diff)]
                
    ls = [randint(0, 50000) for i in range(9000)]
    Solution.two_sum_brute(ls, 9)
    Solution.two_sum(ls, 9)



<h2>Пример работы программы (Пара пробных запусков программы с массивом в 9000 значений)</h2>


<b>Пример 1</b>

<img src="https://nuqbbw.am.files.1drv.com/y4mYNoZOvNUEZL1-S38yGzKB3aYnfi24M9qyqSkmSUAQZtFU-bE3glB5piA4us0wMjUputY7HIx7m1nvmE8l2YJYLbd-3NZeZuD8hlENj-0fCmdiak_6GwBue9vZ7qMtSEzCM2AxXEamCmxYVqMjyZNRBxkt2jJYvrGJCVHk7M9zmwa7hcsZ99DAFLeJL6r4puBVVfqpT1Q4doiys90pP2_QA?width=582&height=71&cropmode=none" width="582" height="71" />


<b>Пример 2</b>

<img src="https://ptyhnq.am.files.1drv.com/y4mYTHXw2PCvxQqEc0Py4C-C7ZI_c3hXk6xrCI0krFJF1N76GAB8VnyuyvJe17CuakrCJfkRw2iBXHDhVgMeWQbw7spsZbvnQLSgrhd9_QIcyWoQvZGu7dMqlKIkw5NvldAyt_EGlXz4iXHT0fURrYwY-1hxhRppXl5390CJt6B3dwJ8UbYfLdc80MAYyJNyt234JknzwSzi0f1HYf-ZvwQCA?width=506&height=75&cropmode=none" width="506" height="75" />



<h2>Вывод: </h2>

Первая функция при запуске с большим массивом начала заметно тормозить, что видно по скриншотам, а вторая напротив выполняется все так же быстро и не загружает ПК
