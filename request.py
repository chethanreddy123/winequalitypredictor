import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={"fixed acidity":7.4,"volatile acidity":3.4,"citric acid":5.5,"residual sugar":5.5,"chlorides":5.5,"free sulfur dioxide":5.5,"total sulfur dioxide":5.5,"density":5.5,"pH":5.5,"sulphates":5.5,"alcohol":4.5})

print(r.json())