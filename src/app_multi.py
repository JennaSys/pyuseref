from pyreact import useEffect, useRef, render, react_component
from pyreact import Form, Label, Input, Div, Button


@react_component
def App():
    inputs = useRef([])

    def addInputs(el):
        if el and el not in inputs['current']:
            inputs['current'].append(el)

    print(inputs)

    def handleSubmit(event):
        event.preventDefault()
        print([ref['value'] for ref in inputs['current']])

    useEffect(lambda: print(inputs), [])

    return Div({'className': 'app'},
               Form({'onSubmit': handleSubmit},
                    Label({'htmlFor': 'name'}, "Name"),
                    Input({'id': 'name', 'type': 'text', 'ref': addInputs}),

                    Label({'htmlFor': 'email'}, "Email"),
                    Input({'id': 'email', 'type': 'text', 'ref': addInputs}),

                    Button(None, "Submit"),
                    )
               )


render(App, None, 'root')
