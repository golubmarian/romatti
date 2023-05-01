from flask import Flask, request
import requests
import ast
import os


app = Flask(__name__)
webhook_hash = os.getenv('HASH')


@app.route('/', methods=['POST'])
def webhook():
    data = request.data.decode()
    email = ast.literal_eval(data)['email']
    gift = ast.literal_eval(data)['gift']
    send_email(email, gift)
    return 'ok'
    # return f'ok {webhook_hash}'


def send_email(email, gift):
    if gift == '500':
        requests.get(
            f'https://mailganer.com/app/trigger/webhook/9602/?email={email}&hash={webhook_hash}'
        )
    elif gift == '1000':
        requests.get(
            f'https://mailganer.com/app/trigger/webhook/9603/?email={email}&hash={webhook_hash}'
        )
    elif gift == '2000':
        requests.get(
            f'https://mailganer.com/app/trigger/webhook/9605/?email={email}&hash={webhook_hash}'
        )
    elif gift == '5':
        requests.get(
            f'https://mailganer.com/app/trigger/webhook/9606/?email={email}&hash={webhook_hash}'
        )
    elif gift == '7':
        requests.get(
            f'https://mailganer.com/app/trigger/webhook/9607/?email={email}&hash={webhook_hash}'
        )
    elif gift == '10':
        requests.get(
            f'https://mailganer.com/app/trigger/webhook/9608/?email={email}&hash={webhook_hash}'
        )
    elif gift == 'gift':
        requests.get(
            f'https://mailganer.com/app/trigger/webhook/9609/?email={email}&hash={webhook_hash}'
        )
    elif gift == 'no':
        requests.get(
            f'https://mailganer.com/app/trigger/webhook/9610/?email={email}&hash={webhook_hash}'
        )


if __name__ == '__main__':
    app.run(debug=True)  # вывод ошибок





