import datetime
import pickle
from configParcer import *
import serialize

class Model:
	def __init__(self, filename):
		self.filename = filename
		self.config = read_config()
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
		load_config = read_last_configs()

		specifier = "rb" if load_config == "pickle" else "r"
		try:
			with open(self.filename, specifier) as source:
				self._db = serialize.load(source, load_config)
		except OSError:
			self._db = []
			
	def save(self):
		specifier = "wb" if self.config == "pickle" else "w"
		with open(self.filename, specifier) as target_file:
			serialize.save(self._db, target_file,self.config)	
			
		save_last_configs(self.config)
