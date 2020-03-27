from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Жди нас, {planet_name}!</h1>
                        <div class="alert alert-dark" role="alert">
                        Эта планета самая лучшая.
                        </div>
                        <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-dark" role="alert">
                        Её можно сделать обитаемой.
                        </div>
                        <div class="alert alert-warning" role="alert">
                        Все на {planet_name}!
                        </div>
                        <div class="alert alert-danger" role="alert">
                        Удачи!
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
