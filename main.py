import pandas as pd 

# Open the file for reading
file_path = r'C:\Users\admin\Desktop\dailyupdate.txt'
with open(file_path, 'r') as file:
    # Read each line (domain) from the file
    registered_domains = [line.strip() for line in file.readlines()]

# Read keywords from Excel file
keywords_df = pd.read_excel('Generic Keywords.xlsx')
keyword_list = keywords_df.iloc[:, 0].tolist()

# Function to check if keywords or their sequences are present in the domain
def check_keywords(domain, keywords):
    for keyword in keywords:
        if keyword in domain:
            return True
    return False

flagged_domains = []

# Check domains for keywords and sequences
for domain in registered_domains:
    if check_keywords(domain, keyword_list):
        flagged_domains.append(domain)

# Create a DataFrame with flagged domains
df = pd.DataFrame({'Flagged Domain': flagged_domains})
