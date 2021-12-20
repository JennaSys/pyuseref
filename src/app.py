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
                    Input({'ref': nameRef, 'type': 'text', 'id': 'name'}),

                    Label({'htmlFor': 'email'}, "Email"),
                    Input({'ref': mailRef, 'type': 'text', 'id': 'email'}),

                    Button(None, "Submit"),
                    )
               )


render(App, None, 'root')
