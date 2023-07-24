from playwright.sync_api import Page


def test_violations_same(page: Page, axe_pytest_snapshot):
    page.goto("https://www.example.com")
    axe_pytest_snapshot(page)


def test_violations_new(page: Page, axe_pytest_snapshot):
    page.goto("https://www.example.com")
    try:
        axe_pytest_snapshot(page)
    except AssertionError as err:
        assert (
            str(err)
            == """\

New violations found: html-has-lang (serious)
That's bad news! 😱 Either fix the issue or run `pytest --snapshot-update` to update the snapshots.
Rule Violated:
html-has-lang - Ensures every HTML document has a lang attribute
	URL: https://dequeuniversity.com/rules/axe/4.4/html-has-lang?application=axeAPI
	Impact Level: serious
	Tags: ['cat.language', 'wcag2a', 'wcag311', 'ACT']
	Elements Affected:


	1)	Target: html
		Snippet: <html>
		Messages:
		* The <html> element does not have a lang attribute
"""
        )


def test_violations_fixed(page: Page, axe_pytest_snapshot):
    page.goto("https://www.example.com")
    try:
        axe_pytest_snapshot(page)
    except AssertionError as err:
        assert (
            str(err)
            == """\

Old violations no longer found: color-contrast (moderate).
That's good news! 🎉 Run `pytest --snapshot-update` to update the snapshots.
"""
        )


def test_violations_more_instances(page: Page, axe_pytest_snapshot):
    page.goto("https://www.example.com")
    try:
        axe_pytest_snapshot(page)
    except AssertionError as err:
        assert (
            str(err)
            == """\

Additional instances of existing violations were found: html-has-lang (serious)
That's bad news! 😱 Either fix the issue or run `pytest --snapshot-update` to update the snapshots.
Rule Violated:
html-has-lang - Ensures every HTML document has a lang attribute
	URL: https://dequeuniversity.com/rules/axe/4.4/html-has-lang?application=axeAPI
	Impact Level: serious
	Tags: ['cat.language', 'wcag2a', 'wcag311', 'ACT']
	Elements Affected:


	1)	Target: html
		Snippet: <html>
		Messages:
		* The <html> element does not have a lang attribute
"""
        )


def test_violations_fewer_instances(page: Page, axe_pytest_snapshot):
    page.goto("https://www.example.com")
    try:
        axe_pytest_snapshot(page)
    except AssertionError as err:
        assert (
            str(err)
            == """\

Fewer instances of existing violations were found: region (moderate).
That's good news! 🎉 Run `pytest --snapshot-update` to update the snapshots.
"""
        )
