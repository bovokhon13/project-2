import random

# Базы данных для генерации истории
characters = ["рыцарь", "маг", "вор", "друид", "варвар", "арбалетчик", "пират", "алхимик", "охотник", "паладин"]
locations = ["лес", "замок", "пещера", "деревня", "горы", "пустыня", "болото", "подземелье", "порт", "древний храм"]
events = [
    "нашел древний артефакт", "встретил дракона", "спас принцессу", "победил армию скелетов", 
    "нашел тайную библиотеку", "столкнулся с загадочным незнакомцем", "обнаружил портал в другой мир",
    "был предан своим союзником", "нашел карту сокровищ", "попал в ловушку древнего культа",
    "столкнулся с мистическим существом", "нашел затерянный город", "обнаружил древний рунический камень"
]
dialogs = [
    "Что это было?!", "Я не могу поверить в это!", "Этот день станет легендой!", 
    "Кто бы мог подумать?", "Мы должны двигаться дальше!", "Это слишком опасно!", 
    "У нас нет выбора...", "Следуй за мной!", "Мы близки к цели!", "Это только начало!"
]
enemies = ["дракон", "орк", "гоблин", "скелет", "демон", "вампир", "гигантский паук", "тролль", "зомби", "химера"]
items = ["меч", "щит", "лук", "зелье здоровья", "магический амулет", "ключ от древнего храма", "карта сокровищ", "доспехи", "кинжал", "посох мага"]
quests = [
    "найти древний артефакт", "спасти деревню от бандитов", "уничтожить злого колдуна", 
    "найти пропавшего кузнеца", "разгадать тайну древнего храма", "собрать редкие травы для зелья",
    "найти сокровища пиратов", "очистить лес от монстров", "найти легендарное оружие"
]

# Класс для персонажа
class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.strength = random.randint(10, 20)
        self.magic = random.randint(10, 20) if character_class in ["маг", "друид", "алхимик"] else 0
        self.inventory = []

    def __str__(self):
        return f"{self.name} ({self.character_class})"

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        return f"Инвентарь {self.name}: {', '.join(self.inventory) if self.inventory else 'пуст'}"

# Класс для локации
class Location:
    def __init__(self, name):
        self.name = name
        self.description = f"Вы находитесь в {name}. Вокруг вас {random.choice(['тишина', 'шум ветра', 'шелест листьев', 'звуки животных', 'шум воды', 'грохот камней'])}."

    def __str__(self):
        return self.description

# Класс для события
class Event:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

# Функция для генерации случайной истории
def generate_story():
    # Создаем главного героя
    hero = Character(random.choice(["Альберт", "Лиана", "Гарольд", "Эльза", "Джек", "Мира", "Тор", "Люциус"]), random.choice(characters))
    
    # Создаем союзника
    ally = Character(random.choice(["Элис", "Боб", "Карл", "Дина", "Финн", "Грейс"]), random.choice(characters))
    
    # Создаем врага
    enemy = random.choice(enemies)
    
    # Создаем несколько локаций
    location1 = Location(random.choice(locations))
    location2 = Location(random.choice(locations))
    location3 = Location(random.choice(locations))
    location4 = Location(random.choice(locations))
    
    # Создаем несколько событий
    event1 = Event(random.choice(events))
    event2 = Event(random.choice(events))
    event3 = Event(random.choice(events))
    event4 = Event(random.choice(events))
    
    # Генерация диалогов
    dialog1 = random.choice(dialogs)
    dialog2 = random.choice(dialogs)
    dialog3 = random.choice(dialogs)
    dialog4 = random.choice(dialogs)
    dialog5 = random.choice(dialogs)
    
    # Создаем квест
    quest = random.choice(quests)
    
    # Собираем историю
    story = []
    story.append(f"Однажды {hero} отправился в {location1.name}.")
    story.append(location1.description)
    story.append(f"Внезапно {hero.name} {event1.description}!")
    story.append(f"{hero.name} воскликнул: '{dialog1}'")
    story.append(f"Спутник {ally.name} ответил: '{dialog2}'")
    
    story.append(f"После этого {hero.name} и {ally.name} отправились в {location2.name}.")
    story.append(location2.description)
    story.append(f"Там они {event2.description}!")
    story.append(f"{ally.name} сказал: '{dialog3}'")
    
    story.append(f"Вскоре они достигли {location3.name}, где их ждал {enemy}.")
    story.append(location3.description)
    story.append(f"{hero.name} и {ally.name} вступили в бой с {enemy}.")
    
    # Результат битвы
    if random.choice([True, False]):
        story.append(f"После долгого боя {hero.name} и {ally.name} победили {enemy}!")
        story.append(f"В награду они нашли {random.choice(items)}.")
        hero.add_item(random.choice(items))
        ally.add_item(random.choice(items))
    else:
        story.append(f"К сожалению, {hero.name} и {ally.name} не смогли победить {enemy} и были вынуждены отступить.")
    
    story.append(f"После этого они решили отправиться в {location4.name}, чтобы выполнить квест: {quest}.")
    story.append(location4.description)
    story.append(f"Там они {event4.description}!")
    story.append(f"{hero.name} сказал: '{dialog4}'")
    story.append(f"{ally.name} ответил: '{dialog5}'")
    
    # Финал истории
    if random.choice([True, False]):
        story.append(f"{hero.name} и {ally.name} успешно выполнили квест и стали героями!")
    else:
        story.append(f"К сожалению, {hero.name} и {ally.name} не смогли выполнить квест и вернулись домой с пустыми руками.")
    
    story.append(hero.show_inventory())
    story.append(ally.show_inventory())
    
    return "\n".join(story)

# Функция для вывода меню
def show_menu():
    print("Добро пожаловать в генератор случайных историй!")
    print("1. Сгенерировать историю")
    print("2. Выйти")

# Основной цикл программы
def main():
    while True:
        show_menu()
        choice = input("Выберите действие: ")
        
        if choice == "1":
            story = generate_story()
            print("\n=== Ваша история ===\n")
            print(story)
            print("\n====================\n")
        elif choice == "2":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

