#from common_components.userinterface_framework import userinterface_module as GUI
from common_components.fileprocessing_framework import fileprocessing_module as File


def runapplication(rootfolderpath):

	#GUI.init()

	rootfilelist = File.getfolderlisting(rootfolderpath)

	for rootitemname in rootfilelist.keys():

		if rootfilelist[rootitemname] == "Folder":

			topfolderpath = File.concatenatepaths(rootfolderpath, rootitemname)

			print topfolderpath

			topfilelist = File.getfolderlisting(topfolderpath)

			processfilepath = File.concatenatepaths(topfolderpath, "index.setinfo")
			processflag = File.doesexist(processfilepath)
			multimovieflag = File.doesexist(File.concatenatepaths(topfolderpath, "index.multimovie"))

			if processflag == True:

				# READ IN SET INFORMATION # !!!!!!!!!!!!!!!!

				for topitemname in topfilelist.keys():

					if rootfilelist[rootitemname] == "Folder":

						# Look in subfolder for files and process

					else:

						if multimovieflag == True:

							# Process file



	#GUI.quit()



def processsubfolder(folderpath, setname):

	filelist = File.getfolderlisting(folderpath)

	multimovieflag = File.doesexist(File.concatenatepaths(folderpath, "index.multimovie"))


	for itemname in filelist.keys():

		if filelist[itemname] == "Folder":
			processsubfolder(File.concatenatepaths(folderpath, itemname), setname)

		else:

			if multimovieflag == True:

