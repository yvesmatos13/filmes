from typing import Union

import conexao
import recomendacoesApi 

import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/filmes")
def getFilmes():
    buscarRecomendacoes()
    filmes = []
    for filme in conexao.collection.find():
        filmes.append({"nome": filme["nome"],
                       "tipo": filme["tipo"]})
    return filmes


def buscarRecomendacoes():
    filmes = []
    filmesNovos = []
    for filme in conexao.collection.find():
        filmes.append({"nome": filme["nome"],
                       "tipo": filme["tipo"]})
    if not filmes:
        for recomendacao in recomendacoesApi.recomendacoes:
            if recomendacao["tipo"] == "filme":
                filmes.append({"nome": recomendacao["nome"],
                               "tipo": recomendacao["tipo"]})
        conexao.collection.insert_many(filmes)

    else:
        for recomendacao in recomendacoesApi.recomendacoes:
            if recomendacao["tipo"] == "filme":
                query = {"nome":recomendacao["nome"],"tipo":recomendacao["tipo"]}
                for filme in conexao.collection.find(query):
                    filmes.append({"nome": filme["nome"],
                                   "tipo": filme["tipo"]})
                if recomendacao["nome"] not in filme["nome"]:
                    filmesNovos.append({"nome": recomendacao["nome"],
                                        "tipo": recomendacao["tipo"]})
        if filmesNovos:
            conexao.collection.insert_many(filmesNovos)
