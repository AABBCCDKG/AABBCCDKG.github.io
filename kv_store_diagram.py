import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

def create_kv_store_diagram():
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('OpenAI KV Store - Serialization Logic', fontsize=16, fontweight='bold')
    
    # 1. Overall Architecture
    ax = axes[0, 0]
    ax.set_title('KV Store Architecture', fontweight='bold', fontsize=14)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    
    # Memory layer
    memory_rect = FancyBboxPatch((1, 6), 8, 1.5, boxstyle="round,pad=0.1",
                                facecolor='lightblue', edgecolor='black', linewidth=2)
    ax.add_patch(memory_rect)
    ax.text(5, 6.75, 'Memory Dict\n{"key1": "value1", "key2": "value2"}', 
            ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Serialization layer
    serialize_rect = FancyBboxPatch((1, 4), 8, 1, boxstyle="round,pad=0.1",
                                   facecolor='lightyellow', edgecolor='black')
    ax.add_patch(serialize_rect)
    ax.text(5, 4.5, 'Serialization Layer\nLength + Data Format', 
            ha='center', va='center', fontsize=11)
    
    # Storage layer
    storage_rect = FancyBboxPatch((1, 2), 8, 1, boxstyle="round,pad=0.1",
                                 facecolor='lightgreen', edgecolor='black')
    ax.add_patch(storage_rect)
    ax.text(5, 2.5, 'File Storage\nsave_blob() / get_blob()', 
            ha='center', va='center', fontsize=11)
    
    # Arrows
    ax.arrow(5, 5.8, 0, -0.6, head_width=0.2, head_length=0.1, fc='red', ec='red', linewidth=2)
    ax.text(5.5, 5.3, 'shutdown()', ha='left', va='center', fontsize=10, color='red', fontweight='bold')
    
    ax.arrow(5, 3.2, 0, -0.6, head_width=0.2, head_length=0.1, fc='red', ec='red', linewidth=2)
    
    ax.arrow(4.8, 3, 0, 0.6, head_width=0.2, head_length=0.1, fc='blue', ec='blue', linewidth=2)
    ax.text(4.3, 3.5, 'restore()', ha='right', va='center', fontsize=10, color='blue', fontweight='bold')
    
    ax.arrow(4.8, 4.8, 0, 0.6, head_width=0.2, head_length=0.1, fc='blue', ec='blue', linewidth=2)
    
    # API methods
    ax.text(0.5, 1, 'API Methods:\n• put(key, value)\n• get(key)\n• shutdown()\n• restore()', 
            ha='left', va='center', fontsize=10, 
            bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.8))
    
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    
    # 2. Serialization Format
    ax = axes[0, 1]
    ax.set_title('Serialization Format (Length + Data)', fontweight='bold', fontsize=14)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    
    # Example data
    ax.text(6, 5.5, 'Example: {"abc": "hello", "x": "world"}', 
            ha='center', va='center', fontsize=12, fontweight='bold',
            bbox=dict(boxstyle="round", facecolor='lightcyan'))
    
    # Byte format visualization
    segments = [
        (0.5, 4, 1, 0.6, '3', 'key1_len'),
        (1.5, 4, 1.5, 0.6, 'abc', 'key1_data'),
        (3, 4, 1, 0.6, '5', 'val1_len'),
        (4, 4, 2.5, 0.6, 'hello', 'val1_data'),
        (6.5, 4, 1, 0.6, '1', 'key2_len'),
        (7.5, 4, 0.5, 0.6, 'x', 'key2_data'),
        (8, 4, 1, 0.6, '5', 'val2_len'),
        (9, 4, 2.5, 0.6, 'world', 'val2_data')
    ]
    
    colors = ['lightcoral', 'lightblue', 'lightcoral', 'lightblue', 
              'lightcoral', 'lightblue', 'lightcoral', 'lightblue']
    
    for i, (x, y, w, h, text, label) in enumerate(segments):
        rect = Rectangle((x, y), w, h, facecolor=colors[i], edgecolor='black')
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=10, fontweight='bold')
        ax.text(x + w/2, y - 0.3, label, ha='center', va='center', fontsize=8, rotation=45)
    
    # Legend
    ax.text(6, 2.5, 'Format: [len][data][len][data]...\n\n• Length: 4 bytes (big endian)\n• Data: UTF-8 encoded string', 
            ha='center', va='center', fontsize=11,
            bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.8))
    
    ax.set_xticks([])
    ax.set_yticks([])
    
    # 3. Core Code Logic
    ax = axes[1, 0]
    ax.set_title('Core Serialization Code', fontweight='bold', fontsize=14)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    
    # Serialize code
    serialize_code = """# Serialize (shutdown)
result = b''
for key, value in data.items():
    key_bytes = key.encode('utf-8')
    val_bytes = value.encode('utf-8')
    
    result += len(key_bytes).to_bytes(4, 'big')
    result += key_bytes
    result += len(val_bytes).to_bytes(4, 'big') 
    result += val_bytes

save_blob(result)"""
    
    ax.text(5, 6, serialize_code, ha='center', va='center', fontsize=9, 
            fontfamily='monospace',
            bbox=dict(boxstyle="round", facecolor='lightcyan', alpha=0.9))
    
    # Deserialize code
    deserialize_code = """# Deserialize (restore)
blob = get_blob()
data, i = {}, 0

while i < len(blob):
    key_len = int.from_bytes(blob[i:i+4], 'big')
    key = blob[i+4:i+4+key_len].decode('utf-8')
    i += 4 + key_len
    
    val_len = int.from_bytes(blob[i:i+4], 'big')
    value = blob[i+4:i+4+val_len].decode('utf-8')
    i += 4 + val_len
    
    data[key] = value"""
    
    ax.text(5, 2.5, deserialize_code, ha='center', va='center', fontsize=9,
            fontfamily='monospace',
            bbox=dict(boxstyle="round", facecolor='lightgreen', alpha=0.9))
    
    ax.set_xticks([])
    ax.set_yticks([])
    
    # 4. Follow-up: File Size Limit
    ax = axes[1, 1]
    ax.set_title('Follow-up: File Size Limit (1KB)', fontweight='bold', fontsize=14)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    
    # Large data
    ax.text(5, 7, 'Large KV Data (> 1KB)', ha='center', va='center', fontsize=12,
            bbox=dict(boxstyle="round", facecolor='lightcoral'))
    
    # Split arrow
    ax.arrow(5, 6.5, 0, -0.5, head_width=0.2, head_length=0.1, fc='black', ec='black')
    ax.text(5.5, 6, 'Split', ha='left', va='center', fontsize=10, fontweight='bold')
    
    # Multiple files
    files = [
        (1.5, 5, 'data_part_1\n(1KB)'),
        (5, 5, 'data_part_2\n(1KB)'),
        (8.5, 5, 'data_part_3\n(0.5KB)')
    ]
    
    for x, y, text in files:
        rect = FancyBboxPatch((x-0.7, y-0.4), 1.4, 0.8, boxstyle="round,pad=0.1",
                             facecolor='lightblue', edgecolor='black')
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=9)
    
    # Metadata file
    metadata_rect = FancyBboxPatch((4, 3), 2, 1, boxstyle="round,pad=0.1",
                                  facecolor='lightyellow', edgecolor='black', linewidth=2)
    ax.add_patch(metadata_rect)
    ax.text(5, 3.5, 'metadata.txt\n["data_part_1",\n "data_part_2",\n "data_part_3"]', 
            ha='center', va='center', fontsize=9, fontweight='bold')
    
    # Arrows to metadata
    for x, y, _ in files:
        ax.arrow(x, y-0.5, 5-x, 3.8-y, head_width=0.1, head_length=0.1, 
                fc='gray', ec='gray', alpha=0.7, linestyle='--')
    
    # Solution text
    ax.text(5, 1.5, 'Solution:\n• Split data into 1KB chunks\n• Create metadata file with file list\n• Read metadata first, then all parts', 
            ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.8))
    
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.tight_layout()
    plt.savefig('/Users/wangbd/Desktop/AABBCCDKG.github.io/kv_store_detailed.jpg', 
                dpi=300, bbox_inches='tight')
    plt.close()
    
    print("KV Store diagram saved as kv_store_detailed.jpg")

if __name__ == "__main__":
    create_kv_store_diagram()
