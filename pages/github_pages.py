import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.step('Открыть главную страницу')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Искать репозитория {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys('eroshenkoam/allure-example').click()
    s('.header-search-input').submit()


@allure.step('Переходить по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открывать таб Issues')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Проверить название Issue с номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text('#' + number)).should(be.visible)
