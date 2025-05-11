# Google ke Generative AI module ko import kar rahe hain
import google.generativeai as genai

# NLPModel class banayi gayi hai jo AI model ko configure karegi
class NLPModel:

    # AI model ko hasil karne ka method
    def get_model(self):
        # Google API key define ki gayi hai
        GOOGLE_API_KEY = "AIzaSyA6_skJD8xkXN5wCMgwTIcDzkQRdyKQVUg"
        try:
            # Google generative AI ko configure kar rahe hain
            genai.configure(api_key=GOOGLE_API_KEY)
            # Gemini model ka ek instance bana rahe hain
            model = genai.GenerativeModel("gemini-1.5-flash")
            return model  # Model return kar rahe hain
        except Exception as e:
            # Agar koi error aaye to use print kar dena
            print(e)

# NLPApp class, NLPModel class se inherit kar rahi hai
class NLPApp(NLPModel):

    # Constructor method jab class ka object banega
    def _init_(self):
        self.__database = {}  # Users ka data rakhne ke liye ek dictionary
        self.first_menu()     # Sab se pehle user se input lene ke liye menu show karte hain

    # First menu method: login ya register ya exit
    def first_menu(self):
        first_input = input("""
        Hi! How would you like to proceed?

            1. Not a member? Register
            2. Already a member? Login
            3. Bhai galti se aa gaya kia? Exit
            """)
        
        if first_input == "1":
            # Agar user new hai to registration method call karein
            self.__register()

        elif first_input == "2":
            # Agar user pehle se register hai to login method call karein
            self.__login()

        else:
            # Kisi aur option par program band ho jaye
            exit()

    # Dusra menu jahan NLP ke features diye gaye hain
    def second_menu(self):
        second_input = input("""
        Hi! How would you like to proceed?

        1. Sentiment Analysis
        2. Language Transilation
        3. Language Detection
        """)

        if second_input == '1':
            # Sentiment analysis method run karo
            self.__sentiment_analysis()

        elif second_input == '2':
            # Translation method run karo
            self.__language_transilation()

        elif second_input == '3':
            # Language detection method run karo
            self.__language_detection()

        else:
            # Invalid input par exit
            exit()

    # User ko register karne ka method
    def __register(self):
        name = input("Enter your Name: ")         # Naam input lo
        email = input("Enter your Email: ")       # Email input lo
        password = input("Enter your Password: ") # Password input lo

        if email in self.__database:
            # Agar email pehle se mojood hai
            print("Email already exists.")
        
        else:
            # Naya user dictionary mein add karo
            self.__database[email] = [name, password]
            print("Registration successful. Now you can login!")
            self.first_menu()  # Dobara first menu par jao

    # Login method
    def __login(self):
        email = input("Enter your Email: ")       # Email input lo
        password = input("Enter your Password: ") # Password input lo

        if email in self.__database:
            # Agar email mojood hai
            if self.__database[email][1] == password:
                # Agar password match kare
                print("Login Successfull")
                self.second_menu()  # Dusra menu dikhao

            else:
                # Agar password ghalat ho
                print("Incorrect Password")
                self.__login()  # Dobara login karne do

        else:
            # Agar email database mein nahi hai
            print("Email not found. Please register first.")
            self.first_menu()  # Dobara pehla menu dikhao

    # Sentiment analysis ka method
    def __sentiment_analysis(self):
        user_text = input("Enter your text: ")  # User se text lo
        model = super().get_model()             # Model hasil karo
        response = model.generate_content(f"Give me the sentiment of this sentence: {user_text}")  # AI se sentiment analysis karwao
        results = response.text                 # AI ka response hasil karo
        print(results)                          # Result show karo
        self.second_menu()                      # Dubara dusra menu dikhao

    # Translation ka method
    def __language_transilation(self):
        user_text = input("Enter your text: ")  # User se text lo
        model = super().get_model()             # Model hasil karo
        response = model.generate_content(f"Give me urdu transilation of this sentence: {user_text}")  # Hindi translation lo
        results = response.text                 # Response hasil karo
        print(results)                          # Result print karo
        self.second_menu()                      # Dubara dusra menu dikhao

    # Language detection ka method
    def __language_detection(self):
        user_text = input("Enter your text: ")  # User se text lo
        model = super().get_model()             # Model hasil karo
        response = model.generate_content(f"Detect the language of this sentence: {user_text}")  # AI se language detect karwao
        results = response.text                 # Result hasil karo
        print(results)                          # Result print karo
        self.second_menu()                      # Dubara dusra menu dikhao

# Program ka entry point
if __name__ == '__main__':
    nlp = NLPApp()  # NLPApp class ka object banao aur program chalao