from collections import deque
import time
from datetime import datetime


print_queue = deque()

def enqueue_print_job(queue, job):
    queue.append(job)
    print(f"Đã thêm tác vụ in: '{job['name']}' vào hàng đợi")
    print(f"Số trang: {job['pages']}, Độ ưu tiên: {job['priority']}")


def dequeue_print_job(queue):
    if queue:
        job = queue.popleft()
        print(f"Đang in: '{job['name']}'")
        print(f"Số trang: {job['pages']}, Người gửi: {job['user']}")
        return job
    else:
        print("Hàng đợi trống! Không có tác vụ in nào.")
        return None
    
def main():
    print("Hệ thống hàng đợi in ấn\n")

    print("Thêm các tác vụ in vào hàng đợi:")
    print("-" * 40)

    jobs = [
        {
            'name': 'Báo cáo tài chính Q3',
            'pages': 15,
            'user': 'Nguyễn Văn A',
            'priority': 'cao',
            'time_added': datetime.now().strftime("%H:%M:%S")
        },
        {
            'name': 'Hợp đồng lao động',
            'pages': 8,
            'user': 'Trần Thị B',
            'priority': 'trung bình',
            'time_added': datetime.now().strftime("%H:%M:%S")
        },
        {
            'name': 'Thư mời họp',
            'pages': 2,
            'user': 'Lê Văn C',
            'priority': 'thấp',
            'time_added': datetime.now().strftime("%H:%M:%S")
        },
        {
            'name': 'Bảng lương tháng 10',
            'pages': 25,
            'user': 'Phạm Thị D',
            'priority': 'cao',
            'time_added': datetime.now().strftime("%H:%M:%S")
        }
    ]

    for job in jobs:
        enqueue_print_job(print_queue, job)
        time.sleep(0.5)

    print(f"\n Số tác vụ trong hàng đợi: {len(print_queue)}")
    print("Dang sách tác vụ đang chờ:")
    for i, job in enumerate(print_queue, 1):
        print(f"{i}. {job['name']} ({job['pages']} trang) - {job['user']}")

    print("\n" + "="*50)
    print("BẮT ĐẦU QUÁ TRÌNH IN")
    print("="*50)

    job_count = 1
    while print_queue:
        print(f"\n--- Tác vụ #{job_count} ---")
        current_job = dequeue_print_job(print_queue)

        if current_job:
            print(f"Ước tính thời gian in: {current_job['pages']} giây")
            print("Đang in", end="")

            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.8)

            print(f"Hoàn thành in '{current_job['name']}'!")
            print(f"Phần còn lại {len(print_queue)} tác vụ trong hàng đợi")
        
        job_count += 1
        time.sleep(0.5)

        print(f"\n Đã hoàn thành tất cả các tác vụ in !")

class PrinterManager:
    def __init__(self, printer_name = "HP LaserJet Pro"):
        self.printer_name = printer_name
        self.print_queue = deque()
        self.completed_jobs = []
        self.is_printing = False

    def add_print_job(self, document_name, pages, user, priority="normal"):
        job = {
            'id': len(self.completed_jobs) + len(self.print_queue) + 1,
            'name': document_name,
            'pages': pages,
            'user': user,
            'priority': priority,
            'added_time': datetime.now(),
            'status': 'waiting'
        }

        if priority == "urgent" and self.print_queue:
            temp_queue = deque()
            inserted = False

            while self.print_queue:
                current = self.print_queue.popleft()
                if current['priority'] != "urgent" and not inserted:
                    temp_queue.append(job)
                    inserted = True
                temp_queue.append(current)

            if not inserted:
                temp_queue.append(job)

            self.print_queue = temp_queue
        else:
            self.print_queue.append(job)

        print(f"Đã thêm '{document_name}' vào hàng đợi in")
        return job['id']
    
    def process_next_job(self):
        if not self.print_queue:
            print("Hàng đợi trống!")
            return None
        
        if self.is_printing:
            print("Máy in đang bận!")
            return None
        
        job = self.print_queue.popleft()
        self.is_printing = True
        job['status'] = 'printing'
        job['start_time'] = datetime.now()
        
        print(f"Bắt đầu in: {job['name']}")

        time.sleep(min(job['pages'] * 0.1, 2))

        job['status'] = 'completed'
        job['end_time'] = datetime.now()
        self.completed_jobs.append(job)
        self.is_printing = False

        print(f"Hoàn thành in: {job['name']}")
        return job
    
    def get_queue_status(self):
        print(f"\n trạng thái máy in: {self.printer_name}")
        print("-" * 40)
        print(f"Đang in: {'Có' if self.is_printing else 'Không'}")
        print(f"Tác vụ đang chờ: {len(self.print_queue)}")
        print(f"Tác vụ hoàn thành: {len(self.completed_jobs)}")

        if self.print_queue:
            print(f"\n Danh sách chờ: ")
            for i, job in enumerate(self.print_queue, 1):
                print(f" {i}. {job['name']} - {job['user']} ({job['priority']})")

    def cancel_job(self, job_id):
        temp_queue = deque()
        cancelled = False

        while self.print_queue:
            job = self.print_queue.popleft()
            if job['id'] == job_id:
                print(f"Đã hủy tác vụ: {job['name']}")
                cancelled = True
            else:
                temp_queue.append(job)

        self.print_queue = temp_queue
        return cancelled
    
def demo_printer_manager():
    print("\n" + "=" * 60)
    print("DEMO HỆ THỐNG PRINTERMANAGER NÂNG CAO")
    print("="*60)

    printer = PrinterManager("Canon PIXMA G3010")

    printer.add_print_job("CV Xin việc", 3, "Sinh viên A", "normal")
    printer.add_print_job("Báo cáo khẩn", 20, "Quản lý B", "urgent")
    printer.add_print_job("Hóa đơn", 1, "Kế toán C", "normal")
    printer.add_print_job("Hợp đồng gấp", 5, "Pháp chế D", "urgent")

    printer.get_queue_status()

    print(f"\n Xử lý tác vụ:")
    for i in range(3):
        printer.process_next_job()
        time.sleep(0.5)

    printer.get_queue_status()

if __name__ == "__main__":
    main()
    demo_printer_manager()