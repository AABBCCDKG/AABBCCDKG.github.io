import uuid

def sendAsyncMessage(nodeId, message):
    """Simulate sending message to another machine"""
    pass

class MachineTree:
    def __init__(self, nodeId, children = None, parent = None):
        self.nodeId = nodeId
        self.children = children or []
        self.parent = parent
        self.pending = {}
        self.results = {}
    
    def count(self):
        request_id = str(uuid.uuid4())
        self.receiveMessage({
            'type': 'count_request',
            'request_id': request_id,
            'from': None
        })
        return request_id
    
    def topology(self):
        request_id = str(uuid.uuid4())
        self.receiveMessage({
            'type': 'topology_request', 
            'request_id': request_id,
            'from': None
        })
        return request_id

    def receiveMessage(self, message):
        msg_type = message['type']
        request_id = message['request_id']

        if msg_type in ['count_request', 'topology_request']:
            if not self.children:
                result = 1 if msg_type == 'count_request' else {self.nodeId: {}}
                self._send_response(message['from'], request_id, msg_type.replace('request', 'response'), result)
            else:
                self.pending[request_id] = len(self.children)
                self.results[request_id] = {}
                for child in self.children:
                    sendAsyncMessage(child, {
                        'type': msg_type,
                        'request_id': request_id,
                        'from': self.nodeId
                    })
        elif msg_type in ['count_response', 'topology_response']:
            self.results[request_id][message['from']] = message['result']
            self.pending[request_id] -= 1
            if self.pending[request_id] == 0:
                if msg_type == 'count_response':
                    total = sum(self.results[request_id].values()) + 1
                else:
                    total = {self.nodeId: {}}
                    for child_topo in self.results[request_id].values():
                        total[self.nodeId].update(child_topo)
                
                if self.parent:
                    self._send_response(self.parent, request_id, msg_type, total)
                else:
                    print(f"Final result: {total}")
                
                del self.pending[request_id]
                del self.results[request_id]

    def _send_response(self, to_node, request_id, msg_type, result):
        if to_node:
            sendAsyncMessage(to_node, {
                'type': msg_type,
                'request_id': request_id,
                'from': self.nodeId,
                'result': result
            })

def main():
    # Create tree: root(1) -> [child1(2), child2(3)] -> [grandchild(4)]
    root = MachineTree("1")
    child1 = MachineTree("2", parent="1")
    child2 = MachineTree("3", parent="1") 
    grandchild = MachineTree("4", parent="2")
    
    root.children = ["2", "3"]
    child1.children = ["4"]
    
    # Test count
    print("Starting count...")
    root.count()
    
    # Test topology
    print("Starting topology...")
    root.topology()

if __name__ == "__main__":
    main()
