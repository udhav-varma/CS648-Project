from manim import *

from manim_slides import Slide
class Present(Slide):
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