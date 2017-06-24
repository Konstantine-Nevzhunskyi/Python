def read_config():
	return read_from_configs("config")

def save_last_configs(type_of_save):
	with open (".lastConfigs", "w") as file:
		file.write("last_save_type=" + type_of_save)

def read_last_configs():
	return read_from_configs(".lastConfigs")

def read_from_configs(file_name):
	result = "pickle"
	delimiter = "="
	comment_symbol = "#"
	with open(file_name, "r") as config_file:
		for line in config_file:
			if (line[0] != comment_symbol):
				separate_list = line.split(delimiter)
				return separate_list[1]
	return result