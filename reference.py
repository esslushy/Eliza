reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}
 
psychobabble_patterns = {
    "need": r'I need (.*)',
    "don't": r'Why don\'?t you ([^\?]*)\??',
    "why_can't": r'Why can\'?t I ([^\?]*)\??',
    "i_can't": r'I can\'?t (.*)',
    "i_am": r'I am (.*)',
    "i'm": r'I\'?m (.*)',
    "are_you": r'Are you ([^\?]*)\??',
    "what": r'What (.*)',
    "how": r'How (.*)',
    "because": r'Because (.*)',
    "sorry": r'(.*) sorry (.*)',
    "hello": r'Hello(.*)',
    "i_think": r'I think (.*)',
    "friend": r'(.*) friend (.*)',
    "yes": r'Yes',
    "computer": r'(.*) computer(.*)',
    "is_it": r'Is it (.*)',
    "it_is":  r'It is (.*)',
    "can_you": r'Can you ([^\?]*)\??',
    "can_i": r'Can I ([^\?]*)\??',
    "you_are": r'You are (.*)',
    "youre": r'You\'?re (.*)',
    "i_dont": r'I don\'?t (.*)',
    "i_feel": r'I feel (.*)',
    "i_have": r'I have (.*)',
    "i_would": r'I would (.*)',
    "is_there": r'Is there (.*)',
    "my": r'My (.*)',
    "you": r'You (.*)',
    "why": r'Why (.*)',
    "i_want": r'I want (.*)',
    "mother": r'(.*) mother(.*)',
    "father": r'(.*) father(.*)',
    "child": r'(.*) child(.*)',
    "question": r'(.*)\?',
    "quit": r'quit',
    "else": r'(.*)'
}

psychobabble_responses = {
    "need": ["Why do you need {0}?",
             "Would it really help you to get {0}?",
             "Are you sure you need {0}?"],
 
    "don't": ["Do you really think I don't {0}?",
              "Perhaps eventually I will {0}.",
              "Do you really want me to {0}?"],
 
    "why_can't": ["Do you think you should be able to {0}?",
                  "If you could {0}, what would you do?",
                  "I don't know -- why can't you {0}?",
                  "Have you really tried?"],
 
    "i_can't": ["How do you know you can't {0}?",
                "Perhaps you could {0} if you tried.",
                "What would it take for you to {0}?"],
 
    "i_am": ["Did you come to me because you are {0}?",
             "How long have you been {0}?",
             "How do you feel about being {0}?"],
 
    "i'm": ["How does being {0} make you feel?",
            "Do you enjoy being {0}?",
            "Why do you tell me you're {0}?",
            "Why do you think you're {0}?"],
 
    "are_you": ["Why does it matter whether I am {0}?",
                "Would you prefer it if I were not {0}?",
                "Perhaps you believe I am {0}.",
                "I may be {0} -- what do you think?"],
 
    "what": ["Why do you ask?",
             "How would an answer to that help you?",
             "What do you think?"],
 
    "how": ["How do you suppose?",
            "Perhaps you can answer your own question.",
            "What is it you're really asking?"],
 
    "because": ["Is that the real reason?",
                "What other reasons come to mind?",
                "Does that reason apply to anything else?",
                "If {0}, what else must be true?"],
 
    "sorry": ["There are many times when no apology is needed.",
              "What feelings do you have when you apologize?"],
 
    "hello": ["Hello... I'm glad you could drop by today.",
              "Hi there... how are you today?",
              "Hello, how are you feeling today?"],
 
    "i_think": ["Do you doubt {0}?",
                "Do you really think so?",
                "But you're not sure {0}?"],
 
    "friend": ["Tell me more about your friends.",
               "When you think of a friend, what comes to mind?",
               "Why don't you tell me about a childhood friend?"],
 
    "yes": ["You seem quite sure.",
            "OK, but can you elaborate a bit?"],
 
    "computer": ["Are you really talking about me?",
                 "Does it seem strange to talk to a computer?",
                 "How do computers make you feel?",
                 "Do you feel threatened by computers?"],
 
    "is_it": ["Do you think it is {0}?",
              "Perhaps it's {0} -- what do you think?",
              "If it were {0}, what would you do?",
              "It could well be that {0}."],
 
    "it_is": ["You seem very certain.",
              "If I told you that it probably isn't {0}, what would you feel?"],
 
    "can_you": ["What makes you think I can't {0}?",
                "If I could {0}, then what?",
                "Why do you ask if I can {0}?"],
 
    "can_i": ["Perhaps you don't want to {0}.",
               "Do you want to be able to {0}?",
               "If you could {0}, would you?"],
 
    "you_are": ["Why do you think I am {0}?",
                "Does it please you to think that I'm {0}?",
                "Perhaps you would like me to be {0}.",
                "Perhaps you're really talking about yourself?"],
 
    "youre": ["Why do you say I am {0}?",
              "Why do you think I am {0}?",
              "Are we talking about you, or me?"],
 
    "i_dont": ["Don't you really {0}?",
               "Why don't you {0}?",
               "Do you want to {0}?"],
 
    "i_feel": ["Good, tell me more about these feelings.",
               "Do you often feel {0}?",
               "When do you usually feel {0}?",
               "When you feel {0}, what do you do?"],
 
    "i_have": ["Why do you tell me that you've {0}?",
               "Have you really {0}?",
               "Now that you have {0}, what will you do next?"],
 
    "i_would": ["Could you explain why you would {0}?",
                "Why would you {0}?",
                "Who else knows that you would {0}?"],
 
    "is_there": ["Do you think there is {0}?",
                 "It's likely that there is {0}.",
                 "Would you like there to be {0}?"],
 
    "my": ["I see, your {0}.",
           "Why do you say that your {0}?",
           "When your {0}, how do you feel?"],
 
    "you": ["We should be discussing you, not me.",
             "Why do you say that about me?",
             "Why do you care whether I {0}?"],
 
    "why": ["Why don't you tell me the reason why {0}?",
             "Why do you think {0}?"],
 
    "i_want": ["What would it mean to you if you got {0}?",
               "Why do you want {0}?",
               "What would you do if you got {0}?",
               "If you got {0}, then what would you do?"],
 
    "mother": ["Tell me more about your mother.",
               "What was your relationship with your mother like?",
      "How do you feel about your mother?",
      "How does this relate to your feelings today?",
      "Good family relations are important."],
 
    "father": ["Tell me more about your father.",
               "How did your father make you feel?",
               "How do you feel about your father?",
               "Does your relationship with your father relate to your feelings today?",
               "Do you have trouble showing affection with your family?"],
 
    "child": ["Did you have close friends as a child?",
              "What is your favorite childhood memory?",
              "Do you remember any dreams or nightmares from childhood?",
              "Did the other children sometimes tease you?",
              "How do you think your childhood experiences relate to your feelings today?"],
 
    "question": ["Why do you ask that?",
                 "Please consider whether you can answer your own question.",
                 "Perhaps the answer lies within yourself?",
                 "Why don't you tell me?"],
 
    "quit": ["Thank you for talking with me.",
             "Good-bye.",
             "Thank you, that will be $150.  Have a good day!"],
 
    "else": ["Please tell me more.",
             "Let's change focus a bit... Tell me about your family.",
             "Can you elaborate on that?",
             "Why do you say that {0}?",
             "I see.",
             "Very interesting.",
             "{0}.",
             "I see.  And what does that tell you?",
             "How does that make you feel?",
             "How do you feel when you say that?"]
}

def format_response(match, response):
  """
  Function that deals with formatting the regex match
  It uses a couple of python tricks we don't know yet, but we can still use it!

  reflect is the reflect function that the student has written
  response is the response that has been chosen from psychobabble
  match is the resulting of the matching regular expression
  """
  return response.format(*[reflect(g) for g in match.groups()])

def reflect(fragment):
    """
    For every word in fragment,
        if that word is in the reflections dictionary from reference
            Replace the word (in the list) with its associated value from reflections
    """
    tokens = fragment.lower().split()
    for i in range(len(tokens)):
        if tokens[i] in reflections:
            tokens[i] = reflections[tokens[i]]
    return ' '.join(tokens)
