# Гарантийный срок Гарантия
def set_gar(result_data, data):
    params = data.get('categori_props').keys()
    if params and ('Гарантийный срок' in params):
        if data.get('param').get('Гарантия'):
            result_data['addin'].append({
                'type': "Гарантийный срок",
                'params': [
                    {
                        "value": data.get('param').get('Гарантия')
                    }
                ]
            })
