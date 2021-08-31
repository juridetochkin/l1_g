from flask import Flask, render_template, request, redirect

app = Flask(__name__)

DATA = [
    {
        'ChannelName': 'Viber',
        'LoadingResource': 'viber://chat&number=%2B79178712564',
    },
    {
        'ChannelName': 'Loader',
        'LoadingResource': 'https://sovcombank.ru',
    },
    {
        'ChannelName': 'WhatsApp',
        'LoadingResource': 'https://wa.me/%2B79178712564',
    },
    {
        'ChannelName': 'Email',
        'LoadingResource': 'mailto:tenav@sovcombank.ru',
    },
]


@app.route('/')
def index():
    channels = DATA
    return render_template('index.html', channels=channels)


@app.route('/event')
def save_event():
    url_to = request.args.get('next')

    return redirect(url_to)


if __name__ == '__main__':
    app.run(debug=True)
