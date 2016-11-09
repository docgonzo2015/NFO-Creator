import os as OperatingSystem


# ---------------------------------------------
# Reads a file from disk and returns a list,
# where each list item is a line in the file
# ---------------------------------------------

def readfromdisk(filename):

	newfilelist = []

	try:
		# Open the file for the duration of this process
		with open(filename) as fileobject:

			# Loop over all lines in the file
			for fileline in fileobject.readlines():

				# Only process if the line isn't blank
				if fileline != "":
					newfilelist.append(fileline.rstrip('\r\n'))

	except:
		# Print an error if the file cannot be read
		print "Cannot read file - ", filename

	return newfilelist

	
	
# ---------------------------------------------
# Returns a list of strings, extracted from a
# single string of tab separated substrings
# ---------------------------------------------

def extracttabulateddata(fileline):

	splitdata = fileline.split("\t")
	return splitdata



# ---------------------------------------------
# Returns a list of strings, extracted from a
# single string of comma-space separated substrings
# ---------------------------------------------

def extractcommadata(fileline):

	splitdata = fileline.split(", ")
	return splitdata



# ---------------------------------------------
# Returns a list of two strings, extracted from a
# single string of space-equals-space separated substrings
# ---------------------------------------------

def extractdatapair(dataitem):

	splitdata = dataitem.split(" = ")
	return splitdata[0], splitdata[1]



# ---------------------------------------------
# Returns a list items found in the specified
# folderpath, with File/Folder/Unknown designations
# ---------------------------------------------

def getfolderlisting(folderpath):

	outcome = {}

	try:
		listing = OperatingSystem.listdir(folderpath)

		for listitem in listing:
			if OperatingSystem.path.isfile(listitem) == True:
				itemtype = "File"
			elif OperatingSystem.path.isdir(listitem) == True:
				itemtype = "Folder"
			else:
				itemtype = "Unknown"
			outcome[listitem] = itemtype

	except:
		print "Cannot access folder - ", folderpath

	return outcome