# Programming Paradigms

## Overview
Programming paradigms are fundamental styles of programming that shape how we structure and organize code. Each paradigm offers different approaches to solving problems and has its own strengths and use cases.

## Object-Oriented Programming (OOP)

### Core Concepts
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

### Example (Java)
```java
// Basic OOP example
public abstract class Shape {
    protected String color;
    
    public abstract double calculateArea();
    
    public void setColor(String color) {
        this.color = color;
    }
}

public class Circle extends Shape {
    private double radius;
    
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
}
```

### When to Use OOP
- Complex systems with clear object hierarchies
- When state management is important
- For building reusable, modular components
- When modeling real-world entities and relationships

## Functional Programming

### Core Concepts
- Immutability
- Pure functions
- First-class functions
- Higher-order functions
- Function composition

### Example (JavaScript)
```javascript
// Functional programming example
const numbers = [1, 2, 3, 4, 5];

const double = x => x * 2;
const isEven = x => x % 2 === 0;

const doubledEvenNumbers = numbers
    .filter(isEven)
    .map(double);
```

### When to Use Functional Programming
- Data processing pipelines
- Concurrent/parallel programming
- When debugging and testing need to be simplified
- For mathematical computations and transformations

## Procedural Programming

### Core Concepts
- Sequential execution
- Procedures/functions
- Global state
- Top-down approach

### Example (C)
```c
void calculateAndPrintAverage(int numbers[], int size) {
    int sum = 0;
    for(int i = 0; i < size; i++) {
        sum += numbers[i];
    }
    float average = (float)sum / size;
    printf("Average: %f\n", average);
}
```

### When to Use Procedural Programming
- Simple, straightforward programs
- System-level programming
- When performance is critical
- For linear problem-solving approaches

## Trade-offs and Considerations

### OOP vs Functional
- State management vs Stateless
- Mutability vs Immutability
- Inheritance vs Composition
- Side effects vs Pure functions

### OOP vs Procedural
- Abstraction level
- Code organization
- Maintainability
- Learning curve

## Best Practices

### OOP
1. Follow SOLID principles
2. Favor composition over inheritance
3. Keep classes focused and single-responsibility
4. Use interfaces for abstraction

### Functional
1. Avoid side effects
2. Use pure functions when possible
3. Leverage function composition
4. Embrace immutability

### Procedural
1. Keep functions small and focused
2. Minimize global state
3. Use clear naming conventions
4. Maintain logical code organization

## Real-world Applications

### OOP
- Large enterprise applications
- GUI frameworks
- Game development
- Complex domain models

### Functional
- Data processing systems
- React/Redux applications
- Stream processing
- Financial calculations

### Procedural
- System utilities
- Embedded systems
- Command-line tools
- Simple data processing scripts