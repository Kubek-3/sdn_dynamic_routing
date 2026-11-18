"""Project topology

In total 8 switches and two hosts that generate traffic:

             S2 --- S3 --- S4
             / \     |     / \
 host1 --- S1   -----------  S5 --- host2
            \  /     |     \ /
             S8 --- S7 --- S6
Links:
- host1: S1
- S1: host1, S2, S8
- S2: S1, S3, S6
- S3: S2, S4, S7
- S4: S3, S5, S8
- S5: host2, S4, S6
- S6: S2, S5, S7
- S7: S3, S6, S8
- S8: S1, S4, S7

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=project_topo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts
        hosts = [self.addHost(f'h{i}') for i in range(1, 3)]

        # Add switches
        switches = [self.addSwitch(f's{i}') for i in range(1, 9)]

        # 3. Add host links
        self.addLink(hosts[0], switches[0])  # host1 -> s1
        self.addLink(hosts[1], switches[4])  # host2 -> s5

        # 4. Add switch-to-switch links using (switch_number_1, switch_number_2)
        switch_links = [
            # Outer ring
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 8),
            (8, 1),
            # Cross-ring connections
            (2, 6),
            (3, 7),
            (4, 8),
        ]

        for s_a, s_b in switch_links:
            self.addLink(switches[s_a - 1], switches[s_b - 1])

topos = { 'mytopo': ( lambda: MyTopo() ) }
