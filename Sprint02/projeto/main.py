from flask import Flask

from routes import home_router
from routes.metas import metas_router 

app = Flask(__name__)

home_router.adicionar_rotas(app)
metas_router.adicionar_rotas(app)