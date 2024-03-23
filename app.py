from flask import Flask
from api.routes import game_blueprint

app = Flask(__name__)
app.register_blueprint(game_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
