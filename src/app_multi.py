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
                    Input({'ref': addInputs, 'type': 'text', 'id': 'name'}),

                    Label({'htmlFor': 'email'}, "Email"),
                    Input({'ref': addInputs, 'type': 'text', 'id': 'email'}),

                    Button(None, "Submit"),
                    )
               )


render(App, None, 'root')
