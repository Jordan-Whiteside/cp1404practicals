"""Wikipedia program."""
import wikipedia

is_valid_input = False
while not is_valid_input:
    try:
        page_name = input("Enter page title: ")
        while page_name != "":
            page = wikipedia.page(page_name, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
            print(sep="")
            page_name = input("Enter page title: ")
        is_valid_input = True
    except wikipedia.exceptions.DisambiguationError as exeption:
        print("We need a more specific title. Try one of the following, or a new search:")
        print("(BeautifulSoup warning)")
        print(exeption.options)
    except wikipedia.exceptions.PageError as exeption:
        print(f"Page id \"{page_name}\" does not match any pages. Try another id!")
print("Thank you.")
