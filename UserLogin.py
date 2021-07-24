class UserLogin(): # UserLogin створений таким чином, що у змінній __user зберігається вся інформація про користувача.
    # через метод fromDB і create буде сформована властивість __user, через яку ми зможемо отримувати ['id'], щоб модуль flask_login міг ідентифікувати поточного користувача
    def fromDB(self, user_id, db):
        self.__user = db.getUser(user_id)  #формуємо особисту властивість __user і присвоюємо їй все те, що повертає метод getUser(бере з бази даних інформацію про користувача з певним user_id)
        return self  # повертаємо екземпляр класу UserLogin

    def create(self, user):
        self.__user = user
        return self



    # Оскільки UserLogin буде представляти тільки авторизованих користувачів, то необхідно, щоб функція is_authenticated завжди повертала True
    def is_authenticated(self):  # функція перевірки авторизації користувача (True - авторизований, False - неавторизований)
        return True

    # Будемо вважати, що користувач завжди активний, тобто True
    def is_active(self):  # функція перевірки що користувач активний (True - для активного, False - для неактивного)
        return True

    # Оскільки UserLogin буде представляти тільки авторизованих користувачів, то необхідно, щоб функція is_anonymous завжди повертала False
    def is_anonymous(self):  # функція, що визначає неавторизованих користувачів (False - для авторизованого, True - для неавторизованого)
        return False


    def get_id(self):  # функція, що повертає угікальний ідентифікатор
        return str(self.__user['id'])  # беремо id з таблиці в БД, і функція get_id повинна повертати строку, тому str()


    def getName(self):  # повертає імя користувача
        return self.__user['name'] if self.__user else "Без імені"  # якщо поле 'name' визначене, то повертаємо його, якщо ні, то повертаємо 'Без імені'.


    def getEmail(self):  # повертає email користувача
        return self.__user['email'] if self.__user else "Без email"  # якщо поле 'email' визначене, то повертаємо його, якщо ні, то повертаємо 'Без email'.
