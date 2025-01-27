# Plethora of Python

A list of Python 3 programming projects ranging from Beginner to Advanced. A work in progress.

### Update Repository on GitHub

```
$ git status
$ git add -A
$ git commit -m "Updated README.md"
$ git push
```

### Virtual Environment

It is recommended to run this program in a ``venv`` environment. Assuming that has already been set up, you can create a ``venv`` environment:
<pre>
<code>$ python3 -m venv plethora</code>
</pre>

Now you have to tell the system that you want to use this virtual environment, and you do that by <i>activating</i> it. To activate your brand new virtual environment you use the following command:
<pre>
<code>$ source plethora/bin/activate
(plethora) $ _</code>
</pre>

### Requirements

Once you're in, please run the following command:

```
(plethora) $ cat requirements.txt | xargs -n 1 pip install
```