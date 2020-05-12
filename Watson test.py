import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions, \
    ConceptsOptions


def watson_request(text):
    authenticator = IAMAuthenticator('your key')

    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-07-12',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url(
        'https://gateway.watsonplatform.net/natural-language-understanding/api')

    response = natural_language_understanding.analyze(
        text=text,
        features=Features(
            concepts=ConceptsOptions(limit=3),
            categories=CategoriesOptions(limit=1),
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=5),
            keywords=KeywordsOptions(emotion=True, sentiment=True, limit=5))).get_result()

    json_string = json.dumps(response, ensure_ascii=False).encode('utf8')

    return json_string


file = ''
Writefile = ''

f = open(file, encoding="utf8")

line = f.readline()
number_comment = 0
texts = ''
write_text = ''
while line != '##endFile':
    line = f.readline()
    if str(line) != '\n':
        texts += str(line)
        number_comment += 1

    if number_comment > 200 and texts != '':
        write_text += str(watson_request(texts).decode('utf8')) + '\n'
        print(write_text)
        number_comment = 0
        texts = ''

if texts != '':
    write_text += str(watson_request(texts)) + '\n'

file = open(Writefile, 'w', encoding="utf8")
file.write(write_text)
file.close()
