import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

# img = "https://i2.wp.com/www.dorsetbutterflies.com/wordpress/wp-content/uploads/2018/08/Adonis-Blue-James-Gould-2017-crop.jpg?fit=2103%2C1402&ssl=1"


data = {'url': "https://i2.wp.com/www.dorsetbutterflies.com/wordpress/wp-content/uploads/2018/08/Adonis-Blue-James-Gould-2017-crop.jpg?fit=2103%2C1402&ssl=1"}


result = requests.post(url, json=data).json()
print(result)