from manim import *

class BubbleSortScene(Scene):
    def construct(self):

        values = [4, 2, 5, 1, 3]
        n = len(values)


        bars = VGroup(*[Rectangle(width=0.5, height=value/2, color=BLUE).move_to([i - n//2, 0, 0]) for i, value in enumerate(values)])
        

        max_height = max(bar.height for bar in bars)
        max_width = max(bar.width for bar in bars)


        labels = VGroup()
        for i, bar in enumerate(bars):
            label = Text(str(values[i]), font_size=24)
            label.next_to(bar.get_top(), direction=UP, buff=0)
            labels.add(label)
        

        labels.arrange_submobjects(buff=max_width * 1.7)

        indices = VGroup(*[Text(str(i)).move_to([bars[i].get_center()[0], -2, 0]) for i in range(n)])


        labels.next_to(bars, direction=UP, buff=0.5)


        self.add(bars, labels, indices)


        for i in range(n - 1):
            for j in range(0, n - i - 1):

                self.play(ApplyMethod(bars[j].set_fill, YELLOW),
                          ApplyMethod(bars[j + 1].set_fill, YELLOW),
                          ApplyMethod(labels[j].set_color, RED),
                          ApplyMethod(labels[j + 1].set_color, RED),
                          ApplyMethod(indices[j].set_color, RED),
                          ApplyMethod(indices[j + 1].set_color, RED))
                self.wait(0.5)


                if values[j] > values[j + 1]:
                    bars[j], bars[j + 1] = bars[j + 1], bars[j]
                    labels[j], labels[j + 1] = labels[j + 1], labels[j]
                    values[j], values[j + 1] = values[j + 1], values[j]

                    self.play(Swap(bars[j], bars[j + 1]),
                              Swap(labels[j], labels[j + 1]))
                    self.wait(0.5)


                self.play(ApplyMethod(bars[j].set_fill, BLUE),
                          ApplyMethod(bars[j + 1].set_fill, BLUE),
                          ApplyMethod(labels[j].set_color, WHITE),
                          ApplyMethod(labels[j + 1].set_color, WHITE),
                          ApplyMethod(indices[j].set_color, WHITE),
                          ApplyMethod(indices[j + 1].set_color, WHITE))

        self.wait(1)


BubbleSortScene().construct()
