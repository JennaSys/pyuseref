from pyreact import useEffect, useRef, render, react_component
from pyreact import Form, Label, Input, Div, Button


@react_component
def App():
    name_ref = useRef()
    mail_ref = useRef()

    print(name_ref)

    def handleSubmit(event):
        event.preventDefault()
        print(name_ref['current']['value'])
        print(mail_ref['current']['value'])

    useEffect(lambda: print(name_ref), [])

    return Div({'className': 'app'},
               Form({'onSubmit': handleSubmit},
                    Label({'htmlFor': 'name'}, "Name"),
                    Input({'id': 'name', 'type': 'text', 'ref': name_ref}),

                    Label({'htmlFor': 'email'}, "Email"),
                    Input({'id': 'email', 'type': 'text', 'ref': mail_ref}),

                    Button(None, "Submit"),
                    )
               )


render(App, None, 'root')
