
protest_template = {
    "who": ["Who is accused of a protest?","How many are accused of a protest?"],
    "where": ["Where a protest has taken place?"],
    "when": ["When is a protest?"],
    "organizer": ["Who leads/organizes a protest?"],
    "occupy": ["What space/building is taken over in a protest?"],
    "wounded": ["Who is injured/wounded in a protest?","How many are injured/wounded in a protest?"],
    "killed": ["Who is killed in a protest?","How many are killed in a protest?"],
    "arrested": ["Who is arrested in a protest?","How many are arrested in a protest?"],
    "imprisoned": ["Who is jailed/imprisoned in a protest?","How many are jailed/imprisoned in a protest?"],
    "protest-for": ["What is the aim of a protest?"],
    "protest-against": ["What a protest is meant to end?"],
    "outcome-occurred": ["What occurred because of a protest?"],
    "outcome-averted": ["What was averted/haven't occurred because of a protest?"],
    "outcome-hypothetical": ["What will potentially occur because of a protest?"]
}

corruption_template = {
    "who": ["Who is accused of a corruption?","How many are accused of a corruption?"],
    "where": ["Where a corruption has taken place?"], # not in the template
    "job": ["What is the role/title/job of someone?"],
    "charged-with": ["What is the crime that someone has been charged with?"],
    "judicial-actions": ["What is the investigation/trial/sentence that has taken place?"],
    "prison-term": ["How long does someone be prisoned/sentenced?"],
    "fine": ["How much is the punishment/seizures?"],
    "outcome-occurred": ["What occurred because of a corruption?"],
    "outcome-averted": ["What was averted/haven't occurred because of a corruption?"],
    "outcome-hypothetical": ["What will potentially occur because of a corruption?"]
}

terrorism_template = {
    # "named-perpetrator": "Whom a terrorist is attributed to?",
    "named-perp": ["Whom a terrorist is attributed to?"],
    # "named-organizer": "Whom the planning of a terrorist is attributed to?",
    "named-perp-org": ["Whom the planning of a terrorist is attributed to?"],
    "claimed-by": ["Who has claimed responsibility for the terrorist?"],
    "blamed-by": ["Who is asserting the identity of the perpetrators?"],
    "where": ["Where a terrorist has taken place?"],
    "when": ["When is a terrorist?"], #"How long is a terrorist last?"
    "target-physical": ["What was the facility/geo-political location being targeted by the terrorist?"],
    "target-human": ["who was the target of a terrorist?"],
    "wounded": ["Who is injured/wounded in a terrorist?","How many are injured/wounded in a terrorist?"],
    "killed": ["Who is killed in a terrorist?","How many are killed in a terrorist?"],
    "weapon": ["What was the weapon/instrument used to carry out a terrorist?"],
    "kidnapped": ["Who is kidnapped in a terrorist?","How many are kidnapped in a terrorist?"],
    # "perpetrator-captured": "Who/How many perpetrators of a terrorist was captured?",
    "perp-captured": ["Who is captured in a terrorist?", "How many perpetrators are captured in a terrorist?"],
    # "perpetrator-wounded": "Who/How many perpetrators was injured/wounded in the course of a terrorist?",
    "perp-wounded": ["Who is injured/wounded in a terrorist?", "How many perpetrators are injured/wounded in a terrorist?"],
    # "perpetrator-killed": "Who/How many perpetrators was killed in the course of a terrorist?",
    "perp-killed": ["Who is killed in a terrorist?", "How many perpetrators are killed in a terrorist?"],
    # "perpetrator-objective": "What was desired to have taken place by virtue of a terrorist?",
    "perp-objective": ["What was desired to have taken place by virtue of a terrorist?"],
    "outcome-occurred": ["What occurred/have actually taken place by virtue of a terrorist?"],
    "outcome-averted": ["What was averted/prevented by virtue of a terrorist?"],
    "outcome-hypothetical": ["What will potentially occur by virtue of a terrorist?"]
}

disease_outbreak_template = {
    "disease": ["What is at the heart of a disease outbreak?"],
    "where": ["Where a disease has occurred?"],
    # 下面这个之前没有注释掉所以test set里面多了两个，就一直沿用了
    # "non-pharmacologic-intervention-events": ["What is the intervention taken by authorities to prevent a further disease?"],
    "NPI-Events": ["What is the intervention taken by authorities to prevent a further disease?"],
    "infected-individuals": ["Who have become infected with the disease?"],
    # "infected-individual": "Who have become infected with the disease?",
    "infected-count": ["How many people have become newly infected?"],
    "infected-cumulative": ["How many people have become infected cumulatively?"],
    "killed-individuals": ["Who have become killed by the disease?"],
    # "killed-individual": "Who have become killed by the disease?",
    "killed-count": ["How many people have become newly infected?"],
    "killed-cumulative": ["How many people have become killed cumulatively?"],
    "exposed-individuals": ["Who have become exposed to the disease?"],
    # "exposed-individual": "Who have become exposed to the disease?",
    "exposed-count": ["How many people have become newly exposed?"],
    "exposed-cumulative": ["How many people have become exposed cumulatively?"],
    "tested-individuals": ["Who have become tested for the disease?"],
    # "tested-individual": "Who have become tested for the disease?",
    "tested-count": ["How many people have become newly tested?"],
    "tested-cumulative": ["How many people have become tested cumulatively?"],
    "vaccinated-individuals": ["Who have become vaccinated against the disease?"],
    # "vaccinated-individual": "Who have become vaccinated against the disease?",
    "vaccinated-count": ["How many people have become newly vaccinated?"],
    "vaccinated-cumulative": ["How many people have become vaccinated cumulatively?"],
    # "hospitalized-individuals": "Who have become hospitalized because of the disease?",
    "hospitalized-individual": ["Who have become hospitalized because of the disease?"],
    "hospitalized-count": ["How many people have become newly hospitalized?"],
    "hospitalized-cumulative": ["How many people have become hospitalized cumulatively?"],
    "recovered-individuals": ["Who have become recovered from the disease?"],
    # "recovered-individual": "Who have become recovered from the disease?",
    "recovered-count": ["How many people have become newly recovered?"],
    "recovered-cumulative": ["How many people have become recovered cumulatively?"]
}

templates={"Protestplate":protest_template,"Corruplate":corruption_template,
           "Terrorplate":terrorism_template,"Epidemiplate":disease_outbreak_template}

keys=[]
keys.extend(protest_template.keys())
keys.extend(corruption_template.keys())
keys.extend(terrorism_template.keys())
keys.extend(disease_outbreak_template.keys())
# print(template_keys)

template_keys={"Protestplate":protest_template.keys(),"Corruplate":corruption_template.keys(),
           "Terrorplate":terrorism_template.keys(),"Epidemiplate":disease_outbreak_template.keys()}

templates_question_to_key={temp_type:{q:key for key,questions in temp.items() for q in questions} for temp_type, temp in templates.items() }
# print(templates_question_to_key)
templates_question_to_type_and_key={q:(temp_type,key) for temp_type, temp in templates.items() for key,questions in temp.items() for q in questions}


protest_template_filler = {
    "who": "entity",
    "where": "entity",
    "when": "entity",
    "organizer": "entity",
    "occupy": "entity",
    "wounded": "entity",
    "killed": "entity",
    "arrested": "entity",
    "imprisoned": "entity",
    "protest-for": "event",
    "protest-against": "event",
    "outcome-occurred": "event",
    "outcome-averted": "event",
    "outcome-hypothetical": "event"
}

corruption_template_filler = {
    "who": "entity",
    "where": "entity", # not in the template
    "job": "entity",
    "charged-with": "event",
    "judicial-actions": "event",
    "prison-term": "entity",
    "fine": "entity",
    "outcome-occurred": "event",
    "outcome-averted": "event",
    "outcome-hypothetical": "event"
}

terrorism_template_filler = {
    # "named-perpetrator": "Whom a terrorist is attributed to?",
    "named-perp": "entity",
    # "named-organizer": "Whom the planning of a terrorist is attributed to?",
    "named-perp-org": "entity",
    "claimed-by": "entity",
    "blamed-by": "entity",
    "where": "entity",
    "when": "entity", #"How long is a terrorist last?"
    "target-physical": "entity",
    "target-human": "entity",
    "wounded": "entity",
    "killed": "entity",
    "weapon": "entity",
    "kidnapped": "entity",
    # "perpetrator-captured": "Who/How many perpetrators of a terrorist was captured?",
    "perp-captured": "entity",
    # "perpetrator-wounded": "Who/How many perpetrators was injured/wounded in the course of a terrorist?",
    "perp-wounded": "entity",
    # "perpetrator-killed": "Who/How many perpetrators was killed in the course of a terrorist?",
    "perp-killed": "entity",
    # "perpetrator-objective": "What was desired to have taken place by virtue of a terrorist?",
    "perp-objective": "event",
    "outcome-occurred": "event",
    "outcome-averted": "event",
    "outcome-hypothetical": "event"
}

disease_outbreak_template_filler = {
    "disease": "entity",
    "where": "entity",
    "non-pharmacologic-intervention-events": "entity",
    "NPI-Events": "event",
    "infected-individuals": "entity",
    # "infected-individual": "Who have become infected with the disease?",
    "infected-count": "entity",
    "infected-cumulative": "entity",
    "killed-individuals": "entity",
    # "killed-individual": "Who have become killed by the disease?",
    "killed-count": "entity",
    "killed-cumulative": "entity",
    "exposed-individuals": "entity",
    # "exposed-individual": "Who have become exposed to the disease?",
    "exposed-count": "entity",
    "exposed-cumulative": "entity",
    "tested-individuals": "entity",
    # "tested-individual": "Who have become tested for the disease?",
    "tested-count": "entity",
    "tested-cumulative": "entity",
    "vaccinated-individuals": "entity",
    # "vaccinated-individual": "Who have become vaccinated against the disease?",
    "vaccinated-count": "entity",
    "vaccinated-cumulative": "entity",
    # "hospitalized-individuals": "Who have become hospitalized because of the disease?",
    "hospitalized-individual": "entity",
    "hospitalized-count": "entity",
    "hospitalized-cumulative": "entity",
    "recovered-individuals": "entity",
    # "recovered-individual": "Who have become recovered from the disease?",
    "recovered-count": "entity",
    "recovered-cumulative": "entity"
}

templates_filler={"Protestplate":protest_template_filler,"Corruplate":corruption_template_filler,
           "Terrorplate":terrorism_template_filler,"Epidemiplate":disease_outbreak_template_filler}

templates_event={"Protestplate":"protest-event","Corruplate":"corrupt-event",
           "Terrorplate":"terror-event","Epidemiplate":"outbreak-event"}

templates_leave={"Protestplate":["over-time"],"Corruplate":["over-time"],
           "Terrorplate":["type","over-time","completion"],"Epidemiplate":[]}

no_answer_question=['Who is jailed/imprisoned in a protest?',
                    'How many are jailed/imprisoned in a protest?',
                    'Who is captured in a terrorist?',
                    'How many perpetrators are captured in a terrorist?',
                    'How many perpetrators are injured/wounded in a terrorist?',
                    'How many perpetrators are killed in a terrorist?',
                    'What was averted/prevented by virtue of a terrorist?',
                    'What will potentially occur by virtue of a terrorist?',
                    'How many people have become newly exposed?',
                    'How many people have become exposed cumulatively?',
                    'How many people have become newly tested?',
                    'How many people have become tested cumulatively?',
                    'Who have become vaccinated against the disease?',
                    'How many people have become newly vaccinated?',
                    'How many people have become vaccinated cumulatively?',
                    'How many people have become hospitalized cumulatively?',
                    'Who have become recovered from the disease?',
                    'How many people have become newly recovered?']

less_answer_question=['Who is injured/wounded in a protest?',
                      "What was averted/haven't occurred because of a protest?",
                      'Who have become exposed to the disease?',
                      'How many people have become recovered cumulatively?',
                      'Who is killed in a protest?',
                      'Who is injured/wounded in a terrorist?',
                      'How many are kidnapped in a terrorist?',
                      'What was desired to have taken place by virtue of a terrorist?',
                      'What occurred/have actually taken place by virtue of a terrorist?',
                      'Who have become hospitalized because of the disease?',
                      'Who has claimed responsibility for the terrorist?',
                      'Who is kidnapped in a terrorist?',
                      'How many people have become newly hospitalized?',
                      'What will potentially occur because of a protest?',
                      'who was the target of a terrorist?',
                      'Who is arrested in a protest?',
                      "What was averted/haven't occurred because of a corruption?",
                      'What will potentially occur because of a corruption?',
                      'What space/building is taken over in a protest?',
                      'How many are arrested in a protest?',
                      'Who is killed in a terrorist?',
                      'How much is the punishment/seizures?',
                      'What was the facility/geo-political location being targeted by the terrorist?',
                      'How many are injured/wounded in a protest?', 'How long does someone be prisoned/sentenced?',
                      'How many are killed in a protest?', 'Where a corruption has taken place?',
                      'What occurred because of a protest?',
                      'Who leads/organizes a protest?']