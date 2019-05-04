import os, sys, re, shutil
from datetime import datetime

def zim_header (created):
    d = datetime.fromordinal(created)
    return "Content-Type: text/x-zim-wiki\nWiki-Format: zim 0.4\nCreation-Date: " + d.isoformat() + "\n\n"

def zim_generate ():
    pass

def zim_make_chapter (cid):
    pass

def zim_make_entry ():
    pass

def write (diary_name, chapters, entries, orphans):
    main = "zim_" + diary_name

    shutil.rmtree(diary_name)
    os.mkdir(diary_name)

    for i in chapters:
        c = chapters[i]

        os.mkdir(diary_name + "/" + c["name"])
        fd = open(diary_name + "/" + c["name"] + ".txt", "w")
        fd.close()

    for i in orphans:
        e = entries[i]
        name = e["title"]

        if name == None:
            continue

        fd = open(diary_name + "/" + name + ".txt", "w")
        created = 1
        fd.write(zim_header(created))

        for line in e["lines"]:
            fd.write(line)

        fd.close()

