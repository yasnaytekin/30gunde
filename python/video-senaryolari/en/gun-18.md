# Video senaryosu: Gün 18, Regular expressions

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~152 sn

In the written cave of Discovery Island, Piko explains building patterns with the re module, and pulling information out of text with findall, search, fullmatch, sub and groups.

Ders metni: [gun-18.md](../../gunler/gun-18.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 13 sn | sasirma (sag) |
| 2 | anlatim | 13 sn | konusma (sag) |
| 3 | anlatim | 15 sn | isaret (sol) |
| 4 | kod | 14 sn | isaret (sag) |
| 5 | kod | 14 sn | isaret (sol) |
| 6 | kod | 16 sn | konusma (sag) |
| 7 | hata | 12 sn | uzgun (sag) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 9 sn | mutlu (sol) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 18: Regular expressions! In this lesson you'll search for patterns in text with the re module, and find and replace information with findall, search and sub.

- What is a pattern?
- findall, search, sub
- Splitting with groups

## Sahne 1: acilis (13 sn)

**Seslendirme:** Hi, I'm Piko! We're in the cave of Discovery Island. The walls are covered in writing, and secret numbers and passwords are hidden somewhere. Reading it all one by one would take days! Luckily, Python has a magnifying glass: regular expressions.

**Ekranda başlık:** Day 18: Regular expressions

**Ekranda maddeler:**

- Discovery Island
- The re module (regex)

**Maskot:** sasirma pozu, sag

## Sahne 2: anlatim (13 sn)

**Seslendirme:** A regular expression is a description of what you're looking for. Like digits next to each other, or a word with the letter e in it. You write the description, and the re module finds it in the text.

**Ekranda başlık:** What is a pattern?

**Ekranda maddeler:**

- Pattern = a description of what you're looking for
- import re
- Put an r before the pattern: r"..."

**Maskot:** konusma pozu, sag

## Sahne 3: anlatim (15 sn)

**Seslendirme:** We use special characters to write descriptions. Backslash d means a digit, and backslash w means a letter or a digit. A plus sign means one or more, and a number in curly braces says exactly how many.

**Ekranda başlık:** Special characters

**Ekranda maddeler:**

- \d digit, \w letter/digit, \s space
- . any character
- + one or more, * zero or more
- {3} exactly 3, [0-9] a range
- ^ start, $ end

**Maskot:** isaret pozu, sol

## Sahne 4: kod (14 sn)

**Seslendirme:** findall gives you every matching piece as a list. The pattern with a plus counts digits next to each other as one piece, so twelve stays whole. The pattern without a plus collects every digit separately.

**Ekranda başlık:** Find the numbers: findall

**Kod** (vurgulanan satırlar: 4, 5):

```python
import re

text = "Piko found 3 apples, 12 gold and 7 potions"
print(re.findall(r"\d+", text))
print(re.findall(r"\d", text))
```

**Çıktı:**

```text
['3', '12', '7']
['3', '1', '2', '7']
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (14 sn)

**Seslendirme:** search finds the first match; here, the first four digits in a row, which is the password. sub replaces everything that matches. I turned all the digits into stars to hide the information.

**Ekranda başlık:** Search and replace: search, sub

**Kod** (vurgulanan satırlar: 4, 5):

```python
import re

msg = "My password is 4821, my phone is 05321234567"
print(re.search(r"\d{4}", msg).group())
print(re.sub(r"\d", "*", msg))
```

**Çıktı:**

```text
4821
My password is ****, my phone is ***********
```

**Maskot:** isaret pozu, sol

## Sahne 6: kod (16 sn)

**Seslendirme:** Parentheses split a pattern into groups. The first group catches the name, the second catches the number, and I take them with group. On a line that doesn't fit the pattern, search gives None, and the if catches that.

**Ekranda başlık:** Split it with groups

**Kod** (vurgulanan satırlar: 4, 6):

```python
import re

for line in ["Ece 45 gold", "Can 7 gold", "wrong line"]:
    m = re.search(r"(\w+) (\d+) gold", line)
    if m:
        print(m.group(1), "->", int(m.group(2)))
    else:
        print("No match:", line)
```

**Çıktı:**

```text
Ece -> 45
Can -> 7
No match: wrong line
```

**Maskot:** konusma pozu, sag

## Sahne 7: hata (12 sn)

**Seslendirme:** Here's the most common mistake: calling group directly when there's no match. If search finds nothing, it returns None, and since None has no group, you get an AttributeError. Check with if m first!

**Ekranda başlık:** Common mistake: None.group()

**Kod** (vurgulanan satırlar: 4):

```python
import re

m = re.search(r"\d+", "no number here")
print(m.group())
```

**Çıktı:**

```text
AttributeError: 'NoneType' object has no attribute 'group'
```

**Maskot:** uzgun pozu, sag

## Sahne 8: soru (10 sn)

**Seslendirme:** Your turn! fullmatch checks whether the whole text fits the pattern. The pattern wants exactly three digits. What do you think the two lines print?

**Ekranda başlık:** What will it print?

**Kod**:

```python
import re

print(bool(re.fullmatch(r"\d{3}", "123")))
print(bool(re.fullmatch(r"\d{3}", "1234")))
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (9 sn)

**Seslendirme:** The first is True, because it's exactly three digits. The second is False: there are four digits, and fullmatch doesn't accept extras.

**Ekranda başlık:** The answer

**Kod**:

```python
import re

print(bool(re.fullmatch(r"\d{3}", "123")))
print(bool(re.fullmatch(r"\d{3}", "1234")))
```

**Çıktı:**

```text
True
False
```

**Maskot:** mutlu pozu, sol

## Sahne 10: gorev (13 sn)

**Seslendirme:** In the tasks you'll find the numbers in a text and add them up, look for an email address, and hide a password. In the project you're writing a function that understands commands like go north three.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Add up the numbers
- Task 2: Is there an email?
- Task 3: Hide the password
- Challenge: Phone number
- Project: Command parser

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** In short: describe the pattern, find them all with findall, catch the first with search, and replace with sub.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- Build patterns with \d, \w, +, {n}
- findall, search, fullmatch, sub
- Groups in parentheses come back with group(1), group(2)

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** We cracked the cave's codes, congratulations! Tomorrow, so we don't lose what we found, we'll learn to write to files and save the game with JSON. See you!

**Ekranda başlık:** Tomorrow: Working with files

**Ekranda maddeler:**

- Write to a file, read from a file
- Save with JSON

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
