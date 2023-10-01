# Setting up Proxies with the requests Library
import requests


def test_proxy(host, port):
	proxy_servers = {
	   'https': f"https://{host}:{port}",
	}


	print(proxy_servers["https"])
	try:
		data = requests.get('https://ipinfo.io/json', proxies=proxy_servers, timeout=5)
		 
		return data.json()
	except Exception as e:
		print(e)
		return None

	# response = requests.get('https://google.com', proxies=proxy_servers)


proxy_servers = {
   'https': 'https://172.234.38.85:8080',
}


def test():
	try:
		# data = requests.get('https://ipinfo.io/json')
		data = requests.get('https://ipinfo.io/json', proxies=proxy_servers)
		 
		print(data.text)
	except Exception as e:
		print(e)

	# response = requests.get('https://google.com', proxies=proxy_servers)
	
# test()
