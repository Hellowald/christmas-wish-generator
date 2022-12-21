import time;
import calendar;
CurrentTime=time.asctime()
CurrentCalender=calendar.month(2022, 12)
print("This is the current calendar of this month.\n"+CurrentCalender)
print("Your current date and time is, "+CurrentTime)
ChristmassTicks=6686465487.520668
ticks=time.time()
#print("Number of ticks that has happened since January 1, 1970 12:00 are,",ticks)
if (ticks<ChristmassTicks):
    print("You are few days away from Christmass eve celebration.\n")
    #Getting user credentials.
    WisherName = input("Please enter your name so as to proceed. \n")
    while(len(WisherName)<3 or WisherName.isspace()):
        WisherName=input("Please key in a valid user name not short forms. \n")
    else:
        print("Hello there, ",WisherName.capitalize(),".")
    #Getting credentials of the wished person.
    WishedName=input("Please enter the name of the person you would like to wish happy Christmas.\n")
    while (len(WishedName) < 3 or WishedName.isspace()):
        WishedName = input("Please key in a valid User name not short forms. \n")
    else:
        print(WisherName.capitalize(),"You have decided to wish, ",WishedName.capitalize(),"a merry christmas.")
        WishMessage=input("Please enter your wish message for, "+WishedName.capitalize()+"\n")
        while(WishMessage.rfind("christmas")==-1):
            WishMessage=input("Key in a message with a christmas wish.\n")
        else:
            print(WishMessage,WishedName.capitalize())

elif(ticks>ChristmassTicks):
    print("You date is past Christmass Date.\n"
          "This game is only valid before 2022 Christmass celebration.\n")
else:
    print("You did not follow the game rules.")




