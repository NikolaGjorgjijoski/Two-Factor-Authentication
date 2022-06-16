from TwoFactorAuthentication.py import Generate_Key, Key

NewKey = Generate_Key()

KEY = Key(NewKey)

CurrentCode = KEY['Code']

Time_Remaining = KEY['Time_Remaining']

print(f"This is your key: {NewKey}")
print(f"This is your current code: {CurrentCode}")
print(f"Your current code with change in {Time_Remaining} seconds")
