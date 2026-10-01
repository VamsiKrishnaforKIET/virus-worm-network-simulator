import networkx as nx


class NetworkModel:
    def __init__(self):
        self.graph = nx.Graph()

    def add_computer(self, computer_id):
        """Add a computer to the network."""
        self.graph.add_node(
            computer_id,
            infected=False,
            protected=False
        )

    def connect_computers(self, computer1, computer2):
        """Create a network connection between two computers."""
        if computer1 in self.graph and computer2 in self.graph:
            self.graph.add_edge(computer1, computer2)

    def infect_computer(self, computer_id):
        """Mark a computer as infected."""
        if computer_id in self.graph:
            self.graph.nodes[computer_id]["infected"] = True

    def protect_computer(self, computer_id):
        """Mark a computer as protected."""
        if computer_id in self.graph:
            self.graph.nodes[computer_id]["protected"] = True

    def get_neighbors(self, computer_id):
        """Return computers directly connected to a computer."""
        if computer_id in self.graph:
            return list(self.graph.neighbors(computer_id))
        return []

    def get_infected_computers(self):
        """Return all currently infected computers."""
        return [
            node
            for node, data in self.graph.nodes(data=True)
            if data["infected"]
        ]

    def display_network(self):
        """Display basic network information."""
        print("\nNetwork Information")
        print("-------------------")

        print("Computers:", list(self.graph.nodes()))
        print("Connections:", list(self.graph.edges()))

        print("Infected:",
              self.get_infected_computers())


if __name__ == "__main__":

    network = NetworkModel()

    # Add computers
    for computer in ["PC1", "PC2", "PC3", "PC4", "PC5"]:
        network.add_computer(computer)

    # Create network connections
    network.connect_computers("PC1", "PC2")
    network.connect_computers("PC1", "PC3")
    network.connect_computers("PC2", "PC4")
    network.connect_computers("PC3", "PC5")

    # Infect initial computer
    network.infect_computer("PC1")

    network.display_network()