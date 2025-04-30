# Message Broker Architectures

```mermaid
mindmap
    root((Message
        Brokers))
        (Patterns)
            [Pub/Sub]
            [Point-to-Point]
            [Request/Reply]
            [Competing Consumers]
        (Features)
            [Reliability]
            [Scalability]
            [Ordering]
            [Persistence]
        (Components)
            [Producers]
            [Consumers]
            [Topics/Queues]
            [Dead Letter]
        (Technologies)
            [Kafka]
            [RabbitMQ]
            [Azure ServiceBus]
            [AWS SQS/SNS]
```

## Core Message Patterns

### 1. Publish/Subscribe Pattern

```mermaid
graph LR
    subgraph "Pub/Sub Architecture"
        P1[Producer 1] --> T[Topic]
        P2[Producer 2] --> T
        T --> S1[Subscription 1]
        T --> S2[Subscription 2]
        T --> S3[Subscription 3]
    end
```

Implementation Example (using Azure Service Bus):
```typescript
// Message publisher with retry policy
class EventPublisher {
    constructor(
        private serviceBusClient: ServiceBusClient,
        private topicName: string
    ) {}

    async publishEvent<T extends DomainEvent>(
        event: T,
        options: PublishOptions = {}
    ): Promise<void> {
        const sender = this.serviceBusClient.createSender(this.topicName);
        
        try {
            const message = {
                body: event,
                contentType: 'application/json',
                messageId: uuidv4(),
                correlationId: options.correlationId,
                subject: event.eventType,
                userProperties: {
                    eventType: event.eventType,
                    version: '1.0',
                    source: 'order-service'
                }
            };

            await this.executeWithRetry(() => 
                sender.sendMessages(message)
            );
        } finally {
            await sender.close();
        }
    }

    private async executeWithRetry(
        operation: () => Promise<void>
    ): Promise<void> {
        const retryOptions = {
            maxRetries: 3,
            delay: 1000,
            backoffCoefficient: 2
        };

        let attempt = 0;
        while (attempt <= retryOptions.maxRetries) {
            try {
                await operation();
                return;
            } catch (error) {
                if (attempt === retryOptions.maxRetries) {
graph TB
    subgraph "Message Components"
        H[Header] --> M[Metadata]
        M --> P[Payload]
        P --> F[Footer]
        
        subgraph "Attributes"
            ID[Message ID]
            TS[Timestamp]
            COR[Correlation ID]
            TTL[Time to Live]
        end
    end
```

### 2. Message Properties
1. **Required Properties**
   - Message ID
   - Timestamp
   - Content type
   - Content encoding

2. **Optional Properties**
   - Correlation ID
   - Reply to
   - Expiration
   - Priority

3. **Custom Headers**
   - Business metadata
   - Routing info
   - Tracking data
   - Version info

## Reliability Patterns

### 1. Message Delivery

```mermaid
graph TB
    subgraph "Delivery Guarantees"
        AO[At-least-once] --> ACK[Acknowledgment]
        MO[At-most-once] --> DLQ[Dead Letter]
        EO[Exactly-once] --> DEDUP[Deduplication]
        
        subgraph "Features"
            PERS[Persistence]
            REPL[Replication]
            TRAN[Transactions]
        end
    end
```

#### Delivery Strategies
| Strategy | Guarantee | Performance | Use Case |
|----------|-----------|-------------|----------|
| At-least-once | High | Medium | Critical Data |
| At-most-once | Low | High | Metrics/Logs |
| Exactly-once | Very High | Low | Transactions |

### 2. Error Handling

```mermaid
graph LR
    subgraph "Error Management"
        F[Failure] --> R[Retry]
        R --> D[DLQ]
        D --> P[Process/Alert]
        
        subgraph "Strategies"
            EXP[Exponential Backoff]
            MAX[Max Retries]
            ALT[Alternative Route]
        end
    end
```

## Performance Optimization

### 1. Scaling Patterns

```mermaid
graph TB
    subgraph "Scaling Architecture"
        P[Partitioning] --> C[Clustering]
        C --> R[Replication]
        R --> L[Load Balancing]
        
        subgraph "Methods"
            HP[Horizontal]
            VP[Vertical]
            GEO[Geographic]
        end
    end
```

### 2. Performance Checklist
- [ ] Message batching
- [ ] Consumer scaling
- [ ] Producer throttling
- [ ] Connection pooling
- [ ] Network optimization
- [ ] Memory management
- [ ] Disk I/O tuning
- [ ] Monitoring setup

## Monitoring Framework

### 1. Key Metrics

```mermaid
graph TB
    subgraph "Monitoring System"
        T[Throughput] --> L[Latency]
        L --> Q[Queue Length]
        Q --> E[Errors]
        
        subgraph "Alerts"
            QF[Queue Full]
            DL[Dead Letter]
            SL[SLA Breach]
        end
    end
```

### 2. Monitoring Checklist
- [ ] Message rates
- [ ] Queue depths
- [ ] Consumer lag
- [ ] Error rates
- [ ] Resource usage
- [ ] Network latency
- [ ] Disk usage
- [ ] Alert thresholds

## Security Framework

### 1. Security Architecture

```mermaid
graph TB
    subgraph "Security Layers"
        A[Authentication] --> Z[Authorization]
        Z --> E[Encryption]
        E --> A[Auditing]
        
        subgraph "Controls"
            AC[Access Control]
            TLS[Transport Security]
            LOG[Logging]
        end
    end
```

### 2. Security Checklist
- [ ] TLS configuration
- [ ] Authentication setup
- [ ] Authorization rules
- [ ] Message encryption
- [ ] Network security
- [ ] Audit logging
- [ ] Access controls
- [ ] Compliance checks

## Implementation Guidance

### 1. Best Practices
1. **Message Design**
   - Schema versioning
   - Backward compatibility
   - Forward compatibility
   - Message validation

2. **Error Handling**
   - Retry policies
   - Dead letter queues
   - Error logging
   - Alert mechanisms

3. **Performance**
   - Connection pooling
   - Message batching
   - Prefetch settings
   - Resource limits

### 2. Anti-patterns to Avoid
- Direct broker-to-broker communication
- Synchronous request-reply over queues
- Large message payloads
- Queue proliferation
- Missing message TTL
- Lack of monitoring
- Insufficient security
- No message schema

## Decision Framework

### 1. Broker Selection
| Feature | RabbitMQ | Kafka | Azure Service Bus |
|---------|----------|-------|-------------------|
| Patterns | All | Streaming | All |
| Scale | Medium | Very High | High |
| Latency | Very Low | Low | Low |
| Features | Rich | Basic | Rich |
| Management | Good | Complex | Excellent |

### 2. Architecture Decisions
1. **Message Flow**
   - Routing patterns
   - Exchange types
   - Queue design
   - Consumer groups

2. **Infrastructure**
   - High availability
   - Disaster recovery
   - Geographic distribution
   - Resource sizing

Remember: Message broker architectures should focus on reliability, scalability, and manageability while ensuring proper message delivery guarantees.