import requests

""" url for local testing """
# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

""" url to test the deployed lambda funcion """
url = "https://19kywrz8ek.execute-api.us-east-1.amazonaws.com/butterfly-classifier/predict"

img = "https://i2.wp.com/www.dorsetbutterflies.com/wordpress/wp-content/uploads/2018/08/Adonis-Blue-James-Gould-2017-crop.jpg?fit=2103%2C1402&ssl=1"


data = {'url': "https://i2.wp.com/www.dorsetbutterflies.com/wordpress/wp-content/uploads/2018/08/Adonis-Blue-James-Gould-2017-crop.jpg?fit=2103%2C1402&ssl=1"}


result = requests.post(url, json=data).json()
print(result)