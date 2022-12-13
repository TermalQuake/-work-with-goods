import bcrypt # Импорт криптографии
import tabulate # Импорт табурета


def main(): # Главная страница пользователя
        print ("Это главная страница пользователя!")
        spisok()
def spisok(): # Страница товаров
        print(" Список всех товаров:")
        from tabulate import tabulate
        data = []
        with open('list.txt',encoding="utf-8") as f: #открытие файла и добавление формата
            for line in f:
             data.append(list(map(str.strip, line.split(',')))) #сама табуретка
        print(tabulate(data, tablefmt='grid', headers=('Товар', 'Цена'))) #формат и что будет написано

#Страница добавления товаров
def additem(Item=None, Prise=None):
        Item = input("Введи название Товара:")
        Prise = input("Введи цену товара:")
        list = open("list.txt", "a", encoding="utf-8")                       # Открывает список товаров и ставит кадировку
        list.write(Item+", "+str(Prise)+"\n")     #записывает товар и цену в файл
        print("Товар успешно добавлен!")
        list.close()                              #сохраняет и закрывает
        admin()                                # кидает обратно в меню админа

#страница удаления товара
def removeitem(Item1=None):
    spisok()
    Item1 = input ("Напиши что ты бы хотел удалить:")
    fn = 'list.txt'   #открывает лист
    f = open(fn, encoding="utf-8")
    output = []
    for line in f:
     if not Item1 in line:      #удаляет Item1
          output.append(line)
    f.close()          #закрывает лист
    f = open(fn, 'w', encoding="utf-8")
    f.writelines(output)
    f.close()
    print('''Ты удалил предмет! Возвращение на главную страницу...
    
    
    ''')
    admin()

#Страница редактирования товара
def changeprise(Item2=None, NewName=None, Newprise=None):
    spisok()
    Item2 = input ("Напиши что ты бы хотел удалить:")
    fn = 'list.txt' #открывает лист
    f = open(fn, encoding="utf-8")
    output = []
    for line in f:
        if not Item2 in line:      #удаляет Item1
            output.append(line)
    f.close()          #закрывает лист
    f = open(fn, 'w' , encoding="utf-8")
    f.writelines(output)
    f.close()
    print('''АЛЁ НИХУЯ СЕБЕ РАБОТАЕТ!''')

    NewName = input("Введи новое название товара:")
    Newprise = input("Введи новую цену товара:")
    list = open("list.txt", "a", encoding="utf-8")                       # Открывает список товаров и ставит кадировку
    list.write(NewName+", "+str(Newprise)+"\n")     #записывает товар и цену в файл
    print("Товар успешно изменён!")
    list.close()                              #сохраняет и закрывает
    admin()                           # кидает обратно в меню админа


def admin(): # Главная страница админа
    print('''Добро пожаловать в главную страницу администатора! Выберите пункт меню:
    1. Просмотреть товар
    2. Добавить товар
    3. Удалить товар
    4. Редактировать товар''')
    user_input = input()
    if user_input == '1':
        spisok()
    elif user_input == '2':
        additem()
    elif user_input == '3':
        removeitem()
    elif user_input == '4':
        changeprise()
    else:
        print("Ты что-то не так написал")

def gainAccess(Username=None, Password=None): # Страница логирования
    Username = input("Введи свой логин:")
    Password = input("Введи свой пароль:")

    if not len(Username or Password) < 1: # Проверка логина и пароля
        db = open("database.txt", "r")  # Сравниние из БД
        d = []
        f = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            c = a, b
            d.append(a)
            f.append(b)
            data = dict(zip(d, f))
            if Username in data:
                if data[Username][0] == 'c': #  Админ
                    hashed = data[Username].strip('c')
                else:
                    hashed = data[Username].strip('b') # Юсер
                hashed = hashed.replace("'", "")
                hashed = hashed.encode('utf-8')

                if bcrypt.checkpw(Password.encode(), hashed):
                    print("Login success!")
                    print("Привет", Username)
                    if data[Username][0] == 'c': # Если Админ, то кидает в строку админа
                        admin()
                    else:                        # Если не админ, то кидает в юсера
                        main()

                    break
                else:  # Если не всё ок, то пишет следующее:
                    print("Не правильный пароль")
        if Username not in data:
            print("Такого пользователя не существует")
    else:
        print("Пожалуйста, попробуйте войти ещё раз")
        gainAccess()
    db.close() #нужно обазятельно закрывать бд, ибо если офф прогу то бд умрёт
    # Страница регистрации
def register(Username=None, Password1=None, Password2=None):
    Username = input("Введите логин:")
    Password1 = input("Придумайте пароль:")
    Password2 = input("Подтвердите пароль:")
    db = open("database.txt", "r")
    d = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        c = a,b
        d.append(a)
    if not len(Password1)<=5:                                # Нужно минимум 5 символов для регистрации
        db = open("database.txt", "r")
        if not Username ==None:
            if len(Username) <1:                              #Нужно минимум 1 символ, для логина
                print("Пожалуйста укажите логин:")
                register()
            elif Username in d:
                print("Этот логин уже используется!")                 # Если такой логин уже есть в БД
                register()
            else:
                if Password1 == Password2:                              # Шифрует БД
                    Password1 = Password1.encode('utf-8')
                    Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())

                    db = open("database.txt", "a")                       # Записывает в БД регистрацию
                    db.write(Username+", "+str(Password1)+"\n")
                    print("Аккаунт успешно создан")
                    print("Пожалуйста, войдите чтобы продолжить")


                # принт текста
                else:
                    print("Пароли не совпадают")
                    register()
    else:
        print("Ваш пароль слишком короткий")
    db.close() #нужно обазятельно закрывать бд, ибо если офф прогу то бд умрёт



def home(option=None):                                       # Главная страница
    print('''Добро пожаловать! Выберите пункт меню:
    1. Вход
    2. Регистрация''')
    user_input = input()
    if user_input == '1':
        gainAccess()
    elif user_input == '2':
        register()
    else:
        print("Ты что-то не так написал")

# Регистрация(Логин, Пароль1, Пароль2)
# Авторизация(Логин, Пароль1)
home()