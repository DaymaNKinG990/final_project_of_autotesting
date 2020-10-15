import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_language, browser, languages = request.config.getoption("language"), None, ['ar', 'ca', 'cs', 'da', 'de',
                                                                                        'en-gb', 'el', 'es', 'fi', 'fr',
                                                                                        'it', 'ko', 'nl', 'pl', 'pt',
                                                                                        'pt-br', 'ro', 'ru', 'sk', 'uk',
                                                                                        'zh-hans', 'en']
    for language in languages:
        if browser_language == language:
            print(f"\n{browser_language} language")
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
            browser = webdriver.Chrome(options=options)
            break
        elif languages.index(language) + 1 == len(languages) and browser_language != language:
            raise pytest.UsageError("--language should be shortcut of language")
        else:
            continue
    yield browser
    print("\nquit browser..")
    browser.quit()
