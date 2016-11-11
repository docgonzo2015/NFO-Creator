from common_components.fileprocessing_framework import fileprocessing_module as File



def outputnfos(folderpath, movielist, setname, nameprefix, nfocount):

    newnfocount = nfocount
    for moviename in movielist.keys():
        newnfocount = newnfocount + 1
        filepath = createfilepath(folderpath, moviename)
        fileoutput = createnfocontent(nameprefix + moviename, movielist[moviename], setname)
        if movielist[moviename] != "":
            messagesuffix = ""
        else:
            messagesuffix = "..................................................[No Image]"

        decision = checkexistingnfo(folderpath, moviename, setname, nameprefix, movielist[moviename])

        if decision == "Missing":
            messageprefix = "          Creating new file "
        elif decision == "Already Up To Date":
            messageprefix = "Not modifying existing file "
        elif decision == "Out Of Date":
            messageprefix = "     Updating existing file "
        else:
            messageprefix = "    Unknown action for file "
        print messageprefix + str(nfocount).zfill(4) + ": " + filepath + messagesuffix
        if (decision == "Out Of Date") or (decision == "Missing"):
            File.writetodisk(filepath, fileoutput)


    return newnfocount



def createnfocontent(moviename, imagename, setname):

    fileoutput = []
    fileoutput.append("<movie>")
    fileoutput.append("\t<title>" + moviename + "</title>")
    fileoutput.append("\t<set>" + setname + "</set>")
    if imagename != "":
        fileoutput.append("\t<thumb>" + imagename + "</thumb>")
    fileoutput.append("</movie>")

    return fileoutput



def createfilepath(folderpath, moviename):

    return File.concatenatepaths(folderpath, moviename + ".nfo")



def checkexistingnfo(folderpath, moviename, setname, nameprefix, imagename):

    outcome = "Missing"

    nfofilepath = createfilepath(folderpath, moviename)
    if File.doesexist(nfofilepath):
        olddata = File.readfromdisk(nfofilepath)
        newdata = createnfocontent(nameprefix + moviename, imagename, setname)
        if len(olddata) == len(newdata):
            outcome = "Already Up To Date"
            for index in range(0, len(olddata)):
                if olddata[index] != newdata[index]:
                    outcome = "Out Of Date"
        else:
            outcome = "Out Of Date"

    return outcome