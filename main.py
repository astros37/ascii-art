from pyfiglet import Figlet

def create_banner(text):
    figlet = Figlet(font='slant')
    banner = figlet.renderText(text)
    with open("banner.txt", "w") as file:
        file.write(banner)
    print(banner)

if __name__ == "__main__":
    user_text = input("Введіть текст для банера: ")
    create_banner(user_text)
