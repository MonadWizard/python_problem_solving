
# স্ট্রাইভার A2Z: প্যাটার্ন প্রিন্টিং – বাংলায় ব্যাখ্যা ও পাইথন সমাধান

> **উদ্দেশ্য**: নেস্টেড লুপ, স্পেস/ক্যারেক্টার গণনা, ইন্ডেক্সিং—এই বেসিক স্কিলগুলো শক্ত করতে ২২টি প্যাটার্ন একে একে কিভাবে চিন্তা করে সমাধান করবেন, তার বাংলা ব্যাখ্যা ও পাইথন কোড।  
> **ইনপুট কনভেনশন**: প্রতিটি উদাহরণে `n` ইনপুট ধরা হয়েছে (সাধারণত সারি/উচ্চতা)।

---

## 1) Solid Rectangle (স্টার রেক্ট্যাঙ্গল)

```
***** 
***** 
***** 
***** 
***** 
```
**ভাবনা**: `rows = n`, `cols = n` (বা আলাদা ইনপুট)। প্রতিটি সারিতে `cols` সংখ্যক `*`।  
**আইডিয়া**: দুইটা লুপ—বাইরে সারি, ভিতরে কলাম।

```python
def pattern1(n, m=None):
    """n rows, m cols (default m=n)"""
    m = m or n
    for _ in range(n):
        print("*" * m)
```

---

## 2) Right-Angled Triangle (বাড়তে থাকা স্টার)

```
*
**
***
****
*****
```
**ভাবনা**: i-তম সারিতে `i`টি `*`।  
**ফর্মুলা**: সারি `i` → `'*' * i`

```python
def pattern2(n):
    for i in range(1, n+1):
        print("*" * i)
```

---

## 3) Number Triangle (১ থেকে ক্রমবর্ধমান)

```
1
12
123
1234
12345
```
**ভাবনা**: i-তম সারিতে ১..i। `join` বা লুপ।

```python
def pattern3(n):
    for i in range(1, n+1):
        row = "".join(str(x) for x in range(1, i+1))
        print(row)
```

---

## 4) Repeated Number Triangle (একই সংখ্যা রিপিট)

```
1
22
333
4444
55555
```
**ভাবনা**: i-তম সারিতে i বার i।

```python
def pattern4(n):
    for i in range(1, n+1):
        print(str(i) * i)
```

---

## 5) Inverted Right Triangle (কমতে থাকা স্টার)

```
*****
****
***
**
*
```
**ভাবনা**: প্রথম সারি `n` স্টার, পরে এক করে কমবে।

```python
def pattern5(n):
    for i in range(n, 0, -1):
        print("*" * i)
```

---

## 6) Inverted Numbered Triangle (প্রিফিক্স কমতে থাকা)

```
12345
1234
123
12
1
```
**ভাবনা**: প্রথম সারি ১..n, পরে শেষ সংখ্যা বাদ।

```python
def pattern6(n):
    for i in range(n, 0, -1):
        row = "".join(str(x) for x in range(1, i+1))
        print(row)
```

---

## 7) Centered Star Pyramid (বাড়তে থাকা, সেন্টারড)

```
    *
   ***
  *****
 *******
*********
```
**ভাবনা**: i-তম সারিতে: `spaces = n-i`, `stars = 2*i-1`।

```python
def pattern7(n):
    for i in range(1, n+1):
        spaces = " " * (n - i)
        stars  = "*" * (2*i - 1)
        print(spaces + stars)
```

---

## 8) Inverted Centered Pyramid (উল্টো, সেন্টারড)

```
*********
 *******
  *****
   ***
    *
```
**ভাবনা**: i-তম সারিতে: `spaces = i-1`, `stars = 2*(n-i)+1`।

```python
def pattern8(n):
    for i in range(1, n+1):
        spaces = " " * (i - 1)
        stars  = "*" * (2*(n - i) + 1)
        print(spaces + stars)
```

---

## 9) Diamond (উপর+নিচ পিরামিড)

```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```
**ভাবনা**: ৭ + ৮ একত্রে।

```python
def pattern9(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "*"*(2*i-1))
    for i in range(n-1, 0, -1):
        print(" "*(n-i) + "*"*(2*i-1))
```

---

## 10) Half Diamond (হাফ ডায়মন্ড)

```
*
**
***
****
*****
****
***
**
*
```
**ভাবনা**: ২ নাম্বার + ৫ নাম্বার জোড়া।

```python
def pattern10(n):
    for i in range(1, n+1):
        print("*" * i)
    for i in range(n-1, 0, -1):
        print("*" * i)
```

---

## 11) Binary Triangle (০/১ পাল্টানো)

```
1
01
101
0101
10101
```
**ভাবনা**: পাল্টানো বিট। সারির parity বা কলামের parity ব্যবহার।

```python
def pattern11(n):
    for i in range(1, n+1):
        row = []
        val = 1 if i % 2 else 0   # সারি বেজড শুরু
        for _ in range(i):
            row.append(str(val))
            val = 1 - val
        print("".join(row))
```

---

## 12) Palindromic Crown (মিররড নাম্বার)

```
1
12
123
1234
1234554321
```
> ভ্যারিয়েন্ট অনেক—জনপ্রিয়টি: মাঝখানে পালিন্ড্রোমিক মিরর।

```python
def pattern12(n):
    # শেষ সারিতে 1..n..1 পালিন্ড্রোম, আগের সারিগুলো মিররের শুরুর দিকে ছোট
    for i in range(1, n+1):
        left = "".join(str(x) for x in range(1, i+1))
        right = "".join(str(x) for x in range(i-1, 0, -1))
        print(left + right)
```

---

## 13) Continuous Increasing Numbers (ক্রমাগত বাড়ে)

```
1
23
456
78910
1112131415
```
**ভাবনা**: একটানা কাউন্টার রাখুন।

```python
def pattern13(n):
    cur = 1
    for i in range(1, n+1):
        row = []
        for _ in range(i):
            row.append(str(cur))
            cur += 1
        print("".join(row))
```

---

## 14) Letter Triangle (A..)

```
A
AB
ABC
ABCD
ABCDE
```
**ভাবনা**: ASCII/chr ব্যবহার।

```python
def pattern14(n):
    for i in range(1, n+1):
        row = "".join(chr(ord('A') + j) for j in range(i))
        print(row)
```

---

## 15) Reverse Letter Triangle (কমতে থাকা)

```
ABCDE
ABCD
ABC
AB
A
```
**ভাবনা**: প্রথম সারি A..(A+n-1), এরপর কাটতে থাকুন।

```python
def pattern15(n):
    for i in range(n, 0, -1):
        row = "".join(chr(ord('A') + j) for j in range(i))
        print(row)
```

---

## 16) Alpha Ramp (রিপিটেড লেটার)

```
A
BB
CCC
DDDD
EEEEE
```
**ভাবনা**: i-তম সারি—অক্ষর = `chr(ord('A') + i - 1)`, রিপিট `i`।

```python
def pattern16(n):
    for i in range(1, n+1):
        ch = chr(ord('A') + i - 1)
        print(ch * i)
```

---

## 17) Alpha Hill (পালিন্ড্রোমিক সেন্টারড)

```
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
```
**ভাবনা**: বামে A.., ডানে ..A উল্টো; মাঝে কেন্দ্র।

```python
def pattern17(n):
    for i in range(1, n+1):
        left = "".join(chr(ord('A') + j) for j in range(i))
        right = "".join(chr(ord('A') + j) for j in range(i-2, -1, -1))
        print(" "*(n-i) + left + right)
```

---

## 18) Alpha Triangle (ডায়াগোনাল শিফট)

```
E
DE
CDE
BCDE
ABCDE
```
**ভাবনা**: i-তম সারিতে শুরু হবে `chr(ord('A') + n - i)` থেকে `E` পর্যন্ত।

```python
def pattern18(n):
    # এখানে n=5 হলে E, DE, CDE...
    for i in range(1, n+1):
        start = ord('A') + (n - i)
        row = "".join(chr(x) for x in range(start, ord('A') + n))
        print(row)
```

---

## 19) Void / Hollow X-like Symmetry (ফাঁপা ভেতর)

```
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
```
**ভাবনা**: উপরের অর্ধে স্পেস ২ করে বাড়ে, স্টার দুই প্রান্তে কমে; নিচে উল্টো।

```python
def pattern19(n):
    # মোট উচ্চতা = 2*n, প্রস্থ = 2*n
    width = 2 * n
    # টপ হাফ
    for i in range(n):
        left = "*" * (n - i)
        mid  = " " * (2 * i)
        right = "*" * (n - i)
        print(left + mid + right)
    # বটম হাফ
    for i in range(n):
        left = "*" * (i + 1)
        mid  = " " * (2 * (n - i - 1))
        right = "*" * (i + 1)
        print(left + mid + right)
```

> নোট: উপর-নিচের সীমানা আপনার কাঙ্ক্ষিত ভ্যারিয়েন্ট অনুযায়ী সামান্য এডজাস্ট করতে পারেন।

---

## 20) Butterfly (ডাবল ট্রায়াঙ্গেল মিরর)

```
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
```
**ভাবনা**: বামে বাড়তে থাকা স্টার, ডানে একই—মাঝখানে ফাঁকা স্পেস কমে/বাড়ে।

```python
def pattern20(n):
    # টপ
    for i in range(1, n+1):
        left = "*" * i
        mid  = " " * (2*(n - i))
        right = "*" * i
        print(left + mid + right)
    # বটম
    for i in range(n-1, 0, -1):
        left = "*" * i
        mid  = " " * (2*(n - i))
        right = "*" * i
        print(left + mid + right)
```

---

## 21) Hollow Rectangle (ফাঁপা বর্গ/আয়ত)

```
*****
*   *
*   *
*   *
*****
```
**ভাবনা**: বর্ডার প্রিন্ট, ভিতরে স্পেস।

```python
def pattern21(n, m=None):
    m = m or n
    for r in range(n):
        if r in (0, n-1):
            print("*" * m)
        else:
            if m >= 2:
                print("*" + " "*(m-2) + "*")
            else:
                print("*")
```

---

## 22) Number Diamond / Layered Square (কেন্দ্রে সবচেয়ে ছোট)

```
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555
```
**ভাবনা**: এটি আসলে **লেয়ার্ড স্কোয়ার** যেখানে (i,j) পজিশনের মান বাউন্ডারি থেকে দূরত্ব দিয়ে নির্ধারিত।

```python
def pattern22(n):
    # n লেয়ার হলে সাইজ হবে 2*n - 1 (এখানে n=5 => 9x9)
    # আউটপুটে বাইরের লেয়ার n, ভেতরে কমতে কমতে 1 কেন্দ্র।
    size = 2*n - 1
    for i in range(size):
        row = []
        for j in range(size):
            top = i
            left = j
            bottom = size - 1 - i
            right = size - 1 - j
            dist = min(top, left, bottom, right)  # বর্ডারি থেকে ন্যূনতম দূরত্ব
            val = n - dist
            row.append(str(val))
        print("".join(row))
```

---

## দ্রুত রিভিশন টিপস

- **সেন্টারড পিরামিড**: `spaces = n-i`, `stars = 2*i-1`  
- **হাফ ডায়মন্ড**: প্রথমে বাড়ে, পরে কমে—দুটি লুপ।  
- **পালিন্ড্রোম** (নাম্বার/অ্যালফা): বামে বাড়ে, ডানে উল্টো করে যোগ।  
- **হলোগ্রিড**: বর্ডার প্রিন্ট, ভিতরে স্পেস।  
- **বাটারফ্লাই**: দুই পাশে স্টার, মাঝখানে স্পেস—স্পেসের পরিমাণ ২*(n-i)।  
- **লেয়ার্ড নাম্বার স্কোয়ার**: বাউন্ডারি দূরত্ব = লেয়ার নির্ধারণ।

---

## সব প্যাটার্ন একসাথে চালানোর ডেমো

```python
def demo():
    n = 5
    print("1)"); pattern1(n)
    print("2)"); pattern2(n)
    print("3)"); pattern3(n)
    print("4)"); pattern4(n)
    print("5)"); pattern5(n)
    print("6)"); pattern6(n)
    print("7)"); pattern7(n)
    print("8)"); pattern8(n)
    print("9)"); pattern9(n)
    print("10)"); pattern10(n)
    print("11)"); pattern11(n)
    print("12)"); pattern12(n)
    print("13)"); pattern13(n)
    print("14)"); pattern14(n)
    print("15)"); pattern15(n)
    print("16)"); pattern16(n)
    print("17)"); pattern17(n)
    print("18)"); pattern18(n)
    print("19)"); pattern19(n)
    print("20)"); pattern20(n)
    print("21)"); pattern21(n)
    print("22)"); pattern22(n)
```

> প্রয়োজনে `print` এর বদলে স্ট্রিং বানিয়ে লিস্টে জমা রাখতে পারেন, বা ফাইলে লিখে দেখতে পারেন।

---

## সাধারণ ভুলত্রুটি (এড়িয়ে চলুন)

- **স্পেস ভুল গণনা**: সেন্টারড প্যাটার্নে `n-i`/`i-1` আলাদা—লজিক মিলিয়ে নিন।  
- **নতুন লাইন**: প্রতিটি সারি শেষে `print()` যেন থাকে।  
- **একই লুপে স্টার/স্পেস**: স্পেস আগে, তারপর স্টার প্রিন্ট করুন (সেন্টারড কেসে)।  
- **ভ্যারিয়েন্ট মিক্সআপ**: অনেক প্যাটার্নের একাধিক ভ্যারিয়েন্ট আছে—প্রশ্নে দেওয়া উদাহরণ অনুযায়ী সমাধান দিন।

---

## বাড়তি অনুশীলন

- প্রতিটি প্যাটার্নে **স্পেস/স্টার** এর সংখ্যা কাগজে লিখে ফর্মুলা বের করুন।  
- একই প্যাটার্ন **`while`** বা **রিকার্শন** দিয়ে লেখার চেষ্টা করুন।  
- `print(..., end="")` এবং লাইনের শেষে `print()`—এই কন্ট্রোলগুলো প্র্যাকটিস করুন।

---

**শুভকামনা!** এই ২২টি প্যাটার্ন ভালোভাবে করলে নেস্টেড লুপ ও ইনডেক্সিংয়ে আপনাকে আত্মবিশ্বাসী করে তুলবে, যা DSA-এর অন্যান্য টপিক বুঝতে অনেক সাহায্য করবে।