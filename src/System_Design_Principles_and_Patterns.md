# System Design Principles and Patterns

## Design Principles

### 1. SOLID Principles

**Single Responsibility Principle (SRP)**
* Definition: A class/module should have only one reason to change
* Example:
  ```
  // Good example
  class UserAuthenticator {
      authenticate(credentials) { /* ... */ }
  }
  class UserProfileManager {
      updateProfile(data) { /* ... */ }
  }

  // Bad example
  class User {
      authenticate() { /* ... */ }
      updateProfile() { /* ... */ }
      sendEmail() { /* ... */ }
  }
  ```

**Open/Closed Principle**
* Definition: Software entities should be open for extension but closed for modification
* Example: Using interfaces for payment methods
  ```
  interface PaymentProcessor {
      process(amount: number): void;
  }

  class CreditCardPayment implements PaymentProcessor {
      process(amount: number) { /* ... */ }
  }

  class PayPalPayment implements PaymentProcessor {
      process(amount: number) { /* ... */ }
  }
  ```

**Liskov Substitution Principle**
* Definition: Objects should be replaceable with their subtypes without affecting program correctness
* Example: Shape hierarchy
  ```
  class Rectangle {
      setWidth(w: number): void
      setHeight(h: number): void
      getArea(): number
  }

  class Square extends Rectangle {
      // Must maintain the rectangle contract
  }
  ```

**Interface Segregation Principle**
* Definition: Clients shouldn't be forced to depend on interfaces they don't use
* Example:
  ```
  // Bad
  interface Worker {
      work(): void;
      eat(): void;
  }

  // Good
  interface Workable {
      work(): void;
  }
  interface Eatable {
      eat(): void;
  }
  ```

**Dependency Inversion Principle**
* Definition: High-level modules shouldn't depend on low-level modules; both should depend on abstractions
* Example:
  ```
  // High-level module depending on abstraction
  class NotificationService {
      constructor(private messenger: IMessenger) {}
  }

  interface IMessenger {
      send(message: string): void;
  }

  // Low-level modules implementing abstraction
  class EmailMessenger implements IMessenger {}
  class SMSMessenger implements IMessenger {}
  ```

### 2. Other Key Principles

**DRY (Don't Repeat Yourself)**
* Definition: Avoid code duplication by extracting common functionality
* Example: Creating reusable utility functions
  ```
  // Instead of repeating validation
  function validateEmail(email: string): boolean {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }
  ```

**KISS (Keep It Simple, Stupid)**
* Definition: Systems work best when kept simple
* Example: Using simple REST APIs over complex GraphQL when basic CRUD is sufficient

**YAGNI (You Aren't Gonna Need It)**
* Definition: Don't add functionality until it's necessary
* Example: Not implementing caching until performance metrics show it's needed

## Design Patterns

### 1. Creational Patterns

**Singleton Pattern**
* Purpose: Ensure a class has only one instance
* Example:
  ```typescript
  class DatabaseConnection {
      private static instance: DatabaseConnection;
      
      private constructor() {}
      
      public static getInstance(): DatabaseConnection {
          if (!DatabaseConnection.instance) {
              DatabaseConnection.instance = new DatabaseConnection();
          }
          return DatabaseConnection.instance;
      }
  }
  ```

**Factory Pattern**
* Purpose: Create objects without exposing creation logic
* Example:
  ```typescript
  interface Animal { speak(): void; }
  
  class Dog implements Animal {
      speak() { console.log('Woof!'); }
  }
  
  class Cat implements Animal {
      speak() { console.log('Meow!'); }
  }
  
  class AnimalFactory {
      createAnimal(type: string): Animal {
          switch(type) {
              case 'dog': return new Dog();
              case 'cat': return new Cat();
              default: throw new Error('Unknown animal type');
          }
      }
  }
  ```

### 2. Structural Patterns

**Adapter Pattern**
* Purpose: Allow incompatible interfaces to work together
* Example:
  ```typescript
  interface ModernPaymentGateway {
      processPayment(amount: number): void;
  }

  class LegacyPaymentSystem {
      oldProcessPayment(sum: number, currency: string): void {}
  }

  class PaymentAdapter implements ModernPaymentGateway {
      constructor(private legacySystem: LegacyPaymentSystem) {}
      
      processPayment(amount: number): void {
          this.legacySystem.oldProcessPayment(amount, 'USD');
      }
  }
  ```

### 3. Behavioral Patterns

**Observer Pattern**
* Purpose: Define one-to-many dependency between objects
* Example:
  ```typescript
  interface Observer {
      update(data: any): void;
  }

  class NewsAgency {
      private observers: Observer[] = [];
      
      attach(observer: Observer): void {
          this.observers.push(observer);
      }
      
      notifyObservers(news: string): void {
          this.observers.forEach(observer => observer.update(news));
      }
  }
  ```

### 4. Architectural Patterns

**Microservices Pattern**
* Purpose: Build application as suite of small services
* Example: E-commerce system split into:
  - User Service (authentication/profiles)
  - Product Service (catalog/inventory)
  - Order Service (order processing)
  - Payment Service (payment processing)

**Event-Driven Architecture**
* Purpose: Design systems around production, detection, and reaction to events
* Example:
  ```typescript
  interface EventBus {
      publish(event: string, data: any): void;
      subscribe(event: string, callback: (data: any) => void): void;
  }

  class OrderService {
      constructor(private eventBus: EventBus) {
          this.eventBus.subscribe('OrderPlaced', this.handleOrderPlaced);
      }
  }
  ```

### 5. Cloud Patterns

**Circuit Breaker Pattern**
* Purpose: Prevent system failure cascade
* Example:
  ```typescript
  class CircuitBreaker {
      private failures = 0;
      private threshold = 5;
      private state: 'CLOSED' | 'OPEN' = 'CLOSED';

      async call(fn: () => Promise<any>) {
          if (this.state === 'OPEN') {
              throw new Error('Circuit is OPEN');
          }

          try {
              const result = await fn();
              this.failures = 0;
              return result;
          } catch (error) {
              this.failures++;
              if (this.failures >= this.threshold) {
                  this.state = 'OPEN';
              }
              throw error;
          }
      }
  }
  ```

**Retry Pattern**
* Purpose: Handle transient failures
* Example:
  ```typescript
  async function withRetry<T>(
      fn: () => Promise<T>,
      maxAttempts: number = 3
  ): Promise<T> {
      let lastError: Error;
      
      for (let attempt = 1; attempt <= maxAttempts; attempt++) {
          try {
              return await fn();
          } catch (error) {
              lastError = error;
              await new Promise(resolve => 
                  setTimeout(resolve, Math.pow(2, attempt) * 1000)
              );
          }
      }
      
      throw lastError;
  }
  ```

## Best Practices for Implementation

1. **Start with Principles**
   * Begin with SOLID principles as foundation
   * Apply patterns only when they solve specific problems

2. **Pattern Selection Criteria**
   * Problem fit
   * Maintenance complexity
   * Team expertise
   * Performance implications
   * Scalability requirements

3. **Common Pitfalls to Avoid**
   * Over-engineering
   * Pattern obsession
   * Premature optimization
   * Ignoring context

4. **Documentation Requirements**
   * Pattern usage justification
   * Trade-off analysis
   * Implementation details
   * Maintenance considerations

Remember: Patterns are solutions to common problems. Don't force them where they're not needed. Always consider the specific context and requirements of your system.