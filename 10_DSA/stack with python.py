Stacks with Python
A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.

Think of it like a stack of pancakes - you can only add or remove pancakes from the top.

Stacks
A stack is a data structure that can hold many elements, and the last element added is the first one to be removed.

Like a pile of pancakes, the pancakes are both added and removed from the top. So when removing a pancake, it will always be the last pancake you added. This way of organizing elements is called LIFO: Last In First Out.

Basic operations we can do on a stack are:

Push: Adds a new element on the stack.
Pop: Removes and returns the top element from the stack.
Peek: Returns the top (last) element on the stack.
isEmpty: Checks if the stack is empty.
Size: Finds the number of elements in the stack.
Stacks can be implemented by using arrays or linked lists.

Stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in graphs, or for backtracking.

Stacks are often mentioned together with Queues, which is a similar data structure described on the next page.

Stack Implementation using Python Lists
For Python lists (and arrays), a stack can look and behave like this:

x = [5, 6, 2, 9, 3, 8, 4, 2]
Add:  Remove: 
Since Python lists has good support for functionality needed to implement stacks, we start with creating a stack and do stack operations with just a few lines like this:

ExampleGet your own Python Server
Using a Python list as a stack:

stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# Pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", stack)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))


Code Breakdown:
class Stack:


👉 This line defines a class named Stack.
A class is like a blueprint to create objects (in this case, a stack).

  def __init__(self):
    self.stack = []


👉 __init__ is a constructor method that runs automatically when you create a new object of Stack.

self.stack = [] → we create an empty list that will be used to store stack elements.

self refers to the object itself.

  def push(self, element):
    self.stack.append(element)


👉 push method adds a new element to the stack.

self.stack.append(element) → adds the element at the end of the list (which represents the top of the stack).

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()


👉 pop method removes and returns the top element of the stack.

First, it checks if self.isEmpty() → if the stack has no elements.

If empty → it returns "Stack is empty".

Otherwise → self.stack.pop() removes and returns the last element of the list (the stack’s top).

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]


👉 peek method returns the top element of the stack without removing it.

If stack is empty → "Stack is empty".

Otherwise → self.stack[-1] gives the last element in the list.

  def isEmpty(self):
    return len(self.stack) == 0


👉 isEmpty checks if the stack has no elements.

len(self.stack) → gives the number of items.

If 0 → returns True, else False.

  def size(self):
    return len(self.stack)


👉 size returns the number of elements in the stack using len.

Now the usage part:
# Create a stack
myStack = Stack()


👉 Creates an object of class Stack.

myStack.stack starts as an empty list [].

myStack.push('A')
myStack.push('B')
myStack.push('C')


👉 Adds elements one by one:

After push('A') → stack = ['A']

After push('B') → stack = ['A', 'B']

After push('C') → stack = ['A', 'B', 'C']

print("Stack: ", myStack.stack)


👉 Prints the whole stack → ['A', 'B', 'C'].

print("Pop: ", myStack.pop())


👉 Removes and prints the top element:

pop() removes 'C' (last element).

Output → "Pop: C"

print("Stack after Pop: ", myStack.stack)


👉 Prints the stack after popping 'C'.

Now → ['A', 'B']

print("Peek: ", myStack.peek())


👉 Looks at the top element without removing it.

Top element = 'B'

Output → "Peek: B"

print("isEmpty: ", myStack.isEmpty())


👉 Checks if stack is empty.

['A', 'B'] is not empty → False

print("Size: ", myStack.size())


👉 Prints the number of elements.

['A', 'B'] has 2 elements → 2

Final Output will be:
Stack:  ['A', 'B', 'C']
Pop:  C
Stack after Pop:  ['A', 'B']
Peek:  B
isEmpty:  False
Size:  2


⚡ Easy way to remember:

Push → Add to top

Pop → Remove from top

Peek → See top element

isEmpty → Check if no elements

Size → Count elements
