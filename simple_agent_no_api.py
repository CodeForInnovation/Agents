class SimpleAgent:
    def __init__(self, name):
        self.name = name

    def respond(self, message):
        return f"{self.name} received: {message}"

    def perform_action(self, action):
        if action == "greet":
            return f"Hello, I'm {self.name}!"
        elif action == "ask_name":
            return f"My name is {self.name}."
        else:
            return "Action not recognized."