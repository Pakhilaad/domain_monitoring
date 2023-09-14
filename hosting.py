import socket
import pandas as pd
from main import df

# Assuming you have a DataFrame 'df' containing flagged domains
registered_domains = df['Flagged Domain'].tolist()

def get_hosting_provider(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        hosting_provider = socket.gethostbyaddr(ip_address)[0]
        return hosting_provider
    except (socket.gaierror, socket.herror):
        return "Unknown"

# Create a list to store domain hosting provider information
domain_hosting_info = []

# Loop through each domain and get the hosting provider
for domain in registered_domains:
    hosting_provider = get_hosting_provider(domain)
    domain_hosting_info.append({'Domain': domain, 'Hosting Provider': hosting_provider})

# Create a DataFrame from the hosting information list
hosting_df = pd.DataFrame(domain_hosting_info)

# Print the DataFrame
print(hosting_df) 
