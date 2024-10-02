import tkinter as tk
from tkinter import messagebox


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
       
class CircularLinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head


    def eliminate_player(self, k):
        if not self.head:
            return


        current = self.head
        while current.next != current:
            for _ in range(k - 1):
                previous_node = current
                current = current.next
            next_player = current.next
            yield current.data
            if current == self.head:
                self.head = next_player
            previous_node.next = next_player  # Remove current player from the list
            current = next_player


        yield current.data
        self.head = None  # Clear the head since there's only one player left


class GameGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Elimination Game")
        self.canvas = tk.Canvas(self.window, width=700, height=350)
        self.canvas.pack()


        self.label_n = tk.Label(self.window, text="Enter value of N (1 < N < 12):")
        self.label_n.pack()
        self.entry_n = tk.Entry(self.window)
        self.entry_n.pack()


        self.label_k = tk.Label(self.window, text="Enter value of K (K >= 1):")
        self.label_k.pack()
        self.entry_k = tk.Entry(self.window)
        self.entry_k.pack()


        self.text_box = tk.Text(self.window, height=10, width=50)
        self.text_box.pack()


        self.start_button = tk.Button(self.window, text="Start", command=self.start_game)
        self.start_button.pack()


        self.eliminate_button = tk.Button(self.window, text="Eliminate", command=self.eliminate_player)
        self.eliminate_button.pack()
        self.eliminate_button.config(state=tk.DISABLED)


        self.players = CircularLinkedList()
        self.player_icons = []
        self.elimination_generator = None


    def display_text(self, text):
        self.text_box.insert(tk.END, text + "\n")
        self.text_box.see(tk.END)


    def clear_text(self):
        self.text_box.delete(1.0, tk.END)


    def validate_input(self, n, k):
        if not (1 < n < 12):
            messagebox.showinfo("Invalid Input", "N should be between 1 and 11.")
            return False
        elif k < 1:
            messagebox.showinfo("Invalid Input", "K should be greater than or equal to 1.")
            return False
        else:
            return True


    def start_game(self):
        n = int(self.entry_n.get())
        k = int(self.entry_k.get())
        if self.validate_input(n, k):
            self.clear_text()
            self.players = CircularLinkedList()
            for i in range(n):
                self.players.append("Player " + str(i))
                self.player_icons.append(self.canvas.create_text(60 * i, 150, text=str(i)))


            self.display_text(f"Game started. N={n} K={k}")
            self.eliminate_button.config(state=tk.NORMAL)
            self.elimination_generator = self.players.eliminate_player(k)


    def eliminate_player(self):
        if len(self.player_icons) == 1:  # If there's only one player left
            winner = self.players.head.data
            messagebox.showinfo("Game Over", f"The winner is {winner}!")
            self.clear_text()
            self.canvas.delete("all")
            self.eliminate_button.config(state=tk.DISABLED)
            self.elimination_generator = None  # Reset the generator for the next game
            return


        if self.elimination_generator is None:
            return  # No active game


        try:
            eliminated_player = next(self.elimination_generator)
            self.display_text("Eliminated player: " + str(eliminated_player))
            self.canvas.delete(self.player_icons.pop(0))
        except StopIteration:
            pass


    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = GameGUI()
    game.run()

