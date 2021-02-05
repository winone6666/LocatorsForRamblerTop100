from selenium.webdriver.common.by import By

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

class AnalyticsCategoryPageLocators:

class AnalyticsDashboardPageLocators:
    CATEGORY_TECHNOLOGY_BTN = (By.CSS_SELECTOR, '[data-newreport="reports::technology"]')
    TECHNOLOGY_BROWSER_BTN = (By.CSS_SELECTOR, '[data-newreport="reports::technology::browser"]')
    ADD_UTM_METRICS_BTN = (By.CSS_SELECTOR, '[data-dashboard="UTM::add_metrics"]')