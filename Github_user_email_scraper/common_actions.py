from bs4 import BeautifulSoup
import time
import gspread
import selenium
from constants import *
from datetime import date


def export_to_gsheet(data, tab_name):
    gc = gspread.service_account(filename='cred.json')
    sh = gc.open('github_emails').worksheet(tab_name)
    sh.append_rows(data)
    return


def get_soup(url, wait):
    driver.get(url)
    time.sleep(wait)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    return soup


def login():
    login_url = GITHUB_URLS['GITHUB_HOME_URL'] + '/login'
    driver.get(login_url)
    time.sleep(3)
    driver.find_element_by_id("login_field").send_keys(GITHUB_CREDENTIALS['username'])
    driver.find_element_by_id("password").send_keys(GITHUB_CREDENTIALS['password'])
    driver.find_element_by_name("commit").click()


def user_data_scrape(user_name):

    following = followers = twitter_url = location = user_website = user_repo_count = 'NA'

    user_page_url = GITHUB_URLS['GITHUB_HOME_URL'] + '/' + user_name
    profile_page = get_soup(user_page_url, 5)
    followers = profile_page.find_all('span', class_=GITHUB_CLASSES['follow_count'])[0].text.strip()
    following = profile_page.find_all('span', class_=GITHUB_CLASSES['follow_count'])[1].text.strip()

    try:
        location_tag = profile_page.find(class_=GITHUB_CLASSES['user_card'], attrs=GITHUB_ATTRIBUTES['location'])
        location = location_tag.find('span').text

    except:
        pass

    try:
        user_website_tag = profile_page.find(class_=GITHUB_CLASSES['user_card'], attrs=GITHUB_ATTRIBUTES['user_website'])
        user_website = user_website_tag.find('a', href=True)['href']

    except:
        pass

    try:
        twitter_url_tag = profile_page.find(class_=GITHUB_CLASSES['user_card'], attrs=GITHUB_ATTRIBUTES['twitter'])
        twitter_url = twitter_url_tag.find('a', href=True)['href']

    except:
        pass

    try:
        user_repo_count_tag = profile_page.find(class_=GITHUB_CLASSES['user_repo_count'], attrs =GITHUB_ATTRIBUTES['user_repo_count'])
        user_repo_count = user_repo_count_tag.find('span').text

    except:
        pass

    return [user_page_url, followers, following, location, user_website, twitter_url, user_repo_count]


def scrape_from_user(org_name):
    org_url = GITHUB_URLS['GITHUB_HOME_URL'] + '/' + org_name
    org_page = get_soup(org_url, 7)
    print(org_url)
    repo_link=org_url+GITHUB_URLS['GITHUB_REPOSTY_URL']
    print(repo_link)
    repo_page=get_soup(repo_link,7)
    print("Hi i am exicutingg")
    find_repo_url=False
    repo_tag = repo_page.find('h3', {"class": 'wb-break-all'})
    if repo_tag is None:
        return
    repostry=repo_tag.find('a',href=True)
    # print(GITHUB_URLS['GITHUB_HOME_URL']+'/'+str(repostry['href']))
    repo_page=get_soup(GITHUB_URLS['GITHUB_HOME_URL']+'/'+str(repostry['href']),7)
    commit_tag=repo_page.find('li',{'class':'ml-0 ml-md-3'})

   # commit_url_tag=repo_tag.find('href',{'class':'pl-3 pr-3 py-3 p-md-0 mt-n3 mb-n3 mr-n3 m-md-0 Link--primary no-underline no-wrap'})
    commit_url=commit_tag.find('a',{'data-pjax':'#repo-content-pjax-container'})
    comit_page=get_soup(GITHUB_URLS['GITHUB_HOME_URL']+str(commit_url['href']),7)
    # print(comit_page)
    # print('Commit page')

    patch_tag=comit_page.find('div',{'class','d-none d-md-block flex-shrink-0'})
    patch_url=patch_tag.find('a', href=True)
    patch_link=GITHUB_URLS['GITHUB_HOME_URL']+patch_url['href']
    print(patch_link)
    if(patch_link==GITHUB_ATTRIBUTES['no_patch']):
        return
    commit_patch_link = patch_link + '.patch'
    commit_patch_page = get_soup(commit_patch_link, 3)

    try:
        commit_data_filter1 = commit_patch_page.find('pre').text.partition('From:')[-1]
        commit_data_filter2 = commit_data_filter1.split('>', 1)[0]
        # print(commit_data_filter2)
        user_email = commit_data_filter2.partition(' <')[-1].strip()
        print(user_email)
        return {'user_email':user_email}
    except AttributeError:
        print('')
    # repo_url=rep[0]


    time.sleep(10)





