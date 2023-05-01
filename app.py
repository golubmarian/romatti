from flask import Flask, request
import requests
import ast

application = Flask(__name__)  # test


@application.route('/', methods=['POST'])
def webhook():
    data = request.data.decode()
    email = ast.literal_eval(data)['email']
    gift = ast.literal_eval(data)['gift']
    send_email(email, gift)
    return 'ok'


def send_email(email, gift):
    if gift == '500':
        response = requests.get(
            f'https://mailganer.com/app/trigger/webhook/9602/?email={email}&hash=Romatti2023$'
        )
        print(f'500 {response}')
    elif gift == '1000':
        response = requests.get(
            f'https://mailganer.com/app/trigger/webhook/9603/?email={email}&hash=Romatti2023$'
        )
        print(f'1000 {response}')
    elif gift == '2000':
        response = requests.get(
            f'https://mailganer.com/app/trigger/webhook/9605/?email={email}&hash=Romatti2023$'
        )
        print(f'2000 {response}')
    elif gift == '5':
        response = requests.get(
            f'https://mailganer.com/app/trigger/webhook/9606/?email={email}&hash=Romatti2023$'
        )
        print(f'5 {response}')
    elif gift == '7':
        response = requests.get(
            f'https://mailganer.com/app/trigger/webhook/9607/?email={email}&hash=Romatti2023$'
        )
        print(f'7 {response}')
    elif gift == '10':
        response = requests.get(
            f'https://mailganer.com/app/trigger/webhook/9608/?email={email}&hash=Romatti2023$'
        )
        print(f'10 {response}')
    elif gift == 'gift':
        response = requests.get(
            f'https://mailganer.com/app/trigger/webhook/9609/?email={email}&hash=Romatti2023$'
        )
        print(f'gift {response}')
    elif gift == 'no':
        response = requests.get(
            f'https://mailganer.com/app/trigger/webhook/9610/?email={email}&hash=Romatti2023$'
        )
        print(f'no {response}')
    else:
        print('no')


if __name__ == '__main__':          # запуск локально
    application.run(debug=True)     # вывод ошибок





