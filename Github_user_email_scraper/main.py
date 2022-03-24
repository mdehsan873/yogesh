from from_repos import get_search_results_from_repos
from from_commits import get_search_results_from_commits
from from_users import get_search_results_from_users
from common_actions import login


# make changes in the following function to remove multiple return statements, currently for testing uncomment 
# the required return statement and run the program.

def run_scraper(keyword):

    # return get_search_results_from_repos(keyword)
    # return get_search_results_from_commits(keyword)
    return get_search_results_from_users(keyword)

# Login is required for scraping data from user page or generally accessing user page.


keyword = 'ehsan'
login()
run_scraper(keyword)
