from ast import arguments
from flask_restful import Resource, reqparse

hoteis = [
    {
        'hotel_id':'alpha',
        'nome':'Alpha Hotel',
        'estrelas': 4.2,
        'diaria' : 280,
        'cidade' : 'Florianopolis',
    },
    {
        'hotel_id':'bravo',
        'nome':'Bravo Hotel',
        'estrelas': 3.8,
        'diaria' : 200,
        'cidade' : 'Florianopolis',
    },
    {
        'hotel_id':'luxo',
        'nome':'hotel_luxo',
        'estrelas': 5,
        'diaria' : 280,
        'cidade' : 'Sao Paulo',
    }

]

class Hoteis(Resource):
    def get(self):
        return {"hoteis": hoteis}

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'Hotel not found'}, 404

    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')

        dados = argumentos.parse_args()

        novo_hotel = {
            'hotel_id' : hotel_id,
            'nome' : dados['nome'],
            'estrelas' : dados['estrelas'],
            'diaria' : dados['diaria'],
            'cidade' : dados['cidade'],
        }

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass