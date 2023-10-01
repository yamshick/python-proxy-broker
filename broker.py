import asyncio
from proxybroker import Broker
import test

proxies_ip = []

async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None: break
        print(f"{proxy.host}:{proxy.port}, {proxy.geo.code}, {proxy.is_working}, {proxy.avg_resp_time}")
#        print('Found proxy: %s' % proxy)
        proxy_data = {"host": proxy.host, "port": proxy.port}
        proxies_ip.append(proxy)
#        proxies_ip.append([proxy.host, proxy.port])
#        print(proxy_data)
		# proxies_ip.append([proxy.host, c])
		

def manage():
	try:
		proxies = asyncio.Queue()
		broker = Broker(proxies)
		types = [('HTTPS', ('Anonymous', 'High')), ]
		tasks = asyncio.gather(
		    broker.find(types=['HTTPS'], limit=30),
		    show(proxies))

		loop = asyncio.get_event_loop()
		loop.run_until_complete(tasks)

		print(proxies_ip)
		print(proxies_ip.reverse())
		for proxy in reversed(proxies_ip):
			proxy_info = test.test_proxy(proxy.host, proxy.port)
			print(proxy_info)
		# print(tasks)
#        info = test.test_proxy(proxy.host, proxy.port)
#        if info is None: break

	except Exception as e:
		print(e)
		
		
manage()		
