

class Urls:
    STELLARBURGERS = 'https://stellarburgers.education-services.ru/'

class API:
    CREATE_USER = Urls.STELLARBURGERS+'api/auth/register'
    DELETE_USER = Urls.STELLARBURGERS+'api/auth/user'

class Pages:
    ORDER_FEED = Urls.STELLARBURGERS+'feed'

class Constant:
    PST_DOMAIN = ['ya.ru', 'yandex.ru', 'google.com', 'yahoo.com', 'mail.ru']
