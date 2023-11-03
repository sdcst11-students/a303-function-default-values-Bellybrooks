#!python3

"""
Create a function called title that creates a single line of output to display the word
"Title" with a box around it.  
The function will have 1 optional input:
symbol : string.  The symbolt to use as the border. Default symbol is "="

The return value is the output string with escaped line breaks.

example assertion:
assert title("*") == "*********\n* Title *\n*********"
assert title("*") == "********\n*title*\n********
assert title() == "=========\n= Title =\n========="
(2 points)

"""
def title(symbol="="):
    title_text=" Title "
    border=symbol*(9)
    output=f"{border}\n{symbol}{title_text}{symbol}\n{border}"
    print(output)
    return output

assert title("*") == "*********\n* Title *\n*********"
assert title() == "=========\n= Title =\n========="