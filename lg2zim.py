import sys
import os
import v1050, v1010, v110

LG_VERSION  = 1050

#
# ZIM GENERATION
#

def zim_header ():
    return "Content-Type: text/x-zim-wiki\nWiki-Format: zim 0.4\nCreation-Date: 2019-05-04T10:45:10+02:00"

print zim_header()

def zim_generate ():
    pass

def zim_make_chapter (cid):
    pass

def zim_make_entry ():
    pass

chapters = {}
entries  = {}

#
# 1010
#

def read_diary_1010 (fd):
    print "version 1010 is not supported"

#
# 110
#

def read_diary_110 (fd):
    print "version 110 is not supported"

def convert_lg_diary (filepath):
    diary_name = filepath.split('.')[0] + "_zim"

    if os.path.exists(diary_name):
        print diary_name, "already exists"
#        return

    try:
        os.rmdir(diary_name)
    except OSError:
        pass

    os.mkdir(diary_name)

    fd = open(filepath)
    line = fd.readline()

    if line != "LIFEOGRAPHDB\n":
        print diary_name, "is not a valid Lifeograph file (does not start with LIFEOGRAPHDB)"
        return

    version = fd.readline()
    vnum = int(version.split(' ')[1])
    fd.close()

    if vnum == 1050 or vnum == 1040 or vnum == 1030 or vnum == 1020:
        v1050.load(filepath)
    elif vnum == 1011 or vnum == 1010:
        read_diary_1010(fd)
    else:
        read_diary_110(fd)

if len(sys.argv) > 1:
    convert_lg_diary(sys.argv[1])

