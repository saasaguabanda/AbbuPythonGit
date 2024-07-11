def greet(lang):
    if lang == 'spanish':
        return "Hola"
    elif lang == 'french':
        return "Bonjour"
    else:
        return "Hello"

lang = input('Write either english, spanish, or french: ')
name = input('What is your name? ')

greet(lang)
print(greet(lang),name)


#alternate use of arguments
def hello(to):
    print("hello, ",to)
name = input("What is your name? ")
hello(name)