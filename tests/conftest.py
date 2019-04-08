# Third party modules
from elementium.drivers.se import SeElements

# Own
import pytest

@pytest.fixture(scope='session', autouse=True)
def driver_get(request):
    from selenium import webdriver
    driver = SeElements(webdriver.Chrome())
    session = request.node

    def exit():
        driver.browser.close()
        driver.browser.quit()

    request.addfinalizer(exit)

    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, 'driver', driver)


@pytest.fixture(scope='class', autouse=True)
def get_page_object(request):
    if callable(getattr(request.cls, 'get_url', None)):
        request.cls.driver.navigate(request.cls.get_url())
    elif getattr(request.cls, 'URL', None):
        request.cls.driver.navigate(request.cls.URL)

    if getattr(request.cls, 'PAGE_OBJECT_CLASS', None):
        setattr(request.cls, 'page_object', request.cls.PAGE_OBJECT_CLASS(request.cls.driver))
