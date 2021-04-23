
#create dictionary with Hello in each language
translator = {"French":"Bonjour",
              "Spanish":"Hola",
              "Italian":"Ciao",
              "German": "Guten Tag",
              "Indian": "Namaste"
              }

#if user enters a language in dictionary, translate the word. Otherwise, let them add it
#if user enters quit, exit program
while True:
    selection = input("Select your language? ").title()
    if selection == "Quit":
        break
    
    elif selection in translator:
        print(translator.get(selection))
    
    elif selection not in translator:
        print("Thats a new language. Lets add it")
        new_language = input(f"What does 'Hello' mean in {selection}: ")
        translator[selection] = new_language
        
        #alternative way of adding a language
        #translator.update({selection:new_language})
        
        


 
