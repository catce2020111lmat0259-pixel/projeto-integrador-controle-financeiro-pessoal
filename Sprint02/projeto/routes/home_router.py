from flask import Flask

from controllers import home_controller

def adicionar_rotas(app: Flask):
    app.add_url_rule(rule="/", endpoint="home_fine", view_func=home_controller.home_fine, methods=["GET"])
