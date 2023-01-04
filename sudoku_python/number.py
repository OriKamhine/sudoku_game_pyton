class Number:
    def __init__(self, value):
        self.is_taken = value > 0  #When the Number is initially created, it is given a value. If it is 0, the user can
        # replace the number, and this boolean checks if that is possible.
        self.value = value  #The number's value

    def replace(self, new_value):
        if not self.is_taken:  #If the user can replace the value
            self.value = new_value  #Replaces the value

