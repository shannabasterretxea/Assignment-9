"""FSU package that performs various natural language processing tasks, including Part-of-Speech tagging
"""

def pos_tag(text: str) -> list:
  """ POS tags an input string, returns a list of tuples of words plus tags
  """
  tokens = tokenise(text)
  pos_dct = retrieve_pos_dct()
  word_tag_pairs = look_up_tags(tokens, pos_dct)
  # output_tags(word_tag_pairs)
  return(word_tag_pairs)


def tokenise(text: str) -> list:
  """ Create list of tokens from input text; currently just a split
  """
  tokens = text.split()
  return(tokens)


def retrieve_pos_dct() -> dict:
  """ Try to load POS dictionary from file
  If dct cannot be loaded, create POS dictionary from
  .conllu training file and save dictionary to file
  """
  try:
    existing_dct_file = open("pos.dct", "r") #TODO implement pickle
  except FileNotFoundError:
    print("WARNING: Could not find pos.dct, trying to build new dct from local .conllu file")
    path_to_dct = input("Enter path of en_gum-ud-sample.conllu file: ")
    ud_corpus = open(path_to_dct + "en_gum-ud-sample.conllu", "r")
    pos_dct = dict()
    for line in ud_corpus:
      line_annotations = line.split("\t")
      if len(line_annotations) > 3:
        word = line_annotations[1]
        pos = line_annotations[3]
        pos_dct[word] = pos
  return(pos_dct)


def look_up_tags(tokens, pos_dct) -> list:
  """ For each token, look-up pos tag in pos dictionary
  """
  word_tag_pairs = list()
  for token in tokens:
    pos_tag = pos_dct[token]
    word_tag_pairs.append((token, pos_tag))
  return(word_tag_pairs)


def output_tags(word_tag_pairs):
  """ Produce some kind of output file
  """
  pass


def get_accuracy():
  """ Evaluate the accuracy of the tagger
  """
  pass


# boilerplate
if __name__ == "__main__":
  print("Script can only run as an import.")
