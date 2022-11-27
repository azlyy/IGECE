P = '\x1b[1;97m'
import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nKONEKSI INTERNET BURUK\n'%(P))
	exit()

if __name__ == "__main__":
	if "Indonesia" == fc:
		__import__("igc").login_kamu()
	else:
		__import__("igc").login_kamu()
