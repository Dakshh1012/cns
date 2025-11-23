"""
Snort - Network Intrusion Detection System (IDS)
Provides real-time traffic analysis and packet logging
This is a configuration/rule demonstration for Snort
"""

class SnortConfiguration:
    """Snort IDS Configuration and Rules"""
    
    def __init__(self):
        self.rules = []
        self.preprocessors = {}
        self.output_plugins = []
    
    def add_rule(self, action, protocol, src_ip, src_port, direction, dst_ip, dst_port, msg, sid):
        """Add a Snort rule
        action: alert, drop, pass, log
        protocol: tcp, udp, icmp, ip
        direction: <> (bidirectional), -> (unidirectional)
        """
        rule = f"{action} {protocol} {src_ip} {src_port} {direction} {dst_ip} {dst_port} (msg:\"{msg}\"; sid:{sid};)"
        self.rules.append(rule)
        return rule
    
    def add_preprocessor(self, name, config):
        """Add Snort preprocessor configuration"""
        self.preprocessors[name] = config
    
    def add_output_plugin(self, plugin_name, config):
        """Add output plugin"""
        self.output_plugins.append(f"output {plugin_name}: {config}")
    
    def display_rules(self):
        """Display all configured rules"""
        print("\n=== SNORT RULES ===")
        for i, rule in enumerate(self.rules, 1):
            print(f"{i}. {rule}")
    
    def display_config(self):
        """Display complete configuration"""
        print("\n=== SNORT CONFIGURATION ===")
        
        print("\n[Preprocessors]")
        for name, config in self.preprocessors.items():
            print(f"{name}: {config}")
        
        print("\n[Output Plugins]")
        for plugin in self.output_plugins:
            print(plugin)
        
        print("\n[Rules]")
        self.display_rules()

def snort_menu():
    """Menu-driven Snort configuration"""
    snort = SnortConfiguration()
    
    # Pre-configured rules
    snort.add_rule("alert", "tcp", "$EXTERNAL_NET", "any", "->", "$HOME_NET", "22", 
                   "SSH connection attempt", "1000001")
    snort.add_rule("alert", "tcp", "$EXTERNAL_NET", "any", "->", "$HOME_NET", "80", 
                   "HTTP connection attempt", "1000002")
    snort.add_rule("alert", "icmp", "$EXTERNAL_NET", "any", "<>", "$HOME_NET", "any", 
                   "PING attempt detected", "1000003")
    snort.add_rule("drop", "tcp", "$EXTERNAL_NET", "any", "->", "$HOME_NET", "445", 
                   "SMB/CIFS connection attempt", "1000004")
    
    # Pre-configured preprocessors
    snort.add_preprocessor("frag3", "max_frags 65536, preproc_memcap 4194304")
    snort.add_preprocessor("stream5", "tcp: detect_anomalies, policy balanced")
    snort.add_preprocessor("http_inspect", "server default, enable_xi_directory")
    
    # Output plugins
    snort.add_output_plugin("unified2", "filename snort.u2")
    snort.add_output_plugin("alert_fast", "file /var/log/snort/alert")
    
    while True:
        print("\n=== SNORT IDS/IPS ===")
        print("1. Display All Rules")
        print("2. Add Custom Rule")
        print("3. Display Configuration")
        print("4. Example Rules Library")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            snort.display_rules()
        
        elif choice == '2':
            try:
                print("\n--- Add Custom Rule ---")
                action = input("Action (alert/drop/pass/log): ").strip()
                protocol = input("Protocol (tcp/udp/icmp/ip): ").strip()
                src_ip = input("Source IP (or $EXTERNAL_NET): ").strip()
                src_port = input("Source Port (or any): ").strip()
                direction = input("Direction (-> or <>): ").strip()
                dst_ip = input("Destination IP (or $HOME_NET): ").strip()
                dst_port = input("Destination Port (or any): ").strip()
                msg = input("Message/Description: ").strip()
                sid = input("SID (unique identifier): ").strip()
                
                rule = snort.add_rule(action, protocol, src_ip, src_port, direction, 
                                    dst_ip, dst_port, msg, sid)
                print(f"✓ Rule added: {rule}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            snort.display_config()
        
        elif choice == '4':
            print("\n=== EXAMPLE SNORT RULES ===")
            examples = [
                "alert tcp any any -> any 25 (msg:\"SMTP traffic\"; sid:1000100;)",
                "alert tcp any any -> any 143 (msg:\"IMAP traffic\"; sid:1000101;)",
                "alert tcp any any -> any 110 (msg:\"POP3 traffic\"; sid:1000102;)",
                "alert tcp any any -> any 3306 (msg:\"MySQL traffic\"; sid:1000103;)",
                "alert tcp any any -> any 5432 (msg:\"PostgreSQL traffic\"; sid:1000104;)",
                "alert icmp any any -> any any (msg:\"ICMP Ping detected\"; sid:1000105;)",
                "drop tcp any any -> any 31337 (msg:\"Back Orifice trojan\"; sid:1000106;)",
                "alert tcp $HOME_NET any -> $EXTERNAL_NET 443 (msg:\"Outbound HTTPS\"; sid:1000107;)",
            ]
            for example in examples:
                print(f"  {example}")
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    snort_menu()
