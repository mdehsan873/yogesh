import time

from common_actions import *
from from_orgnization import *

def get_search_results_from_users(keyword):
    user_details = []
    for page_number in range(1, page_range + 1):

        page_url = GITHUB_URLS['GITHUB_PAGE_SPECIFIC_URL'].format(int(page_number), str(keyword), 'users')
        users_page = get_soup(page_url, 7)
        results = users_page.find_all('div', class_=GITHUB_CLASSES['users_page_results'])

        # print(results)

        if not len(results):

            if page_number == 1:
                print("No results obtained, Try another query")

            driver.quit()
            break

        for result in results:

            try:
                user_name = result.find('a', class_=GITHUB_CLASSES['user_name_in_results'], href=True)['href']
                user_name = str(user_name).partition('/')[-1]
                try:
                    sponser_button = result.find('span', class_=GITHUB_CLASSES['sponser_button'])
                    if sponser_button:
                        print("this is orgnization")
                        print(user_name)
                        org_name = user_name
                        data_from_org = from_org(user_name)

                        print(data_from_user)
                        user_details.append(data_from_user)
                    else:
                        print(user_name)
                        data_from_user = scrape_from_user(user_name)
                        print(data_from_user)
                        user_details.append(data_from_user['user_email'])
                except UnboundLocalError:
                    pass
                more_user_data = user_data_scrape(user_name)
                print(user_name)
                print(user_name, more_user_data)
                user_data = [user_name, more_user_data]
                print(more_user_data)

                user_page_url, followers, following, location, user_website, twitter_url, user_repo_count = user_data_scrape(user_name)
                # print(user_name, more_user_data)
                user_data = [user_name, user_page_url, followers, following, location, user_website, twitter_url, user_repo_count]
                print(user_data)

                user_details.append(user_data)
                export_to_gsheet(user_details, 'new sample')
            except IndexError:
                continue


    export_to_gsheet(user_details, 'new sample')

    driver.quit()



