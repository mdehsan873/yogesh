from common_actions import *


def get_search_results_from_commits(keyword):
    user_details = []
    for page_number in range(1, page_range + 1):

        page_url = GITHUB_URLS['GITHUB_PAGE_SPECIFIC_URL'].format(int(page_number), str(keyword), 'commits')
        commits_page = get_soup(page_url, 7)
        results = commits_page.find_all('div', class_=GITHUB_CLASSES['commit_page_results'])

        if not len(results):

            if page_number == 1:
                print("No results obtained, Try another query")

            driver.quit()
            break

        for result in results:

            commit_link = result.find('a', class_=GITHUB_CLASSES['commit_link'], href=True)['href']
            commit_link = GITHUB_URLS['GITHUB_HOME_URL'] + str(commit_link)
            scrape_date = date.today()
            scrape_id = keyword + 'commit' + str(scrape_date)
            commit_page = get_soup(commit_link, 3)
            try:
                user_name = commit_page.find('a', class_=GITHUB_CLASSES['user_name'], href=True)['href']
                user_name = str(user_name).partition('/')[-1]
                # print(user_name)
            except Exception:
                continue

            commit_patch_link = commit_link + '.patch'
            commit_patch_page = get_soup(commit_patch_link, 3)

            try:
                commit_data_filter1 = commit_patch_page.find('pre').text.partition('From:')[-1]
                commit_data_filter2 = commit_data_filter1.split('>', 1)[0]
                # print(commit_data_filter2)
                user_email = commit_data_filter2.partition(' <')[-1].strip()

                if 'users.noreply.github.com' not in user_email and '=?UTF-8?' not in user_name:
                    more_user_data = user_data_scrape(user_name)
                    user = [user_name, user_email, more_user_data, scrape_id]
                    user_details.append(user)
                    print(user)

            except AttributeError:
                continue
    driver.quit()

    export_to_gsheet(user_details, 'new sample')
    return user_details

