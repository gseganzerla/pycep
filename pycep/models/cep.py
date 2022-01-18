class Cep:

    def __init__(self, cep: str, street: str, district: str, city: str,
                 state: str) -> None:
        self.cep = cep
        self.street = street
        self.district = district
        self.city = city
        self.state = state

    def __repr__(self) -> str:
        return f"""Logradouro: {self.street}\nBairro: {self.district}\nCidade: {self.city}\nEstado: {self.state}
        """
