from urllib.request import Request, urlopen
import urllib.request
import json

#access to random numbers
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data = json.loads(data)
randon_number = data['randomness']

#split randomness into 2 bits of hexadecimal numbers mod 80
A = 2
n3=0
result = []
result2 = []

for i in range(0, len(randon_number), A):   
    result.append(str(randon_number[i : i + A]))

for i in range(0,len(result)):
   number = int(result[i],16)%80
   result2.append(number)

#remove dublicates
print("my numbers: " + str(set(result2))) 


#access to kino lucky numbers
url = 'https://api.opap.gr/draws/v3.0/1100/last-result-and-active'
response = urllib.request.urlopen(url)
html = response.read()
data2 = html.decode()
kino_winning_numbers = json.loads(data2)
kino = kino_winning_numbers['last']['winningNumbers']['list']
print("KINO lucky numbers: " +str(kino))
for n in result2:
   for n2 in kino:
      if n == n2:
         n3= n3+1

print("Score: " + str(n3))
 

