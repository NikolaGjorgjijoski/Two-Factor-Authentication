from datetime import datetime
import pyotp

def Generate_Key():
  return pyotp.random_base32()

def Key(Key):
  Key = pyotp.TOTP(Key)
  Code = Key.now() ## Current Code
  Time_Remaining = Key.interval - datetime.now().timestamp() % Key.interval ## The amount of seconds before new code will be generated.
  return {
    "Code": Code,
    "Time_Remaining": Time_Remaining
  }
