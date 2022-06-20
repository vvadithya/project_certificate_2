# importing the eel library  
import eel  
# initializing the application  
eel.init("web")  
  
# using the eel.expose command  
@eel.expose
def test(name , address , nation , date_of_birth , image , gender , output_path):
    print(name)
    print(address)
    print(nation)
  
# starting the application  
eel.start("resident_card.html" ,size = (800,800))  