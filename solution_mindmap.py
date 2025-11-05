import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

def create_solution_mindmap():
    fig, ax = plt.subplots(1, 1, figsize=(18, 14))
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 16)
    ax.axis('off')
    
    # Central solution
    center_box = FancyBboxPatch((8, 7), 4, 2, boxstyle="round,pad=0.2", 
                               facecolor='#2E86AB', edgecolor='black', linewidth=3)
    ax.add_patch(center_box)
    ax.text(10, 8, 'KV Store\nSolution', ha='center', va='center', 
            fontsize=16, fontweight='bold', color='white')
    
    # Serialization branch
    serialize_box = FancyBboxPatch((2, 12), 4, 1.5, boxstyle="round,pad=0.1",
                                  facecolor='#A23B72', edgecolor='black', linewidth=2)
    ax.add_patch(serialize_box)
    ax.text(4, 12.75, 'Serialization\n(shutdown)', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    
    # Serialization steps
    ser_steps = [
        (1, 10.5, '1. Iterate KV pairs'),
        (1, 9.5, '2. Encode key length (4 bytes)'),
        (1, 8.5, '3. Encode key string'),
        (1, 7.5, '4. Encode value length (4 bytes)'),
        (1, 6.5, '5. Encode value string'),
        (1, 5.5, '6. Concatenate all bytes'),
        (1, 4.5, '7. Call save_blob()')
    ]
    
    for x, y, text in ser_steps:
        box = FancyBboxPatch((x-0.5, y-0.3), 5, 0.6, boxstyle="round,pad=0.05",
                            facecolor='#F18F01', edgecolor='black')
        ax.add_patch(box)
        ax.text(x+2, y, text, ha='center', va='center', fontsize=9)
    
    # Deserialization branch
    deserialize_box = FancyBboxPatch((14, 12), 4, 1.5, boxstyle="round,pad=0.1",
                                    facecolor='#C73E1D', edgecolor='black', linewidth=2)
    ax.add_patch(deserialize_box)
    ax.text(16, 12.75, 'Deserialization\n(restore)', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    
    # Deserialization steps
    deser_steps = [
        (15, 10.5, '1. Call get_blob()'),
        (15, 9.5, '2. Read key length'),
        (15, 8.5, '3. Read key string'),
        (15, 7.5, '4. Read value length'),
        (15, 6.5, '5. Read value string'),
        (15, 5.5, '6. Store in map'),
        (15, 4.5, '7. Repeat until end')
    ]
    
    for x, y, text in deser_steps:
        box = FancyBboxPatch((x-2, y-0.3), 5, 0.6, boxstyle="round,pad=0.05",
                            facecolor='#3F88C5', edgecolor='black')
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, color='white')
    
    # Binary format
    format_box = FancyBboxPatch((8, 3), 4, 1.5, boxstyle="round,pad=0.1",
                               facecolor='#032B43', edgecolor='black', linewidth=2)
    ax.add_patch(format_box)
    ax.text(10, 3.75, 'Binary Format\n[len][data][len][data]...', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    
    # Follow-up solution
    followup_box = FancyBboxPatch((8, 0.5), 4, 1.5, boxstyle="round,pad=0.1",
                                 facecolor='#7209B7', edgecolor='black', linewidth=2)
    ax.add_patch(followup_box)
    ax.text(10, 1.25, 'Multi-file Solution\nSplit + Metadata', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    
    # Multi-file details
    multi_details = [
        (2, 1.5, 'Split data into 1KB chunks'),
        (18, 1.5, 'Save metadata with file count'),
        (2, 0.5, 'Save each chunk separately'),
        (18, 0.5, 'Restore by combining chunks')
    ]
    
    for x, y, text in multi_details:
        box = FancyBboxPatch((x-2, y-0.25), 4, 0.5, boxstyle="round,pad=0.05",
                            facecolor='#D63384', edgecolor='black')
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, color='white')
    
    # Connections
    # Center to serialization
    ax.plot([8, 6], [8.5, 12], 'k-', linewidth=2)
    # Center to deserialization  
    ax.plot([12, 14], [8.5, 12], 'k-', linewidth=2)
    # Center to format
    ax.plot([10, 10], [7, 4.5], 'k-', linewidth=2)
    # Center to follow-up
    ax.plot([10, 10], [7, 2], 'k-', linewidth=2)
    
    # Serialization to steps
    for _, y, _ in ser_steps:
        ax.plot([4, 1], [12, y], 'k-', alpha=0.6)
    
    # Deserialization to steps
    for _, y, _ in deser_steps:
        ax.plot([16, 16], [12, y], 'k-', alpha=0.6)
    
    # Follow-up to details
    for x, y, _ in multi_details:
        ax.plot([10, x], [1.25, y], 'k-', alpha=0.6)
    
    plt.title('KV Store Implementation Solution Flow', fontsize=18, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('/Users/wangbd/Desktop/AABBCCDKG.github.io/solution_diagram.jpg', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

if __name__ == "__main__":
    create_solution_mindmap()
