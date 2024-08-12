class DetailedChatBot:
    def __init__(self):
        self.details = {}

    def set_details(self):
        self.details['name'] = input("Please enter your name: ")
        self.details['age'] = input("Please enter your age: ")
        self.details['city'] = input("Please enter your city: ")
        self.details['email'] = input("Please enter your email address: ")
        self.details['contact_number'] = input("Please enter your contact number: ")
        self.details['family_members'] = input("Please enter the names of your family members (comma-separated): ")

    def greet(self):
        print(f"Hello {self.details['name']}! How can I assist you today?")

    def respond(self, query):
        query = query.lower()
        if 'name' in query:
            print(f"My name is {self.details['name']}.")
        elif 'age' in query:
            print(f"You are {self.details['age']} years old.")
        elif 'city' in query:
            print(f"You live in {self.details['city']}.")
        elif 'email' in query:
            print(f"Your email address is {self.details['email']}.")
        elif 'contact' in query or 'number' in query:
            print(f"Your contact number is {self.details['contact_number']}.")
        elif 'family' in query:
            print(f"Your family members are: {self.details['family_members']}.")
        else:
            print("I don't understand that question. Please ask about your name, age, city, email, contact number, or family.")

def main():
    bot = DetailedChatBot()
    bot.set_details()
    bot.greet()

    while True:
        user_input = input("\nAsk me something: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        bot.respond(user_input)

if __name__ == "__main__":
    main()
