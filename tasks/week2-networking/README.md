# 🌐 Week 2: Networking Fundamentals

*Master networking concepts essential for cloud architecture*

## 📅 Week Overview
**Duration:** Days 8-14  
**Focus Areas:** OSI Model, IP Addressing, Routing, BGP, VPNs, SD-WAN, CDNs  
**Time Commitment:** 1-2 hours per day  
**Week Goal:** Understand network architecture and hybrid cloud connectivity

---

## 🎯 Day 8: OSI Model & IP Addressing

### 📚 Learning Objectives
- [ ] Understand the 7-layer OSI model
- [ ] Master IP addressing and subnetting
- [ ] Learn CIDR notation and subnet calculations
- [ ] Practice IP address planning

### 📖 Core Concepts
- **OSI Model Layers**
  - Physical, Data Link, Network, Transport
  - Session, Presentation, Application
  
- **IP Addressing**
  - IPv4 vs IPv6
  - Public vs Private IP ranges
  - Subnet masks and CIDR notation
  
- **Subnetting**
  - Binary to decimal conversion
  - Subnet calculations
  - VLSM (Variable Length Subnet Masking)

### 🛠️ Hands-On Exercises
1. **Subnet Calculator Practice**
   - Calculate subnets for different network sizes
   - Practice CIDR notation
   - Design IP addressing scheme for a company

2. **Network Planning Exercise**
   - Design network for 1000 hosts
   - Plan subnets for different departments
   - Document IP allocation strategy

### 📝 Review Questions
- What happens at each OSI layer?
- How do you calculate the number of hosts in a subnet?
- What is the difference between /24 and /16 networks?

### 🔗 Resources
- [OSI Model Explained](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)
- [IP Subnetting Tutorial](https://www.9tut.com/subnetting-tutorial)
- [CIDR Calculator](https://cidr.xyz/)

---

## 🎯 Day 9: Switches, VLANs & Routing Basics

### 📚 Learning Objectives
- [ ] Understand switching concepts and VLANs
- [ ] Learn routing fundamentals
- [ ] Configure basic network segmentation
- [ ] Understand broadcast domains

### 📖 Core Concepts
- **Switching**
  - MAC address learning
  - Frame forwarding
  - Switch types (Layer 2 vs Layer 3)
  
- **VLANs**
  - Network segmentation
  - VLAN trunking (802.1Q)
  - Inter-VLAN routing
  
- **Routing Basics**
  - Static vs Dynamic routing
  - Routing tables
  - Next-hop determination

### 🛠️ Hands-On Exercises
1. **VLAN Configuration**
   - Set up VLANs on a switch
   - Configure trunk ports
   - Test VLAN isolation

2. **Basic Routing**
   - Configure static routes
   - Test connectivity between networks
   - Analyze routing tables

### 📝 Review Questions
- How do switches learn MAC addresses?
- What is the purpose of VLANs?
- When would you use static vs dynamic routing?

### 🔗 Resources
- [VLAN Configuration Guide](https://www.cisco.com/c/en/us/support/docs/lan-switching/8021q/17056-741-4.html)
- [Routing Fundamentals](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)

---

## 🎯 Day 10: NAT, Packet Forwarding & Security

### 📚 Learning Objectives
- [ ] Understand NAT concepts and types
- [ ] Learn packet forwarding mechanisms
- [ ] Configure firewalls and security
- [ ] Implement proxy solutions

### 📖 Core Concepts
- **NAT (Network Address Translation)**
  - Static NAT, Dynamic NAT, PAT
  - NAT traversal challenges
  - Cloud NAT considerations
  
- **Packet Forwarding**
  - Routing decisions
  - Packet encapsulation
  - MTU considerations
  
- **Network Security**
  - Firewall types and configurations
  - Proxy servers
  - Intrusion detection/prevention

### 🛠️ Hands-On Exercises
1. **NAT Configuration**
   - Set up NAT on router/firewall
   - Test connectivity
   - Troubleshoot common issues

2. **Firewall Rules**
   - Configure access control lists
   - Test rule effectiveness
   - Monitor traffic logs

### 📝 Review Questions
- What are the different types of NAT?
- How does packet forwarding work?
- What security measures protect network traffic?

### 🔗 Resources
- [NAT Configuration Guide](https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/13772-12.html)
- [Firewall Best Practices](https://www.cisco.com/c/en/us/support/docs/security/firepower-ngfw/118504-configure-fw-00.html)

---

## 🎯 Day 11: BGP Fundamentals & Hybrid Cloud

### 📚 Learning Objectives
- [ ] Understand BGP routing protocol
- [ ] Learn hybrid cloud networking
- [ ] Configure BGP peering
- [ ] Implement route optimization

### 📖 Core Concepts
- **BGP (Border Gateway Protocol)**
  - Path vector routing
  - BGP attributes and path selection
  - ASN (Autonomous System Numbers)
  
- **Hybrid Cloud Routing**
  - On-premises to cloud connectivity
  - Route advertisement
  - Traffic engineering
  
- **Cloud Connectivity**
  - AWS Direct Connect
  - Azure ExpressRoute
  - Google Cloud Interconnect

### 🛠️ Hands-On Exercises
1. **BGP Configuration**
   - Set up BGP peering
   - Configure route advertisements
   - Test failover scenarios

2. **Hybrid Cloud Setup**
   - Configure cloud connectivity
   - Test cross-premises routing
   - Monitor connection health

### 📝 Review Questions
- How does BGP select the best path?
- What are the benefits of hybrid cloud?
- How do you troubleshoot BGP issues?

### 🔗 Resources
- [BGP Configuration Guide](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13762-40.html)
- [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/)
- [Azure ExpressRoute](https://docs.microsoft.com/en-us/azure/expressroute/)

---

## 🎯 Day 12: VPNs & Private Connectivity

### 📚 Learning Objectives
- [ ] Understand VPN technologies
- [ ] Learn private line connectivity
- [ ] Configure site-to-site VPNs
- [ ] Implement client VPNs

### 📖 Core Concepts
- **VPN Types**
  - Site-to-Site VPNs
  - Client VPNs
  - SSL/TLS VPNs
  
- **Private Connectivity**
  - MPLS networks
  - Dark fiber
  - Carrier Ethernet
  
- **Cloud VPN Services**
  - AWS VPN Gateway
  - Azure VPN Gateway
  - Google Cloud VPN

### 🛠️ Hands-On Exercises
1. **VPN Configuration**
   - Set up site-to-site VPN
   - Configure client VPN
   - Test connectivity and performance

2. **Private Line Setup**
   - Configure cloud private connectivity
   - Test bandwidth and latency
   - Monitor connection metrics

### 📝 Review Questions
- What are the advantages of VPNs?
- When would you choose private lines over VPNs?
- How do you secure VPN connections?

### 🔗 Resources
- [VPN Configuration Guide](https://www.cisco.com/c/en/us/support/docs/security-vpn/ipsec-negotiation-ike-protocols/14106-dynamic-crypto-maps.html)
- [AWS VPN](https://docs.aws.amazon.com/vpn/)
- [Azure VPN](https://docs.microsoft.com/en-us/azure/vpn-gateway/)

---

## 🎯 Day 13: SD-WAN & Content Delivery Networks

### 📚 Learning Objectives
- [ ] Understand SD-WAN concepts
- [ ] Learn CDN architecture
- [ ] Configure SD-WAN policies
- [ ] Implement CDN optimization

### 📖 Core Concepts
- **SD-WAN (Software-Defined WAN)**
  - Centralized management
  - Application-aware routing
  - Bandwidth optimization
  
- **CDNs (Content Delivery Networks)**
  - Edge server placement
  - Caching strategies
  - Load balancing
  
- **Cloud CDN Services**
  - AWS CloudFront
  - Azure CDN
  - Google Cloud CDN

### 🛠️ Hands-On Exercises
1. **SD-WAN Configuration**
   - Set up SD-WAN policies
   - Configure traffic steering
   - Test failover scenarios

2. **CDN Implementation**
   - Configure CDN distribution
   - Test caching behavior
   - Monitor performance metrics

### 📝 Review Questions
- What are the benefits of SD-WAN?
- How do CDNs improve performance?
- When would you use SD-WAN vs traditional WAN?

### 🔗 Resources
- [SD-WAN Overview](https://www.cisco.com/c/en/us/solutions/enterprise-networks/sd-wan/what-is-sd-wan.html)
- [AWS CloudFront](https://docs.aws.amazon.com/cloudfront/)
- [Azure CDN](https://docs.microsoft.com/en-us/azure/cdn/)

---

## 🎯 Day 14: Weekly Review & Hybrid Network Design

### 📚 Learning Objectives
- [ ] Consolidate Week 2 learning
- [ ] Design hybrid cloud network
- [ ] Apply networking concepts
- [ ] Plan Week 3 preparation

### 📖 Review Topics
- OSI model and network layers
- IP addressing and subnetting
- Routing protocols and BGP
- VPNs and private connectivity
- SD-WAN and CDN concepts

### 🛠️ Hands-On Exercises
1. **Case Study: Multi-Region E-commerce**
   - Design network architecture
   - Plan connectivity between regions
   - Implement security measures
   - Document design decisions

2. **Network Troubleshooting**
   - Practice common network issues
   - Use diagnostic tools
   - Document troubleshooting steps

3. **Week 3 Preparation**
   - Review compute concepts
   - Set up virtualization tools
   - Prepare for server architecture

### 📝 Review Questions
- Can you explain the OSI model to a developer?
- How would you design a hybrid cloud network?
- What networking challenges arise in multi-cloud?

### 🔗 Resources
- [Week 3 Preview](./../week3-compute-architecture/README.md)
- [Network Design Best Practices](https://www.cisco.com/c/en/us/solutions/enterprise-networks/enterprise-network-design-guide.html)

---

## 📊 Week 2 Progress Tracker

### Daily Progress
- [ ] Day 8: OSI Model & IP Addressing - ___% Complete
- [ ] Day 9: Switches, VLANs & Routing - ___% Complete
- [ ] Day 10: NAT & Security - ___% Complete
- [ ] Day 11: BGP & Hybrid Cloud - ___% Complete
- [ ] Day 12: VPNs & Private Lines - ___% Complete
- [ ] Day 13: SD-WAN & CDNs - ___% Complete
- [ ] Day 14: Weekly Review - ___% Complete

### Weekly Goals
- [ ] Master networking fundamentals
- [ ] Understand hybrid cloud connectivity
- [ ] Complete hands-on exercises
- [ ] Design network architecture
- [ ] Prepare for Week 3

**Week 2 Progress:** ___/7 days completed

---

## 🎯 Next Steps

**Congratulations on completing Week 2!** 🎉

You've mastered essential networking concepts. Next week, you'll explore compute architecture and data center design principles.

**Week 3 Focus:** Servers, virtualization, containers, load balancing, and high availability.

---

*Ready for Week 3? Continue your journey with [Compute Architecture](./../week3-compute-architecture/README.md)!*