# 🌐CascadeAI - An AI Network Failure Simulator

🚀 An interactive **Generative AI-powered simulator** that models cascading failures in complex networks such as **power grids, computer networks, and transportation systems**.

The system visualizes how failures propagate through interconnected nodes and provides **AI-generated explanations and prevention strategies** to improve network resilience.

---

# 🎥 Live Demo

The application is deployed as an interactive web application using **Gradio**.
Users can simulate different network conditions and observe **cascade failures in real time**.
Try the deployed AI Network Failure Simulator here:
https://aditiraj2903-ai-network-failure-simulator.hf.space

---

# ✨ Key Features

🔹 Interactive network simulation  
🔹 AI-generated failure scenarios  
🔹 Cascade failure propagation visualization  
🔹 Critical node detection using graph analysis  
🔹 Network damage assessment  
🔹 AI-generated explanations of network collapse  
🔹 Prevention strategies for improving network resilience  

---

# 🛠 Technologies Used

### 👨‍💻 Programming Language
- Python

### 📚 Libraries
- NetworkX (network modeling)
- Matplotlib (graph visualization)
- Gradio (interactive web interface)

### 🌍 Platforms
- GitHub for version control
- Hugging Face Spaces for deployment

---

# ⚙ System Workflow

1️⃣ User selects network parameters  
2️⃣ Network graph is generated  
3️⃣ Initial node failure is triggered  
4️⃣ Cascade failure spreads through the network  
5️⃣ Failed nodes are visualized in the network graph  
6️⃣ AI generates scenario explanation and prevention recommendations  

---

# 🧠 Project Architecture
User Input
│
▼
Network Graph Generation (NetworkX)
│
▼
Cascade Failure Simulation
│
▼
Graph Visualization (Matplotlib)
│
▼
AI Scenario + Analysis Generation
│
▼
Interactive Interface (Gradio)


---

# 🔬 How the Simulation Works

The simulator models a network as a **graph structure** where:

🔹 **Nodes** represent infrastructure units (servers, substations, transport hubs)  
🔹 **Edges** represent connections between them  

When one node fails, the system simulates **cascading failures** by probabilistically spreading the failure across connected nodes.

The algorithm also calculates **betweenness centrality** to determine the **most critical node in the network**.

---

# 📊 Example Simulation Output

**Initial Failed Node:** Node 7  

**Failure Propagation Path:**  
7 → 9 → 13 → 15  

**Critical Node:** Node 10  

**Network Damage:** 28%

The system also generates an **AI explanation describing why the cascade occurred and how it can be prevented**.

---


---

# 🚀 Future Improvements

Possible enhancements for the project include:

🔹 Integration of **Graph Neural Networks (GNN)** for failure prediction  
🔹 Real-time streaming simulation of cascade propagation  
🔹 Interactive network visualization using advanced graph libraries  
🔹 Integration with real infrastructure datasets  
🔹 AI-based anomaly detection for early failure warnings  

---

## 🌐 Deployment

The application is deployed using Hugging Face Spaces.

Framework: Gradio  
Hosting Platform: Hugging Face Spaces  

Live Application:
https://aditiraj2903-ai-network-failure-simulator.hf.space


# 🌍 Real-World Applications

This project can be applied to multiple domains:

⚡ Power grid failure analysis  
🌐 Internet and communication network resilience  
🚆 Transportation network planning  
🏗 Infrastructure risk assessment  
🔐 Cybersecurity impact simulation  

---

# 👩‍💻 Author

**Aditi Raj**  


---

# 📜 License

This project is open-source and available under the **MIT License**.
