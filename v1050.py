import re, string

chapters        = {}
entries         = {}
last_entry_id   = None
pattern_special = re.compile('[\W_]+')

def new_chapter (code, line):
    split = line.split('	')
    cid = int(split[0])
    name = split[1]

    name = pattern_special.sub('', name)

    chapters[cid] = {"name" : name,
                     "entries" : []}

    print "chapter", cid, name

def new_entry (line):
    eid = int(line[4:])

    entries[eid] = {"id" : eid, 
                    "lines" : []}
    global last_entry_id
    last_entry_id = eid

def new_line (text):
    if last_entry_id == None:
        return

    entries[last_entry_id]["lines"].append(text)

def chapter_parse_line (line):
    code = line[0:2]
    rest = line[2:]

    # ordinal chapter
    if 'CO' == code:
        new_chapter(code, rest)

    # temporal chapter
    if 'CT' == code:
        new_chapter(code, rest)

    # free chapter
    if 'CG' == code or 'CS' == code:
        new_chapter(code, rest)

    # chapter category
    # if 'CC' == code:

    # chapter color
    # if 'Cc' == code:

    # chapter preferences
    # if 'Cp' == code:


def entry_parse_line (line):
    c = line[0]

    if 'E' == c:
        new_entry(line)

    # dates
    if 'D' == c:
        pass

    # tag
    if 'T' == c:
        pass

    if 'P' == c:
        new_line(line)

def load (filename):
    print "version 1050"

    fd = open(filename)

    # skip header
    for i in range(4):
        fd.readline()

    for line in fd:
        chapter_parse_line(line)

        if line == '\n':
            break
    for line in fd:
        entry_parse_line(line)

    fd.close()

    return chapters, entries

