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

def write_entry (entry, directory):
    name = entry["title"]

    fd = open(directory + name + ".txt", "w")
    created = 1
    fd.write(zim_header(created))

    for line in entry["lines"]:
        fd.write(line)

    fd.close()

def write (diary_name, chapters, entries, orphans):
    try:
        shutil.rmtree(diary_name)
    except OSError:
        pass

    os.mkdir(diary_name)

    for i in chapters:
        c = chapters[i]
        dr = diary_name + "/" + c["name"]
        os.mkdir(dr)
        fd = open(dr + ".txt", "w")
        fd.close()

        for j in c["entries"]:
            write_entry(entries[j], diary_name+"/"+c["name"]+"/")
            print entries[j]["title"]

    for i in orphans:
        write_entry(entries[i], diary_name+"/")

