import spacy
import json
import os


class AdvancedChatBot:
    def __init__(self):
        self.details = {}
        self.users = self.load_users()  # Load users from a file
        self.user_details = self.load_user_details()  # Load user details from a file
        self.nlp = spacy.load('en_core_web_sm')

    def load_users(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r') as file:
                return json.load(file)
        return {}

    def save_users(self):
        with open('users.json', 'w') as file:
            json.dump(self.users, file, indent=4)  # Added indent for better readability

    def load_user_details(self):
        if os.path.exists('user_details.json'):
            with open('user_details.json', 'r') as file:
                return json.load(file)
        return {}

    def save_user_details(self):
        with open('user_details.json', 'w') as file:
            json.dump(self.user_details, file, indent=4)  # Added indent for better readability

    def register_user(self):
        print("Register a new user:")
        username = input("Enter a username: ")
        if username in self.users:
            print("Username already exists. Please choose a different one.")
            return

        password = input("Enter a password: ")
        self.users[username] = password
        self.save_users()
        print("Registration successful!")

    def login(self):
        print("Login:")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if self.users.get(username) == password:
            print("Login successful!")
            self.details = self.user_details.get(username, {})
            return username
        else:
            print("Invalid credentials. Please try again.")
            return None

    def set_details(self):
        print("Please enter your details:")
        self.details['name'] = input("Name: ")
        self.details['age'] = input("Age: ")
        self.details['city'] = input("City: ")
        self.details['email'] = input("Email address: ")
        self.details['contact_number'] = input("Contact number: ")

        # Family details
        self.details['mother_name'] = input("Mother's name: ")
        self.details['father_name'] = input("Father's name: ")
        self.details['siblings'] = input("Do you have siblings? If yes, list them (comma-separated): ")

        # Education details
        self.details['school'] = input("School: ")
        self.details['college'] = input("College: ")

        # Save or update details
        username = input("Enter your username to save these details: ")
        self.user_details[username] = self.details
        self.save_user_details()

    def edit_details(self):
        print("Which detail would you like to update?")
        for key in self.details:
            print(f"{key}: {self.details[key]}")

        detail_to_edit = input(
            "Enter the detail you want to edit (e.g., 'name', 'age', 'city', etc.): ").strip().lower()

        if detail_to_edit in self.details:
            new_value = input(f"Enter the new value for {detail_to_edit}: ")
            self.details[detail_to_edit] = new_value
            print(f"{detail_to_edit.capitalize()} updated successfully!")

            # Save the updated details
            username = input("Enter your username to save these updated details: ")
            if username in self.user_details:
                self.user_details[username] = self.details
                self.save_user_details()
        else:
            print("Invalid detail. Please choose from the list.")

    def greet(self):
        print(f"Hello {self.details.get('name', 'User')}! How can I assist you today?")

    def respond(self, query):
        query = query.lower()
        doc = self.nlp(query)

        if 'name' in query:
            print(f"Hello Boss {self.details.get('name', 'User')}.")
            print(f"Your name is {self.details.get('name', 'not set')}.")
        elif 'age' in query:
            print(f"You are {self.details.get('age', 'not set')} years old.")
        elif 'city' in query:
            print(f"You live in {self.details.get('city', 'not set')}.")
        elif 'email' in query:
            print(f"Your email address is {self.details.get('email', 'not set')}.")
        elif 'contact' in query or 'number' in query:
            print(f"Your contact number is {self.details.get('contact_number', 'not set')}.")
        elif 'mother' in query:
            print(f"Your mother's name is {self.details.get('mother_name', 'not set')}.")
        elif 'father' in query:
            print(f"Your father's name is {self.details.get('father_name', 'not set')}.")
        elif 'siblings' in query or 'sibling' in query:
            print(f"Your siblings are: {self.details.get('siblings', 'not set')}.")
        elif 'school' in query:
            print(f"You attended {self.details.get('school', 'not set')}.")
        elif 'college' in query:
            print(f"You attended {self.details.get('college', 'not set')}.")
        else:
            # Using spaCy for entity recognition to improve understanding
            entities = [ent.text for ent in doc.ents]
            if entities:
                print(f"I recognized the following entities in your query: {', '.join(entities)}.")
            else:
                print(
                    "I don't understand that question. Please ask about your name, age, city, email, contact number, "
                    "family details, or education details.")

    def reset_password(self):
        print("Reset Password:")
        username = input("Enter your username: ")
        if username not in self.users:
            print("Username not found.")
            return

        # Verify identity
        if username in self.user_details:
            self.details = self.user_details[username]
        else:
            print("No details found for this user.")
            return

        print("To reset your password, please verify your identity.")
        verification_choice = input(
            "Would you like to verify using email or contact number? (email/contact): ").strip().lower()

        if verification_choice == 'email':
            verification_info = input("Enter your registered email address: ")
            if self.details.get('email') != verification_info:
                print("Verification failed. Email address does not match.")
                return
        elif verification_choice == 'contact':
            verification_info = input("Enter your registered contact number: ")
            if self.details.get('contact_number') != verification_info:
                print("Verification failed. Contact number does not match.")
                return
        else:
            print("Invalid verification method. Please choose 'email' or 'contact'.")
            return

        new_password = input("Enter your new password: ")
        self.users[username] = new_password
        self.save_users()
        print("Password reset successful!")


class BotFacade:
    def __init__(self):
        self.bot = AdvancedChatBot()

    def display_title(self):
        title = r"""
  ____            _            _       
 |  _ \ __ _  ___| | ___  _ __(_)_ __  
 | |_) / _` |/ __| |/ _ \| '__| | '_ \ 
 |  _ < (_| | (__| | (_) | |  | | | | |
 |_| \_\__,_|\___|_|\___/|_|  |_|_| |_|
        """
        print(title)
        print("Welcome to the Personal Bot!")

    def run(self):
        self.display_title()

        while True:
            choice = input(
                "Would you like to register, login, reset password, or exit? (register/login/reset/exit): ").lower()
            if choice == 'register':
                self.bot.register_user()
            elif choice == 'login':
                username = self.bot.login()
                if username:
                    if not self.bot.details:
                        self.bot.set_details()
                    self.bot.greet()
                    while True:
                        user_input = input("\nAsk me something or type 'edit' to update details: ")
                        if user_input.lower() in ['exit', 'quit']:
                            print("Goodbye!")
                            break
                        elif user_input.lower() == 'edit':
                            self.bot.edit_details()
                        else:
                            self.bot.respond(user_input)
            elif choice == 'reset':
                self.bot.reset_password()
            elif choice == 'exit':
                print("Exiting the chatbot. Goodbye!")
                break
            else:
                print("Invalid option. Please choose 'register', 'login', 'reset', or 'exit'.")


if __name__ == "__main__":
    facade = BotFacade()
    facade.run()
