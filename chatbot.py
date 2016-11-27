import nlp
import xml.etree.ElementTree as ET

knowledge = []

#Cargamos los conceptos desde el archivo xml

tree = ET.parse('knowledge.xml')
concepts = tree.getroot()
for concept in concepts:
    stimuli = []
    for stimulus in concept.find("stimuli"):
        stimuli.append(stimulus.text)
    response = concept.find("response").text
    knowledge.append( {"stimuli": stimuli, "response": response} ) # dic


def concept_similarity(concept, user_msg):
    return max([nlp.cosine_sim(user_msg, stimulus) for stimulus in concept["stimuli"]])


def get_best_response(knowledge, user_msg):
    return max(knowledge, key=lambda c: concept_similarity(c, user_msg))["response"]


while True:
    user_msg = input("> ")
    print(get_best_response(knowledge, user_msg))


