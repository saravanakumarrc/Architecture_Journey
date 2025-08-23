# 🌤️ Week 1: Cloud Fundamentals

*Master the foundational concepts of cloud computing and modern infrastructure*

## 📅 Week Overview
**Duration:** Days 1-7  
**Focus Areas:** IaaS, PaaS, SaaS, Virtualization, Containers, Kubernetes, Serverless  
**Time Commitment:** 1-2 hours per day  
**Week Goal:** Understand cloud service models and deployment strategies

---

## 🎯 Day 1: Cloud Service Models (IaaS, PaaS, SaaS)

### 📚 Learning Objectives
- [ ] Define and differentiate IaaS, PaaS, and SaaS
- [ ] Understand the shared responsibility model
- [ ] Identify real-world examples of each service model
- [ ] Analyze trade-offs between service models

### 📖 Core Concepts
- **IaaS (Infrastructure as a Service)**
  - Virtual machines, storage, networking
  - Full control over infrastructure
  - Examples: AWS EC2, Azure VMs, Google Compute Engine
  
- **PaaS (Platform as a Service)**
  - Runtime environment, middleware, development tools
  - Focus on application development
  - Examples: AWS Elastic Beanstalk, Azure App Service, Google App Engine
  
- **SaaS (Software as a Service)**
  - Complete applications delivered over the web
  - No infrastructure management
  - Examples: Salesforce, Office 365, Gmail

### 🛠️ Hands-On Exercises
1. **Service Model Analysis**
   - List 5 applications you use daily
   - Categorize each as IaaS, PaaS, or SaaS
   - Document the reasoning for each classification

2. **Cloud Provider Comparison**
   - Compare AWS, Azure, and GCP service catalogs
   - Identify which services fall into each category
   - Create a comparison matrix

### 📝 Review Questions
- What are the main differences between IaaS and PaaS?
- When would you choose SaaS over building your own solution?
- How does the shared responsibility model work in each service model?

### 🔗 Resources
- [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [Azure Shared Responsibility](https://docs.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility)
- [GCP Security Best Practices](https://cloud.google.com/security/best-practices)

---

## 🎯 Day 2: Virtualization & Hypervisors

### 📚 Learning Objectives
- [ ] Understand virtualization concepts and benefits
- [ ] Compare different hypervisor types (Type 1 vs Type 2)
- [ ] Learn about major hypervisor technologies
- [ ] Understand resource allocation and management

### 📖 Core Concepts
- **Virtualization Types**
  - Full virtualization vs paravirtualization
  - Hardware-assisted virtualization
  - Container-based virtualization
  
- **Hypervisor Technologies**
  - **Type 1 (Bare Metal):** VMware ESXi, Microsoft Hyper-V, KVM
  - **Type 2 (Hosted):** VMware Workstation, VirtualBox, Parallels
  
- **Resource Management**
  - CPU allocation and scheduling
  - Memory management and ballooning
  - Storage thin provisioning

### 🛠️ Hands-On Exercises
1. **Virtual Machine Creation**
   - Install VirtualBox or VMware Player
   - Create a VM with Ubuntu/Debian
   - Configure resource allocation (CPU, RAM, Storage)

2. **Performance Comparison**
   - Run benchmarks on native vs virtualized environment
   - Document performance differences
   - Analyze resource utilization

### 📝 Review Questions
- What are the advantages of Type 1 hypervisors over Type 2?
- How does memory ballooning work in virtualization?
- What is the difference between full and paravirtualization?

### 🔗 Resources
- [VMware Virtualization Guide](https://www.vmware.com/solutions/virtualization.html)
- [KVM Documentation](https://www.linux-kvm.org/page/Main_Page)
- [Hyper-V Overview](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-technology-overview)

---

## 🎯 Day 3: Container Fundamentals (Docker)

### 📚 Learning Objectives
- [ ] Understand container concepts and benefits
- [ ] Learn Docker basics and commands
- [ ] Create and manage containers
- [ ] Understand container lifecycle

### 📖 Core Concepts
- **Container Benefits**
  - Lightweight and portable
  - Consistent runtime environment
  - Fast deployment and scaling
  
- **Docker Components**
  - Images, containers, registries
  - Dockerfile and build process
  - Container networking and storage
  
- **Key Commands**
  - `docker run`, `docker build`, `docker ps`
  - `docker exec`, `docker logs`, `docker stop`

### 🛠️ Hands-On Exercises
1. **Docker Installation & Setup**
   - Install Docker Desktop
   - Verify installation with `docker --version`
   - Run your first container: `docker run hello-world`

2. **Container Management**
   - Pull and run a web server container
   - Create a custom Dockerfile
   - Build and run your own image
   - Practice container lifecycle management

3. **Container Exploration**
   - Inspect running containers
   - View container logs
   - Execute commands inside containers

### 📝 Review Questions
- What is the difference between a Docker image and container?
- How do containers achieve isolation?
- What are the benefits of using containers over VMs?

### 🔗 Resources
- [Docker Official Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Tutorial for Beginners](https://docker-curriculum.com/)

---

## 🎯 Day 4: Kubernetes Introduction

### 📚 Learning Objectives
- [ ] Understand Kubernetes architecture and components
- [ ] Learn basic Kubernetes concepts (pods, services, deployments)
- [ ] Set up a local Kubernetes cluster
- [ ] Deploy and manage simple applications

### 📖 Core Concepts
- **Kubernetes Architecture**
  - Control plane components (API server, etcd, scheduler, controller manager)
  - Worker node components (kubelet, kube-proxy, container runtime)
  
- **Core Resources**
  - **Pods:** Smallest deployable units
  - **Services:** Network abstraction for pods
  - **Deployments:** Declarative updates for applications
  
- **Basic Commands**
  - `kubectl get`, `kubectl describe`, `kubectl apply`
  - `kubectl logs`, `kubectl exec`

### 🛠️ Hands-On Exercises
1. **Local Kubernetes Setup**
   - Install Minikube or Docker Desktop with Kubernetes
   - Verify cluster is running
   - Explore cluster components

2. **First Deployment**
   - Deploy a simple web application
   - Scale the deployment
   - Expose the application via service
   - Access the application

3. **Kubernetes Exploration**
   - Use `kubectl` to explore resources
   - View pod logs and execute commands
   - Understand pod lifecycle

### 📝 Review Questions
- What is the role of the kubelet on worker nodes?
- How do services enable communication between pods?
- What is the difference between a pod and a deployment?

### 🔗 Resources
- [Kubernetes Official Documentation](https://kubernetes.io/docs/)
- [Minikube Getting Started](https://minikube.sigs.k8s.io/docs/start/)
- [Kubernetes Tutorial](https://kubernetes.io/docs/tutorials/)

---

## 🎯 Day 5: Functions as a Service (FaaS)

### 📚 Learning Objectives
- [ ] Understand serverless computing concepts
- [ ] Learn about major FaaS platforms
- [ ] Create and deploy serverless functions
- [ ] Understand FaaS use cases and limitations

### 📖 Core Concepts
- **Serverless Computing**
  - No server management required
  - Pay-per-use pricing model
  - Automatic scaling
  
- **FaaS Platforms**
  - **AWS Lambda:** Event-driven, supports multiple languages
  - **Azure Functions:** Integrated with Azure ecosystem
  - **Google Cloud Functions:** Native GCP integration
  
- **Use Cases**
  - Event processing and automation
  - API endpoints and webhooks
  - Data processing and ETL

### 🛠️ Hands-On Exercises
1. **AWS Lambda Function**
   - Create a simple Lambda function
   - Configure triggers and permissions
   - Test the function
   - Monitor execution metrics

2. **Serverless API**
   - Build a simple REST API using Lambda
   - Configure API Gateway
   - Test API endpoints
   - Add authentication

3. **Event-Driven Architecture**
   - Create Lambda functions triggered by S3 events
   - Process uploaded files
   - Store results in DynamoDB

### 📝 Review Questions
- What are the main benefits of serverless computing?
- When would you choose FaaS over traditional servers?
- What are the limitations of serverless functions?

### 🔗 Resources
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Azure Functions Documentation](https://docs.microsoft.com/en-us/azure/azure-functions/)
- [Google Cloud Functions](https://cloud.google.com/functions/docs)

---

## 🎯 Day 6: VM vs Containers vs Serverless Trade-offs

### 📚 Learning Objectives
- [ ] Compare deployment models across multiple dimensions
- [ ] Understand performance characteristics
- [ ] Analyze cost implications
- [ ] Make informed architectural decisions

### 📖 Core Concepts
- **Comparison Dimensions**
  - **Performance:** Startup time, resource overhead, isolation
  - **Cost:** Resource utilization, billing models, scaling costs
  - **Management:** Operational overhead, monitoring, debugging
  - **Portability:** Environment consistency, deployment complexity
  
- **Decision Framework**
  - Application requirements analysis
  - Team expertise and operational model
  - Business constraints and SLAs

### 🛠️ Hands-On Exercises
1. **Performance Benchmarking**
   - Measure startup times for VMs, containers, and functions
   - Compare resource utilization
   - Document performance characteristics

2. **Cost Analysis**
   - Calculate costs for different deployment models
   - Consider scaling scenarios
   - Factor in operational costs

3. **Architecture Decision Matrix**
   - Create a decision framework
   - Evaluate sample applications
   - Document decision rationale

### 📝 Review Questions
- When would you choose VMs over containers?
- What are the cost implications of serverless vs traditional hosting?
- How do you decide between containers and serverless for a new application?

### 🔗 Resources
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/)
- [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework)

---

## 🎯 Day 7: Weekly Review & Case Study

### 📚 Learning Objectives
- [ ] Consolidate Week 1 learning
- [ ] Apply concepts to real-world scenarios
- [ ] Identify knowledge gaps
- [ ] Plan Week 2 preparation

### 📖 Review Topics
- Cloud service models and their applications
- Virtualization technologies and hypervisors
- Container concepts and Docker usage
- Kubernetes basics and deployment
- Serverless computing and FaaS
- Deployment model trade-offs

### 🛠️ Hands-On Exercises
1. **Case Study: E-commerce Platform**
   - Design a scalable e-commerce architecture
   - Choose appropriate deployment models for different components
   - Justify architectural decisions
   - Document the design

2. **Knowledge Assessment**
   - Complete Week 1 quiz
   - Review key concepts
   - Identify areas for improvement

3. **Week 2 Preparation**
   - Review networking fundamentals
   - Set up networking tools
   - Prepare for OSI model review

### 📝 Review Questions
- Can you explain the difference between IaaS, PaaS, and SaaS to a non-technical person?
- What deployment model would you choose for a microservices application?
- How would you explain container orchestration to a developer?

### 🔗 Resources
- [Week 2 Preview](./../week2-networking/README.md)
- [Cloud Architecture Case Studies](https://aws.amazon.com/solutions/case-studies/)
- [Azure Reference Architectures](https://docs.microsoft.com/en-us/azure/architecture/browse/)

---

## 📊 Week 1 Progress Tracker

### Daily Progress
- [ ] Day 1: Cloud Service Models - ___% Complete
- [ ] Day 2: Virtualization & Hypervisors - ___% Complete
- [ ] Day 3: Container Fundamentals - ___% Complete
- [ ] Day 4: Kubernetes Introduction - ___% Complete
- [ ] Day 5: Functions as a Service - ___% Complete
- [ ] Day 6: Deployment Model Trade-offs - ___% Complete
- [ ] Day 7: Weekly Review - ___% Complete

### Weekly Goals
- [ ] Understand cloud service models
- [ ] Set up development environment
- [ ] Complete hands-on exercises
- [ ] Document learning progress
- [ ] Prepare for Week 2

**Week 1 Progress:** ___/7 days completed

---

## 🎯 Next Steps

**Congratulations on completing Week 1!** 🎉

You've built a solid foundation in cloud fundamentals. Next week, you'll dive into networking concepts that will help you understand how cloud infrastructure communicates and scales.

**Week 2 Focus:** Networking fundamentals, OSI model, routing, and hybrid cloud connectivity.

---

*Ready for Week 2? Continue your journey with [Networking Fundamentals](./../week2-networking/README.md)!*