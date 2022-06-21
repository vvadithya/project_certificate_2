# importing the eel library  
import eel  
import calendar
from fpdf import FPDF 
import datetime
import string
import random
# initializing the application  
eel.init("web")  
# import time

# Today's date,this is used for the date of issue of the card
today = datetime.datetime.now()
# The Characters to be used for making the code number of the card
characters = string.ascii_uppercase + string.digits
# list of nationalities(197 countries in this list)
# list of genders
genders_list = ["Male" , "Female"]

  
def resident_write_pdf(name , address , nation , date_of_birth , image , gender):
                pdf = FPDF(orientation = 'L' , format = 'Legal')
                pdf.add_page()
                pdf.set_font("Arial", 'BU' , 40)                
                title = "Royal Oman Police"
                pdf.cell(200, 15, txt = title, ln = 1, align = 'L') 
                pdf.set_font("Arial", size=14)               
                name = "Name: " + str(name)
                pdf.cell(200, 15, txt = name, ln = 2, align = 'L') 
                address = "Address: " + str(address)
                pdf.cell(200, 15, txt = address, ln = 3, align = 'L')
                gender = "Gender: " + str(gender)
                pdf.cell(200, 15, txt =gender , ln=4 , align = 'L')            
                date_of_issue = "Date of Card Issue: " + str(today.day) + " "  + str(calendar.month_name[today.month]) + " " + str(today.year + 2)
                date_of_expiry = "Date of Card Expiry: " + str(today.day) + " "  + str(calendar.month_name[today.month]) + " " + str(today.year + 2)
                pdf.cell(200, 15, txt = date_of_expiry , ln=7 , align = 'L')
                nationality = "Nationality: " + str(nation)
                pdf.cell(200, 15, txt = nationality , ln=8 , align = 'L')
                code = []
                for i in range(int(17)):
                    value = random.choice(characters)
                    
                    code.append(str(value))                 
                code = "ID Code: " + "".join(code)
                pdf.cell(200, 15, txt = code , ln=9 , align = 'L')
                pdf.image(image , 250 , 50 , w=120)
                pdf.image("web/qrcode.png" , 280 , 150 , w=60)
                pdf.set_font("Arial", size=16)                  
                pdf.cell(200, 15, txt = "Verify this card by scanning the QR Code" , ln=14 , align = 'C')                
                pdf.output("Resident.pdf")    
      
# using the eel.expose command  
@eel.expose
def send_data(name , address , nation , date_of_birth , image , gender):
    name = name
    address = address
    nation = nation
    image = image
    gender = gender
    resident_write_pdf(name , address , nation , date_of_birth , image , gender)
# starting the application  
eel.start("resident_card.html" ,size = (800,800))  