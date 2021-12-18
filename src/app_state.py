from pyreact import useState, render, react_component
from pyreact import Form, Label, Input, Div, Button


@react_component
def App():
    userName, setUserName = useState("")
    email, setEmail = useState("")

    def handleNameUpdate(event):
        event.preventDefault()
        value = event['target']['value']
        setUserName(value)

    def handleEmailUpdate(event):
        event.preventDefault()
        value = event['target']['value']
        setEmail(value)

    def handleSubmit(event):
        event.preventDefault()
        print(userName)
        print(email)

    return Div({'className': 'app'},
               Form({'onSubmit': handleSubmit},
                    Label({'htmlFor': 'name'}, "Name"),
                    Input({'id': 'name',
                           'type': 'text',
                           'onChange': handleNameUpdate,
                           'value': userName}
                          ),

                    Label({'htmlFor': 'email'}, "Email"),
                    Input({'id': 'email',
                           'type': 'text',
                           'onChange': handleEmailUpdate,
                           'value': email}
                          ),

                    Button(None, "Submit"),
                    )
               )


render(App, None, 'root')
