
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"/home/monu/chromedriver")

page_range = 1

GITHUB_URLS = {
    'GITHUB_HOME_URL': 'https://github.com',
    'GITHUB_SEARCH_URL': 'https://github.com/search?q={}',
    'GITHUB_PAGE_SPECIFIC_URL': 'https://github.com/search?p={}&q={}&type={}',
    'GITHUB_MASTER_COMMITS_PAGE_URL': '{}/commits/master',
    'GITHUB_REPOSTY_URL':'?tab=repositories&q=&type=source&language=&sort=',
    'org_user':'https://github.com/orgs/'
}

GITHUB_CLASSES = {
    'repo_list_item': 'repo-list-item hx_hit-repo d-flex flex-justify-start py-4 public source',
    'repo_name': 'v-align-middle',
    'commit_list_item': 'Box-row Box-row--focus-gray mt-0 d-flex js-commits-list-item js-navigation-item js-socket-channel js-updatable-content',
    'commit_extension': 'tooltipped tooltipped-sw btn-outline btn BtnGroup-item text-mono f6',
    'user_name': 'avatar avatar-user',
    'commit_page_results': 'd-flex hx_hit-commit commit commits-list-item js-commits-list-item js-navigation-item js-details-container Details py-4',
    'commit_link': 'message markdown-title js-navigation-open',
    'users_page_results': 'd-flex hx_hit-user px-0 Box-row',
    'user_name_in_results': 'color-fg-muted',
    'follow_button': 'user-following-container js-form-toggle-container',
    'follow_count': 'text-bold color-fg-default',
    'user_card': 'vcard-detail pt-1 css-truncate css-truncate-target hide-sm hide-md',
    'user_repo_count': 'UnderlineNav-item js-responsive-underlinenav-item',
    'sponser_button':'v-align-middle'
}

GITHUB_ATTRIBUTES = {
    'location': {"itemprop": "homeLocation"},
    'user_website': {"data-test-selector": "profile-website-url"},
    'twitter': {"itemprop": "twitter"},
    'user_repo_count': {"data-tab-item": "repositories"},
    'org_user':'/people',
    'no_patch':'https://github.comhttps://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits'

}

GITHUB_XPATHS = {
    'older_button_on_page1': '//*[@id="repo-content-pjax-container"]/div[3]/div/a',
    'older_button': '//*[@id="repo-content-pjax-container"]/div[3]/div/a[2]'
}
GITHUB_CREDENTIALS = {
    'username': '',
    'password': ''
}