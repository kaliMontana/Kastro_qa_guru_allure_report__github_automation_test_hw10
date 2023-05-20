from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github_selene():
    browser.open('https://github.com/')

    s('.header-search-input').click()
    s('.header-search-input').send_keys('eroshenkoam/allure-example').click()
    s('.header-search-input').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text('#81')).should(be.visible)
