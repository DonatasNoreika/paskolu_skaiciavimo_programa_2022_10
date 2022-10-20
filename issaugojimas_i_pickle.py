import pickle

def gauti_paskolas():
    try:
        with open("paskolos.pkl", 'rb') as file:
            paskolos = pickle.load(file)
    except:
        paskolos = []
    return paskolos

def irasyti_paskolas(paskolos):
    with open("paskolos.pkl", 'wb') as file:
        pickle.dump(paskolos, file)