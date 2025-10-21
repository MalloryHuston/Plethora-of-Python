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
