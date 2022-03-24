from common_actions import *
from constants import *
import gspread
import operator
from oauth2client.service_account import ServiceAccountCredentials

scopes = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
cred = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scopes)
client = gspread.authorize(cred)
sheet=client.open('github_emails').get_worksheet_by_id(1987910278)
def from_org(org):
    people_url=GITHUB_URLS['org_user']+org+GITHUB_ATTRIBUTES['org_user']
    user_url=get_soup(people_url,10)

    users=user_url.findAll('a',{'class':'f4 d-block'},href=True)
    print('organization working')
    row=2
    for user in users:
        user_data=scrape_from_user(user['href'])
        more_user_data = user_data_scrape(user['href'])
        print(more_user_data)
        if user_data:
            sheet.update_cell(row, 1, org)
            sheet.update_cell(row, 2, more_user_data[0])
            sheet.update_cell(row, 3, user_data['user_email'])
            sheet.update_cell(row, 4, more_user_data[1])
            sheet.update_cell(row, 5, more_user_data[2])
            sheet.update_cell(row, 6, more_user_data[3])
            sheet.update_cell(row, 7, more_user_data[5])
            row=row+1

