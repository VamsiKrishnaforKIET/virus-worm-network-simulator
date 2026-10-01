import networkx as nx


class WormSimulator:
    def __init__(self, network):
        self.network = network

        # Store computers infected by the worm
        self.infected_computers = set()

        # Store each step of worm propagation
        self.spread_history = []

    def infect_computer(self, computer_id):
        """Infect a computer with the simulated worm."""

        if computer_id not in self.network:
            print(f"Computer {computer_id} does not exist.")
            return False

        if computer_id in self.infected_computers:
            print(f"{computer_id} is already infected.")
            return False

        self.infected_computers.add(computer_id)

        # Mark computer as infected
        self.network.nodes[computer_id]["infected"] = True

        print(f"Worm infected {computer_id}")

        return True

    def spread(self):
        """Simulate autonomous worm propagation."""

        newly_infected = set()

        # Check all currently infected computers
        for computer in self.infected_computers:

            # Get directly connected computers
            neighbors = list(
                self.network.neighbors(computer)
            )

            for neighbor in neighbors:

                # Do not infect protected computers
                protected = self.network.nodes[
                    neighbor
                ].get("protected", False)

                if protected:
                    continue

                # Infect only new computers
                if neighbor not in self.infected_computers:
                    newly_infected.add(neighbor)

        # Add newly infected computers
        for computer in newly_infected:
            self.infected_computers.add(computer)

            self.network.nodes[
                computer
            ]["infected"] = True

        # Save propagation step
        self.spread_history.append(
            list(newly_infected)
        )

        return list(newly_infected)

    def run_simulation(self, steps=5):
        """Run the worm simulation."""

        print("\nWorm Spread Simulation")
        print("----------------------")

        for step in range(1, steps + 1):

            newly_infected = self.spread()

            print(f"\nStep {step}:")

            if newly_infected:
                print(
                    "Newly infected:",
                    newly_infected
                )
            else:
                print(
                    "No new computers infected."
                )
                break

    def get_infected_computers(self):
        """Return all infected computers."""

        return list(self.infected_computers)

    def display_status(self):
        """Display current worm infection status."""

        print("\nWorm Simulation Status")
        print("----------------------")

        print(
            "Infected computers:",
            self.get_infected_computers()
        )

        print(
            "Spread history:",
            self.spread_history
        )


if __name__ == "__main__":

    # Create NetworkX graph
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

    # Protect PC5
    network.nodes["PC5"]["protected"] = True

    # Create worm simulator
    worm = WormSimulator(network)

    # Initially infect PC1
    worm.infect_computer("PC1")

    # Run simulation
    worm.run_simulation(steps=5)

    # Display final status
    worm.display_status()