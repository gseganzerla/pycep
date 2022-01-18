import requests
from collections import namedtuple
from src.models.cep import Cep


class CepService:
    URL = 'https://viacep.com.br/ws'

    def request_by_cep(self, cep: str) -> Cep:
        response = requests.get(f"{self.URL}/{cep}/json").json()

        data = namedtuple('data', response.keys())(*response.values())

        return Cep(data.cep, data.logradouro, data.bairro,
                       data.localidade, data.uf)
