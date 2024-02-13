from manim import *

class BubbleSortScene(Scene):
    def construct(self):

        values = [4, 2, 5, 1, 3]
        n = len(values)


        boxes = VGroup(*[Square(side_length=1, color=BLUE).move_to([i - n//2, 0, 0]) for i in range(n)])
        

        max_side_length = max(box.side_length for box in boxes)


        labels = VGroup()
        for i, box in enumerate(boxes):
            label = Text(str(values[i]), font_size=24)
            label.move_to(box)
            labels.add(label)
        

        labels.align_to(boxes, direction=UP)

        indices = VGroup(*[Text(str(i)).move_to([boxes[i].get_center()[0], -2, 0]) for i in range(n)])


        labels.next_to(boxes, direction=UP, buff=0.5)


        self.add(boxes, labels, indices)


        for i in range(n - 1):
            for j in range(0, n - i - 1):

                self.play(ApplyMethod(boxes[j].set_fill, YELLOW),
                          ApplyMethod(boxes[j + 1].set_fill, YELLOW),
                          ApplyMethod(labels[j].set_color, RED),
                          ApplyMethod(labels[j + 1].set_color, RED),
                          ApplyMethod(indices[j].set_color, RED),
                          ApplyMethod(indices[j + 1].set_color, RED))
                self.wait(0.5)


                if values[j] > values[j + 1]:
                    boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
                    labels[j], labels[j + 1] = labels[j + 1], labels[j]
                    values[j], values[j + 1] = values[j + 1], values[j]

                    self.play(Swap(boxes[j], boxes[j + 1]),
                              Swap(labels[j], labels[j + 1]))
                    self.wait(0.5)


                self.play(ApplyMethod(boxes[j].set_fill, BLUE),
                          ApplyMethod(boxes[j + 1].set_fill, BLUE),
                          ApplyMethod(labels[j].set_color, WHITE),
                          ApplyMethod(labels[j + 1].set_color, WHITE),
                          ApplyMethod(indices[j].set_color, WHITE),
                          ApplyMethod(indices[j + 1].set_color, WHITE))

        self.wait(1)


BubbleSortScene().construct()
