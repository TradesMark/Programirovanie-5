"""
Галкин Антон |  ИВТ | 3 курс | 1 подгруппа
Задача посмотреть какая из функций работает быстрее при подаче большого массива данных со случайными числами

реализация:
from random import randint
ls = [randint(0, 50000) for i in range(9000)]
"""
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



