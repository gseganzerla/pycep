from unittest import TestCase

from pycep.models.cep import Cep
from pycep.services.cep_service import CepService
from vcr import VCR

my_vcr = VCR(cassette_library_dir='tests/cassetts',
           path_transformer=VCR.ensure_suffix('.yaml'),
           record_mode='once')


class TestCep(TestCase):

    def setUp(self):
        self.dummy_cep = '01001-000'
        self.service = CepService()

    @my_vcr.use_cassette
    def test_request_by_cep(self):

        cep = self.service.request_by_cep(self.dummy_cep)

        self.assertIsInstance(cep, Cep)
        self.assertEquals(cep.cep, self.dummy_cep)

    @my_vcr.use_cassette
    def test_request_by_name(self):

        ceps = self.service.request_by_name('RS', 'Porto Alegre', 'Domingos')

        self.assertIsInstance(ceps, list)
