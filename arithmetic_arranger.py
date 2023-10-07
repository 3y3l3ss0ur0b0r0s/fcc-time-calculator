import re

def valid_problem(parts):
  result = True
  errorString = None
  #print("parts:", parts)
  
  if parts[1] != '+' and parts[1] != '-':
    # Check for operator validity
    result = False
    #print("parts[1] != '+' and parts[1] != '-'")
    errorString = "Error: Operator must be '+' or '-'."
  elif len(parts[0]) > 4 or len(parts[2]) > 4:
    # Check for operand lengths
    result = False
    #print("len(parts[0]) > 4 or len(parts[2]]) > 4")
    errorString = "Error: Numbers cannot be more than four digits."
  elif re.search(r'\D', parts[0]) != None or re.search(r'\D', parts[2]) != None:
    # Check for non-digits in operands
    result = False
    #print("re.search(r'\D', parts[0]) != None or re.search(r'\D', parts[2]) != None")
    errorString = "Error: Numbers must only contain digits."
  
  return (result, errorString)

# Width-determining logic
def calculate_width(parts):
  if len(parts[0]) > len(parts[2]):
    return len(parts[0]) + 2
  return len(parts[2]) + 2

# For calulating logic
def calculate(parts):
  match parts[1]:
    case '+': 
      print(int(parts[0]) + int(parts[2]))
      return int(parts[0]) + int(parts[2])
    case '-':
      print(int(parts[0]) - int(parts[2]))
      return int(parts[0]) - int(parts[2])

# Formatting logic
def arithmetic_arranger(problems, displayAnswers=None):
  #print("Displaying answers?", displayAnswers)
  
  if len(problems) > 5:
    return "Error: Too many problems."
  
  arranged_problems = ""
  topLine = ""
  middleLine = ""
  bottomLine = ""
  answerLine = ""

  for p in problems:
    #print(p)
    problemParts = p.split()

    validity = valid_problem(problemParts)
    #print("validity:", validity)
    
    if validity[0] is True:
      #print("The problem is valid!")
      # Calculate number of dashes needed (width of problem)
      width = calculate_width(problemParts)

      topLine += (' '*(width - len(problemParts[0]))) + problemParts[0]
      middleLine += problemParts[1] + (' '*(width - len(problemParts[2]) - 1)) + problemParts[2]
      bottomLine += ('-'*width)

      if displayAnswers == True: 
        answer = str(calculate(problemParts))
        answerLine += (' '*(width - len(answer))) + answer

      # Determine if separator spaces are needed
      if problems.index(p) != (len(problems) - 1):
        topLine += '    '
        middleLine += '    '
        bottomLine += '    '
        answerLine += '    '
    else:
      # Return error string since problem is invalid
      return validity[1]

  arranged_problems = topLine + '\n' + middleLine + '\n' + bottomLine
  
  if displayAnswers == True:
    arranged_problems += '\n' + answerLine

  return arranged_problems
