import networkx as nx

from virus_simulator import VirusSimulator
from worm_simulator import WormSimulator


class DefenseSystem:
    def __init__(self, network):
        self.network = network

    def protect_computer(self, computer_id):
        if computer_id not in self.network:
            print(f"Computer {computer_id} does not exist.")
            return False

        self.network.nodes[computer_id]["protected"] = True
        print(f"{computer_id} is now protected.")
        return True

    def remove_infection(self, computer_id):
        if computer_id not in self.network:
            print(f"Computer {computer_id} does not exist.")
            return False

        self.network.nodes[computer_id]["infected"] = False
        print(f"Infection removed from {computer_id}.")
        return True

    def scan_network(self):
        print("\nNetwork Security Scan")
        print("---------------------")

        for computer in self.network.nodes:
            infected = self.network.nodes[computer].get(
                "infected", False
            )

            protected = self.network.nodes[computer].get(
                "protected", False
            )

            if infected:
                status = "INFECTED"
            elif protected:
                status = "PROTECTED"
            else:
                status = "SAFE"

            print(f"{computer}: {status}")


def create_network():
    """Create the simulated computer network."""

    network = nx.Graph()

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

    network.add_edge("PC1", "PC2")
    network.add_edge("PC1", "PC3")
    network.add_edge("PC2", "PC4")
    network.add_edge("PC3", "PC5")

    return network


def main():

    print("\n====================================")
    print(" VIRUS & WORM NETWORK SIMULATOR")
    print("====================================")

    # Create network
    network = create_network()

    print("\nNetwork Information")
    print("-------------------")
    print("Computers:", list(network.nodes))
    print("Connections:", list(network.edges))

    # ==================================
    # VIRUS SIMULATION
    # ==================================

    print("\n====================================")
    print(" VIRUS SIMULATION")
    print("====================================")

    virus = VirusSimulator(network)

    virus.add_file("PC1", "document.txt")
    virus.add_file("PC2", "report.pdf")
    virus.add_file("PC3", "image.jpg")

    virus.infect_file(
        "PC1",
        "document.txt"
    )

    virus.spread_through_file_sharing(
        "PC1",
        "PC2",
        "document.txt"
    )

    virus.display_status()

    # ==================================
    # WORM SIMULATION
    # ==================================

    print("\n====================================")
    print(" WORM SIMULATION")
    print("====================================")

    worm_network = create_network()

    # Protect PC5
    worm_network.nodes["PC5"]["protected"] = True

    worm = WormSimulator(worm_network)

    worm.infect_computer("PC1")

    worm.run_simulation(
        steps=5
    )

    worm.display_status()

    # ==================================
    # DEFENSE SYSTEM
    # ==================================

    print("\n====================================")
    print(" DEFENSE SYSTEM")
    print("====================================")

    defense = DefenseSystem(worm_network)

    defense.protect_computer("PC4")
    defense.protect_computer("PC5")

    defense.scan_network()

    print("\n====================================")
    print(" SIMULATION COMPLETED")
    print("====================================")


if __name__ == "__main__":
    main()