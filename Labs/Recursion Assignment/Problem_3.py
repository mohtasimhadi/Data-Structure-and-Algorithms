def remove_odds(numbers):
  if not numbers:
    return []
  if numbers[0] % 2 == 0:
    return [numbers[0]] + remove_odds(numbers[1:])
  return remove_odds(numbers[1:])

arr = [1, 2, 3, 4, 5]
arr = remove_odds(arr)
print(arr)