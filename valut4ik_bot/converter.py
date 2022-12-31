from . import parser


class Converter:

    rub_accuracy = 2  # one ruble is a hundred kopecks
    kgs_accuracy = 2  # one som is a hundred tyiyns

    def __init__(self):
        try:
            rate = parser.Parser().get_exchange_rate('RUB', 'KGS')
        except parser.ParseError:
            raise ConversionError
        self._set_exchange_rate(rate)

    def _set_exchange_rate(self, new_rate):
        self.exchange_rate = new_rate

    def one_rub_in_kgs(self):
        return self.exchange_rate

    def one_kgs_in_rub(self):
        return 1.0 / self.exchange_rate

    def rub_to_kgs(self, rubles):
        return round(rubles * self.one_rub_in_kgs(), self.kgs_accuracy)

    def kgs_to_rub(self, soms):
        return round(soms * self.one_kgs_in_rub(), self.rub_accuracy)


class ConversionError(Exception):
    pass


if __name__ == '__main__':
    converter = Converter()

    rate = converter.one_rub_in_kgs()
    print(f'One ruble in soms: {rate}')
    
    rate = converter.one_kgs_in_rub()
    print(f'One som in rubles: {rate}')
    
    soms = converter.rub_to_kgs(10)
    print(f'Ten rubles in soms: {soms}')
    
    rubles = converter.kgs_to_rub(10)
    print(f'Ten soms in rubles: {rubles}')
