import cgi
import http.cookies
import os

def get_cookie_value(cookie, key):
    cookies = http.cookies.SimpleCookie(cookie)
    return cookies.get(key)

def set_cookie(key, value):
    cookie = http.cookies.SimpleCookie()
    cookie[key] = value
    print(cookie)

def delete_cookie(key):
    print(f"Set-Cookie: {key}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/") 

cookie_string = os.environ.get('HTTP_COOKIE', '')
form_counter_cookie = get_cookie_value(cookie_string, 'form_counter')

form_counter = int(form_counter_cookie.value) if form_counter_cookie else 0

form = cgi.FieldStorage()
name = form.getvalue("name")
gender = form.getvalue("gender")
favorite_animals = form.getlist("animals")
favorite_mongt = form.getvalue("month")

if form.getvalue('delete_cookies'):
    delete_cookie('form_counter')
    form_counter = 0
else:
    form_counter += 1
    set_cookie('form_counter', form_counter)

print("Content-type: text/html")
print("Set-Cookie: form_counter={}; path=/".format(form_counter))
print()

arr_print = "<html><head><title>Results</title></head><body><h1>Results:</h1>" + f"<p>Name: {name}</p>" + f"<p>Gender: {gender} </p>" + "<p>Favorite animals: " + f", ".join(favorite_animals) + "</p>" + f"<p>Favorite month on year: {favorite_mongt} </p>" + f"<p>Forms filled out by user: {form_counter}</p>" + "<form action='process_form.py' method='post'> <input type='submit' value='Delete Cookies' name='delete_cookies'></form></body></html>"
print(arr_print)
