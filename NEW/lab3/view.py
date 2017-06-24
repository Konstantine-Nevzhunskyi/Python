class View:
	
	@staticmethod
	def menu():
		print ("1. Add record")
		print ("2. Remove last record")
		print ("3. Show records")
		print ("4. Exit")
	
	@staticmethod
	def show_menu():
		print ("What periond?")
		print ("1. For particular day")
		print ("2. For particular month")
		print ("3. For particular year")
		print ("4. For all time")
			
	@staticmethod
	def exitting_message():
		print("Bye!")
		
	@staticmethod
	def wrong_input():
		print("You have inputted wrong date!")
		
	@staticmethod
	def success_message():
		print("Done!")
	
	@staticmethod
	def deleted_record(record):
		print("Record:\ndate: {}\npressure: {}\nsuccessfully deleted\n".format(record["date"], record["pressure"]))
		
	def print_records(records):
		print("Records: \n")
		for record in records:
			print("Record:\ndate: {}\npressure: {}\n".format(record["date"], record["pressure"]))

		