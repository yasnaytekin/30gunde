# Video senaryosu: Gün 17, Error handling

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~148 sn

On the rotten bridges of Discovery Island, Piko shows how to catch errors with try, except, else and finally, and how to raise his own errors.

Ders metni: [gun-17.md](../../gunler/gun-17.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | konusma (sag) |
| 2 | hata | 11 sn | uzgun (sag) |
| 3 | kod | 15 sn | isaret (sag) |
| 4 | kod | 15 sn | isaret (sol) |
| 5 | anlatim | 10 sn | dusunme (sag) |
| 6 | kod | 14 sn | konusma (sag) |
| 7 | kod | 15 sn | isaret (sol) |
| 8 | soru | 9 sn | dusunme (sag) |
| 9 | cikti | 9 sn | mutlu (sol) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 17: Error handling! In this lesson you'll catch errors with try and except, tidy up with else and finally, and raise your own errors.

- try and except
- else and finally
- Your own errors with raise

## Sahne 1: acilis (14 sn)

**Seslendirme:** Hi, I'm Piko! The bridges on Discovery Island might be rotten. A smart explorer ties a rope around their waist at every step. So can your program hold on to a rope instead of crashing when it hits an error? Yes! Today we learn error handling.

**Ekranda başlık:** Day 17: Error handling

**Ekranda maddeler:**

- Discovery Island
- try, except, else, finally, raise

**Maskot:** konusma pozu, sag

## Sahne 2: hata (11 sn)

**Seslendirme:** First let's see it without a rope. I'm trying to turn twelve, written out in letters, into a number with int. Python gives a ValueError and stops the program right there.

**Ekranda başlık:** No rope: the program crashes

**Kod** (vurgulanan satırlar: 2):

```python
text = "twelve"
age = int(text)
print("Your age:", age)
```

**Çıktı:**

```text
ValueError: invalid literal for int() with base 10: 'twelve'
```

**Maskot:** uzgun pozu, sag

## Sahne 3: kod (15 sn)

**Seslendirme:** Now I tie the rope. I put the code that might fail inside try, and what to do if it fails inside except. When the conversion fails, except runs, and the program keeps going without crashing.

**Ekranda başlık:** try and except

**Kod** (vurgulanan satırlar: 2, 5):

```python
text = "twelve"
try:
    age = int(text)
    print("Your age:", age)
except ValueError:
    print("Please write it in digits.")
print("The program keeps going.")
```

**Çıktı:**

```text
Please write it in digits.
The program keeps going.
```

**Maskot:** isaret pozu, sag

## Sahne 4: kod (15 sn)

**Seslendirme:** Every error has a name. Here I wrote two separate excepts: ValueError for text that isn't a number, and ZeroDivisionError for dividing by zero. I give each one its own answer.

**Ekranda başlık:** Which error are you catching?

**Kod** (vurgulanan satırlar: 4, 6):

```python
for text in ["5", "0", "five"]:
    try:
        print(100 / int(text))
    except ValueError:
        print("Not a number!")
    except ZeroDivisionError:
        print("Can't divide by zero!")
```

**Çıktı:**

```text
20.0
Can't divide by zero!
Not a number!
```

**Maskot:** isaret pozu, sol

## Sahne 5: anlatim (10 sn)

**Seslendirme:** A warning: writing a bare except to catch every error is easy, but it hides real bugs too. Always write the name of the error you expect.

**Ekranda başlık:** Tip

**Ekranda maddeler:**

- except: catches everything, hides bugs
- except ValueError: catches only what you expect
- To see the message: except ValueError as err

**Maskot:** dusunme pozu, sag

## Sahne 6: kod (14 sn)

**Seslendirme:** There are two more helpers. else runs when there's no error at all. finally always runs, error or not; it's perfect for wrapping things up.

**Ekranda başlık:** else and finally

**Kod** (vurgulanan satırlar: 5, 7):

```python
try:
    n = int("5")
except ValueError:
    print("Error!")
else:
    print("Success:", n)
finally:
    print("Check done.")
```

**Çıktı:**

```text
Success: 5
Check done.
```

**Maskot:** konusma pozu, sag

## Sahne 7: kod (15 sn)

**Seslendirme:** Sometimes we throw an error on purpose. The set_hp function raises a ValueError if it gets negative health. Outside, I catch it and print its message with as err.

**Ekranda başlık:** raise: throw your own error

**Kod** (vurgulanan satırlar: 3, 8):

```python
def set_hp(value):
    if value < 0:
        raise ValueError("Health can't be negative")
    return value

try:
    set_hp(-5)
except ValueError as err:
    print("Caught:", err)
```

**Çıktı:**

```text
Caught: Health can't be negative
```

**Maskot:** isaret pozu, sol

## Sahne 8: soru (9 sn)

**Seslendirme:** Mini question! There's no error here; the number converts just fine. Which lines do you think show up on the screen?

**Ekranda başlık:** What will it print?

**Kod**:

```python
try:
    n = int("7")
except ValueError:
    print("Error!")
else:
    print("Number:", n)
finally:
    print("Done.")
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (9 sn)

**Seslendirme:** Since there was no error, except was skipped and else ran. And finally came at the very end, as always.

**Ekranda başlık:** The answer

**Kod**:

```python
try:
    n = int("7")
except ValueError:
    print("Error!")
else:
    print("Number:", n)
finally:
    print("Done.")
```

**Çıktı:**

```text
Number: 7
Done.
```

**Maskot:** mutlu pozu, sol

## Sahne 10: gorev (13 sn)

**Seslendirme:** Your tasks are ready! You'll write a number converter that doesn't crash, a safe division that uses try, and a program that asks your age. In the project, the player's mistyped commands won't break the game.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Safe number
- Task 2: Safe division
- Task 3: Ask the age
- Challenge: Protect with raise
- Project: Sturdy commands

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** In short: try it with try, catch it with except, tidy up with else and finally, and warn yourself with raise when you need to.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- An error inside try is caught by except
- else runs if there's no error, finally always runs
- raise throws a clear error of your own

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** You're awesome! Tomorrow we go into the island's cave. The walls hide secret numbers and passwords. To find them, we'll use Python's magnifying glass: regular expressions. See you!

**Ekranda başlık:** Tomorrow: Regular expressions

**Ekranda maddeler:**

- The re module
- Searching text for patterns

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
