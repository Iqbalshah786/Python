cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        cache[url] = "here is the page content..."
        return "The page data is saved in the cache..."

print(get_page("http://www.google.com"))    
print(get_page("http://www.facebook.com"))
print(get_page("http://www.google.com"))

print(cache)