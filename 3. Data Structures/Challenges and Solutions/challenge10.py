#create dictionary with Hello in each language
translator = {"French":"Bonjour",
              "Spanish":"Hola",
              "Italian":"Ciao",
              "German": "Guten Tag",
              "Indian": "Namaste"
              }

language_selection = input("Select a language: ")

print(translator.get(language_selection))
