"""
Rules for comments in code:

* comments has to help instead mislead;
* update comments with program updates;
* comments as complete sentences;
* for multi-sentence comments -> two spaces after each full stop ending a sentence;
* comments in English;
* comments -> no more than 72 chas per line;

Block comments => refer to the code that follows them and indented to the same level as the code they describe.

Inline comments =>  written on the same line of statement and provide explanation to a single line of code.

Docstrings => descriptions and explanations for public modules, files, functions, classes, and methods in code.
"""


def block_comment():
  # Line 1
  # Line 2
  #
  # Line 3
  pass


inline = 'comment'  # Example of inline comment.


def doc_string():
  """
  Example of docstring comment

  :return: pass
  """
  pass
