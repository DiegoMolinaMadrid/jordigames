import random
import os
from palabras import palabrasDif
from palabras import palabrasFac
from palabras import palabrasMed


while True:
    os.system('cls')
    #Randoms faciles.
    random1 = random.randint(0, len(palabrasFac)-1)
    random12 = random.randint(0, len(palabrasFac)-1)
    random13 = random.randint(0, len(palabrasFac)-1)
    random14 = random.randint(0, len(palabrasFac)-1)

    while random1 == random12 or random1 == random13 or random1 == random14 or random12 == random13 or random12 == random14 or random13 == random14:
        random1 = random.randint(0, len(palabrasFac)-1)
        random12 = random.randint(0, len(palabrasFac)-1)
        random13 = random.randint(0, len(palabrasFac)-1)
        random14 = random.randint(0, len(palabrasFac)-1)
    else:
        pass

    #Randoms medias.
    random2 = random.randint(0, len(palabrasMed)-1)
    random22 = random.randint(0, len(palabrasMed)-1)
    random23 = random.randint(0, len(palabrasMed)-1)
    while random2 == random22 or random2 == random23 or random22 == random23:
        random2 = random.randint(0, len(palabrasMed)-1)
        random22 = random.randint(0, len(palabrasMed)-1)
        random23 = random.randint(0, len(palabrasMed)-1)
    else:
        pass

    #Randoms dificiles.
    random3 = random.randint(0, len(palabrasDif)-1)
    random32 = random.randint(0, len(palabrasDif)-1)
    while random3 == random32:
        random3 = random.randint(0, len(palabrasDif)-1)
        random32 = random.randint(0, len(palabrasDif)-1)
    else:
        pass



    #Aquí van las palabras FÁCILES:
    p2 = palabrasFac[random1]
    p4 = palabrasFac[random12]
    p6 = palabrasFac[random13]
    p8 = palabrasFac[random14]

    #Aquí van las palabras MEDIAS:
    p1 = palabrasMed[random2]
    p5 = palabrasMed[random22]
    p9 = palabrasMed[random23]

    #Aquí van las palabras DIFÍCILES:
    p3 = palabrasDif[random3]
    p7 = palabrasDif[random3]



    print(f"1. {p1}, 2. {p2}, 3. {p3}")
    print(f"4. {p4}, 5. {p5}, 6. {p6}")
    print(f"7. {p7}, 8. {p8}, 9. {p9}")
    input()
