from pyreact import useEffect, useRef, render, react_component
from pyreact import Form, Label, Input, Div, Button, Br


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
                    Label({'htmlFor': 'name'}, "Name"), Br(None),
                    Input({'ref': nameRef, 'type': 'text', 'id': 'name'}),
                    Br(None), Br(None),
                    Label({'htmlFor': 'email'}, "Email"), Br(None),
                    Input({'ref': mailRef, 'type': 'text', 'id': 'email'}),
                    Br(None), Br(None),
                    Button(None, "Submit"),
                    )
               )


render(App, None, 'root')
