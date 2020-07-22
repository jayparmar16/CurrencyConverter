import requests # IMPORTING MODULE

def CurrConvert(): 
  #Countries currencies codes
  currencies = ["USD","EUR","INR","CAD","HKD","ISK","PHP","DKK","HUF","CZK","AUD","RON","SEK","IDR","BRL","RUB","HRK","JPY","THB","CHF","SGD","PLN","BGN","TRY","CNY","NOK","NZD","ZAR","MXN","ILS","GBP","KRW","MYR"]
  print("Accepted Currencies : ")
  for c in currencies:
    print(c,end=" / ")
    
  flag = True
  while flag == True:
    amount = input("Enter the amount = ")
    from_curr = str(input("Enter base currency : ").upper())
    to_curr = str(input("Enter target currency : ").upper())

    url = 'https://api.exchangeratesapi.io/latest?base='+from_curr   #API URL

    if from_curr in currencies and to_curr in currencies: #checking the inputs
      if from_curr != to_curr:    #checking for same to and from currencies
        req = requests.get(url).json() #GETing json file from api
        exchange_rate = req['rates'][to_curr] #getting conversion rate from base to target 
        #print(exchange_rate)
        converted_amount = str(round(float(amount)*exchange_rate,2)) #Finding converted amount
        print('Converted amount : ',converted_amount)
        flag = False
      else:
        print("Wrong inputs !")
    else:
      print("Wrong inputs !")

def main():
  CurrConvert()

if __name__ == '__main__':
  main()
