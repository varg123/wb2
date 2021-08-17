# Ключевые слова
def set_keys(result_data, data):
    if data.get('vat'):
        params = []
        i = 1
        for k in data.get('vat').split(','):
            params.append({
                "value": k
            })
            if i > 2:
                break
            i += 1
        result_data['addin'].append({
            'type': "Ключевые слова",
            'params': params
        })
