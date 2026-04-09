from multiprocessing import context
from operator import index

from flask import request, render_template, redirect, url_for

class MetasController:
    def __init__(self):
        self.metas = []
        self.mensagem = None
        self.tipo_mensagem = None
        
    
    def criar_metas(self):
        context = {
            'metas': self.metas,
            'mensagem': self.mensagem,
            'tipo_mensagem': self.tipo_mensagem
        }
        
        self.mensagem = None
        self.tipo_mensagem = None
        return render_template('metas/form-criar-metas.html', context=context)
    
        
    def adicionar_metas(self):
        if request.method == "POST":
            meta = request.form.get("meta")
            if meta:
                self.metas.append(meta)
                self.mensagem = "Meta financeira criada com sucesso!"
                self.tipo_mensagem = "green"
            else:
                self.mensagem = "Erro: você precisa digitar uma meta."
                self.tipo_mensagem = "red"
        
        return redirect(url_for('criar_metas'))
    
    def listar_metas(self):
        context = {
            'metas': self.metas,
            'mensagem': self.mensagem,
            'tipo_mensagem': self.tipo_mensagem
        }
        
        self.mensagem = None
        self.tipo_mensagem = None
        return render_template("metas/form-listar-metas.html", context=context)
    
    def editar_meta(self, index):
        meta = self.metas[index]
        context = {
            'meta': meta,
            'index': index,
            'metas': self.metas,
            'mensagem': self.mensagem,
            'tipo_mensagem': self.tipo_mensagem
        }
        return render_template("metas/form-listar-metas.html", context=context)

    def atualizar_meta(self, index):
        nova_meta = request.form.get("meta")
        if nova_meta:
            self.metas[index] = nova_meta
            self.mensagem = "Meta atualizada com sucesso!"
            self.tipo_mensagem = "green"
        return redirect(url_for("listar_metas"))

    def excluir_meta(self, index):
        self.metas.pop(index) #eu estou removendo pelo indice usando pop() != remove()
        self.mensagem = "Meta excluída com sucesso!"
        self.tipo_mensagem = "red"
        return redirect(url_for("listar_metas"))

    
metas_controller = MetasController()