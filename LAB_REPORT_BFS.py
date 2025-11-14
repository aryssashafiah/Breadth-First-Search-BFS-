
import streamlit as st

# Directed graph from your lab image
graph = {
    'A': ['D', 'B'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['F']
}

def bfs_with_discovery_levels(start='A'):
    from collections import deque
    visited = set()
    queue = deque([(start, 0)])
    traversal = []
    discovery = []

    while queue:
        node, lvl = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            discovery.append((lvl, node))
            # Alphabetical tie-breaking
            for neighbor in sorted(graph[node]):
                if neighbor not in visited:
                    queue.append((neighbor, lvl + 1))
    return traversal, discovery

# =============== STREAMLIT UI ===============
st.set_page_config(page_title="Lab Report 1 - Introduction to AI – BFS", layout="centered")

# 🖼️ Show your graph image at the very top
st.image("LabReport_BSD2513_1.jpg", caption="Directed Graph from Lab Report", use_container_width=True)

st.title("🔍 Breadth-First Search (BFS)")

if st.button("▶️ Generate BFS Output"):
    traversal, discovery = bfs_with_discovery_levels('A')

    # Traversal Order
    st.subheader("Traversal Order:")
    st.markdown(f"**BFS Traversal Order**: {' → '.join(traversal)}")

    # Node Discovery Level (exact format from your image)
    st.subheader("Node Discovery Level:")
    for lvl, node in discovery:
        st.markdown(f"""
        <div style="
            background-color: #e6f2ff;
            padding: 10px;
            margin: 5px 0;
            border-radius: 8px;
            font-family: monospace;
            font-size: 16px;
            color: #004080;
        ">
            Level {lvl} → {node}
        </div>
        """, unsafe_allow_html=True)