from selenium.webdriver.common.by import By

# SOME LOCATORS FOR SEVERAL PROJECT PAGES

# ДЛЯ ПОНИМАНИЯ ЗНАНИЙ О СЕЛЕНИУМ ДЛЯ WEB И ИСПОЛЬЗОВАНИЯ БИБЛИОТЕКИ REQUEST БУДЕТ ЛУЧШЕ ПОСМОТРЕТЬ ПРОРАБОТАННЫЕ
# ПРОЕКТЫ НА GITHUB, ССЫЛКИ НА КОТОРЫЕ ТАКЖЕ ВЫСЛАЛА :)

class SiteCataloguePageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="search"]')
    SEARCH_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')
    CHANGE_REGION_BTN = (By.CSS_SELECTOR, '[data-category="regional"] button')
    COUNTRY_RUSSIA_BTN = (By.XPATH, '//span[text() = \'Россия\']')
    REGION_SIBERIA_BTN = (By.XPATH, '//span[text() = \'Сибирь\']')
    CITY_NOVOSIBIRSK_BTN = (By.XPATH, '//span[text() = \'Новосибирск\']')
    CONFIRM_REGION_BTN = (By.XPATH, '//button[text() = \'Применить\']')
    OPEN_ALL_TOPICS_BTN = (By.LINK_TEXT, '/navi')
    TOPIC_SUBTITLE = (By.CSS_SELECTOR, '[role="presentation"]>div')
    RESET_FILTER_BTN = (By.XPATH, '//div[text() = \'Сбросить\']')
    AUTO_MOTO_CATEGORY_BTN = (By.CSS_SELECTOR, '[data-category="Авто и мото"]')
    NO_FOUND_SITE_INFO_TITLE = (By.XPATH, '//h2[text() = \'Ничего не найдено\']')
    NO_FOUND_SITE_INFO_MESSAGE = (By.XPATH, '//h2[text() = \'Ничего не найдено\']/following-sibling::p')
    NO_FOUND_SITE_INFO_BTN = (By.XPATH, '//h2[text() = \'Вернуться назад\']')
    LENTA_RU_BTN = (By.ID, '80674')

class AnalyticsDashboardPageLocators:
    CATEGORY_AUDIENCE_BTN = (By.CSS_SELECTOR, '[data-newreport="reports::audience"]')
    CATEGORY_TECHNOLOGY_BTN = (By.CSS_SELECTOR, '[data-newreport="reports::technology"]')
    CATEGORY_SOURCES_BTN = (By.CSS_SELECTOR, '[data-newreport="reports::sources"]')
    CATEGORY_CONTENT_BTN = (By.CSS_SELECTOR, '[data-newreport="reports::content"]')
    CATEGORY_BEHAVIOR_BTN = (By.CSS_SELECTOR, '[data-newreport="reports::behavior"]')
    CATEGORY_RATING_BTN = (By.CSS_SELECTOR, '[data-newreport="reports::rating"]')
    ADD_UTM_METRICS_BTN = (By.CSS_SELECTOR, '[data-dashboard="UTM::add_metrics"]')
    ADD_UTM_ENTRANCE_BTN = (By.CSS_SELECTOR, '[data-dashboard="Entrance::add_metrics"]')
    SELECT_DETALIZATION_BTN = (By.ID, 'icon-simple-arrow-2')
    SELECT_PERIOD_BTN = (By.ID, '[data-dashboard="Calendar"] svg]')

class TechnologyBlockLocators:
    TECHNOLOGY_DEVICE_BTN = (By.CSS_SELECTOR, '[data-newreport="reports::technology::device"]')
    TECHNOLOGY_BROWSER_BTN = (By.CSS_SELECTOR, '[data-newreport="reports::technology::browser"]')
    TECHNOLOGY_OS_BTN = (By.CSS_SELECTOR, '[data-newreport="reports::technology::os"]')
    TECHNOLOGY_SCREENSIZE_BTN = (By.CSS_SELECTOR, '[data-newreport="reports::technology::screensize"]')

class UTMMetricLocators:
    UTM_VISITS_CHBX = (By.CSS_SELECTOR, '[data-dashboard="UTM::Visits"]')
    UTM_DEPTH_CHBX = (By.CSS_SELECTOR, '[data-dashboard="UTM::Depth"]')
    UTM_BOUNCES_CHBX = (By.CSS_SELECTOR, '[data-dashboard="UTM::Bounces"]')
    UTM_VIEWS_CHBX = (By.CSS_SELECTOR, '[data-dashboard="UTM::Views"]')
    TITLE_UTM_BLOCK = (By.XPATH, '//div[text() = \'Популярные  UTM\']')
    TITLE_UTM_VISITS_INDICATOR = (By.XPATH, '//div[text() = \'Популярные  UTM\']/following::span[text() = \'Визиты\']')
    TITLE_UTM_BOUNCES_INDICATOR = (By.XPATH, '//div[text() = \'Популярные  UTM\']/following::span[text() = \'Отказы\']')
    TITLE_UTM_DEPTH_INDICATOR = (By.XPATH, '//div[text() = \'Популярные  UTM\']/following::span[text() = \'Глубина\']')
    UTM_INDICATORS_RESTRICTION = (By.XPATH, '/*[contains(., \'Можно выбрать не больше трех\')]')