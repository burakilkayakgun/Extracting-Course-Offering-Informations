#!/usr/bin/env python3
# CmpE230 HW2
# Emre Demircioğlu 2016400204
# Burak İlkay Akgün 2015400018

import pandas as pd
import sys

# list of all possible course code
course_list = ["ASIA", "ATA", "AUTO", "BM", "BIS", "CHE", "CHEM", "CE", "COGS", "CSE", "CET", "CMPE", "INT", "CEM",
              "CCS","EQE","EC","EF","ED","EE","ETM","ENV","ENVT","XMBA","FE","PA","FLED","GED","GPH",
              "GUID","HIST","HUM","IE","INCT","MIR","INTT","LS","LING","AD","MIS","MATH","SCED","ME",
              "MECA","BIO","PHIL","PE","PHYS","POLS","PRED","PSY","YADYOK","SPL","SOC","SWE","TRM","SCO",
              "WTR","TR","TK","TKL","LL"]
# dictionary according to the codes and their course names
course_dictionary = {
    "ASIA": ["ASIAN+STUDIES","ASIAN+STUDIES+WITH+THESIS"],
    "ATA": ["ATATURK+INSTITUTE+FOR+MODERN+TURKISH+HISTORY"],
    "AUTO": ["AUTOMOTIVE+ENGINEERING"],
    "BM": ["BIOMEDICAL+ENGINEERING"],
    "BIS": ["BUSINESS+INFORMATION+SYSTEMS"],
    "CHE": ["CHEMICAL+ENGINEERING"],
    "CHEM": ["CHEMISTRY"],
    "CE": ["CIVIL+ENGINEERING"],
    "COGS": ["COGNITIVE+SCIENCE"],
    "CSE": ["COMPUTATIONAL+SCIENCE+%26+ENGINEERING"],
    "CET": ["COMPUTER+EDUCATION+%26+EDUCATIONAL+TECHNOLOGY","EDUCATIONAL+TECHNOLOGY"],
    "CMPE": ["COMPUTER+ENGINEERING"],
    "INT": ["CONFERENCE+INTERPRETING"],
    "CEM": ["CONSTRUCTION+ENGINEERING+AND+MANAGEMENT"],
    "CCS": ["CRITICAL+AND+CULTURAL+STUDIES"],
    "EQE": ["EARTHQUAKE+ENGINEERING"],
    "EC": ["ECONOMICS"],
    "EF": ["ECONOMICS+AND+FINANCE"],
    "ED": ["EDUCATIONAL+SCIENCES"],
    "EE" : ["ELECTRICAL+%26+ELECTRONICS+ENGINEERING"],
    "ETM": ["ENGINEERING+AND+TECHNOLOGY+MANAGEMENT"],
    "ENV": ["ENVIRONMENTAL+SCIENCES"],
    "ENVT": ["ENVIRONMENTAL+TECHNOLOGY"],
    "XMBA": ["EXECUTIVE+MBA"],
    "FE": ["FINANCIAL+ENGINEERING"],
    "PA": ["FINE+ARTS"],
    "FLED": ["FOREIGN+LANGUAGE+EDUCATION"],
    "GED": ["GEODESY"],
    "GPH": ["GEOPHYSICS"],
    "GUID": ["GUIDANCE+%26+PSYCHOLOGICAL+COUNSELING"],
    "HIST": ["HISTORY"],
    "HUM": ["HUMANITIES+COURSES+COORDINATOR"],
    "IE":  ["INDUSTRIAL+ENGINEERING"],
    "INCT": ["INTERNATIONAL+COMPETITION+AND+TRADE"],
    "MIR": ["INTERNATIONAL+RELATIONS%3aTURKEY%2cEUROPE+AND+THE+MIDDLE+EAST",
            "INTERNATIONAL+RELATIONS%3aTURKEY%2cEUROPE+AND+THE+MIDDLE+EAST+WITH+THESIS"],
    "INTT": ["INTERNATIONAL+TRADE","INTERNATIONAL+TRADE+MANAGEMENT"],
    "LS": ["LEARNING+SCIENCES"],
    "LING": ["LINGUISTICS"],
    "AD": ["MANAGEMENT"],
    "MIS": ["MANAGEMENT+INFORMATION+SYSTEMS"],
    "MATH": ["MATHEMATICS"],
    "SCED": ["MATHEMATICS+AND+SCIENCE+EDUCATION","SECONDARY+SCHOOL+SCIENCE+AND+MATHEMATICS+EDUCATION"],
    "ME": ["MECHANICAL+ENGINEERING"],
    "MECA": ["MECHATRONICS+ENGINEERING"],
    "BIO": ["MOLECULAR+BIOLOGY+%26+GENETICS"],
    "PHIL": ["PHILOSOPHY"],
    "PE": ["PHYSICAL+EDUCATION"],
    "PHYS": ["PHYSICS"],
    "POLS": ["POLITICAL+SCIENCE%26INTERNATIONAL+RELATIONS"],
    "PRED": ["PRIMARY+EDUCATION"],
    "PSY": ["PSYCHOLOGY"],
    "YADYOK": ["SCHOOL+OF+FOREIGN+LANGUAGES"],
    "SPL": ["SOCIAL+POLICY+WITH+THESIS"],
    "SOC": ["SOCIOLOGY"],
    "SWE": ["SOFTWARE+ENGINEERING","SOFTWARE+ENGINEERING+WITH+THESIS"],
    "TRM": ["SUSTAINABLE+TOURISM+MANAGEMENT","TOURISM+ADMINISTRATION"],
    "SCO": ["SYSTEMS+%26+CONTROL+ENGINEERING"],
    "WTR": ["TRANSLATION"],
    "TR": ["TRANSLATION+AND+INTERPRETING+STUDIES"],
    "TK": ["TURKISH+COURSES+COORDINATOR"],
    "TKL": ["TURKISH+LANGUAGE+%26+LITERATURE"],
    "LL": ["WESTERN+LANGUAGES+%26+LITERATURES"],
}
# list of all semesters
semester_list = ["1998-Fall", "1999-Spring", "1999-Summer", "1999-Fall", "2000-Spring", "2000-Summer", "2000-Fall",
                 "2001-Spring", "2001-Summer", "2001-Fall", "2002-Spring", "2002-Summer", "2002-Fall", "2003-Spring",
                 "2003-Summer", "2003-Fall", "2004-Spring", "2004-Summer", "2004-Fall", "2005-Spring", "2005-Summer",
                 "2005-Fall", "2006-Spring", "2006-Summer", "2006-Fall", "2007-Spring", "2007-Summer", "2007-Fall",
                 "2008-Spring", "2008-Summer", "2008-Fall", "2009-Spring", "2009-Summer", "2009-Fall", "2010-Spring",
                 "2010-Summer", "2010-Fall", "2011-Spring", "2011-Summer", "2011-Fall", "2012-Spring", "2012-Summer",
                 "2012-Fall", "2013-Spring", "2013-Summer", "2013-Fall", "2014-Spring", "2014-Summer", "2014-Fall",
                 "2015-Spring", "2015-Summer", "2015-Fall", "2016-Spring", "2016-Summer", "2016-Fall", "2017-Spring",
                 "2017-Summer", "2017-Fall", "2018-Spring", "2018-Summer", "2018-Fall", "2019-Spring", "2019-Summer",
                 "2019-Fall"]

# this method is used to find the year in the input arguments
# for example if the input is 2017-Spring this method return the 2017
def find_year(str):
    index=str.index("-")
    return int(str[0:index],10)
# this method is used to find the semester in the input arguments
# for example if the input is 2017-Spring this method return the Spring
def find_semester(str):
    index = str.index("-")+1
    return str[index:]
# this method is used in the arranging the html link's semester part
# for example for 2016-Fall semester we need to write 2016/2017-1
# or for 2013-Spring we need to 2013/2014-2, this method help us to these
# translation
def index_semester(str):
    if str=='Fall':
        return 1
    elif str=='Spring':
        return 2
    return 3
# this method create html with the given parameters years is
# the semester, course is the code of course (like CMPE) and
# department is the full name of course (like Computer Engineering)
def create_html(years,course,department):
    str_head = "https://registration.boun.edu.tr/scripts/sch.asp?donem="
    str_middle = "&kisaadi="
    str_tail = "&bolum="
    return str_head + years + str_middle + course + str_tail + department
# this method is used with index_semester method to creating semester
# part of html links, for example input format like 2015-Summer and method
# return 2014/2015-3
def create_year(input):
    year_index = index_semester(find_semester(input))
    year = find_year(input)
    if(year_index==1):
        year_to_return = str(year) + "/" + str((year+1)) + "-1"
    elif(year_index==2):
        year_to_return = str((year-1)) + "/" + str(year) + "-2"
    else:
        year_to_return = str((year-1)) + "/" + str(year) + "-3"
    return year_to_return
# this method is used to creating whole html links for one semester
def create_html_for_one_semester(year):
    list = []
    for x in course_list:
        list.append(create_html(year, x, course_dictionary[x][0]))
        if(len(course_dictionary[x])==2):
            list.append(create_html(year, x, course_dictionary[x][1]))
    for y in list:
        entire_link_list.append(y)
# this method is the starting method of our programs it read
# the arguments and set the bounds (first semester and last semester)
def start():
    start_index = semester_list.index(sys.argv[1])
    end_index = semester_list.index(sys.argv[2])
    for x in range(start_index,end_index+1):
        create_html_for_one_semester(create_year(semester_list[x]))
# this is course class with a constructor that contains
# 2 lists and 3 fields that are yearList(list) for semesters,
# instru(list) for instructors, name for course name, kod for
# course code(CMPE), and ins for instructor and also append year
# and ins to the related list
class Course:
    def __init__(self,kod, name, ins,year):
        self.yearList=[]
        self.instru=[]
        self.name = name
        self.ins = ins
        self.kod=kod
        self.yearList.append(year)
        self.instru.append(ins)
# this is Semester class with a constructor that contains
# 2 lists and 3 field which 2 of them is initialized that are
# courseList(list) for courses, instructor(list) for instructor
# year for semester, under for counting the undergraduate course number,
# grad for counting the graduating course number
class Semester:
    def __init__(self,year):
        self.year=year
        self.courseList = []
        self.under = 0
        self.grad = 0
        self.instructors=[]
# this is Department class with a constructor that contains
# 3 lists, 4 field which 2 of them is initialized and 1 other method
# that are courseList(list) for courses,semesterList(list) for semesters,
# instructors(list) for instructors, kod for course code (like CMPE), name
# for course name, under for counting the undergraduate course number,
# grad for counting the graduating course number and that class also
# contains some other methods that are describe briefly on the written places
class Department:
    def __init__(self, name,kod):
        self.kod=kod
        self.name = name
        self.courseList=[]
        self.under=0
        self.grad=0
        self.semesterList=[]
        self.instructors=[]
        self.createrSemesterList()
    # this method is used to fulfill semesterList according to start semester and
    # end semester
    def createrSemesterList(self):
        start_index = semester_list.index(sys.argv[1])
        end_index = semester_list.index(sys.argv[2])
        for x in range(start_index, end_index + 1):
            self.semesterList.append(Semester(semester_list[x]))
    # this method is used to processing data that are taken from the html links
    # actually we can say that this method is like our main method that's mean reading
    # data and processing them are made in this method
    # this method determine the which courses is in the graduate or undergraduate course and also
    # which semester any courses is given or not and also make some operation to instructor for
    # determine distinct instructor numbers
    def add_course(self,kod,name,ins,year):
        isalready=False
        k=0
        try:
            k = int(kod[-3], 10)
        except:
            k=1
        for c in self.courseList:
            if c.kod==kod:
                isalready=True
                if not(self.instructors.__contains__(ins)):
                    self.instructors.append(ins)
                for x in self.semesterList:
                    if x.year==year:
                        if not(x.courseList.__contains__(kod)):
                            x.courseList.append(kod)
                            if k >= 5:
                                x.grad += 1
                            else:
                                x.under += 1
                            if not (x.instructors.__contains__(ins)):
                                x.instructors.append(ins)
                        elif not (x.instructors.__contains__(ins)):
                            x.instructors.append(ins)
                if not(c.instru.__contains__(ins)) :

                    c.instru.append(ins)

                if not(c.yearList.__contains__(year)):
                    c.yearList.append(year)

        if not(isalready):
            self.courseList.append(Course(kod, name, ins, year))
            if not (self.instructors.__contains__(ins)):
                self.instructors.append(ins)
            if k >= 5:
                self.grad += 1
            else:
                self.under += 1
            for x in self.semesterList:
                if x.year==year:
                    x.courseList.append(kod)
                    if k >= 5:
                        x.grad+=1
                    else:
                        x.under += 1
                    if not(x.instructors.__contains__(ins)):
                        x.instructors.append(ins)

# entire_link_list is the list that will contains all links that will use to reading data
# after running start() method, course_list is sorted to force outputs format in alphabetic order,
# departmentList is list that contains department, ss is the number of the semesters that are
# wanted from the client
entire_link_list = []
course_list.sort()
start()
depatmentList=[]
ss=int(len(entire_link_list)/69)

# this for loop rearrange the course name to writing true format on the output (replace %26 with &)
for x in course_list:
    depatmentList.append(Department( course_dictionary[x][0].replace("%26","&").replace("+"," "),x))
    if (len(course_dictionary[x]) == 2):
        depatmentList.append(Department(course_dictionary[x][1].replace("%26","&").replace("+"," "), x))

# this for loop handle the situation that html link does not contain any data and if there is data on the html link
# progress the data according the type of data
for m in range(0,ss):
    for n in range(m*69,(m+1)*69):
        data=[]
        try:
            data = pd.read_html(entire_link_list[n])
        except:
            data=-1
        year=semester_list[semester_list.index(sys.argv[1])+m]
        if data!=-1:
            size=len(data[-1][0])
            for i in range(1,size):
                kod=str(data[-1][0][i])
                name=str(data[-1][2][i])
                ins=str(data[-1][5][i])
                if kod!="nan":
                    kod=kod[0:-3]
                    depatmentList[n%69].add_course(kod,name,ins,year)

# title is the first row of the output format, it is straightforward in the project description
# moreover, there is a for loop for writing semesters name in given order like
# "Dept./Prog.(name);Course Code;Course Name; 2018-Summer; 2018-Fall; 2019-Spring; Total Offerings"
title="Dept./Prog.(name);Course Code;Course Name; "
start_index = semester_list.index(sys.argv[1])
end_index = semester_list.index(sys.argv[2])
for x in range(start_index,end_index+1):
    title=title+str(semester_list[x])+"; "
title=title+"Total Offerings"
print(title)

# this for loop is used to writing the other rows of output, firstly write the department name, code
# and the numbers of undergraduate and graduate courses for each semester like
# "AD(MANAGEMENT) ;U54 G69 ; ;U6 G0 I3;U34 G45 I41;U32 G41 I38;U139 G166 I46"
# and also after writing this, that loop also write the whole courses that are in that related department like
# " ;AD 312;MONEY & BANKING; ; ;x;1/1 "
for j in depatmentList:
    if len(j.courseList)!=0:
        first_line=j.kod+"("+j.name+")"+" ;"+"U"+str(j.under)+" G"+ str(j.grad) +" ;"+" ;"
        u_total=0
        g_total=0
        for num in j.semesterList:
            u_total+=num.under
            g_total+=num.grad
            if num.instructors.__contains__("STAFF STAFF"):
                first_line = first_line +  "U" + str(num.under) + " G" + str(num.grad) + " I" + str(len(num.instructors) - 1) + ";"
            else:
                first_line = first_line +  "U" + str(num.under) + " G" + str(num.grad) + " I" + str(len(num.instructors)) + ";"
        if j.instructors.__contains__("STAFF STAFF"):
            first_line=first_line + "U" + str(u_total) + " G" + str(g_total) + " I" + str(len(j.instructors) - 1)+ ""
        else:
            first_line = first_line + "U" + str(u_total) + " G" + str(g_total) + " I" + str(len(j.instructors)) + ""
        print(first_line)
        cc_list=[]
        cc_sorted_list=[]
        cc_name_list=[]
        i_list=[]
        for dc in j.courseList:
            i_list.append(len(dc.instru))
            cc_sorted_list.append(dc.kod)
            cc_list.append(dc.kod)
            cc_name_list.append(dc.kod)
            cc_name_list.append(dc.name)
        cc_sorted_list.sort()
        for cc in cc_sorted_list:
            x_counter = 0
            middle_line=" ;"+ cc +";"
            index=cc_name_list.index(cc)
            middle_line=middle_line+cc_name_list[index+1]+";"
            for num in j.semesterList:
                if num.courseList.__contains__(cc):
                    middle_line = middle_line + "x" + ";"
                    x_counter+=1
                else:
                    middle_line = middle_line + "" + " " + ";"
            index2=cc_list.index(cc)
            middle_line=middle_line+str(x_counter)+"/"+str(i_list[index2])
            print(middle_line)

