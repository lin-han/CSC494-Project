import http.client, urllib.request, urllib.parse, urllib.error, base64, ast, time


def capitalize_first_letter(s):
    return s[0].upper() + s[1:]

def strip_punctuation(s):
    str = ''
    for letter in s:
        if letter not in "'.,:!@#$%^&*():;_+=/\\\"":
            if letter == "-":
                str += ' '
            else:
                str += letter
    return str

def pre_process_title(s):
    s = strip_punctuation(s).lower()
    split = s.split(' ')
    words = []
    for item in split:
        if item != '':
            words.append(item)
    return ' '.join(words)

def get_reference_ids(title):
    expr = "Ti==" + "'" + pre_process_title(title) + "'"
    print(pre_process_title(title))

    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '7d60a82d0fa149e6b7574a7abc6c5910',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'expr': expr,
        'model': 'latest',
        'count': '1',
        'offset': '0',
        'attributes': 'RId',
    })

    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai')
        conn.request("GET", "/academic/v1.0/evaluate?%s" % params, '', headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
        data = ast.literal_eval(data.decode('ascii'))
        entities = data['entities']
        if len(entities) > 0:
            try:
                return data['entities'][0]['RId']
            except KeyError:
                return []
        else:
            return []
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def get_references(title):
    reference_ids_list = get_reference_ids(title)
    reference_list = []

    for id in reference_ids_list:
        expr = 'Id=' + str(id)

        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': '7d60a82d0fa149e6b7574a7abc6c5910',
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'expr': expr,
            'model': 'latest',
            'count': '1',
            'offset': '0',
            'attributes': 'Ti',
        })

        try:
            conn = http.client.HTTPSConnection('api.projectoxford.ai')
            conn.request("GET", "/academic/v1.0/evaluate?%s" % params, '', headers)
            response = conn.getresponse()
            data = response.read()
            # print(data)
            conn.close()
            print(data.decode('ascii'))
            data = ast.literal_eval(data.decode('ascii'))
            entities = data['entities']
            if len(entities) > 0:
                reference_list.append(capitalize_first_letter(data['entities'][0]['Ti']))
            else:
                reference_list.append('')
            time.sleep(1)

        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return reference_list

def get_references(title):
    reference_ids_list = get_reference_ids(title)
    reference_list = []

    for id in reference_ids_list:
        expr = 'Id=' + str(id)

        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': '7d60a82d0fa149e6b7574a7abc6c5910',
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'expr': expr,
            'model': 'latest',
            'count': '1',
            'offset': '0',
            'attributes': 'Ti',
        })

        try:
            conn = http.client.HTTPSConnection('api.projectoxford.ai')
            conn.request("GET", "/academic/v1.0/evaluate?%s" % params, '', headers)
            response = conn.getresponse()
            data = response.read()
            # print(data)
            conn.close()
            print(data.decode('ascii'))
            data = ast.literal_eval(data.decode('ascii'))
            entities = data['entities']
            if len(entities) > 0:
                reference_list.append(capitalize_first_letter(data['entities'][0]['Ti']))
            else:
                reference_list.append('')
            time.sleep(1)

        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return reference_list


def get_title(id):
    expr = 'Id=' + str(id)

    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '7d60a82d0fa149e6b7574a7abc6c5910',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'expr': expr,
        'model': 'latest',
        'count': '1',
        'offset': '0',
        'attributes': 'Ti',
    })

    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai')
        conn.request("GET", "/academic/v1.0/evaluate?%s" % params, '', headers)
        response = conn.getresponse()
        data = response.read()
        # print(data)
        conn.close()
        print(data.decode('ascii'))
        data = ast.literal_eval(data.decode('ascii'))
        entities = data['entities']
        if len(entities) > 0:
            return capitalize_first_letter(data['entities'][0]['Ti'])
        else:
            return False
        time.sleep(1)

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


if __name__ == "__main__":
    print(get_references(' Reference  management:  software a comparative analysis of four products '))
