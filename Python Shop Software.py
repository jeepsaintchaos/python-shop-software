import os
from pathlib import Path
path_to_file='config.ini'
path = Path(path_to_file)
import configparser
config = configparser.ConfigParser()
import datetime
from datetime import datetime
from datetime import date
import sys
configsec='section_a'
today = date.today()
now = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
oldstdout = sys.stdout
readme='readme.txt'
VN="1.0.0"


def createreadme():
    if os.path.exists(readme)!=True:
        print('Readme file is being created. Please read it for help.')
        with open(readme, 'w') as f:
            sys.stdout = f
            print('Welcome to Python Shop Software! This program was created by u/Jeepsaintchaos.')
            print('Copyright 2022. All rights reserved.')
            print('This software is designed to take info and write out an invoice for work done on a vehicle.')
            print('The default username is Tech, and the password is password.')
            print('I suggest using the model name and date started as the project name, as the project name determines the name of the output file.')
            print('The output filename will also show the date and time the invoice was created.')
            print('The output file will not show the project name when printed.')
            print('You can change the username, its the same as Technician name in settings. You can also change the password.')
            print('Parts upcharge should be entered as a decimal if you change it. 10% is .10')
            print('Just delete the "config.ini" file to return to stock settings, the program will make a new one for you.')
            print('Outputs are stored in the "Projects" folder.')
            print('This program will call you names if you do something wrong. Sorry/notsorry')
            print('I do not warranty this program against gaining sentience and attempting to take over the world')
            print('Actually I dont warranty this program for anything, really. Use at your own risk.')
            print('For best results, place this program in a folder on the desktop.')       
            print('Please dont put letters where numbers are supposed to go, and dont use symbols like $ or %.')
            print('I am not a very good programmer, and this is the first thing I have ever written.')
            print('If you have any issues with it, please figure it out. I do not care.')
            print('I havent figured out how to set up automatic updates yet, as i didnt really plan on releasing this. But it has been requested.')
            print('This is version', VN)    
            print('Have a great day!')
            f.close
            sys.stdout=oldstdout




def getcustinfo():
    global cstnme
    global cstph
    global projyear
    global projmdl
    global projmake
    global projvin
    print('Please enter customer name.')
    cstnme = input()
    print('Please enter customer phone number')
    cstph = input()
    print('Please enter year of vehicle')
    projyear= input()
    print('Please enter make of vehicle')
    projmake= input()
    print('please enter model of vehicle')
    projmdl = input()
    print('Please enter VIN of vehicle')
    projvin = input()
    print('Customer Name is', cstnme)
    print('Customer Phone number is', str(cstph))
    print('Customers vehicle is a', projyear, projmake, projmdl)
    print('The VIN is ', str(projvin))
    print('Is this information correct? y/n.')
    cstinfo = input()
    if cstinfo == 'y':
            ptf()
    elif cstinfo != 'y':
            getcustinfo()
            




def ptf():
    if ((Path.cwd() / 'projects').exists()):
        print('Projects folder found.')
        print('File name is', PNEX)
        os.chdir("projects")
        with open(PNEX, 'w') as f:
            sys.stdout = f
            print('Todays date is', +today)
            print('This is an invoice of work done from ' +CN)
            print('The vehicle presented to us was a', projyear, projmake, projmdl)
            print('With a VIN of', str(projvin))
            print("After customer complaint of " +MI)
            print("We have determined that the " +MI)
            print("Was caused by " +Diag)
            print("To fix this, we " +Repair)
            print('Your technician today was ' +x)
            if partsused!='none' or '':
                print('Parts used today included ' +partsused)
            print("Parts for this repair comes to $",str(totalpartscost))
            print('Labor rate per hour is $', shoprate)
            print('Diagnostics took', diaghours ,'hours.')
            print('Repair took ', laborhours , 'hours.')
            print('Labor, including diagnostics, comes to $', str(+timecost))
            print("The subtotal is $", str((timecost)+(totalpartscost)),", plus Tax of %", str(Taxpercent))
            print("The total is $", round(float((timecost+totalpartscost+((timecost+totalpartscost)*(float(Taxpercent))))),2))
            print("Thank you for choosing", CN ,"for all of your repair needs.")
            print('Please sign here____________________')
            print('Customer Information:')
            print('Name:')
            print(cstnme)
            print('Phone Number:')
            print(cstph)
    
                
            sys.stdout=oldstdout
            os.chdir('..')
            print('File creation finished.')
            print('Attempting to print...')
            #do printy things here
        f.close
    elif ((Path.cwd() / 'projects').exists())==False:
        os.mkdir("projects")
        ptf()
        
             
    


def readconfig():
    global discount
    global CN
    global Taxpercent
    global shoprate
    global x
    global partsuc
    global pw
    createreadme()
    if os.path.exists(path_to_file)==True:
        config.read_file(open(path_to_file))
        if config.has_section('section_a')==True:
            config.read(path_to_file)
            x = config.get('section_a', 'x')
            CN = config.get('section_a', 'CN')
            pw= config.get('section_a', 'pw')
            discount = config.getfloat('section_a', 'discount')
            Taxpercent = config.getfloat('section_a', 'Taxpercent')
            shoprate = config.getfloat('section_a', 'shoprate')
            partsuc = config.getfloat('section_a', 'partsuc')
            print('Configuration File Loaded!')
            login()
        elif config.has_section('section_a')==False:
            print('Configuration File Damaged, resetting to stock settings.')
            os.remove(path_to_file)
            makeconfig()
    elif os.path.exists(path_to_file)==False:
        makeconfig()


def asksettings():
    print("Welcome "+x)
    print("Access Granted")
    print('Current settings are:')
    print('Company name is ' +CN)
    print('Sales tax is set to %', str(Taxpercent))
    print('Shop rate per hour is $', str(shoprate))
    print('Parts Upcharge is set to %', str((float(partsuc*100))))
    print('Technician Name is ' +x)
    print('Password can be changed.')
    print('Would you like to change any of these settings? y/n')
    changesettings=input()
    if changesettings=="y":
        settings()
    elif changesettings=="n":
        main()
    elif changesettings!=("y" or "n"):
        print('Response not valid.')
        print('Current settings are:')
        print('Company name is ' +CN)
        print('Sales tax is set to %', str(Taxpercent))
        print('Shop rate per hour is $', str(shoprate))
        print('Parts Upcharge is set to ', str(partsuc))
        print('Technician Name is ' +x)
        print('Password can be changed.')
        print('Password for', x, ' can also be changed.')
        print('Would you like to change any of these settings? Press y/n, please.')
    changesettings=input()
    if changesettings=="y":
        settings()
    elif changesettings=="n":
        main()
    elif changesettings!=("y" or "n"):
        print('Response not valid, you were supposed to type y or n')
        asksettings()

        
def main():
    global PN
    global MI
    global totalpartscost
    global totalcost
    global timecost
    global Diag
    global Repair
    global PNEX
    global laborhours
    global diaghours
    global partsused
    PN=input( "Please enter project name, enter 'quit' to close program.")
    if PN=="quit":
            quit()
    if PN!="quit":
            pass
    print("Please type the customer complaint with "+PN)
    MI = input()
    print("Please type diagnosis of " +MI)
    Diag = input()
    print("Please type what you did to fix " +MI)
    Repair = input()
    print('What parts did you use to complete this repair?')
    partsused=input()
    print("How many hours did diagnosis take?")
    diaghours = input()
    print("How many hours did repair take?")
    laborhours = input()
    totalhours= float(laborhours) + float(diaghours)
    timecost= round(float(totalhours)*float(shoprate),2)
    print("Please enter shop cost of parts.")
    partscost =input()
    totalpartscost = ((float(partsuc)*float(partscost))+float(partscost))
    print("Would you like to add a discount? y/n")
    discountanswer=input()
    if discountanswer=="y":
            discount()
    elif discountanswer=="n":
            discount=float("0")
    else:
        print('Input not valid')
        print('Enter y to add a discount. Enter n to deny discount.')
        discountanswer=input()
    if discountanswer=="y":
            discount()
    elif discountanswer=="n":
            discount=float("0")
    else:
        print('Input not valid')
        print('Enter y to add a discount. Enter n to deny discount.')
        discountanswer=input()
    if discountanswer=="y":
            discount()
    elif discountanswer=="n":
            discount=float("0")
    else:
        print('Input not valid for the third fucking time.')
        print('You are stupid. Restarting program.')
        login()
    print("After customer complaint of " +MI)
    print('On your ' +PN)
    print("We have determined that " +MI)
    print("Was caused by " +Diag)
    print("Repairs consisted of " +Repair)
    print('Your technician today was ' +x)
    print('We replaced ' +partsused)
    print("Parts for this repair comes to $",str(totalpartscost))
    print('Labor, including diagnostics, comes to $', str(+timecost))
    print("The subtotal is $", str((timecost)+(totalpartscost)),", plus Tax of %", str(Taxpercent))
    print("The total is $", round(float((timecost+totalpartscost+((timecost+totalpartscost)*(float(Taxpercent))))),2))
    print("Thank you for choosing", CN ,"for all of your repair needs")
    PNEX = PN+(now)+('.txt')
    print('Does this look good? y/n')
    startnew=input()
    if startnew=="y":
        getcustinfo()
    elif startnew=="n":
        asksettings()
    else:
        print('You were asked for a y/n answer, but you failed to provide it.')
        print('In the future, you need to be more careful about your answers.')
        print("After customer complaint of " +MI)
        print('On your ' +PN)
        print("We have determined that " +MI)
        print("Was caused by " +Diag)
        print("Repairs consisted of " +Repair)
        print('Your technician today was ' +x)
        print('We replaced ' +partsused)
        print("Parts for this repair comes to $",str(totalpartscost))
        print('Labor, including diagnostics, comes to $', str(+timecost))
        print("The subtotal is $", str((timecost)+(totalpartscost)),", plus Tax of %", str(Taxpercent))
        print("The total is $", round(float((timecost+totalpartscost+((timecost+totalpartscost)*(float(Taxpercent))))),2))
        print("Thank you for choosing", CN ,"for all of your repair needs")
        PNEX = PN+(now)+('.txt')
        print('Does this look good? y/n')
        startnew=input()
        if startnew=="y":
            getcustinfo()
        elif startnew=="n":
            asksettings()
        elif startnew!='y'or'n':
            print('WARNING:INPUT FAILURE! Your ignorance has been noted. Restarting program.')
            readconfig()
               
        readconfig()
    print('A file has been created on the desktop and the print command has been sent.')
    print('Would you like to start another project writeup? y/n')
    startnew=input()
    if startnew=="y":
        asksettings()
    elif startnew=="n":
        quit()
    else:
        print('You were asked for a y/n answer, but were too dumb to provide it.')
        quit()

    
def password():
    y="p"
    y=input("Enter Password:")
    if y==pw:
        asksettings()
    if y!=pw:
        print("Wrong Password, try again.")
        login()

def login():
 global x
 UN = input("Enter your name:")
 if UN==x:
  password()
 else:
  print("Access Denied")
  retrylogin()

  
def makeconfig():
    global x
    global CN
    global discount
    global Taxpercent
    global Shoprate
    global partsuc
    global pw
    if path.is_file()==True:
        readconfig()
    elif path.is_file()==False:
        print(f'The file {path_to_file} does not exist')
        f=open(path_to_file, 'w')
        f.close
        print('Config File Created, writing stock configuration. Please set settings!')
    if config.has_section("section_a")==True:
        config.set('section_a', 'x', 'Tech')
        config.set('section_a', 'CN', 'Generic Auto Repair Shop')
        config.set('section_a', 'discount', '0')
        config.set('section_a', 'Taxpercent', '.08')
        config.set('section_a', 'shoprate', '100')
        config.set('section_a', 'partsuc', '.10')
        config.set('section_a', 'pw', 'password')
        with open(path_to_file, 'w') as configfile:
             config.write(configfile)
        readconfig()
    elif config.has_section("section_a")==False:
        config.add_section('section_a')
        config.set('section_a', 'x', 'Tech')
        config.set('section_a', 'CN', 'Generic Auto Repair Shop')
        config.set('section_a', 'discount', '0')
        config.set('section_a', 'Taxpercent', '.08')
        config.set('section_a', 'shoprate', '100')
        config.set('section_a', 'partsuc', '.10')
        config.set('section_a', 'pw', 'password')
        with open(path_to_file, 'w') as configfile:
             config.write(configfile)
        readconfig()
    
  
def discount():
    global discount
    print('Please confirm, would you like to add a discount to this transaction? Enter y for yes, n for no.')
    discountyn=input()
    if discountyn=="n":
          return(0)
    elif discount=="y":
        print("Please enter discount percentage.")
        discount= float(input())
        return discount
    else:
        discount()


def retrylogin():
    print("Restarting")
    login()

def password():
    y="p"
    y=input("Enter Password:")
    if y==pw:
        asksettings()
    if y!=pw:
        print("Wrong Password, try again.")
        login()
        
def settings():
    global CN
    global Taxpercent
    global shoprate
    global x
    global partsuc
    global pw
    print('What setting would you like to change today?')
    print('press 1 to change Company Name, currently ', str(CN))
    print('press 2 to change Sales Tax, currently %', str(Taxpercent))
    print('press 3 to change Hourly Shop rate, currently $', str(shoprate))
    print('press 4 to change Technician Name, currently ', str(x))
    print('press 5 to change Upcharge for Parts, currently', str(partsuc))
    print('press p to change password')
    print('press 6 to leave settings alone and return to program.')
    sn=input()
    if sn=="1":
        print('Please Enter New Company Name:')
        CN = input()
        print('Company Name is now set to:' +CN)
        print('Returning to main program.')
        updatesettings()
        asksettings()
    elif sn=="2":
        print('Please enter new sales tax percentage')
        Taxpercent = input()
        print('Sales Tax is now set to:' +Taxpercent)
        print('Returning to main program.')
        updatesettings()
    elif sn=="3":
        print('Please enter new hourly shop rate:')
        shoprate = input()
        print('Shop Rate per hour is now set to:' +shoprate)
        print('Returning to main program.')
        updatesettings()
    elif sn=="4":
        print('Please enter name of new Technician')
        x = input()
        print('Technician Name is now set to:' +x)
        print('Returning to main program.')
        updatesettings()
    elif sn=="5":
        print('Please enter upcharge for parts as a decimal.')
        print('Example: 15% upcharge would be .15')
        partsuc = input()
        print('Parts Upcharge is now set to:', str(partsuc))
        print('Returning to main program.')
        updatesettings()
    elif sn=="p":
        print('Please enter old password.')
        oldp=input()
        if oldp==pw:
            print
            print('Please Enter new Password:')
            pw = input()
            print('Password is now set to:' +pw)
            print('Returning to main program.')
            updatesettings()
            asksettings()
        elif oldp!=pw:
            readconfig()
    elif sn=="6":
        print('Change Settings Menu Cancelled, no changes have been made.')
        print('Returning to main program')
        asksettings()
    else:
        settings()

        
def updatesettings():
    print('Rewriting Configuration file, please wait.')
    f=open(path_to_file, 'w')
    f.close
    if config.has_section('section_a')==True:
        config.set('section_a', 'x', x)
        config.set('section_a', 'CN', CN)
        config.set('section_a', 'discount', str(discount))
        config.set('section_a', 'Taxpercent', str(Taxpercent))
        config.set('section_a', 'shoprate', str(shoprate))
        config.set('section_a', 'partsuc', str(partsuc))
        config.set('section_a', 'pw', str(pw))
    
    elif config.has_section('section_a')!=True:
        config.add_section('section_a')
        updatesettings()
    with open(path_to_file, 'w') as configfile:
         config.write(configfile)
    print('Configuration updated, returning to main program.')
    f.close
    asksettings()


readconfig()
