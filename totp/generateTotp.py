import time
import numpy as np

'''
    Generate a TOTP (Time-based One-Time Password) using the current time
    and a secret key.
    Master password -> "lmao"
    convert to hex -> 6c6d616f
    split into pairs of 2 -> 6c 6d 61 6f
    
    get curent timestamp in seconds and divide by 30 -> 1612345678 / 30 = 53744856
    convert to hex -> 32a0c58
    format to 8 digits -> 032a0c58
    split into pairs of 2 -> 03 2a 0c 58

    do pairwise addition of the 2 hex strings -> 6c ^ 03 = 6f, 6d ^ 2a = 47, 61 ^ 0c = 6d, 6f ^ 58 = 37 -> 6f476d37
    
    split into pairs of 2 -> 6f 47 6d 37
    This is the TOTP

    now we will get back "lmao" from the TOTP
    split into pairs of 2 -> 6f 47 6d 37

    do pairwise subtraction of the 2 hex strings -> 6f ^ 03 = 6c, 47 ^ 2a = 6d, 6d ^ 0c = 61, 37 ^ 58 = 6f -> 6c6d616f

    convert to ascii -> lmao


'''