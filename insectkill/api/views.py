import requests
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse


# TELEGRAM_BOT_TOKEN = '6672470619:AAH6yOHHxIfgJSiyIYG5ZER9VV36X7UZSNM'
# TELEGRAM_CHAT_ID = '552544803'

TELEGRAM_BOT_TOKEN = '7390047516:AAE_CBoNsgYFm2rX6ZTIGRLOnbrIywRLlzY'
TELEGRAM_CHAT_ID = '6017520420'


def send_telegram_message(phone):
    message = (f"Телефон: {phone}")
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    return response.status_code


def index(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')

        if not phone.isdigit() or len(phone) != 11:
            return HttpResponse("Введите данные в указанном формате.", status=400)

        status = send_telegram_message(phone)
        if status == 200:
            return HttpResponse("Заявка отправлена успешно. С вами скоро свяжутся, <a href='" + reverse('api:index') + "'>вернуться на сайт</a>")
        else:
            return HttpResponse("Ошибка отправки заявки.", status=500)
    return render(request, 'index.html')