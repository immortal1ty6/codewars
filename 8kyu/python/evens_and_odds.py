def evens_and_odds(n):
  if n % 2 == 0:
    return bin(n).replace("0b", "")
  else:
    return hex(n).replace("0x", "")

print(evens_and_odds(2))
print(evens_and_odds(13))
