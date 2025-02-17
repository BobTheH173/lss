import requests

url = "https://minfin.com.ua/ua/currency/usd/"
response = requests.get(url)
response_text = response.text

start_marker = 'class="sc-1x32wa2-9'
start_index = response_text.find(start_marker)


def find_usd_rate(hryvnias):
    if start_index != -1:
        value_start = response_text.find(">", start_index) + 1
        value_end = response_text.find("<", value_start)

        usd_rate = response_text[value_start:value_end].strip()
        usd_rate = float(usd_rate.replace(",", "."))

        return float(usd_rate * hryvnias)
    else:
        print("USD rate not found")


print(find_usd_rate(int(input("Enter the amount of hryvnias to convert - "))), "$")
