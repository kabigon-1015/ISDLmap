import requests
import json

def postData(data):
    if(data is None):
        print("params is empty")
        return False
    
    payload = {
        "data": data
    }
    url = "https://script.google.com/macros/s/AKfycbwlwCtvzQuE8Et2__ZiXw2GOwzCDs3fvjSw312q-AT5Mt5x3BU/exec"
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if(response.status_code == 200 and response.text == "success"):
        print("post success!")
        return True
    print(response.text)
    return False

# if __name__ == "__main__":
    # postしたいデータを渡す
    #num = 1116180085
    # postData.postData(num)
