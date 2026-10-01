import networkx as nx

from virus_simulator import VirusSimulator
from worm_simulator import WormSimulator


class NetworkSimulator:
    def __init__(self):
        # Create NetworkX network
        self.network = nx.Graph()

        # Create computers
        for computer in [
            "PC1",
            "PC2",
            "PC3",
            "PC4",
            "PC5"
        ]:
            self.network.add_node(
                computer,
                infected=False,
                protected=False
            )

        # Create network connections
        self.network.add_edge("PC1", "PC2")
        self.network.add_edge("PC1", "PC3")
        self.network.add_edge("PC2", "PC4")
        self.network.add_edge("PC3", "PC5")

        # Protect PC5
        self.network.nodes["PC5"]["protected"] = True

        # Create virus simulator
        self.virus = VirusSimulator(self.network)

        # Create worm simulator
        self.worm = WormSimulator(self.network)

    def setup_files(self):
        """Add simulated files to computers."""

        self.virus.add_file(
            "PC1",
            "document.txt"
        )

        self.virus.add_file(
            "PC2",
            "report.pdf"
        )

        self.virus.add_file(
            "PC3",
            "image.jpg"
        )

        self.virus.add_file(
            "PC4",
            "data.txt"
        )

        self.virus.add_file(
            "PC5",
            "backup.zip"
        )

    def run_virus_simulation(self):
        """Run the simulated virus."""

        print("\n==============================")
        print("VIRUS SIMULATION")
        print("==============================")

        # Infect a file on PC1
        self.virus.infect_file(
            "PC1",
            "document.txt"
        )

        # Share infected file from PC1 to PC2
        self.virus.spread_through_file_sharing(
            "PC1",
            "PC2",
            "document.txt"
        )

        self.virus.display_status()

    def run_worm_simulation(self):
        """Run the simulated worm."""

        print("\n==============================")
        print("WORM SIMULATION")
        print("==============================")

        # Infect PC1
        self.worm.infect_computer("PC1")

        # Run worm propagation
        self.worm.run_simulation(
            steps=5
        )

        self.worm.display_status()

    def display_network(self):
        """Display network information."""

        print("\n==============================")
        print("NETWORK INFORMATION")
        print("==============================")

        print(
            "Computers:",
            list(self.network.nodes)
        )

        print(
            "Connections:",
            list(self.network.edges)
        )

        print(
            "Protected computers:",
            [
                computer
                for computer in self.network.nodes
                if self.network.nodes[computer].get(
                    "protected",
                    False
                )
            ]
        )

    def display_final_status(self):
        """Display final network infection status."""

        print("\n==============================")
        print("FINAL NETWORK STATUS")
        print("==============================")

        for computer in self.network.nodes:

            infected = self.network.nodes[
                computer
            ].get("infected", False)

            protected = self.network.nodes[
                computer
            ].get("protected", False)

            print(
                f"{computer}: "
                f"Infected={infected}, "
                f"Protected={protected}"
            )


if __name__ == "__main__":

    # Create simulator
    simulator = NetworkSimulator()

    # Display network
    simulator.display_network()

    # Add simulated files
    simulator.setup_files()

    # Run virus simulation
    simulator.run_virus_simulation()

    # Run worm simulation
    simulator.run_worm_simulation()

    # Display final status
    simulator.display_final_status()