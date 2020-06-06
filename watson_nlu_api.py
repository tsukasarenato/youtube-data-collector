import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions, \
    ConceptsOptions


def watson_nlu(text):

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


text_example = 'Bacharel em computação pelo Centro Universitário Eurípides de Marília (UNIVEM). Minha experiência na ' \
               'área é com desenvolvimento de projetos, meu primeiro projeto foi para a área de turismo de Marília, ' \
               'o meu segundo foi automação de testes em jogos eletrônicos, no terceiro desenvolvi uma interface de ' \
               'usuário para os bombeiros do DF, e o meu ultimo foi mineração de dados em midias sociais e jornais ' \
               'eletrônicos. Criei este site para compartilhar um pouco do meu conhecimento e do que venho ' \
               'desenvolvendo nos tempos livres. '

print(watson_nlu(text_example))
