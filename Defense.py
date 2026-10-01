import networkx as nx


class DefenseSystem:
    def __init__(self, network):
        self.network = network

    def protect_computer(self, computer_id):
        """Protect a computer from the simulated virus/worm."""

        if computer_id not in self.network:
            print(
                f"Computer {computer_id} does not exist."
            )
            return False

        self.network.nodes[
            computer_id
        ]["protected"] = True

        print(
            f"{computer_id} is now protected."
        )

        return True

    def remove_infection(self, computer_id):
        """Remove simulated infection from a computer."""

        if computer_id not in self.network:
            print(
                f"Computer {computer_id} does not exist."
            )
            return False

        self.network.nodes[
            computer_id
        ]["infected"] = False

        print(
            f"Infection removed from {computer_id}."
        )

        return True

    def check_computer(self, computer_id):
        """Check the security status of a computer."""

        if computer_id not in self.network:
            print(
                f"Computer {computer_id} does not exist."
            )
            return False

        infected = self.network.nodes[
            computer_id
        ].get("infected", False)

        protected = self.network.nodes[
            computer_id
        ].get("protected", False)

        print(f"\nSecurity Status: {computer_id}")
        print("----------------------------")
        print("Protected:", protected)
        print("Infected:", infected)

        return True

    def scan_network(self):
        """Scan all computers for simulated infections."""

        print("\nNetwork Security Scan")
        print("---------------------")

        for computer in self.network.nodes:

            infected = self.network.nodes[
                computer
            ].get("infected", False)

            protected = self.network.nodes[
                computer
            ].get("protected", False)

            if infected:
                status = "INFECTED"
            elif protected:
                status = "PROTECTED"
            else:
                status = "SAFE"

            print(
                f"{computer}: {status}"
            )

    def display_defense_status(self):
        """Display protected and infected computers."""

        print("\nDefense Status")
        print("--------------")

        protected_computers = []
        infected_computers = []

        for computer in self.network.nodes:

            if self.network.nodes[
                computer
            ].get("protected", False):
                protected_computers.append(computer)

            if self.network.nodes[
                computer
            ].get("infected", False):
                infected_computers.append(computer)

        print(
            "Protected computers:",
            protected_computers
        )

        print(
            "Infected computers:",
            infected_computers
        )


if __name__ == "__main__":

    # Create NetworkX network
    network = nx.Graph()

    # Add computers
    for computer in [
        "PC1",
        "PC2",
        "PC3",
        "PC4",
        "PC5"
    ]:
        network.add_node(
            computer,
            infected=False,
            protected=False
        )

    # Create network connections
    network.add_edge("PC1", "PC2")
    network.add_edge("PC1", "PC3")
    network.add_edge("PC2", "PC4")
    network.add_edge("PC3", "PC5")

    # Create defense system
    defense = DefenseSystem(network)

    # Protect computers
    defense.protect_computer("PC4")
    defense.protect_computer("PC5")

    # Simulate infection on PC1
    network.nodes[
        "PC1"
    ]["infected"] = True

    # Scan network
    defense.scan_network()

    # Check individual computer
    defense.check_computer("PC1")
    defense.check_computer("PC5")

    # Remove infection
    defense.remove_infection("PC1")

    # Display final defense status
    defense.display_defense_status()
