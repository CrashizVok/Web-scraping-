import os
import socket
import argparse
import requests
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

# Clear the console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Main:
    def __init__(self, url):
        self.url = url

    def browser(self):
        try:
            response = requests.get(self.url)
            print(f"URL: {self.url}")
            
            # Get IP address
            d = str(urlopen('http://checkip.dyndns.com/').read())
            ip_address = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
            print(ip_address)
            
            # Parse HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string
            print(f"Title of the page: {title}")
            
            # Print cookies
            if response.cookies:
                print("Cookies:")
                for cookie in response.cookies:
                    print(f"  {cookie.name}: {cookie.value}")
                    print(f"____________________________________________")
            else:
                print("No cookies found.")
            
            #Location
            params = ['country', 'countryCode', 'city', 'timezone', 'mobile']
            resp = requests.get('http://ip-api.com/json/' + ip_address, params={'fields': ','.join(params)})
            info = resp.json()
            for param in params:
                print(f"{param}: {info[param]}")
        
        except requests.RequestException as e:
            print(f"Failed to open URL: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

def logo():
    x = r"""
 __      __      ___.                                               
/  \    /  \ ____\_ |__     ______ ________________  ______   ____  
\   \/\/   // __ \| __ \   /  ___// ___\_  __ \__  \ \____ \_/ __ \ 
 \        /\  ___/| \_\ \  \___ \\  \___|  | \// __ \|  |_> >  ___/ 
  \__/\  /  \___  >___  / /____  >\___  >__|  (____  /   __/ \___  >
       \/       \/    \/       \/     \/           \/|__|        \/ 
                                         Created By: Crashi_z
    """
    print(x)

def arguments():
    print("Optional arguments:")
    print("-h, --help           Show help message")
    print("-u URL, --url URL    Website url")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='No description')
    parser.add_argument('--url', '-u', type=str, required=True, help='Website url')
    args = parser.parse_args()
    
    logo()  # Print the logo
    
    if not args.url:
        parser.print_usage()
        print("Error: --url is required.\n")
        arguments()
    else:
        mainurl = Main(args.url)
        mainurl.browser()
