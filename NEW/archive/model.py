import datetime
import pickle
import doctest

class Model:
	def __init__(self, filename):
		"""
		Initialize Model class
		Args : filename
		"""
		self.filename = filename
		#self._db =[]
		self.load()
		super().__init__()
	
	def add_record(self, pressure):
		"""
		Method add new record
		
 		True
 		"""
		now = datetime.datetime.now()
		record = dict([("pressure", pressure),("date", now)])
		self._db.append(record)
	
	def remove_record(self):
		"""
		Method remove record
		
 		[]
		"""
		return self.records.pop()
		
	def get_daily_records(self, year, month, day):
		"""
		
		
		True
		"""
		select_lst = [rec for rec in self._db if rec["date"].year == year\
					  and rec["date"].month == month and rec["date"].day == day ]
		return select_lst
		
	def get_monthly_records(self, year, month):
		"""
		
		
		True
		"""
		select_lst = [rec for rec in self._db if rec["date"].year == year\
					  and rec["date"].month == month]
		return select_lst
		
	def get_yearly_records(self, year):
		"""
		>>>model.add_record(record)
		
		True
		"""
		select_lst = [rec for rec in self._db if rec["date"].year == year]
		return select_lst
		
	@property
	def records(self):
		return self._db
	
	def load(self):
		"""
		Method try to open saved file
		"""
		try:
			with open(self.filename, "rb") as source:
				self._db = pickle.load(source)
		except OSError:
			self._db = []
			
	def save(self):
		"""
		Method save information
		"""
		with open(self.filename, "wb") as target_file:
			pickle.dump(self._db, target_file)

if __name__ = "__main__":
	doctest.testmod(extraglobs={"model": Model("storage"), \
								"record": {"pressure": 1220, "date": datetime.datetime.now()}})
