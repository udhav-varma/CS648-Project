from manim import *  
from manim_slides import Slide

class Kruskal(Slide):
    def construct(self):
        
        opening_text = Tex(r'CS648A Presentation\\', r'Udhav Varma and Yuvraj Kharayat\\', r'\textbf{Expected Value of Weight of MST in a random complete graph}')
        opening_text[2].scale(0.6)
        self.play(Write(opening_text, run_time=2))
        box1 = SurroundingRectangle(opening_text, buff=0.1)
        self.play(Create(box1))
        grp = Group(opening_text, box1)
        self.next_slide()
        title = Title(r'Analysis using Prim\textquotesingle s Algorithm')
        self.wipe(grp, title)
        self.next_slide()
        # self.add(title)
        points = [
            [0, 0, 0], # (x, y, z) coordinates
            [-1, 1, 0],
            [1, 0, 0],
            [-2, 1.5, 0],
            [-2, -2, 0],
            [4, 1, 0]
        ]

        # Create a VGroup of Dots for the points
        point_dots = VGroup(*[Dot(point = p) for p in points])
        self.play(Create(point_dots))
        self.next_slide()
        # Create a VGroup of line segments joining the points
        lines = VGroup()
        for i in range(3):
            line = Line(points[i], points[i+1], color=RED)
            lines.add(line)
        lines.add(Line(points[0], points[4], color=RED))
        lines.add(Line(points[2], points[5], color=RED))
        self.play(Create(lines))
        self.next_slide()
        graph = VGroup(point_dots, lines)
        self.play(graph.animate.shift(2*RIGHT).scale(0.5))
        text = Tex("""We will be proving that \\\\the expected weight of MST \\\\ for a random graph\\\\ with $n$ vertices is $\log_e n$ + $\mathcal{O}(1)$.
                   """).move_to(2.5*LEFT)
        self.play(Write(text)) # Animate FadeIN
        # self.wait()
        self.next_slide()
        self.play(FadeOut(text)) # Animate FadeOut
        self.play(FadeOut(graph))
        text1 = Tex("Suppose during the construction of the MST\\\\ using Prim's Algorithm, first $k$ vertices have been added")
        self.play(Write(text1))
        # self.wait()
        self.next_slide()
        self.play(FadeOut(text1))
        text2 = Tex('''Among the outgoing edges \\\\from the $k$ vertices to the $n - k$ vertices,\\\\ let for $1 \leq i \leq k$ $Y_i$ denote \\\\the random variable which is \\\\equal to the smallest outgoing edge from vertex $i$''')
        self.next_slide()
        self.play(Write(text2))
        # self.wait();
        self.next_slide()
        self.play(FadeOut(text2))
        text3 = Tex('''Let us partition the building of the MST into stages,\\\\ the i\\textsuperscript{th} stage is when $i$ vertices are inside the MST\\\\. Now in the transition from stage $i$ to $i + 1$,\\\\ the weight of the added edge $X_i$ = min($Y_1, Y_2, \\ldots, Y_i$)''')
        self.next_slide()
        self.play(Write(text3))
        self.next_slide();
        self.play(FadeOut(text3))
        text4 = Tex(r'''Suppose for a particular vertex $v$\\
$Z_1, Z_2, \ldots Z_{n - i}$ are the weights of the outgoing\\
edges from $v$. Then''')
        self.next_slide()
        self.play(Write(text4))
        # self.wait();
        self.next_slide()
        self.play(FadeOut(text4))
        mt = MathTex(r'''Y_v = \text{min}(Z_1, Z_2, \ldots Z_{n - i})\; | \;\text{Edges induced from v during the construction are smaller than } Z_i ''').scale(0.5)
        self.next_slide()
        self.play(Write(mt))
        # self.wait();
        self.next_slide()
        self.play(FadeOut(mt))
        text5 = Tex(r'''Now, suppose the edge added in the previous stage is $p$.\\
Then, there are no edges induced from $p$\\
in any of the stages, therefore $Y_p$ is equivalent\\
to the minimum of $n - i$ random variables,\\
each of which are uniformly distributed in $[0, 1]$.\\
Therefore, we have ''')
        self.next_slide()
        self.play(Write(text5))
        # self.wait();
        self.next_slide()
        self.play(FadeOut(text5))
        mt1 = MathTex(r'E(Y_p) = \frac{1}{n - i + 1}')
        self.play(Write(mt1))
        # self.wait()
        self.next_slide()
        self.play(FadeOut(mt1))
        mt2 = MathTex(r'E(\text{min}(Y_1, Y_2 \ldots Y_i)) \leq E(Y_p)')
        self.play(Write(mt2));
        mt3 = MathTex(r'E(\text{min}(Y_1, Y_2 \ldots Y_i)) \leq \frac{1}{n - i + 1}')
        self.next_slide()
        self.play(ReplacementTransform(mt2, mt3))
        self.next_slide()
        self.play(FadeOut(mt3))
        mt4 = MathTex(r'''E(W) = \sum_{i = 1}^{n - 1} X_i''')
        self.next_slide()
        self.play(Write(mt4))
        mt5 = MathTex(r'''E(W) = \sum_{i = 1}^{n - 1} \frac{1}{n - i + 1}''')
        self.next_slide()
        self.play(ReplacementTransform(mt4, mt5));
        mt6 = MathTex(r'''E(W) \leq \log_en''')
        self.next_slide()
        self.play(ReplacementTransform(mt5, mt6));
        self.next_slide()
        t7 = Text("This, however is a very loose bound\nWe shall be showing a stronger bound.")
        self.play(mt6.animate.shift(UP), Write(t7))

        self.next_slide()
        self.play(FadeOut(title), FadeOut(mt6), FadeOut(t7))
        self.next_slide()
        title = VGroup(
            Text("Getting Bound on Weight of MST", t2c={"MST": BLUE}),
            Text("of a complete graph", t2c={"to": BLUE}),
            Text("using Kruskal's algorithm", t2c={"Kruskal's algorithm": YELLOW}),
        ).arrange(DOWN)

        self.play(FadeIn(title))
        self.next_slide()

        head_text = Text("Analysis using Kruskal's algorithm", t2c={"Kruskal's algorithm": BLUE}, font_size=32)
        head_text.to_edge(UP, buff=0.35)
        head_line = Line([-6.5, 3, 0], [6.5, 3, 0])
        head = VGroup(head_text, head_line)
        self.play(Transform(title, head))
        self.next_slide()

        text_1 = Tex(r"Let's add all the edges to the graph in the increasing order of their weights", font_size=36)
        text_1.next_to(head, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(text_1))
        self.next_slide()

        # graph
        vertices_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        edges_1 = []
        graph_1 = Graph(vertices_1, edges_1, layout={
            1: [-3, 0, 0], 2: [-2, -2.1, 0], 3: [-1, 1.5, 0], 4: [0, -1.3, 0], 5: [1, -1.9, 0], 6: [2, 1.6, 0], 7: [3, -2.5, 0], 8:[0.5, 0.5, 0], 9:[2.7, 0.3, 0]
        })     
        self.play(Create(graph_1))
        self.next_slide()
        edges1 = [[1, 4, 0], [5, 8, 0], [9, 5, 0], [3, 6, 0], [1, 8, 0], [8, 9, 1], [6, 8, 0], [1, 3, 1], [1, 2, 0], [3, 8, 1], [7, 9, 0]]
        for x, y, c in edges1:
            color = GREEN if c==0 else RED
            e = graph_1._add_edge([x, y], edge_config={"stroke_color": color})
            self.play(Create(e))
            self.next_slide()

        self.play(graph_1.animate.scale(0.7))
        self.play(graph_1.animate.shift(RIGHT * 4))
        self.next_slide()

        text_2 = Tex(r"Since the weights of the edges are distributed\\ randomly and uniformly in the interval [0, 1], \\the expected value of the weight of the \\$i^{th}$ edge in increasing order is", font_size=32)
        text_2.shift(LEFT * 3.2)
        self.play(Write(text_2))
        self.next_slide()
        text_3 = MathTex(r"\mathbb{E}[W_i] = \frac{i}{\binom{n}{2} + 1}")
        text_3.next_to(text_2, DOWN, buff=0.8)
        self.play(Write(text_3))
        self.next_slide()
        text_4 = MathTex(r"\mathbb{E}[W_i] = i \cdot W_f")
        text_4.next_to(text_2, DOWN, buff=0.8)
        self.play(Transform(text_3, text_4))
        self.next_slide()

        self.play(FadeOut(text_3, shift=DOWN))
        self.next_slide()
        self.play(FadeOut(text_2, shift=DOWN))
        self.next_slide()
        self.play(FadeOut(graph_1, shift=DOWN))
        self.next_slide()
        self.play(FadeOut(text_1, shift=DOWN))
        self.next_slide()


        text_5 = Tex(r"Consider the scenario when the number of connected components is $k+1$", font_size=36)
        text_5.next_to(head, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(text_5))
        self.next_slide()              

        vertices_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        edges_2 = [(1, 3), (2, 5), (3, 7), (4, 7), (4, 6), (2, 4), (7, 1), (1, 4), (2, 6), (8, 10),
                   (8, 11), (10, 9), (10, 12), (10, 11), (13, 14), (14, 15), (14, 18), (13, 16),
                   (13, 17), (15, 13), (16, 17), (19, 20), (19, 21)]
        color_2 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0]
        config = {}
        for edge, color in zip(edges_2, color_2):
            config[edge] = {"stroke_color": GREEN if color==0 else RED}

        graph_2 = Graph(vertices_2, edges_2, layout = {
            1: [-5, 0, 0], 2: [-3.5, -2.1, 0], 3: [-4, 1.5, 0], 4: [-3.8, -1.3, 0], 5: [-4.1, -1.9, 0],
            6: [-3.6, 0.1, 0], 7: [-4.2, 0.4, 0], 8:[0.5, 1.8, 0], 9:[2.4, 1.1, 0], 10: [1.5, 0.8, 0],
            11: [0.2, 0.6, 0], 12: [1.7, 2.0, 0], 13: [1.7, -0.7, 0], 14: [1, -2, 0], 15: [0.2, -1.2, 0],
            16: [2, -2.2, 0], 17: [3, -0.7, 0], 18:[-0.5, -2.3, 0], 19:[-1, -0.6, 0], 20: [-1.5, 0, 0], 
            21: [-2, -1, 0], 22: [-1.5, 2.0, 0]
        }, edge_config=config)     
        self.play(Create(graph_2), run_time=8)
        self.next_slide()

        tempedges = [[6, 22, 0], [11, 15, 0], [21, 18, 0], [1, 5, 1], [8, 12, 1]]
        for x, y, c in tempedges:
            color = GREEN if c==0 else RED
            e = graph_2._add_edge([x, y], edge_config={"stroke_color": BLUE})
            self.play(Create(e))
            self.next_slide()
            self.play(ApplyMethod(e.set_color, color))
            self.next_slide()
            self.play(Uncreate(e))
            graph_2._remove_edge((x, y))
            self.next_slide()

        self.play(graph_2.animate.scale(0.5))
        self.play(graph_2.animate.shift(RIGHT * 4.8))

        text_6 = Tex(r"Let $S_{i}$ denote the number of edges \\ which have been added such that there\\ are exactly $i$ components in the graph\\ after the addition of the ${S_i}^{th}$ edge, and $i+1$\\ components before adding the ${S_i}^{th}$ edge.", font_size=36)
        text_6.next_to(text_5, DOWN, aligned_edge=LEFT, buff=0.7)
        self.play(Write(text_6))
        self.next_slide() 

        text_7 = Tex(r"Clearly, $S_n = 0$", font_size=40)
        text_7.next_to(text_6, DOWN, buff=0.3)
        self.play(Write(text_7))
        self.next_slide() 

        text_8 = Tex(r"Also, $u_k = S_k - S_{k+1}$ denotes \\the number of edges we need to add,\\ to reduce the number of components\\ from $k+1$ to $k$", font_size=40)
        text_8.next_to(text_7, DOWN, buff=0.3)
        self.play(Write(text_8))
        self.next_slide()

        self.play(FadeOut(text_8, shift=DOWN), FadeOut(text_7, shift=DOWN), FadeOut(text_6, shift=DOWN))
        # self.play(FadeOut(text_7, shift=DOWN))
        # self.play(FadeOut(text_6, shift=DOWN))

        text_9 = Tex(r"Now, we need to find the expected number of \\edges we need to add to get a green edge $(\mathbb{E}[u_k])$.", font_size=36)
        text_9.next_to(text_5, DOWN, aligned_edge=LEFT, buff=0.7)
        self.play(Write(text_9))
        self.next_slide()

        text_10 = Tex(r"Let's take an arbitrary graph with $n$ vertices and \\$k+1$ connected components. Let $n_i$ be the \\ number of vertices in the $i^{th}$ component.", font_size=32)
        text_10.next_to(text_9, DOWN, buff=0.3)
        self.play(Write(text_10))
        self.next_slide()

        self.play(FadeOut(text_9, shift=LEFT))
        self.play(text_10.animate.shift(UP*1.1))

        text_11 = MathTex(r"\text{Number of remaining edges} = \binom{n}{2} - S_{k+1}", font_size = 28)
        text_11.next_to(text_10, DOWN, buff=0.2)
        self.play(Write(text_11))
        self.next_slide()

        text_12 = MathTex(r"\text{Number of possible green edges} = \sum_{i=1}^{k+1} \sum_{j=i+1}^{k+1} n_i \cdot n_j", font_size = 28)
        text_12.next_to(text_11, DOWN, buff=0.2)
        text_12[0][16:26].set_color(GREEN)
        self.play(Write(text_12))
        self.next_slide()

        text_13= Tex(r"This sum is minimum when one of the\\ component has $n-k$ vertices and all the\\ other components have 1 vertex each", font_size=28)
        text_13.next_to(text_12, DOWN, buff=0.4)
        rect_1 = SurroundingRectangle(text_13, color=BLUE, buff=0.15)
        self.play(Write(text_13), Create(rect_1))
        self.next_slide()

        text_14 = MathTex(r"\text{Number of possible green edges} \geq k \cdot (n-k) + \binom{k}{2}", font_size = 28)
        text_14.next_to(text_11, DOWN, buff=0.2)
        text_14[0][16:26].set_color(GREEN)
        text_14[0][26:39].set_color(BLUE)
        self.play(Transform(text_12, text_14))
        self.next_slide()

        self.play(FadeOut(text_13, shift=DOWN), FadeOut(rect_1, shift=DOWN))
        self.play(FadeOut(text_12, shift=DOWN))
        self.play(FadeOut(text_11, shift=DOWN))
        self.play(FadeOut(text_10, shift=DOWN))

        text_15 = Tex(r"Now, we need to find the upper bound on $\mathbb{E}[u_k]$.", font_size=32)
        text_15.next_to(text_5, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(text_15))
        self.next_slide()

        text_16 = Tex(r"Since, every edge is equally likely to be in any\\ position in the ordering, this problem is equivalent\\ to finding the expected number of red edges\\ which preceed all green edges.", font_size=32)
        text_16[0][111:119].set_color(RED)
        text_16[0][134:144].set_color(GREEN)
        text_16.next_to(text_15, DOWN, buff=0.2)
        self.play(Write(text_16))
        self.next_slide()

        text_17 = MathTex(r"\mathbb{E}[u_k] = \frac{N_r}{N_g+1} + 1")
        text_17.next_to(text_16, DOWN, buff=0.35)
        self.play(Write(text_17))
        self.next_slide()

        text_18 = MathTex(r"\mathbb{E}[u_k] = \frac{N_r+N_g+1}{N_g+1}")
        text_18.next_to(text_16, DOWN, buff=0.35)
        self.play(Transform(text_17, text_18))
        self.next_slide()

        text_19 = MathTex(r"\mathbb{E}[u_k] = \frac{\binom{n}{2} - S_{k+1} + 1}{N_g+1}")
        text_19.next_to(text_16, DOWN, buff=0.35)
        self.play(Transform(text_17, text_19))
        self.next_slide()

        text_20 = MathTex(r"\mathbb{E}[u_k] \leq \frac{\binom{n}{2} - S_{k+1} + 1}{k \cdot (n-k)+\binom{k}{2}+1}")
        text_20.next_to(text_16, DOWN, buff=0.35)
        self.play(Transform(text_17, text_20))
        self.next_slide()

        text_21 = MathTex(r"\mathbb{E}[u_k] \leq \frac{\binom{n}{2} + 1}{k \cdot (n-k)+\binom{k}{2}+1}")
        text_21.next_to(text_16, DOWN, buff=0.35)
        self.play(Transform(text_17, text_21))
        self.next_slide()

        self.play(FadeOut(text_17, shift=DOWN))
        self.play(FadeOut(text_16, shift=DOWN))
        self.play(FadeOut(text_15, shift=DOWN))
        self.play(FadeOut(graph_2, shift=DOWN))
        self.play(FadeOut(text_5, shift=DOWN))

        text_22 = MathTex(r"S_{n-1} = u_{n-1}", font_size=32)
        text_22.next_to(head, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(text_22))
        self.next_slide()

        text_23 = MathTex(r"S_{n-2} = u_{n-1} + u_{n-2}", font_size=32)
        text_23.next_to(text_22, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(text_23))
        self.next_slide()

        text_24 = MathTex(r"S_{n-3} = u_{n-1} + u_{n-2} + u_{n-3}", font_size=32)
        text_24.next_to(text_23, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(text_24))
        self.next_slide()

        dot1 = Dot(point=LEFT*5.6+UP*1, radius=0.04)
        dot2 = Dot(point=LEFT*5.6+UP*0.75, radius=0.04)
        dot3 = Dot(point=LEFT*5.6+UP*0.5, radius=0.04)
        dot4 = Dot(point=LEFT*5.6+UP*0.25, radius=0.04)
        dot5 = Dot(point=LEFT*5.6, radius=0.04)
        self.play(Create(dot1), Create(dot2), Create(dot3), Create(dot4), Create(dot5))
        self.next_slide()

        text_25 = MathTex(r"S_{2} = u_{n-1} + u_{n-2} + u_{n-3} + \cdots \cdots \cdots + u_{3} + u_{2}", font_size=32)
        text_25.next_to(text_24, DOWN, aligned_edge=LEFT+0.2*RIGHT, buff=1.6)
        self.play(Write(text_25))
        self.next_slide()

        text_26 = MathTex(r"S_{1} = u_{n-1} + u_{n-2} + u_{n-3} + \cdots \cdots \cdots + u_{3} + u_{2} + u_{1}", font_size=32)
        text_26.next_to(text_25, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(text_26))
        self.next_slide()

        line = Line([-6.5, -1.2, 0], [3, -1.2, 0], stroke_width=1)
        self.play(Create(line))

        text_27 = MathTex(r"\sum_{i=1}^{n-1} S_i = (n-1) \cdot u_{n-1} + (n-2) \cdot u_{n-2} \cdots \cdots \cdots + 2 \cdot u_{2} + 1 \cdot u_{1}", font_size=32)
        text_27.next_to(text_26, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(text_27))
        self.next_slide()

        text_28 = MathTex(r"\sum_{i=1}^{n-1} S_i = \sum_{i=1}^{n-1} i \cdot u_{i}", font_size=32)
        text_28.next_to(text_26, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Transform(text_27, text_28))
        self.next_slide()

        prev = VGroup(text_22, text_23, text_24, text_25, text_26, text_27, text_28, dot1, dot2, dot3, dot4, dot5, line)

        text_29 = MathTex(r"\sum_{i=1}^{n-1} S_i = \sum_{i=1}^{n-1} i \cdot u_{i}", font_size=34, color=BLUE)
        text_29.next_to(head, DOWN, buff=0.4)
        self.play(Transform(prev, text_29))
        self.next_slide()

        text_30 = MathTex(r"W_f \cdot \sum_{i=1}^{n-1} S_i = W_f \cdot \sum_{i=1}^{n-1} i \cdot u_{i}", font_size=28)
        text_30.next_to(text_29, DOWN, buff=0.2)
        self.play(Write(text_30))
        self.next_slide()

        text_31 = MathTex(r" \sum_{i=1}^{n-1} W_i = W_f \cdot \sum_{i=1}^{n-1} i \cdot u_{i}", font_size=28)
        text_31.next_to(text_30, DOWN, buff=0.2)
        self.play(Write(text_31))
        self.next_slide()

        text_32 = MathTex(r" \mathbb{E} \Bigg[ \sum_{i=1}^{n-1} W_i \Bigg] = \mathbb{E} \Bigg[ W_f \cdot \sum_{i=1}^{n-1} i \cdot u_{i}\Bigg]", font_size=28)
        text_32.next_to(text_31, DOWN, buff=0.2)
        self.play(Write(text_32))
        self.next_slide()

        text_33 = MathTex(r" \mathbb{E} \Bigg[ \sum_{i=1}^{n-1} W_i \Bigg] = W_f \cdot \sum_{i=1}^{n-1} i \cdot \mathbb{E} [u_{i}]", font_size=28)
        text_33.next_to(text_32, DOWN, buff=0.2)
        self.play(Write(text_33))
        self.next_slide()

        self.play(FadeOut(prev, shift=LEFT), FadeOut(text_30, shift=LEFT), FadeOut(text_31, shift=LEFT), FadeOut(text_32, shift=LEFT))
        # self.play(FadeOut(text_30, shift=LEFT))
        # self.play(FadeOut(text_31, shift=LEFT))
        # self.play(FadeOut(text_32, shift=LEFT))
        self.play(text_33.animate.shift(UP*4.5))

        text_34 = MathTex(r" \mathbb{E} \Bigg[ \sum_{i=1}^{n-1} W_i \Bigg] \leq W_f \cdot \sum_{i=1}^{n-1} i \cdot \bigg( \frac{\binom{n}{2} + 1}{i \cdot (n-i) + \binom{i}{2} + 1} \bigg)", font_size=28)
        text_34.next_to(text_33, DOWN, buff=0.2)
        self.play(Write(text_34))
        self.next_slide()

        text_35 = MathTex(r" \mathbb{E} \Bigg[ \sum_{i=1}^{n-1} W_i \Bigg] \leq \sum_{i=1}^{n-1} \frac{i}{i \cdot (n-i) + \binom{i}{2} + 1}", font_size=28)
        text_35.next_to(text_33, DOWN, buff=0.2)
        self.play(Transform(text_34, text_35))
        self.next_slide()

        text_36 = MathTex(r" \lim_{n\to\infty} \mathbb{E} \Bigg[ \sum_{i=1}^{n-1} W_i \Bigg] \leq \lim_{n\to\infty} \sum_{i=1}^{n-1} \frac{i}{i \cdot (n-i) + \binom{i}{2} + 1}", font_size=28)
        text_36.next_to(text_35, DOWN, buff=0.2)
        self.play(Write(text_36))
        self.next_slide()

        text_37 = MathTex(r" \lim_{n\to\infty} \mathbb{E} \Bigg[ \sum_{i=1}^{n-1} W_i \Bigg] \leq \lim_{n\to\infty} \sum_{i=1}^{n-1} \bigg( \frac{\frac{i}{n}}{\frac{i}{n} \cdot \big(1-\frac{i}{n} \big) + \frac{i}{2n} \cdot \big(\frac{i-1}{n}\big) + \frac{1}{n^2}} \bigg) \cdot \frac{1}{n}", font_size=28)
        text_37.next_to(text_36, DOWN, buff=0.2)
        self.play(Write(text_37))
        self.next_slide()

        self.play(FadeOut(text_33, shift=LEFT), FadeOut(text_34, shift=LEFT), FadeOut(text_36, shift=LEFT))
        # self.play(FadeOut(text_34, shift=LEFT))
        # self.play(FadeOut(text_36, shift=LEFT))
        self.play(text_37.animate.shift(UP*3))

        text_38 = MathTex(r" \lim_{n\to\infty} \mathbb{E} \Bigg[ \sum_{i=1}^{n-1} W_i \Bigg] \leq \int_{0}^{1} \frac{x}{x\cdot (1-x) + \frac{x^2}{2}} \, dx", font_size=28)
        text_38.next_to(text_37, DOWN, buff=0.2)
        self.play(Write(text_38))
        self.next_slide()

        text_39 = MathTex(r" \lim_{n\to\infty} \mathbb{E} \Bigg[ \sum_{i=1}^{n-1} W_i \Bigg] \leq \int_{0}^{1} \frac{1}{1-x + \frac{x}{2}} \, dx", font_size=28)
        text_39.next_to(text_38, DOWN, buff=0.2)
        self.play(Write(text_39))
        self.next_slide()

        text_40 = MathTex(r" \lim_{n\to\infty} \mathbb{E} \Bigg[ \sum_{i=1}^{n-1} W_i \Bigg] \leq \int_{0}^{1} \frac{2}{2-x} \, dx", font_size=28)
        text_40.next_to(text_38, DOWN, buff=0.2)
        self.play(Transform(text_39, text_40))
        self.next_slide()

        text_41 = MathTex(r" \lim_{n\to\infty} \mathbb{E} \Bigg[ \sum_{i=1}^{n-1} W_i \Bigg] \leq 2 \cdot ln(2)", font_size=28)
        text_41.next_to(text_39, DOWN, buff=0.5)
        self.play(Write(text_41))
        self.next_slide()

        rect_2 = SurroundingRectangle(text_41, color=BLUE, buff=0.15)
        self.play(Create(rect_2))
        self.next_slide()
        
