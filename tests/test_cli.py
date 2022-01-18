from unittest import TestCase

from click.testing import CliRunner
from vcr import VCR

from src import cli

vcr_ = VCR(
    cassette_library_dir='tests/cassetts',
    path_transformer=VCR.ensure_suffix('.yaml'),
    record_mode='once'
)


class TestCli(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @vcr_.use_cassette
    def test_cep(self):
        result = self.runner.invoke(cli.cep, '07713045')

        self.assertEqual(result.exit_code, 0)

    @vcr_.use_cassette
    def test_get_by_name(self):
        result = self.runner.invoke(cli.name, ['sp', 'osasco', 'sabirigui'])

        self.assertEqual(result.exit_code, 0)