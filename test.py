def greet(name):
  """Greets the person passed in as a parameter."""
  print(f"Hello, {name}!")

def add(x, y):
  """Adds two numbers and returns the sum."""
  return x + y

def main():
  """Main function to demonstrate the greetings and addition."""
  greet("World")
  result = add(5, 3)
  print(f"The sum of 5 and 3 is: {result}")

if __name__ == "__main__":
  main()