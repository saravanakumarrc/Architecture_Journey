# Message Broker Architectures

```mermaid
mindmap
    root((Message
        Brokers))
        (Patterns)
            [Pub/Sub]
            [Queue]
            [Topic]
            [Event Bus]
        (Technologies)
            [Kafka]
            [RabbitMQ]
            [Azure Service Bus]
            [Amazon SQS/SNS]
        (Features)
            [Durability]
            [Ordering]
            [Scalability]
            [Delivery Guarantees]
```

## Core Message Patterns

### 1. Messaging Models

```mermaid
graph TB
    subgraph "Communication Models"
        direction TB
        
        subgraph "Point-to-Point"
            P1[Producer] --> Q[Queue]
            Q --> C1[Consumer]
        end
        
        subgraph "Publish/Subscribe"
            P2[Publisher] --> T[Topic]
            T --> S1[Subscriber 1]
            T --> S2[Subscriber 2]
            T --> S3[Subscriber 3]
        end
        
        subgraph "Event Bus"
            E1[Event 1] --> B[Bus]
            E2[Event 2] --> B
            B --> H1[Handler 1]
            B --> H2[Handler 2]
        end
    end
```

### 2. Message Flow Types

```mermaid
sequenceDiagram
    participant P as Producer
    participant B as Broker
    participant C as Consumer
    
    P->>B: Send Message
    B->>B: Store Message
    B->>C: Deliver Message
    C-->>B: Acknowledge
    B->>B: Remove Message
```

## Implementation Patterns

### 1. Queue Pattern
```typescript
// Azure Service Bus Queue Example
class OrderProcessor {
    private serviceBusClient: ServiceBusClient;
    private sender: ServiceBusSender;
    private receiver: ServiceBusReceiver;

    async sendOrder(order: Order): Promise<void> {
        const message = {
            body: order,
            contentType: "application/json",
            messageId: order.id
        };
        await this.sender.sendMessages(message);
    }

    async processOrders(): Promise<void> {
        const messages = await this.receiver.receiveMessages(10);
        for (const message of messages) {
            try {
                await this.processOrder(message.body);
                await this.receiver.completeMessage(message);
            } catch (error) {
                await this.receiver.abandonMessage(message);
            }
        }
    }
}
```

### 2. Pub/Sub Pattern

```mermaid
graph TB
    subgraph "Event Publishing"
        direction TB
        
        P[Publisher] --> T[Topic]
        
        subgraph "Subscriptions"
            T --> F1[Filter 1] --> S1[Subscriber 1]
            T --> F2[Filter 2] --> S2[Subscriber 2]
            T --> F3[Filter 3] --> S3[Subscriber 3]
        end
    end
```

### Implementation Example
```typescript
// Event Publishing with Filtering
class EventPublisher {
    private topicClient: TopicClient;

    async publishEvent(event: Event): Promise<void> {
        const message = {
            body: event,
            label: event.type,
            userProperties: {
                category: event.category,
                priority: event.priority
            }
        };
        await this.topicClient.send(message);
    }
}

class EventSubscriber {
    private subscriptionClient: SubscriptionClient;

    async setupSubscription(): Promise<void> {
        const rules = [
            {
                name: "HighPriorityFilter",
                filter: "priority = 'high'"
            },
            {
                name: "OrdersFilter",
                filter: "category = 'orders'"
            }
        ];
        await this.subscriptionClient.addRules(rules);
    }
}
```

## Message Reliability Patterns

### 1. Exactly-Once Delivery

```mermaid
sequenceDiagram
    participant P as Producer
    participant B as Broker
    participant C as Consumer
    participant S as Store
    
    P->>B: Send(MessageId=1)
    B->>S: Store Message
    B->>C: Deliver Message
    C->>S: Check If Processed
    S-->>C: Not Processed
    C->>B: Process & Acknowledge
    C->>S: Mark as Processed
```

### 2. Dead Letter Pattern
```typescript
// Dead Letter Handling
class MessageProcessor {
    private receiver: MessageReceiver;
    private deadLetterSender: MessageSender;

    async processMessage(message: Message): Promise<void> {
        try {
            await this.processBusinessLogic(message);
            await this.receiver.complete(message);
        } catch (error) {
            if (message.deliveryCount > 3) {
                await this.moveToDeadLetter(message, error);
            } else {
                await this.receiver.abandon(message);
            }
        }
    }

    private async moveToDeadLetter(message: Message, error: Error): Promise<void> {
        const deadLetterMessage = {
            body: message.body,
            userProperties: {
                originalMessageId: message.messageId,
                error: error.message,
                failedAt: new Date().toISOString()
            }
        };
        await this.deadLetterSender.send(deadLetterMessage);
        await this.receiver.complete(message);
    }
}
```

## Scalability Patterns

### 1. Competing Consumers

```mermaid
graph TB
    subgraph "Load Distribution"
        direction TB
        
        Q[Queue] --> C1[Consumer 1]
        Q --> C2[Consumer 2]
        Q --> C3[Consumer 3]
        
        subgraph "Auto-scaling"
            M[Metrics]
            M --> S[Scaler]
            S -.-> C4[Consumer 4]
        end
    end
```

### 2. Partitioning Pattern
```typescript
// Partitioned Queue Processing
class PartitionedProcessor {
    private partitionReceivers: Map<number, MessageReceiver>;

    async processPartition(partitionId: number): Promise<void> {
        const receiver = this.partitionReceivers.get(partitionId);
        const messages = await receiver.receiveMessages(100);

        await Promise.all(messages.map(async message => {
            try {
                await this.processMessage(message);
                await receiver.complete(message);
            } catch (error) {
                await receiver.abandon(message);
            }
        }));
    }
}
```

## Monitoring and Management

### 1. Health Metrics

```mermaid
graph TB
    subgraph "Monitoring Points"
        direction TB
        
        subgraph "Queue Metrics"
            M1[Message Count]
            M2[Processing Time]
            M3[Error Rate]
            M4[Dead Letters]
        end
        
        subgraph "System Metrics"
            S1[CPU Usage]
            S2[Memory]
            S3[Network]
            S4[Disk IO]
        end
        
        M1 & M2 & M3 & M4 --> A[Alerts]
        S1 & S2 & S3 & S4 --> A
    end
```

## Best Practices

1. **Message Design**
   - Use clear message schemas
   - Include metadata
   - Version messages
   - Keep messages small

2. **Error Handling**
   - Implement retry policies
   - Use dead letter queues
   - Log failed messages
   - Monitor error rates

3. **Performance**
   - Batch messages when possible
   - Use async operations
   - Implement partitioning
   - Consider message compression

4. **Security**
   - Encrypt messages
   - Use access control
   - Implement authentication
   - Audit message access

Remember: Message brokers are crucial for building resilient, decoupled systems. Choose patterns and implementations that match your reliability and scalability requirements.