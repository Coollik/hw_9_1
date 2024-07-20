from selene import browser, have

def test_shold_find(browser_open, type_text):
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_shold_not_find(browser_open, type_text):
    browser.element('[id="search"]').should(have.text('BlaBlaBla'))


