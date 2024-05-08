import torch
from gliner import GLiNER
def loading_DistilBert_base():
    print(f"Loading the DistilBert base model for summerization")
    # Setting up the device for Event Classification computation
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    EVENT_CLASSIFICATION_MODEL_PATH = 'gliner_model.pt'
    # Load the saved model state dictionary
    try: 
        x = torch.load(EVENT_CLASSIFICATION_MODEL_PATH)
        config = x["config"]
        loaded_model = GLiNER(config)
        loaded_model.load_state_dict(x["model_weights"])
        

    except Exception as e:
        print("Using cpu",e)
    
    return loaded_model

x = loading_DistilBert_base()

text = """
Libretto by Marius Petipa, based on the 1822 novella ``Trilby, ou Le Lutin d'Argail`` by Charles Nodier, first presented by the Ballet of the Moscow Imperial Bolshoi Theatre on January 25/February 6 (Julian/Gregorian calendar dates), 1870, in Moscow with Polina Karpakova as Trilby and Ludiia Geiten as Miranda and restaged by Petipa for the Imperial Ballet at the Imperial Bolshoi Kamenny Theatre on January 17–29, 1871 in St. Petersburg with Adèle Grantzow as Trilby and Lev Ivanov as Count Leopold.
"""

labels = ["person", "book", "location", "date", "actor", "character"]

entities = x.predict_entities(text, labels, threshold=0.4)

for entity in entities:
    print(entity["text"], "=>", entity["label"])
