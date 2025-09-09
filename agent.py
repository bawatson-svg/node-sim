import random
import time

class Node:
        def __init__(self, node_id):
                self.node_id = node_id
                self.state = "idle"

        def simulate_activity(self):
                self.state = random.choice(["idle", "sending"])
                print(f"Node {self.node_id} is now {self.state}")

if __name__ == "__main__":
        nodes = [Node(i) for i in range(3)]
        while True:
                for node in nodes:
                        node.simulate_activity()
                time.sleep(2)   