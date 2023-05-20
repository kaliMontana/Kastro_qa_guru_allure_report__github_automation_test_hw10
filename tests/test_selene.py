from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open('https://github.com/')

    s('.header-search-input').click()