from ast import arguments
from flask_restful import Resource, reqparse
from models.hotel import HotelModel

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
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found'}, 404

    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200 #atualizado
        hoteis.append(novo_hotel)
        return novo_hotel, 201 #criado


    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message' : 'Hotel deleted.'}