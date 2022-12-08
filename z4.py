# 4-Создайте два списка — один с названиями языков программирования, другой — с их нумерацией.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, 
# состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая (обязательно используйте tuple unpacking) — которая отфильтрует этот список 
# следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже,
# то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

def create_list_of_tuples(list1, list2):
    return list(zip(list1, [l.upper() for l in list2]))


def get_sum_of_codes(value):
    return sum([ord(ch) for ch in value])


def my_filter(lst_vals):
    return [(get_sum_of_codes(lan), lan) for i, lan in lst_vals if not get_sum_of_codes(lan) % i]


def func(lst_values):
    print(lst_values)
    lst_nums = [i for i in range(1, len(lst_values) + 1)]
    lst_tuples = create_list_of_tuples(lst_nums, lst_values)
    lst_res = my_filter(lst_tuples)
    print(lst_res)


lst_languages = ['python', 'c#', 'javascript', 'java', 'pascal', 'c++', 'delfi', 'visual basic']
func(lst_languages)