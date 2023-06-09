import allure
from allure_commons.types import Severity
from selene import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from pages.github_pages import open_main_page, search_for_repository, go_to_repository, open_issue_tab, \
    should_see_issue_with_number


def test_lamda_steps():
    allure.dynamic.tag('Web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label('owner', 'Kastro')
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Невторизованный пользователь не может создать задачу в репозитории')
    allure.dynamic.link('https://github.com', name='Testing')

    with allure.step('Открыть главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Искать репозитория'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example').click()
        s('.header-search-input').submit()

    with allure.step('Переходить по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открывать таб Issues'):
        s('#issues-tab').click()

    with allure.step('Проверить название Issue с номером 81'):
        s(by.partial_text('#81')).should(be.visible)


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Kastro')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Testing')
def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('81')
