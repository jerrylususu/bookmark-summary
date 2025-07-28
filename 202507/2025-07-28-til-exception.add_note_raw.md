Title: TIL: Exception.add_note

URL Source: https://daniel.feldroy.com/posts/til-2025-05-exception-add_note

Markdown Content:
_Adding extra info to exceptions the easy way._

2025-05-13T14:10:31.105025

Python 3.11 introduced a new method called `add_note` for exceptions, which allows you to add extra information to exceptions in an easy, intuitive way.

```
try:
    1/0
except ZeroDivisionError as e:
    e.add_note("This is a note about the error")
    e.add_note("This is another note")
    e.add_note("All notes must be strings")
    raise
```

The output will look something like this:

```
=========================================================
ZeroDivisionError       Traceback (most recent call last)
Cell In[1], line 2
      1 try:
====> 2     1/0
      3 except ZeroDivisionError as e:
      4     e.add_note("This is a note about the error")

ZeroDivisionError: division by zero
This is a note about the error
This is another note
All notes must be strings
```

See those last three lines? Those are the notes we added to the exception!

The `add_note` allows for adding extra info without overriding the normal error, printing after the rest of the exception. The notes must be strings, and are stored in a list at the `__notes__` attribute.

Finally, technically speaking, `add_note` is a method of the `BaseException` class, which is the base class for Python exceptions. This means that we can use it with any and all Python exceptions.

Tags: [TIL](https://daniel.feldroy.com/tags/TIL)[python](https://daniel.feldroy.com/tags/python)

[← Back to all articles](https://daniel.feldroy.com/)
