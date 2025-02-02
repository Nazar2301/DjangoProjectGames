from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import UserRegister
from .models import Buyer, Game, News

users = ['existing_user1', 'existing_user2']

# Главная страница
def home(request):
    return render(request, 'task1/home.html')

# Список товаров
def shop(request):
    games = Game.objects.all()
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

# Новости
def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 10)  # Показывать 10 новостей на странице

    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)

    context = {'news': news_page}
    return render(request, 'task1/news.html', context)
