from flask import Flask


app = Flask(__name__)


@app.route('/')
def name_mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def slogan():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    with open('design.html', 'r', encoding='utf-8') as des:
        return des.read()


@app.route('/image_mars')
def image_mars():
    with open('image.html', 'r', encoding='utf-8') as image:
        return image.read()


@app.route('/promotion_image')
def promotion_image():
    with open('image_1.html', 'r', encoding='utf-8') as image_1:
        return image_1.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
