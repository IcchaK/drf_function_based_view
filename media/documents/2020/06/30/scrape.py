import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import json,csv
import urllib.request
url = "https://www.amazon.in/l/21570135031/ref=s9_acss_bw_cg_LFENPC_4a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=WHVGHKCBRDDK28V1266W&pf_rd_t=101&pf_rd_p=8de60e3c-e172-4965-a5cc-cec2c9fc7fc3&pf_rd_i=21532970031"
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)
#parse the html content
page_soup = soup(htmlContent, 'html.parser')

prod_titles=[]
prod_links=[]
prod_price=[]
Prime=[]
images=[]
def main():
	containers = page_soup.find_all("div",{"class":"s-item-container"})
	def title():
		for c in containers[:24]:
			title=c.find("div",{"class":"a-row a-spacing-mini"})
			#print(title.h2.text.strip())
			a=title.h2.text.strip()
			prod_titles.append(a)
	title()
	def links():
		for l in containers[:24]:
			links = l.find("div",{"class":"a-row a-spacing-base"})
			#print(links.div.div.a["href"])
			b=links.div.div.a["href"]
			prod_links.append(b)
	links()

	def price():
		for p in containers[:24]:
			price = p.find("span",{"class":"a-size-base"})
			#print(price.text.strip())
			c=price.text.strip()
			prod_price.append(c)
	price()

	def prime():
		for pr in containers[:24]:
			prime = pr.find("i",{"class":"a-icon a-icon-prime a-icon-small s-align-text-bottom"})
			if prime == None:
				Prime.append("No")
			else:
				Prime.append("Yes")
	prime()

	def img():
		number = 0
		for image in page_soup.find_all('img',{"class":"s-access-image cfMarker"}):
			images.append(image['src'])
			#print(image_src)
			urllib.request.urlretrieve(image['src'],str(number) +".jpeg")
			number+=1
	img()

	def conversion():
		df = pd.DataFrame({'ProductTitle':prod_titles,'Price':prod_price,'Productlinks':prod_links,'prime':Prime,'images':images}) 
		df.to_csv('prod.csv', index=False, encoding='utf-8')

		csvFilePath = "prod.csv"
		jsonFilePath = "prod.json"

		#reading csv and adding data to dictionary
		data = {}
		with open(csvFilePath,'r+') as csvFile:
		    csvReader = csv.DictReader(csvFile)
		    for csvRow in csvReader:
		        product_id = csvRow['ProductTitle']
		        data[product_id] = csvRow 

		#write to json file
		with open(jsonFilePath, 'w+') as jsonFile:
		    jsonFile.write(json.dumps(data, indent=4))

		    
	conversion()


if __name__ == '__main__':
	main()
	

# ondem
# liquid parafin