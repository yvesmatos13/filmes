from typing import Union

import conexao
import recomendacoesApi

import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/series")
def getseries():
    buscarRecomendacoes()
    series = []
    for serie in conexao.collection.find():
        series.append({"nome": serie["nome"],
                       "tipo": serie["tipo"]})
    return series


def buscarRecomendacoes():
    series = []
    seriesNovas = []
    for serie in conexao.collection.find():
        series.append({"nome": serie["nome"],
                       "tipo": serie["tipo"]})
    if not series:
        for recomendacao in recomendacoesApi.recomendacoes:
            if recomendacao["tipo"] == "serie":
                series.append({"nome": recomendacao["nome"],
                               "tipo": recomendacao["tipo"]})
        conexao.collection.insert_many(series)

    else:
        for recomendacao in recomendacoesApi.recomendacoes:
            if recomendacao["tipo"] == "serie":
                query = {"nome":recomendacao["nome"],"tipo":recomendacao["tipo"]}
                for serie in conexao.collection.find(query):
                    series.append({"nome": serie["nome"],
                                   "tipo": serie["tipo"]})
                if recomendacao["nome"] not in serie["nome"]:
                    seriesNovas.append({"nome": recomendacao["nome"],
                                        "tipo": recomendacao["tipo"]})
        if seriesNovas:
            conexao.collection.insert_many(seriesNovas)