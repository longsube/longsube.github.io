input = ["masturbation", "pussy", "discipline", "beer", "familug"]
letters = 'abcdefghijklmnopqrstuvwxyz'
letter_mark = {y:x for x,y in enumerate(letters, start = 1)}
total_mark = []

for word in input:
    mark = 0
    for letter in word:
            mark += letter_mark.get(letter)
    total_mark.append(mark)         
print total_mark


