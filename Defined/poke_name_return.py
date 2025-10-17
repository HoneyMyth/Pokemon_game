from Defined.poke_input_name import FnPoke_input

def FnPoke_name(jasonfile):
    forms = jasonfile["forms"]
    forms = forms[0]
    return forms["name"]
