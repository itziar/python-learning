import string


### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print 'Loading word list from file...'
    # inFile: file
    in_file = open(file_name, 'r', 0)
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print '  ', len(word_list), 'words loaded.'
    in_file.close()
    return word_list


### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'

'''
Problem 1: Build the Shift Dictionary and Apply Shift

The Message class contains methods that could be used to apply a cipher to a string, either to encrypt or to decrypt a message (since for Caesar codes this is the same action).

In the next two questions, you will fill in the methods of the Message class found in ps6.py according to the specifications in the docstrings. The methods in the Message class already filled in are:

__init__(self, text)
The getter method get_message_text(self)
The getter method get_valid_words(self), notice that this one returns a copy of self.valid_words to prevent someone from mutating the original list.
In this problem, you will fill in two methods:

Fill in the build_shift_dict(self, shift) method of the Message class. Be sure that your dictionary includes both lower and upper case letters, but that the shifted character for a lower case letter and its uppercase version are lower and upper case instances of the same letter. What this means is that if the original letter is "a" and its shifted value is "c", the letter "A" should shift to the letter "C".

If you are unfamiliar with the ordering or characters of the English alphabet, we will be following the letter ordering displayed by string.ascii_lowercase and string.ascii_uppercase:

>>> import string
>>> print string.ascii_lowercase
abcdefghijklmnopqrstuvwxyz
>>> print string.ascii_uppercase
ABCDEFGHIJKLMNOPQRSTUVWXYZ
A reminder from the introduction page - characters such as the space character, commas, periods, exclamation points, etc will not be encrypted by this cipher - basically, all the characters within string.punctuation, plus the space (' ') and all numerical characters (0 - 9) found in string.digits.

Fill in the apply_shift(self, shift) method of the Message class. You may find it easier to use build_shift_dict(self, shift). Remember that spaces and punctuation should not be changed by the cipher.
'''
class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        dict1 = {}
        str1 = string.ascii_uppercase
        for s in str1:
            if (ord(s) + shift - 65) < 26:
                dict1[s] = chr(ord(s) + shift)
            elif (ord(s) + shift - 65) >= 26:
                dict1[s] = chr(ord(s) + shift - 26)

        str1 = string.ascii_lowercase
        for s in str1:
            if (ord(s) + shift - 97) < 26:
                dict1[s] = chr(ord(s) + shift)
            elif (ord(s) + shift - 97) >= 26:
                dict1[s] = chr(ord(s) + shift - 26)

        return dict1

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        msg = self.get_message_text()
        newMsg = ""
        dict1 = self.build_shift_dict(shift)
        for i in range(len(msg)):
            if dict1.has_key(msg[i]):
                newMsg += dict1.get(msg[i])
            else:
                newMsg += msg[i]
        return newMsg

'''
Problem 2: PlaintextMessage

For this problem, the graders will use our implementation of the Message class, so don't worry if you did not get the previous parts correct.

PlaintextMessage is a subclass of Message and has methods to encode a string using a specified shift value. Our class will always create an encoded version of the message, and will have methods for changing the encoding.

Implement the methods in the class PlaintextMessage according to the specifications in ps6.py. The methods you should fill in are:

__init__(self, text, shift): Use the parent class constructor to make your code more concise.
The getter method get_shift(self)
The getter method get_encrypting_dict(self): This should return a COPY of self.encrypting_dict to prevent someone from mutating the original dictionary.
The getter method get_message_text_encrypted(self)
change_shift(self, shift): Think about what other methods you can use to make this easier. It shouldn’t take more than a couple lines of code.

'''
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        dict1 = {}
        str1 = string.ascii_uppercase
        for s in str1:
            if (ord(s) + shift - 65) < 26:
                dict1[s] = chr(ord(s) + shift)
            elif (ord(s) + shift - 65) >= 26:
                dict1[s] = chr(ord(s) + shift - 26)

        str1 = string.ascii_lowercase
        for s in str1:
            if (ord(s) + shift - 97) < 26:
                dict1[s] = chr(ord(s) + shift)
            elif (ord(s) + shift - 97) >= 26:
                dict1[s] = chr(ord(s) + shift - 26)

        return dict1

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        msg = self.get_message_text()
        newMsg = ""
        dict1 = self.build_shift_dict(shift)
        for i in range(len(msg)):
            if dict1.has_key(msg[i]):
                newMsg += dict1.get(msg[i])
            else:
                newMsg += msg[i]
        return newMsg

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        encrypting_dict = dict(self.encrypting_dict)
        return encrypting_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

'''
Problem 3: CiphertextMessage

For this problem, the graders will use our implementation of the Message and PlaintextMessage classes, so don't worry if you did not get the previous parts correct.

Given an encrypted message, if you know the shift used to encode the message, decoding it is trivial. If message is the encrypted message, and s is the shift used to encrypt the message, then apply_shift(message, 26-s) gives you the original plaintext message. Do you see why?

The problem, of course, is that you don’t know the shift. But our encryption method only has 26 distinct possible values for the shift! We know English is the main language of these emails, so if we can write a program that tries each shift and maximizes the number of English words in the decoded message, we can decrypt their cipher! A simple indication of whether or not the correct shift has been found is if most of the words obtained after a shift are valid words. Note that this only means that most of the words obtained are actual words. It is possible to have a message that can be decoded by two separate shifts into different sets of words. While there are various strategies for deciding between ambiguous decryptions, for this problem we are only looking for a simple solution.

Fill in the methods in the class CiphertextMessage acording to the specifications in ps6.py. The methods you should fill in are:

__init__(self, text): Use the parent class constructor to make your code more concise.
decrypt_message(self): You may find the helper function is_word(wordlist, word) and the string method split() useful. Note that is_word will ignore punctuation and other special characters when considering whether a word is valid.
'''
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        dict1 = {}
        str1 = string.ascii_uppercase
        for s in str1:
            if (ord(s) + shift - 65) < 26:
                dict1[s] = chr(ord(s) + shift)
            elif (ord(s) + shift - 65) >= 26:
                dict1[s] = chr(ord(s) + shift - 26)

        str1 = string.ascii_lowercase
        for s in str1:
            if (ord(s) + shift - 97) < 26:
                dict1[s] = chr(ord(s) + shift)
            elif (ord(s) + shift - 97) >= 26:
                dict1[s] = chr(ord(s) + shift - 26)

        return dict1
    def apply_shift(self, msg,  shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        newMsg = ""
        dict1 = self.build_shift_dict(shift)
        for i in range(len(msg)):
            if dict1.has_key(msg[i]):
                newMsg += dict1.get(msg[i])
            else:
                newMsg += msg[i]
        return newMsg
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        tupla=()
        msg=self.get_message_text()
        cadena=msg.split(" ")
        contador_palabras=len(cadena)
        #for s in range(26):
        contador=0
        palabras=[]
        shift=0
        contadoruno=0
        s=0
        self.build_shift_dict(s)
        for s in range(26):
            contador=0
            for i in cadena:
                mensaje=self.apply_shift(i, s)
                if is_word(self.valid_words, mensaje):
                    contador+=1
            if contador > contadoruno:
                contadoruno=contador
                shift=s
        string=""
        primera=0
        for i in cadena:
            mensaje=self.apply_shift(i, shift)
            if primera==0:
                string=mensaje
            else:
                string=string + " " + mensaje
            primera+=1
        tupla=(shift, string)
        return tupla

                #print mensaje
        #if contador==contador_palabras:
         #   print s
     #       return s
          #  print "aqui"


        #return tupla


# Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello what', 2)
print 'Expected Output: jgnnq yjcv'
print 'Actual Output:', plaintext.get_message_text_encrypted()

# Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq yjcv')
print 'Expected Output:', (24, 'hello what')
print 'Actual Output:', ciphertext.decrypt_message()

'''
Problem 4: Decrypt a Story

For this problem, the graders will use our implementation of the Message, PlaintextMessage, and CiphertextMessage classes, so don't worry if you did not get the previous parts correct.

Now that you have all the pieces to the puzzle, please use them to decode the file story.txt. The file ps6.py contains a helper function get_story_string() that returns the encrypted version of the story as a string. Create a CiphertextMessage object using the story string and use decrypt_message to return the appropriate shift value and unencrypted story string.
'''
def build_shift_dict(shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        dict1 = {}
        str1 = string.ascii_uppercase
        for s in str1:
            if (ord(s) + shift - 65) < 26:
                dict1[s] = chr(ord(s) + shift)
            elif (ord(s) + shift - 65) >= 26:
                dict1[s] = chr(ord(s) + shift - 26)

        str1 = string.ascii_lowercase
        for s in str1:
            if (ord(s) + shift - 97) < 26:
                dict1[s] = chr(ord(s) + shift)
            elif (ord(s) + shift - 97) >= 26:
                dict1[s] = chr(ord(s) + shift - 26)

        return dict1

def apply_shift(msg,  shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        newMsg = ""
        dict1 = build_shift_dict(shift)
        for i in range(len(msg)):
            if dict1.has_key(msg[i]):
                newMsg += dict1.get(msg[i])
            else:
                newMsg += msg[i]
        return newMsg

def decrypt_story():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.
    returns: string - story in plain text
    """
    story = get_story_string()
    wordList = load_words(WORDLIST_FILENAME)

    cadena=story.split(" ")
    contador_palabras=len(cadena)
    contador=0
    shift=0
    contadoruno=0
    s=0
    for s in range(26):
        contador=0
        for i in cadena:
            mensaje=apply_shift(i, s)
            if is_word(wordList, mensaje):
                contador+=1
        if contador > contadoruno:
            contadoruno=contador
            shift=s
    string=""
    primera=0
    for i in cadena:
        mensaje=apply_shift(i, shift)
        if primera==0:
            string=mensaje
        else:
            string=string + " " + mensaje
        primera+=1
    tupla=(shift, string)
    return tupla

print decrypt_story()