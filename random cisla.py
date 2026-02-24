import random
x = 0
def setup():
    global x
    try:
        print("#"*40)
        x1 = int(input("Zadejte od jakého čísla chcete hádat: ").replace(" ", ""))
        print("-"*40)
        x2 = int(input("Zadejte do jakého čísla chcete hádat: ").replace(" ", ""))
        
        if x1 > x2:
            print("-"*40)
            print("První číslo musí být menší nebo rovno druhému.")
            return None
            
    except ValueError:
        print("-"*40)
        print("Neplatný vstup. Zadejte prosím celé číslo.")
        return None
    print("-"*40)
    print(f"Zkuste uhádnout náhodné číslo od {x1} do {x2}")
    x = random.randint(x1, x2)

def guess(secret_number):
    while True:
        try:
            print("-"*40)
            y = int(input("Zadejte svůj tip: ").replace(" ", ""))
            
            if y < secret_number:
                print("-"*40)
                print("Příliš nízké, zkuste to znovu.")
            elif y > secret_number:
                print("-"*40)
                print("Příliš vysoké, zkuste to znovu.")
            else:
                print("-"*40)
                print("Gratulujeme! Uhodli jste správné číslo!")
                break
                
        except ValueError:
            print("-"*40)
            print("Neplatný vstup. Zadejte prosím celé číslo.")


while True:
    setup()
    if x is not None:
        guess(x)
    print("-"*40)
    print("Chcete hrát znovu? (ano/ne)")
    if input().lower() not in ["ano", "jo", "yes"]:
        break
