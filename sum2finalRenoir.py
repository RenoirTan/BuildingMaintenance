#note: All comments are written one line above the referenced line of code to make it easier to write and to read with minimal need to scroll.

#module test code at bottom because otherwise functions will not be defined

#introduction
print("Thank you for using NUS Building Maintenance Department's building maintenance code services written and produced by Renoir.\n\n\nThis module consists of the following functions:\n\ntotal_venues(filename)\n\navailable_venues(filename,start,end,day)\n\nvenue_occupancy(filename)\n\navailable_timing(filename,day,venue)\n\npp_schedule(filename,venue)\n\n\nIf you need more details on any of the functions, type in 'help(function)' without the function's brackets and arguments, and apostrophes.\n\nFor instance:\n\nhelp(total_venues)\n\n\nIf you need the list of commands again, type in 'commands()' without the apostrophes.\n\n\nTo get information on what files are required for this compilation of code, run 'requiry()' without the apostrophes.")

#list of commands printer

def commands():
    print("This module consists of the following functions:\n\ntotal_venues(filename)\n\navailable_venues(filename,start,end,day)\n\nvenue_occupancy(filename)\n\navailable_timing(filename,day,venue)\n\npp_schedule(filename,venue)\n\n\nIf you need more details on any of the functions, type in 'help(function)' without the function's brackets and arguments, and apostrophes.\n\nFor instance:\n\nhelp(total_venues)\n\n\nIf you need the list of commands again, type in 'commands()' without the apostrophes.\n\n\nTo get information on what files are required for this compilation of code, run 'requiry()' without the apostrophes.")

#requirements text

def requiry():
    #reading the file
    f = open("requirements.txt","r")
    incsv = f.readlines()
    #removing affixes
    incsv[:] = [i.rstrip('\n') for i in incsv]
    #print everything except first 2 lines
    for i in incsv[2:]:
        print(i)

#part a

def total_venues(filename):
    """total_venues(filename) returns an integer that tells you how many different unique values there are in the csv timetable file.
    
    To use total_venues, enter the filename in the function. The function should return an integer.
    For example:
    
    >>> total_venues("timetable1.csv")
    344
    
    >>> total_venues("timetable2.csv")
    71

    >>> total_venues("timetable3.csv")
    184
    """
    #reading the file
    f = open(filename,"r")
    #incsv is a short form of 'input csv file'
    incsv = f.readlines()
    #removing affixes
    incsv[:] = [i.rstrip('\n') for i in incsv]
    #lines into lists
    #tempstr and templist are temporary variables to split the strings in incsv
    tempstr = ""
    templist = []
    for j in range(len(incsv)):
        #enters each line into temporary string variable
        tempstr = incsv[j]
        #enters the split string into a temporary list variable
        templist.append(tempstr.split(","))
        #modify original line in original list with split list
        incsv[j] = templist
        #reset temporary variables
        tempstr = ""
        templist = []
    #final format of incsv: [[[moduleCode,ClassNo,LessonType,DayCode,DayText,StartTime,EndTime,Venue,AcadYear,Semester]],...]
    #yes each line is nested in two lists for some reason
    #lists all venues
    #venuelist stores all occurrences of the venues. venues can be repeated
    venuelist = []
    for k in range(len(incsv)):
        #append venue to venuelist
        venuelist.append(incsv[k][0][7])
    #filter all unique venues by checking whether venue is already in filterlist
    filterlist = []
    #check is temporary variable to decide whether to add venue
    check = True
    #for all venues in venuelist
    for l in range(len(venuelist)):
        #if venue in venuelist already in filterlist
        if venuelist[l] in filterlist:
            #decision to add venue is false
            check = False
        #if decision is to add the venue in venuelist
        if check == True:
            #append new venue to filterlist
            filterlist.append(venuelist[l])
        #reset decision to true
        check = True
    return (len(filterlist)-1)

#test cases for part a

def assert_total_venues():
    assert total_venues("timetable1.csv") == 344
    assert total_venues("timetable2.csv") == 71
    assert total_venues("timetable3.csv") == 184

#part b

def available_venues(filename,start,end,day):
    """available_venues(filename,start,end,day) returns a list of venues that are not occupied in a certain time range in a certain day.

    To use available_venues, enter the filename as the first argument, followed by the start time, end time and an integer end code. The function should return a list with all available venues.
    For example:
    
    >>> available_venues("timetable2.csv",1000,2200,4)
    ['CAPT-SR4', 'CAPT-SR6', 'CEProj', 'CMS', 'COM1-0208', 'COM1-0212', 'COM1-0217', 'COM1-B111', 'COM1-B113', 'DV1', 'E1-06-01', 'E1-06-11', 'CELC-SR2A', 'COM1-0203', 'COM2-0108', 'CR4-1', 'DV2', 'E-LAB', 'E1-06-07', 'CAPT-DV', 'COFM-LAB', 'CR1', 'CAPT-SR2', 'COM1-B102', 'COM1-B112', 'CR3-4', 'CR4-2', 'DV', 'E1-06-05', 'E2-03-03', 'CELC-SR1A']

    >>> available_venues("timetable1.csv",800,2200,1)
    ['AS1-0201', 'AS1-0210', 'AS1-0302', 'AS1-0303', 'AS1-0304', 'AS1-0548', 'AS2-0312', 'AS2-0413', 'AS2-0510', 'AS3-0212', 'AS3-0214', 'AS3-0308', 'AS3-0523', 'AS4-0110', 'AS4-0114', 'AS4-0117', 'AS4-0118', 'AS4-0119', 'AS4-0335', 'AS4-B109', 'AS4-B110', 'AS5-0205', 'AS5-0309', 'AS6-0214', 'AS6-0333', 'AS6-0425', 'AS7-0102', 'AS7-0214', 'AS7-0302', 'AS7-0411', 'BIZ-0118', 'BIZ1-0201', 'BIZ1-0202', 'BIZ1-0203', 'BIZ1-0205', 'BIZ1-0206', 'BIZ1-0301', 'BIZ1-0302', 'BIZ1-0303', 'BIZ1-0304', 'BIZ2-0224', 'BIZ2-0228', 'BIZ2-0229', 'BIZ2-0301', 'BIZ2-0302', 'BIZ2-0413B', 'BIZ2-0420', 'BIZ2-0422', 'BIZ2-0509', 'BIZ2-0510', 'CAPT-DV', 'CAPT-SR2', 'CAPT-SR4', 'CAPT-SR6', 'CELC-SR1A', 'CELC-SR2A', 'CEProj', 'CMS', 'COFM-LAB', 'COM1-0203', 'COM1-0208', 'COM1-0212', 'COM1-0217', 'COM1-B102', 'COM1-B111', 'COM1-B112', 'COM1-B113', 'COM2-0108', 'CR1', 'CR2-1', 'CR3-4', 'CR3-6', 'CR4-2', 'DV', 'DV1', 'DV2', 'E-LAB', 'E1-06-01', 'E1-06-05', 'E1-06-07', 'E1-06-11', 'E2-03-03', 'E3-0301ESP', 'E3-0519ESP', 'E3-06-01', 'E3-06-07', 'E3-06-10', 'E4-02-01', 'E4-04-02', 'E4-04-03', 'E4-04-07', 'E5-03-22', 'E5-03-23', 'EA-02-11', 'EA-06-02', 'EA-06-05', 'ELC-T8', 'ENG-AUD', 'ER2', 'ER3', 'ER4', 'ERC-SR11', 'ERC-SR8', 'ERC-SR9CAM', 'ES1', 'ESE-Lab', 'ESE-LAB4', 'EXEC-SR', 'GIS', 'i3-0337', 'i3-Aud', 'LSLAB2', 'LT10', 'LT12', 'LT15', 'LT18', 'LT19', 'LT2', 'LT20', 'LT21', 'LT26', 'LT5', 'LT8', 'LT9', 'MD4-03SR', 'MD6-0101A', 'MD6-0201D', 'MD6-0202A', 'MLounge', 'MMSR2-1', 'MMSR2-3', 'NAK-AUD', 'NGS-MPR', 'NUR-S4A', 'RS', 'S14-0620', 'S16-0307', 'S16-03ALR', 'S16-0430', 'S16-0903', 'S17-0405', 'S17-0406', 'S17-0611', 'S1A-0217', 'S4-0103', 'S4-04Lab', 'S4-0516', 'S4A-02Lab', 'S4A-0308', 'S5-0224', 'SDE-DV3', 'SPSLab', 'SR@LT19', 'SR1', 'SR10', 'SR12', 'SR13', 'SR15', 'SR3', 'SR5', 'SR5-2', 'SR5-5', 'SR7']
    """
    #open file
    f = open(filename,"r")
    incsv = f.readlines()
    #removing affixes
    incsv[:] = [i.rstrip('\n') for i in incsv]
    #lines into lists
    tempstr = ""
    templist = []
    for j in range(len(incsv)):
        #enters each line into temporary string variable
        tempstr = incsv[j]
        #enters the split string into a temporary list variable
        templist.append(tempstr.split(","))
        #modify original line in original list with split list
        incsv[j] = templist
        #reset temporary variables
        tempstr = ""
        templist = []
    #lists all venues
    venuelist = []
    for k in range(len(incsv)):
        venuelist.append(incsv[k][0][7])
    #filter all unique venues by checking whether venue is already in filterlist
    filterlist = []
    #check is temporary variable to decide whether to add venue
    check = True
    #for all venues in venuelist
    for l in range(len(venuelist)):
        #if venue in venuelist already in filterlist
        if venuelist[l] in filterlist:
            #decision to add venue is false
            check = False
        #if decision is to add the venue in venuelist
        if check == True:
            #append new venue to filterlist
            filterlist.append(venuelist[l])
        #reset decision to true
        check = True
    #finding all available venues
    #for all lines in the timetable
    for m in range(1,len(incsv)):
        #if the start time of the venue is in between the desired start time or the end time of the venue is in between the desired end time
        if ((int(incsv[m][0][5]) >= start and int(incsv[m][0][5]) < end) or (int(incsv[m][0][6]) > start and int(incsv[m][0][6]) <= end)) and int(incsv[m][0][3]) == 4:
            #if the venue is still in list of venues (filterlist)
            if incsv[m][0][7] in filterlist:
                #remove venue from filterlist
                filterlist.remove(incsv[m][0][7])
    #remove header "venue" from filterlist
    filterlist.remove("Venue")
    return filterlist

#test cases for part b

def assert_available_venues():
    assert available_venues("timetable2.csv",1000,2200,4) == ['CAPT-SR4', 'CAPT-SR6', 'CEProj', 'CMS', 'COM1-0208', 'COM1-0212', 'COM1-0217', 'COM1-B111', 'COM1-B113', 'DV1', 'E1-06-01', 'E1-06-11', 'CELC-SR2A', 'COM1-0203', 'COM2-0108', 'CR4-1', 'DV2', 'E-LAB', 'E1-06-07', 'CAPT-DV', 'COFM-LAB', 'CR1', 'CAPT-SR2', 'COM1-B102', 'COM1-B112', 'CR3-4', 'CR4-2', 'DV', 'E1-06-05', 'E2-03-03', 'CELC-SR1A']
    assert available_venues("timetable1.csv",800,2200,1) == ['AS1-0201', 'AS1-0210', 'AS1-0302', 'AS1-0303', 'AS1-0304', 'AS1-0548', 'AS2-0312', 'AS2-0413', 'AS2-0510', 'AS3-0212', 'AS3-0214', 'AS3-0308', 'AS3-0523', 'AS4-0110', 'AS4-0114', 'AS4-0117', 'AS4-0118', 'AS4-0119', 'AS4-0335', 'AS4-B109', 'AS4-B110', 'AS5-0205', 'AS5-0309', 'AS6-0214', 'AS6-0333', 'AS6-0425', 'AS7-0102', 'AS7-0214', 'AS7-0302', 'AS7-0411', 'BIZ-0118', 'BIZ1-0201', 'BIZ1-0202', 'BIZ1-0203', 'BIZ1-0205', 'BIZ1-0206', 'BIZ1-0301', 'BIZ1-0302', 'BIZ1-0303', 'BIZ1-0304', 'BIZ2-0224', 'BIZ2-0228', 'BIZ2-0229', 'BIZ2-0301', 'BIZ2-0302', 'BIZ2-0413B', 'BIZ2-0420', 'BIZ2-0422', 'BIZ2-0509', 'BIZ2-0510', 'CAPT-DV', 'CAPT-SR2', 'CAPT-SR4', 'CAPT-SR6', 'CELC-SR1A', 'CELC-SR2A', 'CEProj', 'CMS', 'COFM-LAB', 'COM1-0203', 'COM1-0208', 'COM1-0212', 'COM1-0217', 'COM1-B102', 'COM1-B111', 'COM1-B112', 'COM1-B113', 'COM2-0108', 'CR1', 'CR2-1', 'CR3-4', 'CR3-6', 'CR4-2', 'DV', 'DV1', 'DV2', 'E-LAB', 'E1-06-01', 'E1-06-05', 'E1-06-07', 'E1-06-11', 'E2-03-03', 'E3-0301ESP', 'E3-0519ESP', 'E3-06-01', 'E3-06-07', 'E3-06-10', 'E4-02-01', 'E4-04-02', 'E4-04-03', 'E4-04-07', 'E5-03-22', 'E5-03-23', 'EA-02-11', 'EA-06-02', 'EA-06-05', 'ELC-T8', 'ENG-AUD', 'ER2', 'ER3', 'ER4', 'ERC-SR11', 'ERC-SR8', 'ERC-SR9CAM', 'ES1', 'ESE-Lab', 'ESE-LAB4', 'EXEC-SR', 'GIS', 'i3-0337', 'i3-Aud', 'LSLAB2', 'LT10', 'LT12', 'LT15', 'LT18', 'LT19', 'LT2', 'LT20', 'LT21', 'LT26', 'LT5', 'LT8', 'LT9', 'MD4-03SR', 'MD6-0101A', 'MD6-0201D', 'MD6-0202A', 'MLounge', 'MMSR2-1', 'MMSR2-3', 'NAK-AUD', 'NGS-MPR', 'NUR-S4A', 'RS', 'S14-0620', 'S16-0307', 'S16-03ALR', 'S16-0430', 'S16-0903', 'S17-0405', 'S17-0406', 'S17-0611', 'S1A-0217', 'S4-0103', 'S4-04Lab', 'S4-0516', 'S4A-02Lab', 'S4A-0308', 'S5-0224', 'SDE-DV3', 'SPSLab', 'SR@LT19', 'SR1', 'SR10', 'SR12', 'SR13', 'SR15', 'SR3', 'SR5', 'SR5-2', 'SR5-5', 'SR7']

#part c

def venue_occupancy(filename):
    """venue_occupancy(filename) returns the value of the average venue occupancy for all the venues.

    To use venue_occupancy, enter the filename in between the parentheses. The function should return a number that tells you the average venue occupancy in the timetable file.
    For example:
    
    >>> venue_occupancy("timetable1.csv")
    0.14354005167958656

    >>> venue_occupancy("timetable2.csv")
    0.12550860719874804

    >>> venue_occupancy("timetable3.csv")
    0.14330917874396135
    """
    #open file
    f = open(filename,"r")
    incsv = f.readlines()
    #removing affixes
    incsv[:] = [i.rstrip('\n') for i in incsv]
    #lines into lists
    tempstr = ""
    templist = []
    for j in range(len(incsv)):
        #enters each line into temporary string variable
        tempstr = incsv[j]
        #enters the split string into a temporary list variable
        templist.append(tempstr.split(","))
        #modify original line in original list with split list
        incsv[j] = templist
        #reset temporary variables
        tempstr = ""
        templist = []
    #all venues
    venuelist = []
    for k in range(1,len(incsv)):
        venuelist.append(incsv[k][0][7])
    #filter all unique venues by checking whether venue is already in filterlist
    filterlist = []
    #check is temporary variable to decide whether to add venue
    check = True
    #for all venues in venuelist
    for l in range(len(venuelist)):
        #if venue in venuelist already in filterlist
        if venuelist[l] in filterlist:
            #decision to add venue is false
            check = False
        #if decision is to add the venue in venuelist
        if check == True:
            #append new venue to filterlist
            filterlist.append(venuelist[l])
        #reset decision to true
        check = True
    #add hours to total count (time)
    time = 0
    #for all lines in file
    for m in range(1,len(incsv)):
        #if time of venue falls within office hours for weekdays
        if int(incsv[m][0][5]) >= 800 and int(incsv[m][0][5]) <= 1700 and int(incsv[m][0][6]) <= 1700 and int(incsv[m][0][6]) >= 800 and int(incsv[m][0][3]) >= 1 and int(incsv[m][0][3]) <= 5:
            #add hour to total count
            time += (int(incsv[m][0][6]) - int(incsv[m][0][5]))
        #if start time falls before office hours but end time is within office hours
        elif int(incsv[m][0][5]) < 800 and int(incsv[m][0][6]) <= 1700 and int(incsv[m][0][5]) > 800 and int(incsv[m][0][3]) >= 1 and int(incsv[m][0][3]) <= 5:
            #ignore hours before 800 and add remaining hours
            time += (int(incsv[m][0][6]) - 800)
        #if end time falls after office hours but start time is within office housr
        elif int(incsv[m][0][5]) >= 800 and int(incsv[m][0][5]) < 1700 and int(incsv[m][0][6]) > 1700 and int(incsv[m][0][3]) >= 1 and int(incsv[m][0][3]) <= 5:
            #ignore hours after 1700 and add remaining hours
            time += (1700 - int(incsv[m][0][5]))
        #if start time falls before 800 and end time falls after 1700
        elif int(incsv[m][0][5]) < 800 and int(incsv[m][0][6]) > 1700 and int(incsv[m][0][3]) >= 1 and int(incsv[m][0][3]) <= 5:
            #add the maximum of 9 hours
            time += 900
        #if time range falls outside of office hours
        elif ((int(incsv[m][0][5]) < 800 and int(incsv[m][0][6]) <= 800) or (int(incsv[m][0][5]) >= 1700 and int(incsv[m][0][6]) > 1700)) and int(incsv[m][0][3]) >= 1 and int(incsv[m][0][3]) <= 5:
            #total hours remain
            time = time
    #average (avr)
    avr = 0
    #average = total hours / (number of unique venues) * 45 hours
    avr = (time/(len(filterlist)*4500))
    return avr

#test cases for part c

def assert_venue_occupancy():
    assert venue_occupancy("timetable1.csv") == 0.14354005167958656
    assert venue_occupancy("timetable2.csv") == 0.12550860719874804
    assert venue_occupancy("timetable3.csv") == 0.14330917874396135

#part d

def available_timing(filename,day,venue):
    """available_timing(filename,day,venue) returns a list of available timings for a certain venue in a certain day.

    To use available_timing, enter the filename as the first argument, followed by an integer day code and finally the venue. The function should return a list with a range of available timings in round brackets.
    For example:
    
    >>> available_timing("timetable2.csv",5,"CR1")
    [(600, 1200), (1800, 2400)]
    
    >>> available_timing("timetable2.csv",3,"CR1")
    [(600,1400),(1800,2400)]

    >>> available_timing("timetable2.csv",1,"CR1")
    [(600,2400)]

    >>> available_timing("timetable1.csv",1,"AS1-0201")
    [(600, 800), (1000, 1200), (1500, 1900), (2100, 2400)]
    """
    #reading the file
    f = open(filename,"r")
    incsv = f.readlines()
    #removing affixes
    incsv[:] = [i.rstrip('\n') for i in incsv]
    #lines into lists
    tempstr = ""
    templist = []
    for j in range(len(incsv)):
        #enters each line into temporary string variable
        tempstr = incsv[j]
        #enters the split string into a temporary list variable
        templist.append(tempstr.split(","))
        #modify original line in original list with split list
        incsv[j] = templist
        #reset temporary variables
        tempstr = ""
        templist = []
    #finding occupied hours
    brlist = []
    #for all lines in file
    for k in range(len(incsv)):
        #if venue in line matches desired venue and day in line matches desired day
        if incsv[k][0][7] == venue and int(incsv[k][0][3]) == day:
            #add time range of line into brlist
            brlist.append([int(incsv[k][0][5]),int(incsv[k][0][6])])
    #pruning
    #tlist stands for timelist. stores remaining hours for synthesis
    tlist = []
    #list of hours
    tlist = [600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400]
    #for line in brlist
    for l in range(len(brlist)):
        #for the range of hours of the line
        for m in range(int((brlist[l][1]-brlist[l][0])/100)):
            #if hours in range still in tlist
            if (brlist[l][0] + m*100) in tlist:
                #remove from tlist
                tlist.remove(brlist[l][0] + m*100)
    #plist for partition list. range of available timings appended here
    plist = []
    #check is for the start time of each available time ranges
    check = 0
    #formation of time ranges
    #for hours in tlist
    for n in range(len(tlist)):
        #if code is checking element 2. Could have used range(1,len(tlist)) but nevermind
        if n >= 1:
            #if 2 adjacent hours are not consecutive
            if tlist[n] != (tlist[n-1]+100):
                #add time range to plist
                plist.append((tlist[check],tlist[n-1]+100))
                #set check to next minimum available start time
                check = n
            #adding range with last hour
            #if last hour in tlist is 2400 and precedent hour in tlist is 2300
            if tlist[n] == 2400 and tlist[n-1] == 2300:
                #add time range
                plist.append((tlist[check],2400))
    return plist

#test cases for part d

def assert_available_timings():
    assert available_timing("timetable2.csv",5,"CR1") == [(600, 1200), (1800, 2400)]
    assert available_timing("timetable2.csv",3,"CR1") == [(600,1400),(1800,2400)]
    assert available_timing("timetable2.csv",1,"CR1") == [(600,2400)]
    assert available_timing("timetable1.csv",1,"AS1-0201") == [(600, 800), (1000, 1200), (1500, 1900), (2100, 2400)]

#part e
#for part e, there are some functions that may not be used by normal people but may be checked or modified by other programmers, hence documentation is given for these functions but these functions are not listed in the introduction

from turtle import *

def ttint(timelist,venue):
    """ttint(timelist,venue) takes a timelist list from pp_schedule and draws in python turtle graphics as a readable table. Venue is the string to be printed at the bottom of the screen denoting the venue that is concerned."""
    #setup
    showturtle()
    #make python turtle graphics window 1260 pixels wide and 800 pixels tall
    setup(width = 1260, height = 800, startx = None, starty = None)
    reset()
    #text at top
    pen(pencolor="black")
    pu()
    setpos(0,380)
    write("Welcome to your schedule. Use the arrow keys to toggle the day of the week",move=False,align="center",font=("Courier New",10,"normal"))
    setpos(0,360)
    write("In Idle, type 'quit()' to exit turtle.",move=False,align="center",font=("Courier New",10,"normal"))
    dayl = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    setpos(0,-350)
    #writes venue at bottom of GUI
    write(venue,move=False,align="center",font=("Courier New",20,"normal"))
    #drawing the lines and timing
    #baseY = 300 because y = 300 is the height of the line for monday
    baseY = 300
    for ch in range(7):
        pu()
        #goes to relevant y position for respective day code
        setpos(-570,(baseY-(100*ch)))
        #writes day name at side
        write(dayl[ch],move=False,align="center",font=("Courier New",20,"normal"))
        pen(pencolor="black",pensize="3")
        #draws lines
        #for each hour
        for dh in range(19):
            #move right 60 steps
            setx(xcor()+60)
            pd()
            #move up 20 steps
            sety(ycor()+20)
            pu()
            #stop drawing. move up 10 steps and write hour
            sety(ycor()+10)
            write(str((600+(dh*100))),move=False,align="center",font=("Courier New",10,"normal"))
            #go back down 30 steps to main line
            sety(ycor()-30)
            #continue drawing
            pd()
    pu()
    #goes to each relevant timing to write module code
    #for every time range in timelist. dp stands for day parse
    for dp in range(len(timelist)):
        #if week day in timelist is not empty
        if len(timelist[dp]) >= 1:
            #for each timing in the week day. hp stands for hour parse
            for hp in range(1,len(timelist[dp])):
                #for each hour in the time range. pr is an arbitrary variable which helps to direct the turtle to the timings in between the start and end time to write the module code at the relevant location
                for pr in range(int((timelist[dp][hp][1]-timelist[dp][hp][0])/100)):
                    #go to the relevant time and write the module code in between
                    setpos((-840+(int(timelist[dp][hp][0]/100)+pr)*60),(410-timelist[dp][0]*100))
                    write(timelist[dp][hp][2],move=False,align="center",font=("Courier New",8,"normal"))
    

def quit():
    """commanding quit() quits from python turtle graphics."""
    #quits from python turtle graphics screen
    bye()

def vergangenheit():
    #little easter egg
    reset()
    write("Of course, as a developer, I must add easter eggs somewhere. If you want to return to your schedule, type in the 'pp_schedule' command again.",move=False,align="center",font=("Courier New",9,"normal"))

#pp_schedule to make a list to give to ttint to make a table

def pp_schedule(filename,venue):
    """pp_schedule(filename,venue) opens up a python turtle graphics window which shows what times of each of the seven days of the week is occupied by which module in which venue.

    To use pp_schedule, enter a filename as the first element and a venue as the second element. pp_schedule commands ttint(timelist,venue) to create a table in python turtles graphics using a timelist created by pp_schedule.

    When pp_schedule is run, a list with day codes, start times, end times and modules is created. It is neither returned nor printed, but if the code is modified to show the table, the following outputs are expected to be seen.
    For example:

    >>> pp_schedule("timetable1.csv","AS1-0201")
    Your timetable is being printed on Python Turtle Graphics. This may take a while.
    [[1, [800, 1000, 'LAC3201'], [1200, 1500, 'NM4204'], [1900, 2100, 'ECA5333']], [2, [1200, 1300, 'EC4372']], [3, [1800, 2000, 'LAK2201']], [4], [5], [6], [7]]
    
    >>> pp_schedule("timetable2.csv","CR1")
    Your timetable is being printed on Python Turtle Graphics. This may take a while.
    [[1], [2], [3, [1400, 1800, 'LA5301']], [4], [5, [1200, 1400, 'PF2401'], [1400, 1600, 'AR5421'], [1600, 1700, 'AR2223'], [1700, 1800, 'AR2223']], [6], [7]]

    If an error occurs, input the code again. It should work.

    *A note to developers*
    This function does not have assert test cases as the table is printed on a separate module window.
    """
    #reading the file
    f = open(filename,"r")
    incsv = f.readlines()
    #removing affixes
    incsv[:] = [i.rstrip('\n') for i in incsv]
    #lines into lists
    tempstr = ""
    templist = []
    for j in range(len(incsv)):
        #enters each line into temporary string variable
        tempstr = incsv[j]
        #enters the split string into a temporary list variable
        templist.append(tempstr.split(","))
        #modify original line in original list with split list
        incsv[j] = templist
        #reset temporary variables
        tempstr = ""
        templist = []
    #timelist stands for timetable list
    #format of timelist: [[day,[start,end,module],...],...]
    timelist = []
    for k in range(1,8):
        #for each day code add day code
        timelist.append([k])
    #assign and make list for ttint
    #for all lines in file
    for l in range(len(incsv)):
        #if venue in line matches desired venue
        if incsv[l][0][7] == venue:
            #after each day code, add a list with start time, end time and module. Repeat for each relevant line
            timelist[(int(incsv[l][0][3])-1)].append([int(incsv[l][0][5]),int(incsv[l][0][6]),incsv[l][0][0]])
    #turtle
    print("Your timetable is being printed on Python Turtle Graphics. This may take a while.")
    ttint(timelist,venue)


#module test

if __name__ == "__main__":
    """If this current source file is run directly as the main program, perform the tests."""
    print(total_venues("timetable1.csv"))
    print(total_venues("timetable2.csv"))
    print(available_venues("timetable2.csv",1000,2200,4))
    print(len(available_venues("timetable2.csv",1000,2200,4)))
    print(venue_occupancy("timetable1.csv"))
    print(venue_occupancy("timetable2.csv"))
    print(available_timing("timetable2.csv",5,"CR1"))
    print(available_timing("timetable2.csv",3,"CR1"))
    print(available_timing("timetable2.csv",1,"CR1"))
    pp_schedule("timetable2.csv","CR1")
    #All test cases from Building Maintenance.doc
