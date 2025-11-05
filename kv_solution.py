class KVStore:
    def __init__(self):
        self.data = {}
    
    def put(self, key: str, value: str):
        self.data[key] = value
    
    def get(self, key: str):
        return self.data.get(key)
    
    def shutdown(self):
        result = bytearray()
        for key, value in self.data.items():
            key_bytes = key.encode('utf-8')
            value_bytes = value.encode('utf-8')
            
            result.extend(len(key_bytes).to_bytes(4, 'big'))
            result.extend(key_bytes)
            result.extend(len(value_bytes).to_bytes(4, 'big'))
            result.extend(value_bytes)
        
        save_blob(bytes(result))
    
    def restore(self):
        data = get_blob()
        self.data = {}
        
        i = 0
        while i < len(data):
            key_len = int.from_bytes(data[i:i+4], 'big')
            i += 4
            key = data[i:i+key_len].decode('utf-8')
            i += key_len
            
            value_len = int.from_bytes(data[i:i+4], 'big')
            i += 4
            value = data[i:i+value_len].decode('utf-8')
            i += value_len
            
            self.data[key] = value

# Follow-up: Multi-file when > 1KB
class KVStoreMultiFile:
    def __init__(self, max_size=1024):
        self.data = {}
        self.max_size = max_size
    
    def put(self, key: str, value: str):
        self.data[key] = value
    
    def get(self, key: str):
        return self.data.get(key)
    
    def shutdown(self):
        # Serialize
        all_data = bytearray()
        for key, value in self.data.items():
            key_bytes = key.encode('utf-8')
            value_bytes = value.encode('utf-8')
            
            all_data.extend(len(key_bytes).to_bytes(4, 'big'))
            all_data.extend(key_bytes)
            all_data.extend(len(value_bytes).to_bytes(4, 'big'))
            all_data.extend(value_bytes)
        
        # Split into chunks
        chunks = [all_data[i:i+self.max_size] for i in range(0, len(all_data), self.max_size)]
        
        # Save metadata and chunks
        save_metadata(len(chunks))
        for i, chunk in enumerate(chunks):
            save_blob_with_id(bytes(chunk), i)
    
    def restore(self):
        num_files = get_metadata()
        
        all_data = bytearray()
        for i in range(num_files):
            all_data.extend(get_blob_with_id(i))
        
        # Deserialize
        self.data = {}
        i = 0
        while i < len(all_data):
            key_len = int.from_bytes(all_data[i:i+4], 'big')
            i += 4
            key = all_data[i:i+key_len].decode('utf-8')
            i += key_len
            
            value_len = int.from_bytes(all_data[i:i+4], 'big')
            i += 4
            value = all_data[i:i+value_len].decode('utf-8')
            i += value_len
            
            self.data[key] = value

# Mock helpers (provided in interview)
def save_blob(data: bytes): pass
def get_blob() -> bytes: pass
def save_metadata(count: int): pass
def get_metadata() -> int: pass
def save_blob_with_id(data: bytes, file_id: int): pass
def get_blob_with_id(file_id: int) -> bytes: pass
