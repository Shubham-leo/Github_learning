from gliner import GLiNER
from collections import defaultdict
#model = GLiNER.from_pretrained("urchade/gliner_base")

# Custom cleaning of result (Spacy + Custom Cleaning)
def clean_result(result):

    """
    This function takes the output from the spacy model and cleans repetition of
    ORG names.

    args: Result from spacy model - extract_org_frequency_spacy, ( Dictionary )
    
    returns: Cleaned result without repeated ORG names. ( Dictionary )

    Example:
        article = "An article about technology companies such as Google, and Google's Success."
        result = extract_org_frequency(article)
        print(result)
        Output: [{'entity': 'Google', 'frequency': 1}, {'entity': 'Google's Success', 'frequency': 1}]

        result = clean_result(result)
        print(result)
        Output: [{'entity': 'Google', 'frequency': 2}]
    
    """

    result = sorted(result, key=lambda x: x['frequency'], reverse=True)

    custom = set()
    master = result.copy()

    for id, i in enumerate(result):
        contestant = i["entity"]
        contestant_freq = i["frequency"]

        for ii in result:
            compi = ii["entity"]
            compi_freq = ii["frequency"]

            if contestant != compi and contestant in compi:
                # print(f"Contestant: {contestant, contestant_freq} is INSIDE {compi, compi_freq}")
                if contestant_freq > compi_freq or contestant_freq == compi_freq:
                    master[id]["frequency"] += 1
                    custom.add(compi)

    clean = []
    for i in result:
        if i['entity'] not in custom:
            clean.append(i)

    # print(clean)
    return clean


def extract_org_gliner(article):
  labels = ["organisation"]

  entities = model.predict_entities(article, labels)

  entity_frequency = defaultdict(int)
  for entity in entities:
      entity_text = entity['text']
      entity_frequency[entity_text] += 1

  result = [{'entity': entity_text, 'frequency': frequency} for entity_text, frequency in entity_frequency.items()]
  lst = []
  for item in result:
      lst.append(item)
  return lst

def extract_org_frequency(article,nlp):
    """
    Extracts organizations (ORG entities) from the given article and returns their frequency.

    Args:
        article (str): The input article to extract organizations from.

    Returns:
        list: A list of dictionaries, each containing the 'entity' (organization) and 'frequency' keys.

    Example:
        article = "An article about technology companies such as Google, Apple, and Microsoft."
        result = extract_org_frequency(article)
        print(result)
        Output: [{'entity': 'Google', 'frequency': 1}, {'entity': 'Apple', 'frequency': 1},
                 {'entity': 'Microsoft', 'frequency': 1}]
    """
    try:
      result = extract_org_gliner(article)
      print("Orgs extracted using gliner")
    except Exception as e:
      print("Error extracting orgs using gliner:", e)
      doc = nlp(article)
      org_frequency = {}

      for entity in doc.ents:
          if entity.label_ == 'ORG':
              org = entity.text
              org_frequency[org] = org_frequency.get(org, 0) + 1

      result = [{'entity': org, 'frequency': freq} for org, freq in org_frequency.items()]
      print(type(result))
      # Applying custom function to clean the result
      result = clean_result(result)
      print("Orgs extracted using NLP")

    return result


import time
def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Function "{func.__name__}" elapsed time: {(end - start) * 1000:.3f}ms')
        return result
    return wrapper

import spacy
from fastcoref import spacy_component
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("fastcoref")
arti = "CrowdStrike and Tata Consultancy Services (TCS) today announced a strategic partnership to power TCS' extended managed detection and response (XMDR) services with the AI-native CrowdStrike Falcon XDR platform. Through this partnership, TCS will unlock the unified protection of the Falcon platform encompassing cloud security and next-gen SIEM, delivering AI-powered SOC transformation that stops breaches. As the velocity and sophistication of today’s cyberattacks continue to increase, organisations need outcome-based security protection focused on stopping breaches. With cloud intrusions growing 75% in the past year, breakout times now measured in minutes, and the growing cybersecurity skills gap, managed security solutions serve as the force multiplier customers need to protect their critical assets and securely drive digital transformation initiatives. The powerful combination of TCS’s worldwide team of expert practitioners with the ubiquitous Falcon platform’s CrowdStrike Falcon Cloud Security and CrowdStrike Falcon Next-Gen SIEM provides customers with the protection they need to stop breaches. “TCS has been partnering with enterprises across the globe for over 20 years to protect their businesses. As the attack surface evolves, enterprises must secure their digital core with robust cybersecurity to grow and innovate,” said Ganesa Subramanian Vaikuntam, vice president and Global Head, Cybersecurity Business Group, TCS. “Our partnership with CrowdStrike bolsters our capabilities to offer stronger cyber defense to our customers and protect them from modern, sophisticated cyber threats.” “The Falcon platform has set the global standard, becoming cybersecurity’s AI platform of choice for businesses and their trusted delivery partners. This partnership brings CrowdStrike closer to customers, empowering TCS’s large, global footprint to modernise, innovate and standardiae on the Falcon platform,” said Daniel Bernard, chief business officer, CrowdStrike. “Stopping the breach, consolidating point products and driving down costs – CrowdStrike’s collaboration with TCS exemplifies our partner-first approach to platform success, delivering the very best outcomes for customers with the partners they trust to design, deploy, and operate their cybersecurity programs.”"
print(extract_org_frequency(arti,nlp))