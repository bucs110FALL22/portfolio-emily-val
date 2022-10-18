def percentage_to_letter(a):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  elif score < 60: 
    return "F"

def is_passing(letter):
  if result == "A" or "B" or "C":
    return True
  elif result == "D" or "F":
    return False

score = float(input("Please input your exam score: "))
print(percentage_to_letter(score))
result = percentage_to_letter(score)
print(is_passing(result))