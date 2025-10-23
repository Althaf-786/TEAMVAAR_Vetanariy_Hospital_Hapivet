import requests

def send_image(file, url):
    files = {"image": (file.name, file, "multipart/form-data")}
    try:
        response = requests.post(url, files=files)
        response.raise_for_status()  # raise HTTPError if 4xx/5xx
        try:
            return response.json()
        except ValueError:
            return {"error": "Backend did not return JSON", "status_code": response.status_code, "text": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return {"error": "Backend did not return JSON", "status_code": response.status_code, "text": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def get_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return {"error": "Backend did not return JSON", "status_code": response.status_code, "text": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
