def domain_name(url):
    elements = url.replace("https://", "").replace("http://", "").split(".")
    return elements[0] if elements[0] != "www" else elements[1]


# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"