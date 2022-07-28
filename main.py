import PySimpleGUI as sg
from uuid_retriever import get_uuid
import json

sg.theme('Default1')

layout = [
    [sg.Text(text='Enter comma-separated list of usernames:', text_color='black')],
    [sg.Input(key='input', do_not_clear=True)],
    [sg.Button(button_text='OK')]
]

window = sg.Window(title='MC Whitelister', layout=layout)

while True:   
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'OK' and values['input']: # only execute if text box is not empty
        input = values['input'] # store the user's input

        usernames = input.split(',') # create list of usernames from input
        usernames = set(usernames) # remove duplicates by converting to set

        whitelist = [] # the actual content of whitelist.json
        failed_names = []

        for username in usernames:
            try:
                uuid = get_uuid(username)
            except KeyError:
                failed_names.append(username)
            else:
                # this is the format minecraft is expecting for whitelist.json
                user = {
                    "uuid": uuid,
                    "name": username
                }
                whitelist.append(user)

        with open('whitelist.json', 'w') as f:
            json.dump(whitelist, f, indent=2)

        if whitelist:
            sg.popup(f'Successfully created whitelist.json for {len(whitelist)} users.', title='Success')

        if failed_names:
            string_display = ''

            for name in failed_names:
                if name != failed_names[-1]:
                    string_display += f'"{name}"\n' # display each failed username by line
                else:
                    string_display += f'"{name}"'   # no line break for the last username

            sg.popup(f"The following usernames were skipped due to being invalid or due to an issue with the API:\n\n{string_display}", title='Failed Usernames')

window.close()