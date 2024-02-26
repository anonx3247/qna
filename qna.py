def binary_question(question):
    while True:
        answer = input(f"{question} (y/n):")
        if answer.strip().lower() == "y":
            return True
        elif answer.strip().lower() == "n":
            return False

def text_input(question, validation=None, confirm=True):
    confirmed = False
    answer = ""
    while not confirmed:
        answer = input(question)
        if binary_question(f"You answered: {answer}\nConfirm?"):
            confirmed = True
            if validation is not None:
                is_valid, message = validation(answer)
                if is_valid:
                    return answer
                else:
                    print(message)
                    confirmed = False
        else:
            confirmed = False

            
    return answer

def list_input(question, options, validation=None, confirm=True):
    answer = ""
    available = ""
    for i in range(len(options)):
        available += f"{i+1}. {options[i]}\n"
    
    def valid(x):
        try:
            x = int(x)
            if 0 < x <= len(options):
                return True, ""
            else:
                return False, f"{x} is not a valid option"
        except:
            return False, f"{x} is not a valid option"
    answer = text_input(f"{question}\nAvailable options:\n{available}\nSelection:", validation=valid, confirm=confirm)
    return options[int(answer)-1]