import telebot

from django.views import View
from django.shortcuts import render, redirect

from .forms import OrderForm


bot = telebot.TeleBot("1051471905:AAEf8-enWvdUxNtCAHuUcb0QmNBaWa0am98")


def index(request):
    return render(request, 'mainapp/index.html')


def thanks(request):
    return render(request, 'mainapp/thanks.html')


def wrong(request):
    return render(request, 'mainapp/wrong.html')


class OrderView(View):

    def post(self, request):
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']

                message = 'Новая заявка с Сайта!\r\n\r\nИмя: ' + name + '\r\n'
                message += 'Телефон: ' + phone + '\r\n\r\nДоступные мессенджеры:\r\n'
                if form.cleaned_data['telegram'] == 'True':
                    message += 'Telegram\r\n'
                if form.cleaned_data['whatsapp'] == 'True':
                    message += 'WhatsApp\r\n'
                if form.cleaned_data['viber'] == 'True':
                    message += 'Viber\r\n'
                if form.cleaned_data['skype'] == 'True':
                    message += 'Skype\r\n'
                bot.send_message(104566710, message)
                return redirect('/thank-you')
        return redirect('/wrong')