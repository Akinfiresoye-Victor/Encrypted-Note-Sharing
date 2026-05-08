import random
import string
import hashlib # Needed to create a consistent seed

# --- Shared Secret Key ---
# This key MUST be the exact same string in both files.
SHARED_SECRET_STRING = 'YourSecureNoteSharingKey123' # <--- IMPORTANT: CHANGE THIS TO YOUR OWN SECRET PHRASE!

# Define the character set we WILL substitute.
# Includes space, punctuation, digits, ASCII letters (upper and lower)
# If you need other characters (like international ones), you'd need to add them here.
CHARS = " " + string.punctuation + string.digits + string.ascii_letters
CHARS = list(CHARS) # Convert string to list of characters

# Create the substitution key list deterministically
# We use a hash of the shared secret string as a seed for the random number generator
# This makes the 'shuffle' predictable and the same every time the script runs with the same key.
seed_value = int(hashlib.sha256(SHARED_SECRET_STRING.encode('utf-8')).hexdigest(), 16)
rng = random.Random(seed_value)

# Create a copy of the CHARS list to shuffle
KEY = CHARS[:]
# Deterministically shuffle the KEY list
rng.shuffle(KEY)


'''Simplified Character-based Substitution (Prevents ValueError)'''

def simple_encrypt_char(text):
    """
    Encrypts text using a simple character substitution.
    Characters NOT in the CHARS list are left unchanged.
    """
    cipher_text = ""
    for letter in text:
        try:
            # Find the index of the letter in the original CHARS list
            index = CHARS.index(letter)
            # Append the character from the KEY list at that index
            cipher_text += KEY[index]
        except ValueError:
            # If the letter is NOT in CHARS (e.g., a character you didn't include)
            # just append the original letter. This prevents the ValueError.
            cipher_text += letter
    return cipher_text

def simple_decrypt_char(text):
    """
    Decrypts text using a simple character substitution.
    Characters NOT found in the KEY list are left unchanged.
    """
    plain_text = ""
    for letter in text:
        try:
            # Find the index of the letter in the KEY list (the shuffled one)
            index = KEY.index(letter)
            # Append the character from the original CHARS list at that index
            plain_text += CHARS[index]
        except ValueError:
             # If the letter is NOT in KEY (meaning it wasn't encrypted), just append it.
             # This prevents the ValueError and handles characters left unchanged by encryption.
            plain_text += letter
    return plain_text

# --- End of section to add ---