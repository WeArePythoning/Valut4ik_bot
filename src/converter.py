from parser import Parser


class Converter:

	exchange_rate = None

	def __init__(self):
		if not self.exchange_rate:
			self.set_exchange_rate(Parser().get_exchange_rate('RUB', 'KGS'))

	def set_exchange_rate(self, new_rate):
		self.exchange_rate = new_rate

	def one_rub_in_kgs(self):
		return self.exchange_rate

	def one_kgs_in_rub(self):
		return 1.0 / self.exchange_rate

	def rub_to_kgs(self, rubles):
		return rubles * self.one_rub_in_kgs()

	def kgs_to_rub(self, soms):
		return soms * self.one_kgs_in_rub()
