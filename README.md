# консольный проект по работе с товарами
консольный проект по работе с товарами на питоне
# Вики
Профиль админа:
admin | 123456
Профиль юсера:
user | 123456

Можно сделать админом любого пользователя, для этого в `database.txt` найдите нужного вам пользователя и измените `b` на `c`

# Тз
Необходимо разработать консольный проект по работе с товарами
Все данные должны хранится в файлах. Всего должно быть 2 файла: 1 – информация о пользователях(логин, пароль, роль), информация о товарах(наименование, описание, поставщик, цена, доступное количество)

При запуске программы данные из файлов должны считываться и помещаться в список/словарь. При запуске программы должно выводиться консольное меню: 

1 – авторизироваться: При авторизации пользователь вводит логин и пароль. Эти данные проверяются со значением в списке/словаре. Если у пользователя роль обычного пользователя то он попадает в личный кабинет пользователя(Вывод всех товаров в библиотеку tabulate). Если у пользователя роль администратора то он попадает в личный кабинет администратора(вывод всех товаров в библиотеку tabulate, редактирование товара, добавление товара, удаление товара)

2 – зарегистрироваться: Пользователь должен ввести логин, пароль, повторный ввод пароля. Если первый ввод пароля и второй ввод пароля не совпадают необходимо выводить соответствующее сообщение и вызывать функцию авторизации. Если логин уже занят необходимо выводить соответствующее сообщение и вызывать функцию авторизации. По умолчанию все пользователи регистрируются как обычные пользователи. В файле изначально должен быть 1 администратор
