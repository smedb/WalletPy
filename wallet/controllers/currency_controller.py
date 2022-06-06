from models.currency import Currency


class CurrencyController:
    def __init__(self):
        self.currencies = Currency()

    def create_currency(self, name: str, overdraft_limit: int) -> str:
        currency = Currency()
        currency.name = name
        currency.overdraft_limit = overdraft_limit
        currency.save()

        return currency.name

    def list_currencies(self) -> list[str]:
        currency_list = []

        for currency in self.currencies.getAll():
            currency_list.append(currency.name)

        return currency_list
