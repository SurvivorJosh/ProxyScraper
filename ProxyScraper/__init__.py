import requests


class ProxyScraper:

    
    def GenerateProxies(directory: str):
       
        with open(directory, "wb") as file:
            session = requests.Session()
            response = session.get(
                "https://api.proxyscrape.com/v2/?request=displayproxies$protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
            ).content
            file.write(response)
            file.close()