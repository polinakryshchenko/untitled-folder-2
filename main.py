import colorama

# Інтроспекція атрибутів та методів
#print(dir(colorama))
#Бібліотека colorama дозволяє додавати кольори та стилі до текстового виводу у консолі, що корисно для поліпшення читабельності та виділення важливих повідомлень.
#Користуючись атрибутами Fore, Back та Style, можна змінювати колір тексту, фону та стиль виводу.

from colorama import Fore, Back, Style, init

# Ініціалізація colorama
init()

def print_colored_text():
    print(Fore.RED + "Це текст з червоним кольором" + Style.RESET_ALL)
    print(Back.GREEN + "Це текст з зеленим фоном" + Style.RESET_ALL)
    print(Fore.BLUE + Back.YELLOW + Style.BRIGHT + "Це текст з синім текстом, жовтим фоном та яскравим стилем" + Style.RESET_ALL)
print_colored_text()