import re, string, sys

chapters        = {}
orphans         = []
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
                    "title" : None,
                    "lines" : []}

    global last_entry_id
    last_entry_id = eid

    orphan = True
    chapter_id = 0
    chapter_ids = sorted(chapters)

    for i in chapter_ids:
        if eid > i:
            chapter_id = i
            orphan = False

    if orphan:
        orphans.append(eid)
    else:
        c = chapters[chapter_id]
        c["entries"].append(eid)

def new_line (text):
    if last_entry_id == None:
        return
  
    e = entries[last_entry_id]
    e["lines"].append(text)

    if e["title"] == None:
        text = pattern_special.sub('', text)
        e["title"] = text

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
        new_line(line[2:])

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

    return chapters, entries, orphans

