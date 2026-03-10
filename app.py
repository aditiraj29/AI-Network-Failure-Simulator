import networkx as nx
import matplotlib.pyplot as plt
import random
import gradio as gr


# -----------------------------
# AI Scenario Generator
# -----------------------------
def generate_failure_scenario(network_type):

    scenarios = {
        "Power Grid": [
            "A transformer overload at a central power station caused cascading outages.",
            "Lightning damaged a major substation leading to overload in nearby stations.",
            "Unexpected electricity demand forced generators offline."
        ],

        "Computer Network": [
            "A router firmware crash caused packet loss across multiple servers.",
            "A distributed cyber attack overloaded a gateway router.",
            "A data center switch failure disconnected several nodes."
        ],

        "Transport Network": [
            "Closure of a major highway junction overloaded nearby roads.",
            "Railway signaling failure created cascading train delays.",
            "Airport control system outage disrupted connecting flights."
        ]
    }

    return random.choice(scenarios[network_type])


# -----------------------------
# AI Explanation Generator
# -----------------------------
def generate_ai_explanation(scenario, damage):

    explanation = f"""
### AI Network Analysis

The simulation indicates that the network experienced cascading failures triggered by the following event:

**{scenario}**

### Impact Assessment
Approximately **{damage:.2f}% of the network infrastructure** was affected during this cascade event.

### Recommended Prevention Strategies

• Introduce redundancy in critical nodes  
• Implement load balancing across network connections  
• Deploy anomaly detection systems to identify overload risks  
• Strengthen protection for key infrastructure components  

These strategies improve the resilience of complex networked systems.
"""

    return explanation


# -----------------------------
# Network Simulation
# -----------------------------
def simulate_network(num_nodes, risk, network_type):

    scenario = generate_failure_scenario(network_type)

    if risk == "Low":
        failure_probability = 0.1
    elif risk == "Medium":
        failure_probability = 0.3
    else:
        failure_probability = 0.5

    G = nx.erdos_renyi_graph(num_nodes, 0.2)

    failed_nodes = set()
    initial_node = random.choice(list(G.nodes()))
    failed_nodes.add(initial_node)

    propagation_steps = []

    for node in G.nodes():
        if random.random() < failure_probability:
            failed_nodes.add(node)
            propagation_steps.append(node)

    # Node colors
    colors = []

    for node in G.nodes():
        if node in failed_nodes:
            colors.append("red")
        else:
            colors.append("green")

    # Find critical node
    centrality = nx.betweenness_centrality(G)
    critical_node = max(centrality, key=centrality.get)

    damage = (len(failed_nodes) / num_nodes) * 100

    # Draw graph
    fig, ax = plt.subplots(figsize=(6,6))
    nx.draw(G, node_color=colors, with_labels=True, ax=ax)

    propagation_text = " ➜ ".join(map(str, propagation_steps))

    results = f"""
### Simulation Results

**Initial Failed Node:** Node {initial_node}

**Failure Propagation Path:**  
{propagation_text}

**Critical Node:** Node {critical_node}

**Total Failed Nodes:** {len(failed_nodes)} / {num_nodes}

**Network Damage:** {damage:.2f}%
"""

    explanation = generate_ai_explanation(scenario, damage)

    return fig, results, explanation


# -----------------------------
# Gradio Interface
# -----------------------------
interface = gr.Interface(

    fn=simulate_network,

    inputs=[
        gr.Slider(10, 50, value=20, label="Number of Nodes"),
        gr.Radio(["Low", "Medium", "High"], label="Risk Level"),
        gr.Dropdown(
            ["Power Grid", "Computer Network", "Transport Network"],
            label="Network Type"
        )
    ],

    outputs=[
        gr.Plot(label="Network Failure Visualization"),
        gr.Markdown(label="Simulation Results"),
        gr.Markdown(label="AI Network Analysis")
    ],

    title="AI Network Failure Simulator",

    description="""
Interactive simulator that models cascading failures in complex networks.

🔴 Red nodes = Failed nodes  
🟢 Green nodes = Active nodes

The system generates AI-based explanations and prevention strategies for network failures.
"""
)


interface.launch()