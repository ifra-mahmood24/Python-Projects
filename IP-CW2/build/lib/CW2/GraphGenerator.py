from .AlsoLikes import AlsoLikes

class GraphGenerator:
    def __init__(self, df_copy):
        self.df_copy = df_copy
        self.also_likes = AlsoLikes(df_copy)

    @staticmethod
    def short_id(uuid: str) -> str:
        return uuid[-4:]

    def build_graph_data(self, main_doc, liked_docs):
        docs = set([main_doc]) | set(liked_docs)
        edges = set()
        readers = set()

        # Readers of main doc
        readers_main = self.also_likes.getReaders(main_doc)

        for doc in liked_docs:
            readers_doc = self.also_likes.getReaders(doc)
            common_readers = set(readers_main) & set(readers_doc)
            for r in common_readers:
                readers.add(r)
                edges.add((r, main_doc))
                edges.add((r, doc))

        return {
            "docs": docs,
            "readers": readers,
            "edges": list(edges),
        }

    def generate_dot(self, main_doc, liked_docs, highlight_reader=None):
        data = self.build_graph_data(main_doc, liked_docs)
        docs = data["docs"]
        readers = data["readers"]
        edges = data["edges"]

        lines = []
        lines.append("digraph AlsoLikes {")
        lines.append('  rankdir=TB;')
        lines.append('  node [fontname="Helvetica"];')

        # Document nodes
        for d in docs:
            sid = self.short_id(d)
            if d == main_doc:
                lines.append(
                    f'  "{sid}" [shape=circle, style=filled, fillcolor="green", label="{sid}"];'
                )
            else:
                lines.append(f'  "{sid}" [shape=circle, label="{sid}"];')

        # Reader nodes
        for r in readers:
            sid = self.short_id(r)
            if highlight_reader and r == highlight_reader:
                lines.append(
                    f'  "{sid}" [shape=box, style=filled, fillcolor="green", label="{sid}"];'
                )
            else:
                lines.append(f'  "{sid}" [shape=box, label="{sid}"];')

        # Edges
        for r, d in edges:
            r_sid = self.short_id(r)
            d_sid = self.short_id(d)
            lines.append(f'  "{r_sid}" -> "{d_sid}";')

        lines.append("}")
        return "\n".join(lines)

    def write_dot_file(self, main_doc, liked_docs, highlight_reader=None, filename="also_likes.dot"):
        dot_text = self.generate_dot(main_doc, liked_docs, highlight_reader)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(dot_text)
        return filename