import sys
import os

LG_VERSION  = 1050

def new_chapter (chapter_name):
    pass

def new_entry (entry_name):
    pass

def new_line (text):
    pass

def parse_line (line):
    code = line[0]
    rest = line[2:]

    if 'V' == code:
        version = int(rest)

        if version != LG_VERSION:
            print "This format version ({}) is not supported.".format(version)

    if 'P' == code:
        new_line(rest)

def convert_lg_diary (filepath):
    diary_name = filepath.split('.')[0] + "_zim"

    if os.path.exists(diary_name):
        print diary_name, "already exists"
#        return

    os.rmtree(diary_name)
    os.mkdir(diary_name)

    fd = open(filepath)

    for line in fd:
        parse_line(line)

    fd.close()

if len(sys.argv) > 1:
    convert_lg_diary(sys.argv[1])

