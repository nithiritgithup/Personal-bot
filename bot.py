class SimpleChatBot:
    def __init__(self):
        self.name = ""
        self.details = {}

    def set_details(self):
        self.name = input("Please enter your name: ")
        self.details['age'] = input("Please enter your age: ")
        self.details['city'] = input("Please enter your city: ")

    def greet(self):
        print(f"Hello {self.name}! How can I assist you today?")

    def respond(self, query):
        if 'name' in query.lower():
            print(f"My name is {self.name}.")
        elif 'age' in query.lower():
            print(f"You are {self.details['age']} years old.")
        elif 'city' in query.lower():
            print(f"You live in {self.details['city']}.")
        else:
            print("I don't understand that question. Please ask about your name, age, or city.")

def main():
    bot = SimpleChatBot()
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
