import requests
import json
def analyseResp(a):
    dict1 = d[0]
    new_d = {}
    actual_response = ' '
    for k,v in dict1.items():
        if k == 'classifications':
            new_d = v[0]
            for k1,v1 in new_d.items():
                if k1 == 'tag_name':
                    actual_response = v1
                    return actual_response
            
    

api_key =  "a69f786c0e8987224cd3cc779e238e679e6703c7"
url = "https://api.monkeylearn.com/v3/classifiers/cl_pi3C7JiL/classify/"
header = {"Authorization": f"Token {api_key}"}
user_inp = input("Enter an sentimental statement")
data = {'data' :[user_inp]}
response = requests.post(url,headers=header, json=data)
d = response.json()
sentiment = analyseResp(d)
print(sentiment)
