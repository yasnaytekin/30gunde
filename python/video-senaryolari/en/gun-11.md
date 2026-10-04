# Video senaryosu: Gün 11, Functions

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~135 sn

In the Tool Workshop, Piko shows how to build your own tools: defining functions with def, parameters, returning results with return, default values, and *args.

Ders metni: [gun-11.md](../../gunler/gun-11.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 13 sn | mutlu (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 10 sn | konusma (sag) |
| 4 | kod | 13 sn | isaret (sag) |
| 5 | kod | 11 sn | konusma (sag) |
| 6 | kod | 11 sn | mutlu (sag) |
| 7 | hata | 13 sn | sasirma (sag) |
| 8 | soru | 9 sn | dusunme (sag) |
| 9 | cikti | 10 sn | mutlu (sag) |
| 10 | gorev | 13 sn | isaret (sol) |
| 11 | ozet | 8 sn | on (sag) |
| 12 | kapanis | 10 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 11: Functions! In this lesson you'll write your own functions with def, give them parameters, and get results back with return.

- Writing functions with def
- Parameters and return
- Default values and *args

## Sahne 1: acilis (13 sn)

**Seslendirme:** Hi, I'm Piko! Welcome to the Tool Workshop. Every tool here has a job: a hammer hammers, a saw cuts. A tool you make once can be used again and again. The same is possible in code! We call these tools functions.

**Ekranda başlık:** Day 11: Functions

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** mutlu pozu, sag

## Sahne 2: kod (14 sn)

**Seslendirme:** With def you make your own function. The lines inside are indented, and they don't run until the function is called. Wherever you write its name and parentheses, it gets to work: here, twice.

**Ekranda başlık:** Defining a function with def

**Kod** (vurgulanan satırlar: 1, 4, 5):

```python
def greet():
    print("Hello!")

greet()
greet()
```

**Çıktı:**

```text
Hello!
Hello!
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (10 sn)

**Seslendirme:** The names inside the parentheses are parameters. When you call the function, you put values into these boxes. The same tool gives different results with different materials.

**Ekranda başlık:** Parameters

**Kod** (vurgulanan satırlar: 1, 4, 5):

```python
def greet(name):
    print(f"Hello {name}, welcome to the workshop!")

greet("Piko")
greet("Deniz")
```

**Çıktı:**

```text
Hello Piko, welcome to the workshop!
Hello Deniz, welcome to the workshop!
```

**Maskot:** konusma pozu, sag

## Sahne 4: kod (13 sn)

**Seslendirme:** print only writes the result on the screen. return hands the result back to where the function was called, so you can put it in a variable and use it again. Careful: once return runs, the function stops right there.

**Ekranda başlık:** return: hand back the result

**Kod** (vurgulanan satırlar: 2, 4):

```python
def add(a, b):
    return a + b

total = add(3, 4)
print(total * 2)
```

**Çıktı:**

```text
14
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (11 sn)

**Seslendirme:** If you give a parameter a default value, you don't have to write that value when you call it. If no amount is given, twenty is used; if you give one, yours wins.

**Ekranda başlık:** Default values

**Kod** (vurgulanan satırlar: 1):

```python
def heal(hp, amount=20):
    return hp + amount

print(heal(50))
print(heal(50, 5))
```

**Çıktı:**

```text
70
55
```

**Maskot:** konusma pozu, sag

## Sahne 6: kod (11 sn)

**Seslendirme:** For functions that take as many values as you like, we use a starred parameter. All the numbers that come in are gathered in a tuple, and we add them all up with a loop.

**Ekranda başlık:** *args: as many values as you like

**Kod** (vurgulanan satırlar: 1):

```python
def total(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result

print(total(1, 2, 3, 4))
```

**Çıktı:**

```text
10
```

**Maskot:** mutlu pozu, sag

## Sahne 7: hata (13 sn)

**Seslendirme:** The most common mix-up: writing print instead of return. The function prints seven on the screen but gives nothing back, so it returns None. Python can't multiply None by two, so we get a TypeError.

**Ekranda başlık:** print or return?

**Kod** (vurgulanan satırlar: 2, 5):

```python
def add(a, b):
    print(a + b)

total = add(3, 4)
print(total * 2)
```

**Çıktı:**

```text
7
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```

**Maskot:** sasirma pozu, sag

## Sahne 8: soru (9 sn)

**Seslendirme:** You can pass a function's result back into the same function. What do you think this code prints? Does Hello get printed?

**Ekranda başlık:** What will it print?

**Kod**:

```python
def double(x):
    return x * 2
    print("Hello")

print(double(double(3)))
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (10 sn)

**Seslendirme:** Twelve! The inner call gave six, and the outer one turned it into twelve. Hello was never printed, because once return runs, the function stops right there.

**Ekranda başlık:** The answer

**Kod** (vurgulanan satırlar: 2, 3):

```python
def double(x):
    return x * 2
    print("Hello")

print(double(double(3)))
```

**Çıktı:**

```text
12
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** In the tasks you'll write a greeting function, return the area of a rectangle, and give an attack a default damage. In the stage task you'll build an army factory. And in the challenge you'll find the highest score without using max.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Greeting function
- Task 2: Area calculator
- Task 3: Default damage
- Stage task: Army factory
- Challenge: Highest score

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (8 sn)

**Seslendirme:** Today we built our own tools: we gave them materials, got their results back, and added default settings.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- Define with def, call it by name
- Parameters are the materials, return is the result
- Default value: amount=20; many values: *args

**Maskot:** on pozu, sag

## Sahne 12: kapanis (10 sn)

**Seslendirme:** Your first tools are ready, congratulations! Tomorrow we open the workshop's giant tool cabinet: modules written by other makers. We'll roll dice and create random events.

**Ekranda başlık:** Tomorrow: Modules

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
