from model import Model
from view import View

class Controller:
	def __init__(self, records):
		self.model = records
		super().__init__()
		
	def start(self):
		f = 0
		while  f != 4:
			View.menu()
			try: 
				f = int(input("choose: "))
			except ValueError:
				View.wrong_input()
				f = 0
			
			if f == 0: 
				View.menu()
			elif f == 1:
				p = int(input("your pressure: "))
				self.model.add_record(p)
			elif f == 2:
				View.deleted_record(self.model.remove_record())
			elif f == 3:
				View.show_menu()
				f = int(input("choose: "))
				self.showing_record(f)
				f = 0

	def showing_record(self, f):
		if f != 4:
			year = int(input("year: "))
		if f == 1 or f == 2:
			month = int(input("month: "))
		if f == 1:
			day = int(input("day: "))
			
		if f == 1:
			View.print_records(self.model.get_daily_records(year, month, day))
		elif f == 2:
			View.print_records(self.model.get_monthly_records(year, month))
		elif f == 3:
			View.print_records(self.model.get_yearly_records(year))
		elif f == 4:
			View.print_records(self.model.records)
		elif f == 5:
			View.wrong_input()
		
		