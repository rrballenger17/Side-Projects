# rename files in /Users/Ryan/Desktop/Prank without numbers to show the hidden message

import os

def rename_files():
	#get file names from folder
	file_list = os.listdir("/Users/Ryan/Desktop/Prank")
	
	saved_path = os.getcwd()

	print("Current Working Directory is " + saved_path)

	os.chdir("/Users/Ryan/Desktop/Prank")

	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))

	os.chdir(saved_path)


rename_files()

