# -*- coding: utf-8 -*-


BASE_SELECTORS = {
    'canonical_url': ['link[rel="canonical"]', 'href'],
    'description': ['meta[name="description"]', 'content'],
    'twitter_card': ['meta[name="twitter:card"]', 'content'],
    'twitter_site': ['meta[name="twitter:site"]', 'content'],
}


class BasePageObject(object):
    def __init__(self, driver):
        self.driver = driver
        for attr, args in BASE_SELECTORS.items():
            setattr(self, attr, get_attribute_from_selector(self.driver,
                                                            *args))

    def __repr__(self):
        return '{0} at {1}'.format(self.__class__.__name__,
                                   self.driver.current_url())

    @property
    def title(self):
        return self.driver.browser.title
        
def get_attribute_from_selector(driver, selector, attribute):
    return driver.find(selector, only_displayed=False).attribute(attribute)
