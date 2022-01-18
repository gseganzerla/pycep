import requests
from collections import namedtuple
from src.models.cep import Cep


class CepService:
    URL = 'https://viacep.com.br/ws'

    def request_by_cep(self, cep: str) -> Cep:
        response = requests.get(f"{self.URL}/{cep}/json").json()

        data = namedtuple('data', response.keys())(*response.values())

        return Cep(data.cep, data.logradouro, data.bairro, data.localidade,
                   data.uf)

    def request_by_name(self, uf: str, city: str, street: str) -> Cep:
        response = requests.get(f"{self.URL}/{uf}/{city}/{street}/json").json()

        addresses = []
        for data in response:
            address = namedtuple('address', data.keys())(*data.values())

            addresses.append(
                Cep(address.cep, address.logradouro, address.bairro,
                    address.localidade, address.uf))

        return addresses
