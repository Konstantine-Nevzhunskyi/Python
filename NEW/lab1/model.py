import datetime
import pickle

class Model:
	def __init__(self, filename):
		self.filename = filename
		#self._db =[]
		self.load()
		super().__init__()
	
	def add_record(self, pressure):
		""" This method adds one new record with time of adding and getted pressure
			Tests:
			>>> model.add_record(220)
			>>> model.records[0]["pressure"]
			220
		"""
		now = datetime.datetime.now()
		record = dict([("pressure", pressure),("date", now)])
		self._db.append(record)
	
	def remove_record(self):
		""" This method removes last record
			Tests:
			>>> r = model.remove_record()
			>>> r["pressure"] == 220
			True
		"""
		return self.records.pop()
		
	def get_daily_records(self, year, month, day):
		""" This method returns records of some day
			Tests:
			>>> model.add_record(220)
			>>> r = model.get_daily_records(now.year, now.month, now.day)
			>>> model.remove_record()["pressure"] == 220
			True
		"""
		select_lst = [rec for rec in self._db if rec["date"].year == year\
					  and rec["date"].month == month and rec["date"].day == day ]
		return select_lst
		
	def get_monthly_records(self, year, month):
		""" This method returns records of some moth
			Tests:
			>>> model.add_record(170)
			>>> r = model.get_daily_records(now.year, now.month, now.day)
			>>> model.remove_record()["pressure"] == 170
			True
		"""
		select_lst = [rec for rec in self._db if rec["date"].year == year\
					  and rec["date"].month == month]
		return select_lst
		
	def get_yearly_records(self, year):
		""" This method returns records of some year
			Tests:
			>>> model.add_record(150)
			>>> r = model.get_daily_records(now.year, now.month, now.day)
			>>> model.remove_record()["pressure"] == 150
			True
		"""
		select_lst = [rec for rec in self._db if rec["date"].year == year]
		return select_lst
		
	@property
	def records(self):
		""" This method returns all records
			Tests:
			>>> model.records == model._db
			True
		"""
		return self._db
	
	def load(self):
		try:
			with open(self.filename, "rb") as source:
				self._db = pickle.load(source)
		except OSError:
			self._db = []
			
	def save(self):
		with open(self.filename, "wb") as target_file:
			pickle.dump(self._db, target_file)	

if __name__ == "__main__":
	import doctest
	doctest.testmod(extraglobs={"model": Model("none"), \
								"record": {"pressure": 1220, "date": datetime.datetime.now()}, \
								"now": datetime.datetime.now()})
