import itinerary_data
import random
import pandas as pd

def create_disruption():
    csv_path = './Caspar/historique_disruptions_2024_ligne9.csv'
    df = pd.read_csv(csv_path)
    df_metro_9 = df[df['impacted_objects_pt_object_name'] == 'RATP Métro 9']
    df_metro_9_noservice = df_metro_9[df_metro_9['severity.effect'] == 'NO_SERVICE']
    df_metro_9_noservice_active = df_metro_9_noservice[df_metro_9_noservice['status'] == 'active']

    #Period begin
    period_begin_list = df_metro_9_noservice_active['period_begin'].unique()
    period_begin_list = list(period_begin_list)

    #Status
    status_list = df_metro_9_noservice_active['status'].unique()
    status_list = list(status_list)

    #Severity Effect
    severity_effect_list = df_metro_9_noservice_active['severity.effect'].unique()
    severity_effect_list = list(severity_effect_list)

    #Message Text
    messages_text_list = df_metro_9_noservice_active['messages_text'].unique()
    messages_text_list = list(messages_text_list)

    #Impacted Objects Pt Object ID
    impacted_objects_pt_object_id_list = df_metro_9_noservice_active['impacted_objects_pt_object_id'].unique()
    impacted_objects_pt_object_id_list = list(impacted_objects_pt_object_id_list)

    period_begin = period_begin_list[random.randint(0,len(period_begin_list)-1)]
    status = status_list[random.randint(0,len(status_list)-1)]
    severity_effect = severity_effect_list[random.randint(0,len(severity_effect_list)-1)]
    messages_text = messages_text_list[random.randint(0,len(messages_text_list)-1)]
    impacted_objects_pt_object_id = impacted_objects_pt_object_id_list[random.randint(0,len(impacted_objects_pt_object_id_list)-1)]


    dico = {
        'date_fichier': '/',
        'id': '/',
        'disruption_id': '/',
        'impact_id': '/',
        'period_begin': period_begin,
        'period_end': '/',
        'status': status,
        'updated_at': '/',
        'tags': '/',
        'cause': '/',
        'category': '/',
        'severity.name': '/',
        'severity.effect': severity_effect,
        'severity.color': '/',
        'severity.priority': '/',
        'messages_text': messages_text,
        'impacted_objects_pt_object_id': impacted_objects_pt_object_id,
        'impacted_objects_pt_object_name': '/'
    }

    cles_a_conserver =['period_begin','status','severity.effect','messages_text','impacted_objects_pt_object_id']

    dico_filtre = {key : dico[key] for key in cles_a_conserver if key in dico}

    if dico_filtre.get('status') == 'active' and dico_filtre.get('severity.effect') == 'NO_SERVICE':
        disruption = itinerary_data.Disruption(dico_filtre.get('period_begin'), dico_filtre.get('status'), dico_filtre.get('severity.effect'), dico_filtre.get('messages_text'), dico_filtre.get('impacted_objects_pt_object_id'))

    return disruption