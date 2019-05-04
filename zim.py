import os, sys, re, string

def zim_header ():
    return "Content-Type: text/x-zim-wiki\nWiki-Format: zim 0.4\nCreation-Date: 2019-05-04T10:45:10+02:00"

print zim_header()

def zim_generate ():
    pass

def zim_make_chapter (cid):
    pass

def zim_make_entry ():
    pass

def write (diary_name, chapters, entries):
    main = "zim_" + diary_name

    try:
        os.rmdir(diary_name)
    except OSError:
        pass

    os.mkdir(diary_name)

    for i in chapters:
        c = chapters[i]

        os.mkdir(diary_name + "/" + c["name"])
        fd = open(diary_name + "/" + c["name"] + ".txt", "w")
        fd.close()

