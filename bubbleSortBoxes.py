from manim import *

class BubbleSortScene(Scene):
    def construct(self):
        # Define values to be sorted
        values = [4, 2, 5, 1, 3]
        n = len(values)

        # Create boxes to represent elements
        boxes = VGroup(*[Square(side_length=1, color=BLUE).move_to([i - n//2, 0, 0]) for i in range(n)])
        
        # Find the maximum height and width of boxes
        max_side_length = max(box.side_length for box in boxes)

        # Create labels and align them in a straight line above the boxes
        labels = VGroup()
        for i, box in enumerate(boxes):
            label = Text(str(values[i]), font_size=24)
            label.move_to(box)
            labels.add(label)
        
        # Adjust label positions to ensure they are centered within the boxes
        labels.align_to(boxes, direction=UP)

        indices = VGroup(*[Text(str(i)).move_to([boxes[i].get_center()[0], -2, 0]) for i in range(n)])

        # Position labels near the top of the screen, aligned with the indices
        labels.next_to(boxes, direction=UP, buff=0.5)

        # Add boxes, labels, and indices to the scene
        self.add(boxes, labels, indices)

        # Run the bubble sort algorithm
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                # Highlight the elements being compared
                self.play(ApplyMethod(boxes[j].set_fill, YELLOW),
                          ApplyMethod(boxes[j + 1].set_fill, YELLOW),
                          ApplyMethod(labels[j].set_color, RED),
                          ApplyMethod(labels[j + 1].set_color, RED),
                          ApplyMethod(indices[j].set_color, RED),
                          ApplyMethod(indices[j + 1].set_color, RED))
                self.wait(0.5)

                # If the current element is greater than the next one, swap them
                if values[j] > values[j + 1]:
                    boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
                    labels[j], labels[j + 1] = labels[j + 1], labels[j]
                    values[j], values[j + 1] = values[j + 1], values[j]
                    # Update positions of boxes and labels together
                    self.play(Swap(boxes[j], boxes[j + 1]),
                              Swap(labels[j], labels[j + 1]))
                    self.wait(0.5)

                # Remove highlight from elements
                self.play(ApplyMethod(boxes[j].set_fill, BLUE),
                          ApplyMethod(boxes[j + 1].set_fill, BLUE),
                          ApplyMethod(labels[j].set_color, WHITE),
                          ApplyMethod(labels[j + 1].set_color, WHITE),
                          ApplyMethod(indices[j].set_color, WHITE),
                          ApplyMethod(indices[j + 1].set_color, WHITE))

        self.wait(1)

# Create the scene
BubbleSortScene().construct()
