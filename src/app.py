from pyreact import useEffect, useRef, render, react_component
from pyreact import Form, Label, Input, Div, Button


@react_component
def App():
    nameRef = useRef()
    mailRef = useRef()

    print(nameRef)

    def handleSubmit(event):
        event.preventDefault()
        print(nameRef['current']['value'])
        print(mailRef['current']['value'])

    useEffect(lambda: print(nameRef), [])

    return Div({'className': 'app'},
               Form({'onSubmit': handleSubmit},
                    Label({'htmlFor': 'name'}, "Name"),
                    Input({'id': 'name', 'type': 'text', 'ref': nameRef}),

                    Label({'htmlFor': 'email'}, "Email"),
                    Input({'id': 'email', 'type': 'text', 'ref': mailRef}),

                    Button(None, "Submit"),
                    )
               )


render(App, None, 'root')
