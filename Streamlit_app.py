import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt


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


def display_network(network):
    figure, axis = plt.subplots()

    positions = nx.spring_layout(
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

    nx.draw(
        network,
        positions,
        ax=axis,
        with_labels=True,
        node_color=node_colors,
        node_size=2000,
        font_size=10
    )

    st.pyplot(figure)
    plt.close(figure)


def virus_simulation(network):
    st.header("Virus Simulation")

    st.write(
        "Virus simulation demonstrates how a virus "
        "can attach to a simulated file."
    )

    if "virus_infected" not in st.session_state:
        st.session_state.virus_infected = []

    if st.button("Infect PC1 File"):
        if "PC1" not in st.session_state.virus_infected:
            st.session_state.virus_infected.append("PC1")
            network.nodes["PC1"]["infected"] = True

            st.success(
                "Virus attached to document.txt on PC1."
            )
        else:
            st.info(
                "PC1 file is already infected."
            )

    if st.button("Spread Virus to PC2"):
        if "PC1" in st.session_state.virus_infected:
            if "PC2" not in st.session_state.virus_infected:
                st.session_state.virus_infected.append("PC2")
                network.nodes["PC2"]["infected"] = True

                st.warning(
                    "Virus spread from PC1 to PC2."
                )
            else:
                st.info(
                    "PC2 is already infected."
                )
        else:
            st.error(
                "First infect the file on PC1."
            )

    st.write(
        "Infected computers:",
        st.session_state.virus_infected
    )


def worm_simulation(network):
    st.header("Worm Simulation")

    st.write(
        "Worm simulation demonstrates autonomous "
        "spread between connected computers."
    )

    network.nodes["PC5"]["protected"] = True

    if "worm_infected" not in st.session_state:
        st.session_state.worm_infected = ["PC1"]
        network.nodes["PC1"]["infected"] = True

    if st.button("Run Worm Step"):
        current_infected = list(
            st.session_state.worm_infected
        )

        new_infections = []

        for computer in current_infected:
            for neighbor in network.neighbors(computer):
                if neighbor in st.session_state.worm_infected:
                    continue

                if network.nodes[neighbor]["protected"]:
                    continue

                if neighbor not in new_infections:
                    new_infections.append(neighbor)

        for computer in new_infections:
            if computer not in st.session_state.worm_infected:
                st.session_state.worm_infected.append(
                    computer
                )

                network.nodes[
                    computer
                ]["infected"] = True

        if new_infections:
            st.success(
                "Newly infected: "
                + str(new_infections)
            )
        else:
            st.info(
                "No new computers were infected."
            )

    st.write(
        "Infected computers:",
        st.session_state.worm_infected
    )


def defense_simulation(network):
    st.header("Network Defense")

    if st.button("Protect PC4 and PC5"):
        network.nodes["PC4"]["protected"] = True
        network.nodes["PC5"]["protected"] = True

        st.success(
            "PC4 and PC5 are now protected."
        )

    if st.button("Scan Network"):
        st.subheader("Security Status")

        for computer in network.nodes:
            infected = network.nodes[
                computer
            ]["infected"]

            protected = network.nodes[
                computer
            ]["protected"]

            if infected:
                status = "INFECTED"
            elif protected:
                status = "PROTECTED"
            else:
                status = "SAFE"

            st.write(
                computer + " : " + status
            )


def main():
    st.set_page_config(
        page_title="Virus and Worm Network Simulator",
        layout="wide"
    )

    st.title(
        "Virus and Worm Network Spread Simulator"
    )

    st.write(
        "Educational simulation of virus and worm "
        "spread through a computer network."
    )

    network = create_network()

    st.sidebar.header("Simulation Control")

    simulation_type = st.sidebar.selectbox(
        "Select Simulation",
        [
            "Network",
            "Virus Simulation",
            "Worm Simulation",
            "Defense Scan"
        ]
    )

    if simulation_type == "Network":
        st.header("Computer Network")

        display_network(network)

        st.write(
            "Computers: PC1, PC2, PC3, PC4, PC5"
        )

        st.write(
            "Connections: PC1-PC2, PC1-PC3, "
            "PC2-PC4, PC3-PC5"
        )

    elif simulation_type == "Virus Simulation":
        virus_simulation(network)
        display_network(network)

    elif simulation_type == "Worm Simulation":
        worm_simulation(network)
        display_network(network)

    elif simulation_type == "Defense Scan":
        defense_simulation(network)
        display_network(network)

    st.header("Defense Tips")

    st.write(
        "1. Keep systems and security software updated."
    )

    st.write(
        "2. Avoid opening unknown or suspicious files."
    )

    st.write(
        "3. Isolate infected computers from the network."
    )

    st.write(
        "4. Use network protection and access controls."
    )

    st.write(
        "5. Regularly scan computers for infections."
    )


if __name__ == "__main__":
    main()