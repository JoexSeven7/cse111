def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")


  # Reverse the list and print it
  fruit_reverse = fruit_list[::-1]
  print(f"reversed: {fruit_reverse}")

  fruit_list.append("orange")

  print(f"append: {fruit_list}" )

  # Find where "apple" is located in fruit_list
  apple_index = fruit_list.index("apple")
  print(f"apple is at index: {apple_index}")

  # Insert "cherry" before "apple" in the list
  fruit_list.insert(apple_index, "cherry")
  print(f"insert: {fruit_list}")

  # Remove "banana" from fruit_list and print the list
  fruit_list.remove("banana")
  print(f"remove banana: {fruit_list}")

  # Pop the last element from fruit_list and print the popped element and the list
  popped_element = fruit_list.pop()
  print(f"popped element: {popped_element}")
  print(f"after pop: {fruit_list}")

  # Sort and print fruit_list
  fruit_list.sort()
  print(f"sorted: {fruit_list}")

  # Clear and print fruit_list
  fruit_list.clear()
  print(f"cleared: {fruit_list}")


if __name__ == "__main__":
    main() 