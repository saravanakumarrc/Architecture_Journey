# Domain-Driven Design (DDD)

```mermaid
mindmap
    root((Domain-Driven
        Design))
        (Strategic Design)
            [Bounded Context]
            [Ubiquitous Language]
            [Context Mapping]
            [Core Domain]
        (Tactical Design)
            [Aggregates]
            [Entities]
            [Value Objects]
            [Domain Events]
        (Architecture)
            [Layered Architecture]
            [Hexagonal Architecture]
            [CQRS]
            [Event Sourcing]
```

## Strategic Design Patterns

### 1. Bounded Contexts

```mermaid
graph TB
    subgraph "E-commerce Example"
        direction TB
        
        subgraph "Order Context"
            O[Order]
            C[Customer]
            P[Payment]
        end
        
        subgraph "Inventory Context"
            I[Product]
            S[Stock]
            W[Warehouse]
        end
        
        subgraph "Shipping Context"
            D[Delivery]
            A[Address]
            R[Route]
        end
        
        O --> I
        O --> D
    end
```

### 2. Context Mapping

```mermaid
graph LR
    subgraph "Context Relationships"
        direction LR
        
        C1[Context A] -->|Partnership| C2[Context B]
        C2 -->|Customer/Supplier| C3[Context C]
        C3 -->|Conformist| C4[Context D]
        C1 -->|Anti-corruption Layer| C4
    end
```

## Tactical Design Patterns

### 1. Entity Pattern
```typescript
class Order {
    private readonly id: OrderId;
    private items: OrderItem[];
    private status: OrderStatus;

    constructor(id: OrderId) {
        this.id = id;
        this.items = [];
        this.status = OrderStatus.Created;
    }

    addItem(item: OrderItem): void {
        if (this.status !== OrderStatus.Created) {
            throw new OrderModificationError();
        }
        this.items.push(item);
    }
}
```

### 2. Value Object Pattern
```typescript
class Money {
    private readonly amount: number;
    private readonly currency: Currency;

    constructor(amount: number, currency: Currency) {
        this.amount = amount;
        this.currency = currency;
    }

    add(other: Money): Money {
        if (this.currency !== other.currency) {
            throw new CurrencyMismatchError();
        }
        return new Money(this.amount + other.amount, this.currency);
    }
}
```

### 3. Aggregate Pattern

```mermaid
graph TB
    subgraph "Order Aggregate"
        O[Order Root] --> I[OrderItem]
        O --> A[Address]
        O --> P[Payment]
        I --> D[Discount]
    end
```

## Domain Events

### Event Flow Pattern
```mermaid
sequenceDiagram
    participant O as Order Service
    participant E as Event Bus
    participant I as Inventory Service
    participant S as Shipping Service

    O->>E: OrderCreated
    E->>I: Update Inventory
    E->>S: Prepare Shipment
    I-->>E: InventoryUpdated
    S-->>E: ShipmentPrepared
    E-->>O: Order Status Updated
```

## Implementation Guidelines

### 1. Ubiquitous Language
- Use domain terms consistently
- Document domain vocabulary
- Reflect language in code
- Evolve language with domain experts

### 2. Bounded Context Guidelines
- Define clear boundaries
- Identify context relationships
- Document context maps
- Maintain context integrity

### 3. Aggregate Design Rules
- Keep aggregates small
- Ensure business invariants
- Use eventual consistency between aggregates
- Reference other aggregates by ID

## Architecture Patterns

### 1. Layered Architecture
```mermaid
graph TB
    subgraph "DDD Layers"
        UI[User Interface]
        APP[Application]
        DOM[Domain]
        INF[Infrastructure]
        
        UI --> APP
        APP --> DOM
        APP --> INF
        INF --> DOM
    end
```

### 2. CQRS with Domain Events
```mermaid
graph TB
    subgraph "CQRS Pattern"
        C[Commands] --> M[Command Handler]
        M --> A[Aggregate]
        A --> E[Events]
        E --> P[Projections]
        Q[Queries] --> V[View Model]
    end
```

## Best Practices

1. **Domain Modeling**
   - Focus on business rules
   - Identify domain experts
   - Model state transitions
   - Document assumptions

2. **Testing Strategy**
   - Unit test domain logic
   - Test aggregate invariants
   - Verify event handling
   - Test business scenarios

3. **Performance Considerations**
   - Aggregate size limits
   - Event sourcing overhead
   - Read model optimization
   - Eventual consistency impact

4. **Common Pitfalls**
   - Over-complicated models
   - Missing bounded contexts
   - Anemic domain models
   - Inconsistent language

Remember: DDD is most valuable for complex domains with sophisticated business rules. For simpler applications, a more straightforward approach might be more appropriate.