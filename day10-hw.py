import csv

def process_attendees(file_path):
    registered_emails = set()
    company_attendees = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) == 3:
                name, company, email = [item.strip() for item in row]

                registered_emails.add(email)

                company_attendees[company] = company_attendees.get(company, 0) + 1

    total_attendees = len(registered_emails)
    print(f"Số đại biểu dự kiến tham dự: {total_attendees}")

    # Danh sách công ty và số lượng đại biểu
    sorted_list = []
    for company, count in company_attendees.items():
        sorted_list.append((count, company))

    sorted_list.sort(reverse=True)

    for count, company in sorted_list:
        print(f"- {company}: {count} đại biểu")


csv_data = """Tên đại biểu 1, công ty A, email@example.com
Tên đại biểu 2, công ty B, email@gmail.com
Tên đại biểu 3, công ty C, email@gmail.com
Tên đại biểu 4, công ty D, email@gmail.com
Tên đại biểu 5, công ty E, email@gmail.com
Tên đại biểu 6, công ty G, email@gmail.com
Tên đại biểu 7, công ty F, email@gmail.com
"""

with open('attendees.csv', 'w', encoding='utf-8') as f:
    f.write(csv_data)

process_attendees('attendees.csv')