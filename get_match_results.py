import pandas as pd
import requests
import csv
from bs4 import BeautifulSoup

try:
    source = requests.get('https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450')
    soup = BeautifulSoup(source.text, 'html.parser')
    list_of_results = soup.find_all('tr')

    # Open CSV file for writing
    with open('match-results.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write column headers to CSV file
        writer.writerow(['team1', 'team2', 'winner', 'margin', 'ground', 'matchDate', 'scoreCard'])

        # Iterate through each match result and write to CSV file
        for row in list_of_results:
            columns = row.find_all('td')
            team1 = columns[0].find('span').text
            team2 = columns[1].find('span').text
            winner = columns[2].find('span').text
            margin = columns[3].find('span').text
            ground = columns[4].find('span').text
            matchDate = columns[5].find('span').text
            scoreCard = columns[6].find('span').text
            writer.writerow([team1, team2, winner, margin, ground, matchDate, scoreCard])

    # Read CSV file into DataFrame
    df = pd.read_csv('match-results.csv')
    print(df.head())  # Print first few rows of DataFrame

except Exception as e:
    print(e)