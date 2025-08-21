"""
# ví dụ
# Khởi tạo stack rỗng
move_stack = []

# Ghi lại các di chuyển
record_move(move_stack, "Đi lên")
record_move(move_stack, "Đi qua phải")
record_move(move_stack, "Đi xuống")

# In ra lịch sử di chuyển hiện tại
print("Lịch sử di chuyển:", move_stack)

# Hoàn tác lại di chuyển gần nhất
last_move = undo_move(move_stack)
print("Di chuyển vừa hoàn tác: ", last_move)

# In ra lịch sử di chuyển mới
print("Lịch sử di chuyển mới: ", move_stack)

lịch sử di chuyển: ['Đi lên', 'Đi qua phải' , 'Đi xuống']
di chuyển vừa hoàn tác: 'Đi xuống'
Lịch sử di chuyển mới: ['ĐI lên', 'Đi qua phải']"""


move_stack = []

def record_move(stack, move):
    stack.append(move)
    print(f"Đã ghi lại di chuyển: {move}")

def undo_move(stack):
    if stack:
        last_move = stack.pop()
        print(f"Đã hoàn tác di chuyển: {last_move}")
    else:
        print("Không có di chuyển nào để hoàn tác")
        return None
    
def main():
    print("Demo tính năng hoàn tác trong game\n")

    print("Ghi lại các di chuyển: ")
    record_move(move_stack, "Đi lên")
    record_move(move_stack, "Đi qua phải")
    record_move(move_stack, "Đi xuống")

    print(f"\n Lịch sử di chuyển hiện tại: {move_stack}")

    print(f"\n Hoàn tác di chuyển gần nhất: ")
    last_move = undo_move(move_stack)
    if last_move:
        print(f"Di chuyển vừa hoàn tác: {last_move}")

    print(f"\n lịch sử di chuyển sau hoàn tác: {move_stack}")

    print(f"\n demo thêm các thao tác")

    record_move(move_stack, "Đi lên trên")
    print(f"lịch sử sau khi thêm: {move_stack}")

    print(f"\n hoàn tác tất cả di chuyển: ")
    while move_stack:
        undo_move(move_stack)
        print(f"lịch sử còn lại: {move_stack}")

    print(f"\n thử hoàn tác khi không còn di chuyển nào: ")
    undo_move(move_stack)

class GameUndoSystem:
    def __init__(self):
        self.move_history = []
        self.max_history = 50

    def record_move(self, move_data):
        if len(self.move_history) >= self.max_history:
            self.move_history.pop(0)

        self.move_history.append({
            'action' : move_data['action'],
            'from_position': move_data.get('from', None),
            'to_position' : move_data.get('to', None),
            'timestamp': move_data.get('timestamp', None)
        })

    def undo_last_move(self):
        if self.move_history:
            return self.move_history.pop()
        return None
    
    def get_history_size(self):
        return len(self.move_history)
    
    def clear_history(self):
        self.move_history.clear()


def demo_undo_system():
    print("\n" + "="*50)
    print("Demo lớp GAMEUNDOSYSTEM")
    print("="*50)

    game = GameUndoSystem()

    moves = [
        {'action': 'move', 'from': (0, 0), 'to': (1, 0)},
        {'action': 'move', 'from': (1, 0), 'to': (2, 0)},
        {'action': 'attack', 'target': 'enemy1'},
        {'action': 'move', 'from': (2, 0), 'to': (2, 1)}
    ]

    for move in moves:
        game.record_move(move)
        print(f"Ghi lại: {move['action']}")

    print(f"\n Số di chuyển trong lịch sử: {game.get_history_size()}")

    print("\nhoàn tác 2 di chuyển gần nhất: ")
    for i in range(2):
        undone = game.undo_last_move()
        if undone:
            print(f"Đã hoàn tác: {undone}")

    print(f"Số di chuyển còn lại: {game.get_history_size()}")

if __name__ == "__main__":
    main()
    demo_undo_system()