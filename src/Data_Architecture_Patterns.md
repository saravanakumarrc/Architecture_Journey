# Data Architecture Patterns

```mermaid
mindmap
    root((Data
        Architecture))
        (Storage Types)
            [Relational]
            [Document]
            [Key-Value]
            [Graph]
        (Access Patterns)
            [CRUD]
            [CQRS]
            [Event Sourcing]
            [Polyglot]
        (Distribution)
            [Sharding]
            [Replication]
            [Partitioning]
            [Federation]
        (Integration)
            [ETL]
            [Change Data Capture]
            [Data Lake]
            [Data Mesh]
```

## Core Data Patterns

### 1. CQRS (Command Query Responsibility Segregation)

```mermaid
graph TB
    subgraph "CQRS Architecture"
        C[Client] --> CM[Command Model]
        C --> QM[Query Model]
        
        CM --> WDB[(Write DB)]
        QM --> RDB[(Read DB)]
        
        subgraph "Sync Process"
            WDB --> SYNC[Sync/ETL]
            SYNC --> RDB
        end
    end
```

Implementation Example:
```typescript
// Command side
interface OrderCommand {
    createOrder(order: Order): Promise<string>;
    updateOrder(orderId: string, update: OrderUpdate): Promise<void>;
}

class OrderCommandHandler implements OrderCommand {
    constructor(private writeDb: Database) {}

    async createOrder(order: Order): Promise<string> {
        const orderId = generateId();
        await this.writeDb.execute(
            'INSERT INTO orders (id, customer, items, status) VALUES (?, ?, ?, ?)',
            [orderId, order.customer, JSON.stringify(order.items), 'pending']
        );
        await this.publishEvent('OrderCreated', { orderId, order });
        return orderId;
    }
}

// Query side
interface OrderQuery {
    getOrder(orderId: string): Promise<OrderDetails>;
    getCustomerOrders(customerId: string): Promise<OrderSummary[]>;
}

class OrderQueryHandler implements OrderQuery {
    constructor(private readDb: Database) {}

    async getOrder(orderId: string): Promise<OrderDetails> {
        return this.readDb.queryOne(
            'SELECT * FROM order_details_view WHERE id = ?',
            [orderId]
        );
    }
}
```

### 2. Event Sourcing Pattern

```mermaid
graph LR
    subgraph "Event Sourcing"
        E[Events] --> ES[Event Store]
        ES --> S[Snapshots]
        ES --> P1[Projection 1]
        ES --> P2[Projection 2]
        ES --> P3[Projection 3]
    end
```

Implementation Example:
```typescript
// Event sourcing with snapshots
class OrderAggregate {
    private state: OrderState;
    private version: number = 0;
    
    async loadFromHistory(events: Event[]): Promise<void> {
        for (const event of events) {
            this.apply(event);
            this.version = event.version;
        }
    }
    
    createOrder(order: Order): Event {
        this.ensureCanCreate(order);
        
        const event = {
            type: 'OrderCreated',
            data: order,
            version: this.version + 1
        };
        
        this.apply(event);
        return event;
    }
    
    private apply(event: Event): void {
        switch (event.type) {
            case 'OrderCreated':
                this.state = {
                    ...event.data,
                    status: 'created'
                };
                break;
            case 'OrderItemAdded':
                this.state.items.push(event.data);
                break;
            // ... other event handlers
        }
    }
}
```

### 3. Polyglot Persistence

```mermaid
graph TB
    subgraph "Polyglot Storage"
        direction TB
        
        subgraph "Data Types"
            T1[Transactional]
            T2[Document]
            T3[Search]
            T4[Cache]
        end
        
        T1 --> DB1[(PostgreSQL)]
        T2 --> DB2[(MongoDB)]
        T3 --> DB3[(Elasticsearch)]
        T4 --> DB4[(Redis)]
    end
```

Implementation Example:
```typescript
// Polyglot persistence manager
class DataManager {
    constructor(
        private relationalDb: RelationalDB,
        private documentDb: DocumentDB,
        private searchDb: SearchDB,
        private cacheDb: CacheDB
    ) {}

    async saveOrder(order: Order): Promise<void> {
        // Save core transaction data
        const orderId = await this.relationalDb.execute(
            'INSERT INTO orders ...',
            [order.id, order.customerId]
        );

        // Save order details as document
        await this.documentDb.orders.insertOne({
            _id: orderId,
            ...order,
            metadata: { created: new Date() }
        });

        // Index for search
        await this.searchDb.index('orders', {
            id: orderId,
            customerName: order.customerName,
            items: order.items.map(i => i.name)
        });

        // Cache for quick access
        await this.cacheDb.set(
            `order:${orderId}`,
            JSON.stringify(order),
            'EX',
            3600
        );
    }
}
```

## Data Distribution Patterns

### 1. Sharding Strategy

```mermaid
graph TB
    subgraph "Sharding Architecture"
        LB[Load Balancer]
        
        subgraph "Shard 1"
            S1[Server 1]
            DB1[(Database 1)]
        end
        
        subgraph "Shard 2"
            S2[Server 2]
            DB2[(Database 2)]
        end
        
        subgraph "Shard 3"
            S3[Server 3]
            DB3[(Database 3)]
        end
        
        LB --> S1
        LB --> S2
        LB --> S3
    end
```

Implementation Example:
```typescript
// Sharding manager with consistent hashing
class ShardManager {
    private shards: Map<string, DatabaseConnection>;
    private hashRing: ConsistentHashRing;

    constructor(shardConfigs: ShardConfig[]) {
        this.hashRing = new ConsistentHashRing();
        
        for (const config of shardConfigs) {
            const connection = createConnection(config);
            this.shards.set(config.id, connection);
            this.hashRing.addNode(config.id);
        }
    }

    async executeQuery(shardKey: string, query: string): Promise<any> {
        const shardId = this.hashRing.getNode(shardKey);
        const shard = this.shards.get(shardId);
        
        return shard.execute(query);
    }
}
```

### 2. Multi-Region Replication

```mermaid
graph TB
    subgraph "Multi-Region Architecture"
        direction TB
        
        subgraph "Region 1"
            P1[Primary]
            S1[Secondary]
        end
        
        subgraph "Region 2"
            P2[Primary]
            S2[Secondary]
        end
        
        P1 -->|Sync| S2
        P2 -->|Sync| S1
    end
```

Implementation Example (using Azure Cosmos DB):
```typescript
import { CosmosClient } from "@azure/cosmos";

class MultiRegionDatabase {
    constructor(private client: CosmosClient) {}

    async writeWithConsistency(
        document: any,
        writeRegion: string,
        consistencyLevel: ConsistencyLevel
    ): Promise<void> {
        const container = this.client
            .database('mydb')
            .container('mycollection');

        const options = {
            consistencyLevel,
            sessionToken: null
        };

        if (writeRegion) {
            options.preferredLocations = [writeRegion];
        }

        await container.items.create(document, options);
    }
}
```

## Best Practices

1. **Data Access Patterns**
   - Use appropriate consistency levels
   - Implement proper caching strategy
   - Consider access patterns in schema design
   - Use connection pooling

2. **Data Distribution**
   - Choose sharding key carefully
   - Plan for data locality
   - Implement proper backup strategy
   - Monitor replication lag

3. **Performance Optimization**
   - Index strategically
   - Use appropriate partitioning
   - Monitor query performance
   - Optimize data access patterns

4. **Data Governance**
   - Implement data validation
   - Maintain data quality
   - Apply security controls
   - Monitor data usage

Remember: Data architecture decisions have long-lasting implications for system performance, scalability, and maintenance. Choose patterns that align with your specific requirements while considering future growth.