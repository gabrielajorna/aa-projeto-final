import requests
import bs4

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
url_insper = "https://www.insper.edu.br/imprensa/"

def raspar_insper(headers, url_insper):
  result_insper = requests.get(url_insper,  headers = headers)
  soup_insper = bs4.BeautifulSoup(result_insper.text, 'html.parser')
  links_insper = soup_insper.find_all('div', { 'class': '_thumbnail__descricao no-paddingM' })
  noticias_insper = []
  for link in links_insper:
    link_insper = link.find('a').get('href')
    titulo = link.find('a').text.strip()
    noticias_insper.append({"titulo": titulo, "url": link_insper})
  return noticias_insper

raspar_insper(headers, url_insper)