# Video senaryosu: Gün 4, Strings

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~122 sn

Using the signs of Python Village, Piko explains joining strings, indexes and slices, string methods, and formatting with f-strings.

Ders metni: [gun-04.md](../../gunler/gun-04.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | mutlu (sag) |
| 2 | kod | 12 sn | isaret (sag) |
| 3 | kod | 14 sn | isaret (sag) |
| 4 | kod | 14 sn | konusma (sag) |
| 5 | kod | 11 sn | mutlu (sag) |
| 6 | hata | 11 sn | sasirma (sag) |
| 7 | soru | 10 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 13 sn | isaret (sol) |
| 10 | ozet | 7 sn | on (sag) |
| 11 | kapanis | 8 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 4: Strings! In this lesson you'll join text, slice it letter by letter, and decorate it with f-strings.

- Joining and repeating
- Indexes and slices
- Methods and f-strings

## Sahne 1: acilis (12 sn)

**Seslendirme:** Hi, I'm Piko! Python Village is full of signs, conversations and letters. In games, characters talk and names shine on the screen. Today we play with text, which we call strings. Want to print a word backwards?

**Ekranda başlık:** Day 4: Strings

**Görsel:** `gorseller/python/harita/koy.webp`

**Maskot:** mutlu pozu, sag

## Sahne 2: kod (12 sn)

**Seslendirme:** A string is a sequence of characters inside quotes. You join strings with plus, repeat them with a star, and measure how many characters they have with len. Spaces and apostrophes count too!

**Ekranda başlık:** Join and repeat

**Kod**:

```python
first = "Pi"
second = "ko"
print(first + second)
print("ha" * 3)
print(len("Piko's Adventure"))
```

**Çıktı:**

```text
Piko
hahaha
16
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (14 sn)

**Seslendirme:** Every letter has a position number, and counting starts at zero. Minus one gives the last letter. A slice from zero to three doesn't include three. And with a step of minus one, the word flips backwards!

**Ekranda başlık:** Indexes and slices

**Kod** (vurgulanan satırlar: 3, 4):

```python
word = "Python"
print(word[0], word[-1])
print(word[0:3])
print(word[::-1])
```

**Çıktı:**

```text
P n
Pyt
nohtyP
```

**Maskot:** isaret pozu, sag

## Sahne 4: kod (14 sn)

**Seslendirme:** Strings come with their own tools, called methods. strip removes spaces at the edges, upper makes everything uppercase, title capitalizes each word, count counts, and replace swaps one piece of text for another.

**Ekranda başlık:** String methods

**Kod** (vurgulanan satırlar: 5):

```python
name = "  piko  "
print(name.strip().upper())
print("python village".title())
print("banana".count("a"))
print("hello world".replace("world", "Piko"))
```

**Çıktı:**

```text
PIKO
Python Village
3
hello Piko
```

**Maskot:** konusma pozu, sag

## Sahne 5: kod (11 sn)

**Seslendirme:** My favorite tool: the f-string! Put an f before the quotes, and variables inside curly braces are replaced by their values. You can even call a method inside the braces.

**Ekranda başlık:** f-strings

**Kod** (vurgulanan satırlar: 3, 4):

```python
name = "Piko"
gold = 42
print(f"{name} carries {gold} gold coins.")
print(f"{name.upper()} is coming!")
```

**Çıktı:**

```text
Piko carries 42 gold coins.
PIKO is coming!
```

**Maskot:** mutlu pozu, sag

## Sahne 6: hata (11 sn)

**Seslendirme:** Try to join text and a number with plus, and Python gives you a TypeError again: you can only add text to text. Your rescuers are ready: an f-string or the str function.

**Ekranda başlık:** Text + number = TypeError

**Kod** (vurgulanan satırlar: 3):

```python
name = "Piko"
level = 3
print(name + " level " + level)
```

**Çıktı:**

```text
TypeError: can only concatenate str (not "int") to str
```

**Düzeltilmiş kod:**

```python
name = "Piko"
level = 3
print(f"{name} level {level}")
```

**Düzeltilmiş çıktı:**

```text
Piko level 3
```

**Maskot:** sasirma pozu, sag

## Sahne 7: soru (10 sn)

**Seslendirme:** A hint: in asks whether one piece of text is inside another. Now tell me: what does this code print?

**Ekranda başlık:** What will it print?

**Kod**:

```python
word = "Python"
print(word[1:4])
print("th" in word)
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** The slice from one to four: y, t, h. Four isn't included! And yes, t h appears in the word, so in says True.

**Ekranda başlık:** The answer

**Kod**:

```python
word = "Python"
print(word[1:4])
print("th" in word)
```

**Çıktı:**

```text
yth
True
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (13 sn)

**Seslendirme:** In the tasks you'll write a sign in shouting capital letters, catch the first and last letter of a name, and build a level message with an f-string. In the challenge you'll hunt words that read the same backwards, like level!

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: The sign
- Task 2: First and last letter
- Task 3: Level message
- Stage task: Piko at the castle
- Challenge: Palindrome hunter

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (7 sn)

**Seslendirme:** Today we joined text, sliced it letter by letter, changed it with methods and decorated it with f-strings.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- + joins, * repeats, len() measures
- Indexes start at 0; [0:3] slices, [::-1] reverses
- upper, title, strip, count and f-strings

**Maskot:** on pozu, sag

## Sahne 11: kapanis (8 sn)

**Seslendirme:** You're the village's word master! Tomorrow we enter the Data Forest and gather everything in the hero's bag into a single list.

**Ekranda başlık:** Tomorrow: Lists

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
