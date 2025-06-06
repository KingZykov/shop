from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def index(request):
    return render(request, 'index.html')



def register_view(request):
    if request.method == 'POST':
        login_value = request.POST.get('email')  # email — логин
        name_value = request.POST.get('name')
        phone_value = request.POST.get('phone') 
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, "Пароли не совпадают")
            return redirect('home')

        if User.objects.filter(login=login_value).exists():
            messages.error(request, "Пользователь с таким email уже зарегистрирован")
            return redirect('home')

        # создаём юзера и сразу указываем роль
        user = User.objects.create_user(
            login=login_value,
            name=name_value,
            phone=phone_value,
            password=password,
            role='user'            # <-- здесь
        )

        user = authenticate(request, username=login_value, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Регистрация и вход выполнены успешно!")
        
        return redirect('home')

def login_view(request):
    if request.method == 'POST':
        login_value = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=login_value, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Вход выполнен успешно!")
            return redirect('home')
        else:
            messages.error(request, "Неверный email или пароль")
            return redirect('home')



def logout_view(request):
    logout(request)
    messages.success(request, "Вы успешно вышли из системы")
    return redirect('home')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def store(request):
    return render(request, 'store.html')



@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('login')

        # Валидация email и т.п. можно добавить
        user.name = name
        user.phone = phone
        user.email = email
        user.save()

        messages.success(request, "Данные успешно обновлены")
        return redirect('home')



# views.py
import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_yookassa_payment(request):
    if request.method == 'POST':
        try:
            # Получаем данные из запроса
            amount = request.POST.get('amount')
            order_id = request.POST.get('orderId')
            email = request.POST.get('email')
            
            # Формируем запрос к API ЮКассы
            headers = {
                'Idempotence-Key': str(order_id),
                'Content-Type': 'application/json'
            }
            
            auth = (settings.YOOKASSA_SHOP_ID, settings.YOOKASSA_SECRET_KEY)
            
            payload = {
                "amount": {
                    "value": amount,
                    "currency": "RUB"
                },
                "capture": True,
                "confirmation": {
                    "type": "redirect",
                    "return_url": f"{settings.SITE_URL}/payment/success/"
                },
                "description": f"Оплата заказа #{order_id}",
                "receipt": {
                    "customer": {
                        "email": email
                    },
                    "items": [
                        {
                            "description": item['name'],
                            "quantity": item['quantity'],
                            "amount": {
                                "value": item['price'],
                                "currency": "RUB"
                            },
                            "vat_code": "1",
                            "payment_mode": "full_payment",
                            "payment_subject": "commodity"
                        } for item in request.POST.get('items', [])
                    ]
                }
            }
            
            response = requests.post(
                'https://api.yookassa.ru/v3/payments',
                json=payload,
                headers=headers,
                auth=auth
            )
            
            data = response.json()
            
            if response.status_code == 200:
                return JsonResponse({
                    'success': True,
                    'payment_url': data['confirmation']['confirmation_url']
                })
            else:
                return JsonResponse({
                    'success': False,
                    'error': data.get('description', 'Unknown error')
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()

@login_required
def monitoring_users(request):
    # доступ только админам
    if getattr(request.user, 'role', None) != 'admin':
        return HttpResponseForbidden("Доступ запрещён")
    users = User.objects.all()
    return render(request, 'monitoring_users.html', {'users': users})
