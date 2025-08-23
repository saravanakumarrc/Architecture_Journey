# 🖥️ Week 3: Compute & Data Center Architecture

*Master compute infrastructure and data center design principles*

## 📅 Week Overview
**Duration:** Days 15-21  
**Focus Areas:** Servers, VMs, Containers, Load Balancing, High Availability  
**Time Commitment:** 1-2 hours per day  
**Week Goal:** Understand compute architecture and data center design

---

## 🎯 Day 15: Physical Servers & Hardware Architecture

### 📚 Learning Objectives
- [ ] Understand server hardware components
- [ ] Learn CPU architecture and NUMA concepts
- [ ] Master DRAM sizing and memory hierarchy
- [ ] Plan server capacity requirements

### 📖 Core Concepts
- **Server Components**
  - CPU sockets and cores
  - Memory channels and DIMMs
  - Storage interfaces (SATA, SAS, NVMe)
  - Network interface cards
  
- **CPU Architecture**
  - NUMA (Non-Uniform Memory Access)
  - Cache hierarchy (L1, L2, L3)
  - Hyper-threading and SMT
  - CPU affinity and pinning
  
- **Memory Management**
  - DRAM types and speeds
  - Memory channels and bandwidth
  - ECC vs non-ECC memory
  - Memory sizing strategies

### 🛠️ Hands-On Exercises
1. **Server Specification Analysis**
   - Analyze server specifications
   - Calculate memory bandwidth
   - Plan CPU and memory ratios

2. **Hardware Benchmarking**
   - Run CPU and memory benchmarks
   - Analyze NUMA performance
   - Document performance characteristics

### 📝 Review Questions
- What is NUMA and why is it important?
- How do you calculate memory bandwidth?
- When would you choose ECC memory?

### 🔗 Resources
- [Server Hardware Guide](https://www.intel.com/content/www/us/en/architecture-and-technology/server-hardware.html)
- [NUMA Architecture](https://www.kernel.org/doc/html/latest/vm/numa.html)
- [Memory Performance](https://www.intel.com/content/www/us/en/architecture-and-technology/memory-storage.html)

---

## 🎯 Day 16: Virtual Machine Architecture & Management

### 📚 Learning Objectives
- [ ] Understand VM provisioning and lifecycle
- [ ] Learn high availability strategies
- [ ] Master VM scaling techniques
- [ ] Implement VM monitoring

### 📖 Core Concepts
- **VM Provisioning**
  - Template-based deployment
  - Customization specifications
  - Resource allocation policies
  - Storage provisioning
  
- **High Availability**
  - VM failover mechanisms
  - Resource reservation
  - Anti-affinity rules
  - Fault tolerance
  
- **Scaling Strategies**
  - Horizontal vs vertical scaling
  - Auto-scaling policies
  - Resource pools
  - DRS (Distributed Resource Scheduler)

### 🛠️ Hands-On Exercises
1. **VM Lifecycle Management**
   - Create VM templates
   - Deploy VMs from templates
   - Configure resource policies
   - Monitor VM performance

2. **High Availability Setup**
   - Configure VM failover
   - Test HA scenarios
   - Monitor HA events
   - Document HA procedures

### 📝 Review Questions
- How does VM failover work?
- What are the benefits of resource pools?
- When would you use anti-affinity rules?

### 🔗 Resources
- [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/)
- [Microsoft Hyper-V](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/)
- [KVM Virtualization](https://www.linux-kvm.org/page/Main_Page)

---

## 🎯 Day 17: Containers vs VMs Deep Dive

### 📚 Learning Objectives
- [ ] Compare containers and VMs in real workloads
- [ ] Understand performance characteristics
- [ ] Learn deployment strategies
- [ ] Analyze resource utilization

### 📖 Core Concepts
- **Performance Comparison**
  - Startup time and resource overhead
  - Memory and CPU utilization
  - Network and storage performance
  - Security isolation levels
  
- **Use Case Analysis**
  - Microservices architecture
  - Legacy application migration
  - Development vs production
  - Hybrid deployment models
  
- **Resource Management**
  - Container resource limits
  - Namespace isolation
  - Cgroup management
  - Resource monitoring

### 🛠️ Hands-On Exercises
1. **Performance Benchmarking**
   - Compare startup times
   - Measure resource usage
   - Analyze performance differences
   - Document findings

2. **Deployment Comparison**
   - Deploy same app in VM and container
   - Compare deployment complexity
   - Analyze operational overhead
   - Document trade-offs

### 📝 Review Questions
- When would you choose VMs over containers?
- How do containers achieve isolation?
- What are the performance implications?

### 🔗 Resources
- [Docker Performance](https://docs.docker.com/desktop/use-desktop/)
- [Container vs VM Comparison](https://www.vmware.com/topics/glossary/content/container-vs-vm.html)
- [Kubernetes Resource Management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)

---

## 🎯 Day 18: Application Virtualization & VDI

### 📚 Learning Objectives
- [ ] Understand VDI concepts and architecture
- [ ] Learn Citrix and other VDI solutions
- [ ] Configure virtual desktop pools
- [ ] Implement VDI management

### 📖 Core Concepts
- **VDI (Virtual Desktop Infrastructure)**
  - Desktop virtualization models
  - User profile management
  - Application delivery
  - Endpoint management
  
- **VDI Solutions**
  - Citrix Virtual Apps and Desktops
  - VMware Horizon
  - Microsoft Remote Desktop Services
  - Cloud VDI (AWS WorkSpaces, Azure Virtual Desktop)
  
- **VDI Architecture**
  - Connection brokers
  - Desktop pools
  - Storage optimization
  - Network requirements

### 🛠️ Hands-On Exercises
1. **VDI Setup**
   - Install VDI solution
   - Configure desktop pools
   - Test user connections
   - Monitor performance

2. **Application Virtualization**
   - Package applications
   - Deploy virtual apps
   - Test application compatibility
   - Document procedures

### 📝 Review Questions
- What are the benefits of VDI?
- How does application virtualization work?
- When would you choose VDI over physical desktops?

### 🔗 Resources
- [Citrix Virtual Apps and Desktops](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/)
- [VMware Horizon](https://docs.vmware.com/en/VMware-Horizon/)
- [AWS WorkSpaces](https://docs.aws.amazon.com/workspaces/)

---

## 🎯 Day 19: Serverless Deep Dive & FaaS Architecture

### 📚 Learning Objectives
- [ ] Understand serverless architecture patterns
- [ ] Learn FaaS implementation strategies
- [ ] Master event-driven design
- [ ] Implement serverless applications

### 📖 Core Concepts
- **Serverless Patterns**
  - Event-driven architecture
  - Microservices with FaaS
  - API composition
  - State management
  
- **FaaS Implementation**
  - Function design principles
  - Event sources and triggers
  - Cold start optimization
  - Monitoring and debugging
  
- **Advanced Concepts**
  - Function composition
  - Orchestration patterns
  - Error handling strategies
  - Cost optimization

### 🛠️ Hands-On Exercises
1. **Serverless Application**
   - Design event-driven architecture
   - Implement multiple functions
   - Configure event triggers
   - Test end-to-end flow

2. **Performance Optimization**
   - Optimize cold start times
   - Implement caching strategies
   - Monitor function performance
   - Analyze cost implications

### 📝 Review Questions
- How do you handle state in serverless?
- What are cold starts and how do you minimize them?
- When is serverless not appropriate?

### 🔗 Resources
- [AWS Serverless Patterns](https://serverlessland.com/patterns)
- [Azure Serverless](https://docs.microsoft.com/en-us/azure/azure-functions/)
- [Serverless Architecture](https://martinfowler.com/articles/serverless.html)

---

## 🎯 Day 20: Load Balancing & Traffic Management

### 📚 Learning Objectives
- [ ] Understand load balancing concepts
- [ ] Learn DNS-based load balancing
- [ ] Master L4 vs L7 load balancing
- [ ] Configure HAProxy and Nginx

### 📖 Core Concepts
- **Load Balancing Types**
  - DNS-based load balancing
  - Layer 4 (Transport) load balancing
  - Layer 7 (Application) load balancing
  - Global load balancing
  
- **Load Balancing Algorithms**
  - Round-robin and weighted round-robin
  - Least connections
  - IP hash and session affinity
  - Health check integration
  
- **Load Balancer Solutions**
  - HAProxy configuration
  - Nginx load balancing
  - Cloud load balancers (ALB, ELB, CLB)
  - Service mesh load balancing

### 🛠️ Hands-On Exercises
1. **Load Balancer Setup**
   - Configure HAProxy
   - Set up Nginx load balancing
   - Test different algorithms
   - Monitor load distribution

2. **Health Check Implementation**
   - Configure health checks
   - Test failover scenarios
   - Monitor backend health
   - Document procedures

### 📝 Review Questions
- What's the difference between L4 and L7 load balancing?
- How do health checks work?
- When would you use session affinity?

### 🔗 Resources
- [HAProxy Documentation](https://www.haproxy.org/download/2.4/doc/intro.txt)
- [Nginx Load Balancing](https://nginx.org/en/docs/http/load_balancing.html)
- [AWS Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/)

---

## 🎯 Day 21: Weekly Review & Compute Architecture Design

### 📚 Learning Objectives
- [ ] Consolidate Week 3 learning
- [ ] Design compute architecture
- [ ] Apply load balancing concepts
- [ ] Plan Week 4 preparation

### 📖 Review Topics
- Server hardware and architecture
- Virtual machine management
- Container vs VM comparison
- Application virtualization
- Serverless architecture
- Load balancing strategies

### 🛠️ Hands-On Exercises
1. **Case Study: High-Traffic Web Application**
   - Design compute architecture
   - Plan load balancing strategy
   - Implement high availability
   - Document design decisions

2. **Performance Testing**
   - Test load balancer performance
   - Measure failover times
   - Analyze resource utilization
   - Document test results

3. **Week 4 Preparation**
   - Review storage concepts
   - Set up storage testing tools
   - Prepare for storage architecture

### 📝 Review Questions
- How would you design a highly available compute infrastructure?
- What load balancing strategy would you choose for a microservices app?
- How do you decide between VMs, containers, and serverless?

### 🔗 Resources
- [Week 4 Preview](./../week4-storage-systems/README.md)
- [Compute Architecture Best Practices](https://aws.amazon.com/architecture/compute/)
- [High Availability Design](https://docs.microsoft.com/en-us/azure/architecture/guide/design-principles/availability)

---

## 📊 Week 3 Progress Tracker

### Daily Progress
- [ ] Day 15: Physical Servers - ___% Complete
- [ ] Day 16: VM Architecture - ___% Complete
- [ ] Day 17: Containers vs VMs - ___% Complete
- [ ] Day 18: Application Virtualization - ___% Complete
- [ ] Day 19: Serverless Deep Dive - ___% Complete
- [ ] Day 20: Load Balancing - ___% Complete
- [ ] Day 21: Weekly Review - ___% Complete

### Weekly Goals
- [ ] Understand compute architecture
- [ ] Master virtualization concepts
- [ ] Implement load balancing
- [ ] Design high availability
- [ ] Prepare for Week 4

**Week 3 Progress:** ___/7 days completed

---

## 🎯 Next Steps

**Congratulations on completing Week 3!** 🎉

You've mastered compute architecture and data center design. Next week, you'll explore storage systems and data management strategies.

**Week 4 Focus:** Storage performance, block/file/object storage, RAID, and storage optimization.

---

*Ready for Week 4? Continue your journey with [Storage Systems](./../week4-storage-systems/README.md)!*