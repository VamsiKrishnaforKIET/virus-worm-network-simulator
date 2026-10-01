import networkx as nx


class VirusSimulator:
    def __init__(self, network):
        self.network = network

        # Store simulated files on each computer
        self.files = {}

        # Store infected simulated files
        self.infected_files = {}

    def add_file(self, computer_id, filename):
        """Add a simulated file to a computer."""

        if computer_id not in self.network:
            print(f"Computer {computer_id} does not exist.")
            return False

        if computer_id not in self.files:
            self.files[computer_id] = []

        if filename not in self.files[computer_id]:
            self.files[computer_id].append(filename)

        print(f"File '{filename}' added to {computer_id}")
        return True

    def infect_file(self, computer_id, filename):
        """Simulate a virus attaching to a file."""

        if computer_id not in self.files:
            print(f"No files found on {computer_id}.")
            return False

        if filename not in self.files[computer_id]:
            print(
                f"File '{filename}' not found on {computer_id}."
            )
            return False

        if computer_id not in self.infected_files:
            self.infected_files[computer_id] = []

        if filename not in self.infected_files[computer_id]:
            self.infected_files[computer_id].append(filename)

        # Mark computer as infected
        self.network.nodes[computer_id]["infected"] = True

        print(
            f"Virus attached to '{filename}' on {computer_id}"
        )

        return True

    def is_file_infected(self, computer_id, filename):
        """Check whether a simulated file is infected."""

        return (
            computer_id in self.infected_files
            and filename in self.infected_files[computer_id]
        )

    def get_infected_files(self, computer_id):
        """Return infected files on a computer."""

        return self.infected_files.get(
            computer_id,
            []
        )

    def spread_through_file_sharing(
        self,
        source_computer,
        target_computer,
        filename
    ):
        """Simulate virus spreading through file sharing."""

        if not self.is_file_infected(
            source_computer,
            filename
        ):
            print(
                f"'{filename}' is not infected on "
                f"{source_computer}."
            )
            return False

        if not self.network.has_edge(
            source_computer,
            target_computer
        ):
            print(
                f"{source_computer} is not directly "
                f"connected to {target_computer}."
            )
            return False

        if target_computer not in self.files:
            self.files[target_computer] = []

        if filename not in self.files[target_computer]:
            self.files[target_computer].append(filename)

        self.infect_file(
            target_computer,
            filename
        )

        print(
            f"Virus spread from {source_computer} "
            f"to {target_computer} through '{filename}'"
        )

        return True

    def display_status(self):
        """Display virus infection status."""

        print("\nVirus Simulation Status")
        print("-----------------------")

        for computer in self.files:
            print(f"\n{computer}")

            print(
                "Files:",
                self.files[computer]
            )

            print(
                "Infected files:",
                self.infected_files.get(
                    computer,
                    []
                )
            )


if __name__ == "__main__":

    # Create NetworkX graph
    network = nx.Graph()

    # Add computers
    for computer in ["PC1", "PC2", "PC3"]:
        network.add_node(
            computer,
            infected=False,
            protected=False
        )

    # Connect computers
    network.add_edge("PC1", "PC2")
    network.add_edge("PC2", "PC3")

    # Create virus simulator
    virus = VirusSimulator(network)

    # Add simulated files
    virus.add_file(
        "PC1",
        "document.txt"
    )

    virus.add_file(
        "PC2",
        "report.pdf"
    )

    virus.add_file(
        "PC3",
        "image.jpg"
    )

    # Infect a file
    virus.infect_file(
        "PC1",
        "document.txt"
    )

    # Spread infected file
    virus.spread_through_file_sharing(
        "PC1",
        "PC2",
        "document.txt"
    )

    # Display status
    virus.display_status()