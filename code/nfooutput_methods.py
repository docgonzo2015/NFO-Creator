from common_components.fileprocessing_framework import fileprocessing_module as File



def outputnfos(folderpath, movielist, setname, nameprefix, nfocount):

    newnfocount = nfocount
    for moviename in movielist.keys():
        newnfocount = newnfocount + 1
        filepath = File.concatenatepaths(folderpath, moviename + ".nfo")
        fileoutput = []
        fileoutput.append("<movie>")
        fileoutput.append("\t<title>" + nameprefix + moviename + "</title>")
        fileoutput.append("\t<set>" + setname + "</set>")
        if movielist[moviename] != "":
            fileoutput.append("\t<thumb>" + movielist[moviename] + "</thumb>")
            suffix = ""
        else:
            suffix = "..................................................[No Image]"
        fileoutput.append("</movie>")

        print "Writing file " + filepath + suffix

        File.writetodisk(filepath, fileoutput)


    return newnfocount




