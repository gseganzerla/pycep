from unittest import TestCase

from vcr import VCR
from src.services.cep_service import CepService
from src.models.cep import Cep

vcr_ = VCR(cassette_library_dir='tests/cassetts',
           path_transformer=VCR.ensure_suffix('.yaml'),
           record_mode='once')


class TestCep(TestCase):

    def setUp(self):
        self.dummy_cep = '01001-000'
        self.service = CepService()

    @vcr_.use_cassette
    def test_request_by_cep(self):

        cep = self.service.request_by_cep(self.dummy_cep)

        self.assertIsInstance(cep, Cep)
        self.assertEquals(cep.cep, self.dummy_cep)
