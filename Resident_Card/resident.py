# importing the eel library  
import eel  
import calendar
from fpdf import FPDF 
import datetime
import string
import random
from os import chdir
# initializing the application  
eel.init("web")  
# import time
nation_list = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean']

# Today's date,this is used for the date of issue of the card
today = datetime.datetime.now()
# The Characters to be used for making the code number of the card
characters = string.ascii_uppercase + string.digits
# list of nationalities(197 countries in this list)
# list of genders
genders_list = ["Male" , "Female"]
errors = 0
errors_list = []
def close(x,port):
    if x > 0:
        exit()
def check_data(name , address , nation , date_of_birth , image , gender):
    global errors , errors_list
    if date_of_birth == "":
        errors = errors + 1
        errors_list.append("Empty date of birth!")    
    if name == "":
        errors_list.append("You have entered an empty name!")
        errors = errors + 1
    if address == "":
        errors_list.append("You have entered an empty address!")
        errors = errors + 1
    if nation == "Choose" or nation not in nation_list:
        errors = errors + 1
        errors_list.append("You have to choose a country from the options given!")                
    if image == "":
        errors = errors + 1
        errors_list.append("Enter the path of the .jpg image!")
    if gender == "Choose" or gender not in genders_list:
        errors = errors + 1
        errors_list.append("You have to choose a gender from the options given!")

        
def resident_write_pdf(name , address , nation , date_of_birth , image , gender):

                date_of_birth = list(date_of_birth)
                year = date_of_birth[0:4]
                year = "".join(year)
                month = date_of_birth[5:7]
                month = list(month)
                if 0 in month:
                    month.remove(0)
                month = "".join(month)                  
                month = str(calendar.month_name[today.month])
                day = date_of_birth[8:10]
                day = "".join(day)
                date_of_birth = str(day) + " " + str(month) + " " + str(year)
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
                date_of_birth = "Date of Birth: " + str(date_of_birth)
                pdf.cell(200, 15, txt = date_of_birth , ln=5 , align = 'L')
                date_of_issue = "Date of Card Issue: " + str(today.day) + " "  + str(calendar.month_name[today.month]) + " " + str(today.year)                
                pdf.cell(200, 15, txt = date_of_issue , ln=6 , align = 'L')                
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
                pdf.image(image , 280 , 50 , w=60)
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
    date_of_birth = date_of_birth
    check_data(name , address , nation , date_of_birth , image , gender)
    if errors == 0:
        resident_write_pdf(name , address , nation , date_of_birth , image , gender)
        eel.start("success.html" , port = 8002)
    if errors > 0:
        print(address)
        file = open('errors.txt' , 'w')
        data = "No. Of Errors: " + str(len(errors_list)) + "\n"                    
        file.write(data)
        for a in errors_list:
            data = a + "\n"
            file.write(data)
        file.close()            
        eel.start("error.html" , mode = 'chrome' , port = 8001)

 

            


        
# starting the application  
eel.start("resident_card.html" ,size = (800,800) , port = 8000)  