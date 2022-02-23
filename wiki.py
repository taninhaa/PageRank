import wikipediaapi

wiki_wiki=wikipediaapi.Wikipedia('en')
"""
page_py = wiki_wiki.page('Python_(programming_language)')

page_py = wiki_wiki.page('Python_(programming_language)')
print("Page - Exists: %s" % page_py.exists())
# Page - Exists: True

page_missing = wiki_wiki.page('NonExistingPageWithStrangeName')
print("Page - Exists: %s" %     page_missing.exists())
# Page - Exists: False

print("Page - Title: %s" % page_py.title)
# Page - Title: Python (programming language)

print("Page - Summary: %s" % page_py.summary[0:60])
# Page - Summary: Python is a widely used high-level programming language for
"""
page=wiki_wiki.page('Jean-Yves Chemin')
#print("Page - Title: %s" % page.title)
#print("Page - Summary: %s" % page.summary[0:60])

#print(page.fullurl)
# https://en.wikipedia.org/wiki/Python_(programming_language)

#print(page.canonicalurl)
# https://en.wikipedia.org/wiki/Python_(programming_language)

"""def print_links(page):
        links = page.links
        for title in sorted(links.keys()):
            print("%s: %s" % (title, links[title]))

print_links(page)"""

def print_categories(page):
        categories = page.categories
        for title in sorted(categories.keys()):
            print("%s: %s" % (title, categories[title]))


print("Categories")
print_categories(page)