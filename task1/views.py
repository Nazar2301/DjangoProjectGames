from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer
from .models import Game

users = ['existing_user1', 'existing_user2']

# Главная страница
def home(request):
    return render(request, 'task1/home.html')

# Список товаров
def shop(request):
    games = [
        {'title': 'Cyberpunk 2007', 'description': 'Game of the year', 'cost': 31.00},
        {'title': 'Mario', 'description': 'Old game', 'cost': 5.00},
        {'title': 'Hitman', 'description': 'Who kills Mark?', 'cost': 12.00},
    ]
    context = {'games': games}
    return render(request, 'task1/shop.html', context)

# Корзина
def cart(request):
    return render(request, 'task1/cart.html')

# Регистрация
def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            # Получаем всех пользователей из таблицы Buyer
            buyers = Buyer.objects.all()
            buyer_names = [buyer.name for buyer in buyers]

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in buyer_names:
                info['error'] = 'Пользователь уже существует'
            else:
                # Создаем нового пользователя
                Buyer.objects.create(name=username, balance=0.00, age=age)
                info['message'] = f'Приветствуем, {username}!'
        info['form'] = form
    else:
        info['form'] = UserRegister()
    return render(request, 'task1/registration_page.html', info)
