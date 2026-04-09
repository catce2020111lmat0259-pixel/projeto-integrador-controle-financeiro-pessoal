from flask import Flask

from controllers.metas.metas_controller import metas_controller

def adicionar_rotas(app: Flask):
    app.add_url_rule(rule="/criar-metas", endpoint="criar_metas", view_func=metas_controller.criar_metas, methods=["GET"])
    app.add_url_rule(rule="/criar-metas/adicionar-metas", endpoint="adicionar_metas", view_func=metas_controller.adicionar_metas, methods=["POST"])
    app.add_url_rule(rule="/listar-metas", endpoint="listar_metas", view_func=metas_controller.listar_metas, methods=["GET"])
    app.add_url_rule(rule="/criar-metas/editar-meta/<int:index>", endpoint="editar_meta", view_func=metas_controller.editar_meta, methods=["GET"])
    app.add_url_rule(rule="/criar-metas/atualizar-meta/<int:index>", endpoint="atualizar_meta", view_func=metas_controller.atualizar_meta, methods=["POST"])
    app.add_url_rule(rule="/criar-metas/excluir-meta/<int:index>", endpoint="excluir_meta", view_func=metas_controller.excluir_meta, methods=["GET"])