# Extract Arbitrum dexes to CSV file

import csv
from dextools_python import DextoolsAPI

API_KEY = "YOUR_API_KEY"
NETWORK = "arbitrum"



dextools = DextoolsAPI(API_KEY)
response = dextools.get_exchange_list(NETWORK, pageSize=50)
data = response["data"]

with open("exchanges.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)

    count = 0

    for dex in data:
        if count == 0:
            header = dex.keys()
            csv_writer.writerow(header)
            count = count + 1

        csv_writer.writerow(dex.values())

    csv_file.close()
