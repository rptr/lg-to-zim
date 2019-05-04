import sys
import os
import v1050, v1010, v110, zim

LG_VERSION  = 1050

chapters = {}
entries  = {}

# 1010
def read_diary_1010 (fd):
    print "version 1010 is not supported"

# 110
def read_diary_110 (fd):
    print "version 110 is not supported"

def convert_lg_diary (filepath):
    diary_name = filepath.split('.')[0]

    if os.path.exists(diary_name):
        print diary_name, "already exists"
#        return

    fd = open(filepath)
    line = fd.readline()

    if line != "LIFEOGRAPHDB\n":
        print diary_name, "is not a valid Lifeograph file (does not start with LIFEOGRAPHDB)"
        return

    version = fd.readline()
    vnum = int(version.split(' ')[1])
    fd.close()

    if vnum == 1050 or vnum == 1040 or vnum == 1030 or vnum == 1020:
        chapters, entries = v1050.load(filepath)
    elif vnum == 1011 or vnum == 1010:
        read_diary_1010(fd)
    else:
        read_diary_110(fd)

    zim.write(diary_name, chapters, entries)

if len(sys.argv) > 1:
    convert_lg_diary(sys.argv[1])

