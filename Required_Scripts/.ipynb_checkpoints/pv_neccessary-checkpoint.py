class pv_necessary:
    
    def get_token(String api_name=None)
        if api_name==None:
            return "NO API FOUND / API NAME NOT PASSED"
        else:
            #Key access
            fileLocation = '../../keys.json'
            with open(fileLocation) as f:
                data = json.load(f)

            for i in data['keys']:
                if i['name'] == api_name
                    return i['token']
                