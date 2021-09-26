from PyInquirer import prompt
import func

questions = [
    {
        "type": "list",
        "name": "user_option",
        "message": "Choose a command",
        "choices": ["Set Master Password", "Add Password", "Read Password", "Delete Password", "Generate Password"] 
    },

]

answers = prompt(questions) #style=custom_style_2)
promptCon = answers.get("user_option")

if promptCon == "Set Master Password":
    func.setMasPass()

elif promptCon == "Add Password":
    func.savepassMAS()

elif promptCon == "Read Password":
    func.readpassMAS()

elif promptCon == "Delete Password"
    func.deletepassMAS()

elif promptCon == "Generate Password":
    func.generatePassword()
