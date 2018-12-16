# Галкин Антон |  ИВТ | 3 курс | 1 подгруппа

import pytest
import main

def testing_fun1():
    assert main.FromJsonToTable('json.json') == 5, '1'
