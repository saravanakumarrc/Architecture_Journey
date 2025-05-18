# IRCTC Railway Reservation System - Comprehensive Design Document

## Table of Contents
1. [System Overview](#system-overview)
2. [Functional Requirements](#functional-requirements)
3. [Non-Functional Requirements](#non-functional-requirements)
4. [High-Level Design (HLD)](#high-level-design-hld)
5. [Low-Level Design (LLD)](#low-level-design-lld)
6. [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
7. [UML Diagrams](#uml-diagrams)
8. [API Design](#api-design)
9. [System Architecture](#system-architecture)
10. [Data Flow](#data-flow)
11. [Security Considerations](#security-considerations)
12. [Performance & Scalability](#performance--scalability)
13. [Monitoring & Observability](#monitoring--observability)
14. [Deployment Architecture](#deployment-architecture)

## System Overview

The IRCTC (Indian Railway Catering and Tourism Corporation) system is a comprehensive railway reservation platform that enables users to:
- Search and book train tickets
- Manage reservations
- Handle payments
- Book meals and accommodations
- Access tourism packages

### Key Stakeholders
- **Passengers**: End users booking tickets
- **Railway Staff**: Managing train schedules and operations
- **System Administrators**: Platform maintenance
- **Payment Partners**: Payment gateway providers
- **Tourism Partners**: Hotel and tour operators

## Functional Requirements

### Core Features
1. **User Management**
   - User registration and authentication
   - Profile management
   - Role-based access control

2. **Train Search & Booking**
   - Search trains by route, date, class
   - Real-time seat availability
   - Ticket booking with passenger details
   - Quota management (General, Tatkal, Ladies, etc.)
   - Waitlist management

3. **Payment Processing**
   - Multiple payment methods (UPI, Cards, Wallets)
   - Payment gateway integration
   - Refund processing
   - Transaction history

4. **Reservation Management**
   - View bookings
   - Cancel/modify reservations
   - Print tickets/e-tickets
   - Booking status tracking

5. **Additional Services**
   - Meal booking
   - Hotel reservations
   - Tourism packages
   - Travel insurance

### Business Rules
- Maximum 6 passengers per booking
- Advance booking period: 120 days
- Tatkal booking: 1 day advance
- Dynamic pricing for premium trains
- Cancellation charges based on time before departure

## Non-Functional Requirements

### Performance Requirements
- **Response Time**: 
  - Search results: < 2 seconds
  - Booking confirmation: < 5 seconds
  - Page load time: < 3 seconds
- **Throughput**: 
  - Support 100,000+ concurrent users
  - Handle 10,000+ bookings per minute during peak hours
- **Availability**: 99.9% uptime (8.76 hours downtime/year)

### Scalability Requirements
- Horizontal scaling capability
- Auto-scaling based on load
- Database sharding support
- CDN integration for static content

### Security Requirements
- HTTPS encryption for all communications
- PCI DSS compliance for payment processing
- Two-factor authentication
- Rate limiting and DDoS protection
- Data encryption at rest and in transit

### Reliability Requirements
- Database backup and recovery
- Disaster recovery with RTO < 4 hours, RPO < 1 hour
- Circuit breaker pattern for external services
- Graceful degradation during partial failures

### Usability Requirements
- Responsive design for mobile and desktop
- Multi-language support
- Accessibility compliance (WCAG 2.1)
- Intuitive user interface

## High-Level Design (HLD)

```mermaid
graph TB
    subgraph "Client Layer"
        WEB[Web Browser]
        MOB[Mobile App]
        API_CLIENT[API Clients]
    end
    
    subgraph "Load Balancer"
        LB[Load Balancer]
    end
    
    subgraph "API Gateway"
        GATEWAY[API Gateway]
    end
    
    subgraph "Microservices"
        USER_SVC[User Service]
        SEARCH_SVC[Search Service]
        BOOKING_SVC[Booking Service]
        PAYMENT_SVC[Payment Service]
        NOTIFICATION_SVC[Notification Service]
        INVENTORY_SVC[Inventory Service]
    end
    
    subgraph "Data Layer"
        USER_DB[(User Database)]
        BOOKING_DB[(Booking Database)]
        INVENTORY_DB[(Inventory Database)]
        CACHE[(Redis Cache)]
    end
    
    subgraph "External Services"
        PAYMENT_GW[Payment Gateway]
        SMS_SVC[SMS Service]
        EMAIL_SVC[Email Service]
    end
    
    WEB --> LB
    MOB --> LB
    API_CLIENT --> LB
    LB --> GATEWAY
    
    GATEWAY --> USER_SVC
    GATEWAY --> SEARCH_SVC
    GATEWAY --> BOOKING_SVC
    GATEWAY --> PAYMENT_SVC
    GATEWAY --> NOTIFICATION_SVC
    GATEWAY --> INVENTORY_SVC
    
    USER_SVC --> USER_DB
    BOOKING_SVC --> BOOKING_DB
    INVENTORY_SVC --> INVENTORY_DB
    SEARCH_SVC --> CACHE
    
    PAYMENT_SVC --> PAYMENT_GW
    NOTIFICATION_SVC --> SMS_SVC
    NOTIFICATION_SVC --> EMAIL_SVC
```

### Component Description

1. **API Gateway**: Single entry point for all client requests
2. **User Service**: Authentication, authorization, profile management
3. **Search Service**: Train search, availability checking
4. **Booking Service**: Reservation creation, modification, cancellation
5. **Payment Service**: Payment processing, refunds
6. **Inventory Service**: Seat/berth availability management
7. **Notification Service**: Email, SMS notifications

## Low-Level Design (LLD)

### Search Service Architecture

```mermaid
graph TB
    subgraph "Search Service"
        CONTROLLER[Search Controller]
        SERVICE[Search Service Logic]
        CACHE_MGR[Cache Manager]
        DB_ACCESS[Database Access Layer]
    end
    
    subgraph "Data Sources"
        TRAIN_DB[(Train Database)]
        ROUTE_DB[(Route Database)]
        REDIS[(Redis Cache)]
    end
    
    CLIENT[Client Request] --> CONTROLLER
    CONTROLLER --> SERVICE
    SERVICE --> CACHE_MGR
    CACHE_MGR --> REDIS
    SERVICE --> DB_ACCESS
    DB_ACCESS --> TRAIN_DB
    DB_ACCESS --> ROUTE_DB
```

### Booking Service Architecture

```mermaid
graph TB
    subgraph "Booking Service"
        CONTROLLER[Booking Controller]
        BOOKING_MGR[Booking Manager]
        SEAT_ALLOC[Seat Allocator]
        WAITLIST_MGR[Waitlist Manager]
        VALIDATION[Validation Service]
    end
    
    subgraph "External Dependencies"
        INVENTORY[Inventory Service]
        PAYMENT[Payment Service]
        USER[User Service]
    end
    
    CLIENT[Client Request] --> CONTROLLER
    CONTROLLER --> VALIDATION
    VALIDATION --> BOOKING_MGR
    BOOKING_MGR --> SEAT_ALLOC
    BOOKING_MGR --> WAITLIST_MGR
    BOOKING_MGR --> INVENTORY
    BOOKING_MGR --> PAYMENT
    BOOKING_MGR --> USER
```

## Entity Relationship Diagram (ERD)

```mermaid
erDiagram
    USER {
        bigint id PK
        varchar email UK
        varchar phone UK
        varchar first_name
        varchar last_name
        date date_of_birth
        enum gender
        varchar address
        datetime created_at
        datetime updated_at
    }
    
    TRAIN {
        bigint id PK
        varchar train_number UK
        varchar train_name
        enum train_type
        boolean is_active
        datetime created_at
        datetime updated_at
    }
    
    STATION {
        bigint id PK
        varchar station_code UK
        varchar station_name
        varchar city
        varchar state
        decimal latitude
        decimal longitude
    }
    
    ROUTE {
        bigint id PK
        bigint train_id FK
        bigint station_id FK
        int sequence_number
        time arrival_time
        time departure_time
        int distance_from_source
        int halt_duration_minutes
    }
    
    COACH {
        bigint id PK
        bigint train_id FK
        varchar coach_number
        enum coach_type
        int total_seats
        int available_seats
    }
    
    SEAT {
        bigint id PK
        bigint coach_id FK
        varchar seat_number
        enum seat_type
        boolean is_available
    }
    
    BOOKING {
        bigint id PK
        varchar pnr_number UK
        bigint user_id FK
        bigint train_id FK
        bigint source_station_id FK
        bigint destination_station_id FK
        date journey_date
        enum booking_status
        decimal total_amount
        datetime booking_time
        datetime created_at
        datetime updated_at
    }
    
    PASSENGER {
        bigint id PK
        bigint booking_id FK
        varchar name
        int age
        enum gender
        bigint seat_id FK
        enum status
    }
    
    PAYMENT {
        bigint id PK
        bigint booking_id FK
        decimal amount
        enum payment_method
        enum payment_status
        varchar transaction_id
        varchar gateway_response
        datetime payment_time
        datetime created_at
    }
    
    WAITLIST {
        bigint id PK
        bigint booking_id FK
        int queue_position
        datetime created_at
        datetime updated_at
    }
    
    USER ||--o{ BOOKING : makes
    TRAIN ||--o{ ROUTE : has
    TRAIN ||--o{ COACH : contains
    STATION ||--o{ ROUTE : includes
    COACH ||--o{ SEAT : has
    BOOKING ||--o{ PASSENGER : includes
    BOOKING ||--|| PAYMENT : processes
    BOOKING ||--o| WAITLIST : may_have
    SEAT ||--o| PASSENGER : assigned_to
    TRAIN ||--o{ BOOKING : booked_for
    STATION ||--o{ BOOKING : source
    STATION ||--o{ BOOKING : destination
```

## UML Diagrams

### Class Diagram

```mermaid
classDiagram
    class User {
        -Long id
        -String email
        -String phone
        -String firstName
        -String lastName
        -Date dateOfBirth
        -Gender gender
        +register()
        +login()
        +updateProfile()
    }
    
    class Booking {
        -Long id
        -String pnrNumber
        -Long userId
        -Long trainId
        -Date journeyDate
        -BookingStatus status
        -BigDecimal totalAmount
        +createBooking()
        +cancelBooking()
        +modifyBooking()
        +getStatus()
    }
    
    class Train {
        -Long id
        -String trainNumber
        -String trainName
        -TrainType type
        +searchTrains()
        +getAvailability()
        +getSchedule()
    }
    
    class Passenger {
        -Long id
        -String name
        -Integer age
        -Gender gender
        -PassengerStatus status
        +addToBooking()
        +assignSeat()
    }
    
    class Payment {
        -Long id
        -BigDecimal amount
        -PaymentMethod method
        -PaymentStatus status
        -String transactionId
        +processPayment()
        +refund()
        +getStatus()
    }
    
    class Seat {
        -Long id
        -String seatNumber
        -SeatType type
        -Boolean isAvailable
        +book()
        +release()
        +checkAvailability()
    }
    
    User ||--o{ Booking : creates
    Booking ||--o{ Passenger : contains
    Booking ||--|| Payment : processes
    Booking }o--|| Train : for
    Passenger }o--|| Seat : assigned
```

### Sequence Diagram - Ticket Booking Flow

```mermaid
sequenceDiagram
    participant Client
    participant Gateway
    participant UserService
    participant SearchService
    participant BookingService
    participant InventoryService
    participant PaymentService
    participant NotificationService
    
    Client->>Gateway: Search trains
    Gateway->>SearchService: GET /search
    SearchService->>SearchService: Query available trains
    SearchService-->>Gateway: Return search results
    Gateway-->>Client: Search results
    
    Client->>Gateway: Initiate booking
    Gateway->>UserService: Validate user session
    UserService-->>Gateway: Session valid
    
    Gateway->>BookingService: POST /booking
    BookingService->>InventoryService: Reserve seats
    InventoryService-->>BookingService: Seats reserved
    
    BookingService->>PaymentService: Process payment
    PaymentService->>PaymentService: Call payment gateway
    PaymentService-->>BookingService: Payment successful
    
    BookingService->>BookingService: Confirm booking
    BookingService->>NotificationService: Send confirmation
    NotificationService->>NotificationService: Send email/SMS
    
    BookingService-->>Gateway: Booking confirmed
    Gateway-->>Client: Booking confirmation
```

## API Design

### RESTful API Endpoints

#### User Management APIs

```http
POST /api/v1/users/register
POST /api/v1/users/login
POST /api/v1/users/logout
GET /api/v1/users/profile
PUT /api/v1/users/profile
POST /api/v1/users/change-password
```

#### Train Search APIs

```http
GET /api/v1/trains/search
GET /api/v1/trains/{trainId}/availability
GET /api/v1/trains/{trainId}/schedule
GET /api/v1/stations
GET /api/v1/stations/search
```

#### Booking APIs

```http
POST /api/v1/bookings
GET /api/v1/bookings
GET /api/v1/bookings/{pnr}
PUT /api/v1/bookings/{pnr}/modify
DELETE /api/v1/bookings/{pnr}/cancel
GET /api/v1/bookings/{pnr}/status
```

#### Payment APIs

```http
POST /api/v1/payments
GET /api/v1/payments/{transactionId}
POST /api/v1/payments/{transactionId}/refund
GET /api/v1/payments/history
```

### API Request/Response Examples

#### Train Search Request

```json
{
  "method": "GET",
  "endpoint": "/api/v1/trains/search",
  "parameters": {
    "source": "DEL",
    "destination": "BOM",
    "journeyDate": "2025-06-15",
    "class": "3A",
    "quota": "GN"
  }
}
```

#### Train Search Response

```json
{
  "status": "success",
  "data": {
    "trains": [
      {
        "trainId": 12951,
        "trainNumber": "12951",
        "trainName": "MUMBAI RAJDHANI",
        "departureTime": "16:55",
        "arrivalTime": "08:35",
        "duration": "15:40",
        "classes": [
          {
            "classType": "3A",
            "availableSeats": 45,
            "fare": 2550.00,
            "waitlistCount": 0
          }
        ]
      }
    ]
  },
  "timestamp": "2025-05-18T10:30:00Z"
}
```

#### Booking Request

```json
{
  "method": "POST",
  "endpoint": "/api/v1/bookings",
  "body": {
    "trainId": 12951,
    "sourceStation": "DEL",
    "destinationStation": "BOM",
    "journeyDate": "2025-06-15",
    "classType": "3A",
    "quota": "GN",
    "passengers": [
      {
        "name": "John Doe",
        "age": 30,
        "gender": "MALE",
        "nationality": "INDIAN",
        "idType": "AADHAR",
        "idNumber": "123456789012"
      }
    ],
    "contactDetails": {
      "email": "john@example.com",
      "phone": "+919876543210"
    }
  }
}
```

#### Booking Response

```json
{
  "status": "success",
  "data": {
    "pnr": "8217654321",
    "bookingStatus": "CONFIRMED",
    "trainDetails": {
      "trainNumber": "12951",
      "trainName": "MUMBAI RAJDHANI",
      "source": "NEW DELHI",
      "destination": "MUMBAI CENTRAL",
      "journeyDate": "2025-06-15",
      "departureTime": "16:55",
      "arrivalTime": "08:35"
    },
    "passengers": [
      {
        "name": "John Doe",
        "age": 30,
        "seatNumber": "A1-25",
        "status": "CONFIRMED"
      }
    ],
    "totalFare": 2550.00,
    "bookingTime": "2025-05-18T11:15:30Z"
  }
}
```

### API Security

- JWT tokens for authentication
- Rate limiting: 1000 requests per hour per user
- API versioning for backward compatibility
- Input validation and sanitization
- CORS configuration

## System Architecture

### Microservices Architecture

```mermaid
graph TB
    subgraph "Frontend Tier"
        WEBAPP[Web Application]
        MOBILE[Mobile App]
    end
    
    subgraph "API Gateway Tier"
        GATEWAY[API Gateway]
        RATE_LIMITER[Rate Limiter]
        AUTH[Authentication]
    end
    
    subgraph "Service Tier"
        USER_SVC[User Service]
        SEARCH_SVC[Search Service]
        BOOKING_SVC[Booking Service]
        PAYMENT_SVC[Payment Service]
        INVENTORY_SVC[Inventory Service]
        NOTIFICATION_SVC[Notification Service]
    end
    
    subgraph "Data Tier"
        USER_DB[(User DB)]
        BOOKING_DB[(Booking DB)]
        INVENTORY_DB[(Inventory DB)]
        CACHE[(Redis)]
        SEARCH_INDEX[(Elasticsearch)]
    end
    
    subgraph "Message Queue"
        KAFKA[Apache Kafka]
    end
    
    WEBAPP --> GATEWAY
    MOBILE --> GATEWAY
    GATEWAY --> RATE_LIMITER
    RATE_LIMITER --> AUTH
    AUTH --> USER_SVC
    AUTH --> SEARCH_SVC
    AUTH --> BOOKING_SVC
    AUTH --> PAYMENT_SVC
    
    USER_SVC --> USER_DB
    SEARCH_SVC --> CACHE
    SEARCH_SVC --> SEARCH_INDEX
    BOOKING_SVC --> BOOKING_DB
    BOOKING_SVC --> KAFKA
    INVENTORY_SVC --> INVENTORY_DB
    NOTIFICATION_SVC --> KAFKA
```

### Technology Stack

#### Backend
- **Programming Language**: Java 17 / Spring Boot
- **Microservices Framework**: Spring Cloud
- **API Gateway**: Spring Cloud Gateway
- **Service Discovery**: Eureka
- **Configuration Management**: Spring Cloud Config

#### Database
- **Primary Database**: PostgreSQL (for transactional data)
- **Cache**: Redis (for session, search results)
- **Search Engine**: Elasticsearch (for train search)
- **Message Queue**: Apache Kafka

#### DevOps & Infrastructure
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: Jenkins / GitLab CI
- **Monitoring**: Prometheus, Grafana
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)

#### Frontend
- **Web Framework**: React.js / Angular
- **Mobile**: React Native / Flutter
- **State Management**: Redux / MobX

## Data Flow

### Booking Process Flow

```mermaid
flowchart TD
    START([User initiates booking]) --> SEARCH[Search trains]
    SEARCH --> SELECT[Select train and class]
    SELECT --> LOGIN{User logged in?}
    LOGIN -->|No| AUTH[Login/Register]
    LOGIN -->|Yes| PASSENGER[Enter passenger details]
    AUTH --> PASSENGER
    PASSENGER --> VALIDATE[Validate details]
    VALIDATE --> AVAILABLE{Seats available?}
    AVAILABLE -->|No| WAITLIST[Add to waitlist]
    AVAILABLE -->|Yes| RESERVE[Reserve seats]
    RESERVE --> PAYMENT[Process payment]
    PAYMENT --> SUCCESS{Payment successful?}
    SUCCESS -->|No| RELEASE[Release seats]
    SUCCESS -->|Yes| CONFIRM[Confirm booking]
    RELEASE --> FAILURE([Booking failed])
    CONFIRM --> NOTIFY[Send confirmation]
    NOTIFY --> END([Booking completed])
    WAITLIST --> QUEUE[Queue position assigned]
    QUEUE --> WAIT([Wait for confirmation])
```

### Payment Flow

```mermaid
sequenceDiagram
    participant User
    participant BookingService
    participant PaymentService
    participant PaymentGateway
    participant Bank
    
    User->>BookingService: Confirm booking
    BookingService->>PaymentService: Initiate payment
    PaymentService->>PaymentGateway: Create payment session
    PaymentGateway-->>PaymentService: Payment session created
    PaymentService-->>BookingService: Redirect to payment
    BookingService-->>User: Redirect to payment page
    
    User->>PaymentGateway: Enter payment details
    PaymentGateway->>Bank: Process payment
    Bank-->>PaymentGateway: Payment response
    PaymentGateway->>PaymentService: Payment webhook
    PaymentService->>BookingService: Payment status update
    BookingService->>BookingService: Confirm/cancel booking
    BookingService-->>User: Booking confirmation
```

## Security Considerations

### Authentication & Authorization
- JWT-based authentication
- Role-based access control (RBAC)
- Multi-factor authentication for sensitive operations
- OAuth 2.0 integration for social login

### Data Protection
- Encryption at rest (AES-256)
- Encryption in transit (TLS 1.3)
- PII data masking in logs
- GDPR compliance measures

### API Security
- Rate limiting and throttling
- API key management
- Input validation and sanitization
- SQL injection prevention
- XSS protection

### Infrastructure Security
- Network segmentation
- VPC with private subnets
- Web Application Firewall (WAF)
- DDoS protection
- Regular security audits

## Performance & Scalability

### Performance Optimization
- Database indexing strategy
- Query optimization
- Caching layers (Redis, CDN)
- Connection pooling
- Asynchronous proce