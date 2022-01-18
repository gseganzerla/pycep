import click

from src.services.cep_service import CepService


@click.group('cep_cli')
def cep_cli():
    """pycep utilitaries"""
    pass


@cep_cli.command()
@click.argument('nr_cep', type=click.STRING)
def cep(nr_cep):
    """
    Get CEP information
    """

    service = CepService()
    cep = service.request_by_cep(nr_cep)

    click.echo(cep)


@cep_cli.command()
@click.argument('uf', type=click.STRING)
@click.argument('city', type=click.STRING)
@click.argument('street', type=click.STRING)
def name(uf, city, street):
    """
    Type <uf> <city> <street> to request by name's street.
    """

    service = CepService()
    data = service.request_by_name(uf, city, street)

    click.echo(data)