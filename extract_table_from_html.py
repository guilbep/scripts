#!/opt/local/bin/python

import os,sys
import re
import Queue
import pprint
import pickle
import BeautifulSoup
import timeit

# we should use args to open file



lensys = len(sys.argv)

def get_input_file_open():
    if lensys == 2 or lensys == 3:
        f = open(sys.argv[1], 'r')
    else:
        print "bad file input"
        f = None
    return f

def close_input_file(f):
    f.close()


def get_tables2():
    print "not implemented yet"
"""
    file = get_intput_file_open()
    temp = file.read()
    end = Queue.Queue()
    start = []
    inc = 0
    ps = temp.find("<ta",inc)
    if ps != -1:
        start.append(ps)
        inc = ps + 1
        tmp_start = temp.find("<ta",inc)
        tmp_end = temp.find("</ta",inc)
        if (tmp_start < tmp_end):
            # it means that we did'nt close the previous
            # so we put it in the
"""

def get_table_via_dom():
#    print "table via dom"
    return

def get_table_via_beautiful_soup():
#   print "table via beautifulsoup"
    blop = get_input_file_open()

    soup = BeautifulSoup.BeautifulSoup(blop)

    listofhtmltable = soup.findAll('table')

    f = open("a.out","wb")
    listofhtmltable2 = []
    for i in listofhtmltable:
        listofhtmltable2.append(i.prettify())
    pickle.dump(listofhtmltable2, f)
    f.close()
    blop.close()
    return listofhtmltable2


# best for the moment
def get_tables():
    file = get_input_file_open()
    temp = file.read()
    starts = [match.start() for match in re.finditer(re.escape("<ta"),temp)]
    starts2 = [match.start() for match in re.finditer(re.escape("</ta"),temp)]
    # check if len starts and starts2 are equal if not --> raise error
    print starts, "\n", starts2

    lenstarts = len(starts)
    lenstarts2 = len(starts2)

    listofhtmltable = []
    if lenstarts2 == lenstarts:
        for i in range(lenstarts):
            tempstart = starts[i]
            j = i
            # CODE NOT SAFE == TO ENHANCE
            while (j+1) < lenstarts and starts[j+1] < starts2[j]:
                j += 1
            # 8 is the len of "</table> # fixed the magic number
            table_content = temp[tempstart:starts2[j]+8]
            listofhtmltable.append(table_content)
    file.close()
    return listofhtmltable

def get_tables_own():
    file = get_input_file_open()
    temp = file.read()
    starts = [match.start() for match in re.finditer(re.escape("<ta"),temp)]
    starts2 = [match.start() for match in re.finditer(re.escape("</ta"),temp)]
    listofhtmltable = []
    # check if len starts and starts2 are equal if not --> raise error

    lenstarts = len(starts)
    lenstarts2 = len(starts2)

    if lenstarts2 == lenstarts:
        # we destroy the elements of the tables each time
        while len(starts) > 0:
            tempstart = starts[0]
            j = 0
            while (j+1) < len(starts) and starts[j+1] < starts2[j]:
                j += 1
            # 8 is the len of "</table>
            table_content = temp[tempstart:starts2[j]+8]

            listofhtmltable.append(table_content)
            # remove the already extracted tables
            starts.pop(0)
            starts2.pop(j)

        f = open("a.out","wb")

        pickle.dump(listofhtmltable, f)
        f.close()

    close_input_file(file)

    return listofhtmltable

## Here is the code for the benchmark via timeIT
## between beautiful_soup and owncode ## add other html_parser

setup1 ="from __main__ import get_tables"
setup2 ="from __main__ import get_table_via_beautiful_soup"

t1 = timeit.Timer("get_table_via_beautiful_soup()",setup2)
t2 = timeit.Timer("get_tables()",setup1)


# pickle double the time of t2.. too expensive. hadoop will handle this
#print t1.timeit(1)
#print t2.timeit(2000)
get_tables()
