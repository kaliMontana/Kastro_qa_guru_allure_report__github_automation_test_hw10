# Kastro_qa_guru_allure_report__github_automation_test_hw10
Задание:

Написать тест на проверку названия Issue в репозитории через Web-интерфейс.

Этот тест представить в трех вариантах:

1. Чистый Selene (без шагов)

2. Лямбда шаги через with allure.step

3. Шаги с декоратором @allure.step

4. Разметку тестов всеми аннотациями


- Чтобы для каждого теста не прописывать настройки для аллюр отчета надо в корне проекта файл 
pytest.ini с настройкой:
[pytest]
addopts = --alluredir=allure-results

- Or Additional argument for test in pycharm: --alluredir=allure-results


- Start from terminal: python -m pytest