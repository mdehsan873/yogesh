
from common_actions import *


def get_user_data(commits_page_url, id):
    commits_page = get_soup(commits_page_url, 7)
    commits = commits_page.find_all('li', class_=GITHUB_CLASSES['commit_list_item'])
    user_details = []

    for commit in commits:

        try:
            user_name = commit.find('a', class_=GITHUB_CLASSES['user_name'], href=True)['href']
            user_name = str(user_name).partition('/')[-1]

        except Exception:
            continue

        commit_extension = commit.find('a', class_=GITHUB_CLASSES['commit_extension'], href=True)['href']
        commit_patch_link = GITHUB_URLS['GITHUB_HOME_URL'] + commit_extension + '.patch'
        # print(commit_patch_link)
        commit_patch_page = get_soup(commit_patch_link, 3)

        try:
            commit_data_filter1 = commit_patch_page.find('pre').text.partition('From:')[-1]
            commit_data_filter2 = commit_data_filter1.split('>', 1)[0]
            # print(commit_data_filter2)
            user_email = commit_data_filter2.partition(' <')[-1].strip()

            if 'users.noreply.github.com' not in user_email and '=?UTF-8?' not in user_name:
                more_user_data = user_data_scrape(user_name)
                user = [user_name, user_email, more_user_data, id]
                user_details.append(user)
                print(user)

        except AttributeError:
            continue
    export_to_gsheet(user_details, 'new sample')
    return user_details


def multiple_commit_page_scrape(repo_url, id):
    all_user_details = []
    commits_page_url = GITHUB_URLS['GITHUB_MASTER_COMMITS_PAGE_URL'].format(repo_url)
    user_details = get_user_data(commits_page_url, id)
    all_user_details.append(user_details)
    driver.get(commits_page_url)

    try:
        older_button = driver.find_element_by_xpath(GITHUB_XPATHS['older_button_on_page1']).get_attribute('href')

    except Exception as e:
        older_button = False

    # print(user_details)

    while older_button:

        commits_page_url = older_button
        user_details = get_user_data(commits_page_url, id)
        # print(user_details)
        all_user_details.append(user_details)
        driver.get(commits_page_url)

        try:
            older_button = driver.find_element_by_xpath(GITHUB_XPATHS['older_button']).get_attribute('href')

        except Exception:
            older_button = False

    return user_details


def get_search_results_from_repos(keyword):
    repo_list = []
    contributor_list = []

    for page_number in range(1, page_range + 1):

        page_url = GITHUB_URLS['GITHUB_PAGE_SPECIFIC_URL'].format(int(page_number), str(keyword), 'repositories')
        repo_page = get_soup(page_url, 7)
        repositories = repo_page.find_all(class_=GITHUB_CLASSES['repo_list_item'])

        if not len(repositories):

            if page_number == 1:
                print("No results obtained, Try another query")

            driver.quit()
            break

        for repo in repositories:
            repository_name = repo.find(class_=GITHUB_CLASSES['repo_name']).text
            repo_link = GITHUB_URLS['GITHUB_HOME_URL'] + '/' + repository_name
            scrape_date = date.today()
            repo_id = repository_name + str(scrape_date)
            contributor_details = multiple_commit_page_scrape(repo_link, repo_id)
            repo_details = [repository_name, repo_link, contributor_details]
            repo_list.append(repo_details)
            contributor_list.append(contributor_details)

    driver.quit()


