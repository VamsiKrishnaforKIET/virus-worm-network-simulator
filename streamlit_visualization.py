import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Network Spread Visualization",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Network Virus & Worm Visualization")

st.write(
    "Visual representation of virus and worm spread "
    "in a simulated computer network."
)


def create_network():
    network = nx.Graph()

    computers = [
        "PC1",
        "PC2",
        "PC3",
        "PC4",
        "PC5"
    ]

    for computer in computers:
        network.add_node(
            computer,
            infected=False,
            protected=False
        )

    network.add_edge("PC1", "PC2")
    network.add_edge("PC1", "PC3")
    network.add_edge("PC2", "PC4")
    network.add_edge("PC3", "PC5")

    return network


network = create_network()

st.sidebar.header("Simulation Stage")

stage = st.sidebar.slider(
    "Select Spread Stage",
    min_value=0,
    max_value=4,
    value=0
)


infection_stages = {
    0: [],
    1: ["PC1"],
    2: ["PC1", "PC2", "PC3"],
    3: ["PC1", "PC2", "PC3", "PC4"],
    4: ["PC1", "PC2", "PC3", "PC4"]
}


infected = infection_stages[stage]

for computer in infected:
    network.nodes[computer]["infected"] = True


network.nodes["PC5"]["protected"] = True


st.subheader(
    f"Network Spread - Stage {stage}"
)


fig, ax = plt.subplots()

pos = nx.spring_layout(
    network,
    seed=42
)


node_colors = []

for computer in network.nodes:
    if network.nodes[computer]["infected"]:
        node_colors.append("red")
    elif network.nodes[computer]["protected"]:
        node_colors.append("green")
    else:
        node_colors.append("skyblue")


node_sizes = []

for computer in network.nodes:
    node_sizes.append(1800)


nx.draw(
    network,
    pos,
    ax=ax,
    with_labels=True,
    node_color=node_colors,
    node_size=node_sizes,
    font_size=10
)


st.pyplot(fig)

plt.close(fig)


st.subheader("Computer Status")


for computer in network.nodes:
    if network.nodes[computer].get("infected", False):
        st.error(
            f"{computer} - INFECTED"
        )
    elif network.nodes[computer].get("protected", False):
        st.success(
            f"{computer} - PROTECTED"
        )
    else:
        st.info(
            f"{computer} - SAFE"
        )


st.subheader("Defense Tips")


if stage == 0:
    st.write(
        "• Keep security software updated."
    )
elif stage == 1:
    st.write(
        "• Isolate the infected computer."
    )
elif stage == 2:
    st.write(
        "• Avoid opening unknown files."
    )
elif stage == 3:
    st.write(
        "• Use network segmentation and access controls."
    )
else:
    st.write(
        "• Scan infected systems and remove the infection."
    )