def domain_name(url):
    url = url.replace("http://", "").replace("https://",
                                             "").replace("www.", "")
    urlDot = url.find(".")
    url = url[0:urlDot]
    return url


print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
