def main():
    farm_tasks = []

    while True:
        print("\n--- ระบบจัดการงานในฟาร์ม ---")
        print("1. เพิ่มงานในฟาร์ม")
        print("2. แสดงรายการงานทั้งหมด")
        print("3. ลบงาน")
        print("4. สรุปงานในแต่ละประเภท")
        print("5. ออกจากโปรแกรม")

        choice = input("กรุณาเลือกเมนู (1-5): ")

        if choice == "1":
            add_task(farm_tasks)
        elif choice == "2":
            show_tasks(farm_tasks)
        elif choice == "3":
            delete_task(farm_tasks)
        elif choice == "4":
            summarize_tasks(farm_tasks)
        elif choice == "5":
            print("ออกจากโปรแกรมแล้ว ขอบคุณที่ใช้บริการ")
            break
        else:
            print("กรุณาเลือกเมนูให้ถูกต้อง (1-5)")

def add_task(tasks):
    name = input("Samrt Farm Task Organizer: ")
    task_type = input("ประเภทของงาน (เช่น ให้อาหาร, รดน้ำ, เก็บเกี่ยว): ")
    tasks.append({'name': name, 'type': task_type})
    print("เพิ่มงานเรียบร้อยแล้ว")

def show_tasks(tasks):
    if not tasks:
        print("ยังไม่มีงานในระบบ")
    else:
        print("\nรายการงานทั้งหมด:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['name']} (ประเภท: {task['type']})")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            index = int(input("กรุณาระบุหมายเลขงานที่ต้องการลบ: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"ลบงาน '{removed['name']}' เรียบร้อยแล้ว")
            else:
                print("หมายเลขไม่ถูกต้อง")
        except ValueError:
            print("กรุณาใส่ตัวเลขเท่านั้น")

def summarize_tasks(tasks):
    summary = {}
    for task in tasks:
        summary[task['type']] = summary.get(task['type'], 0) + 1

    if not summary:
        print("ยังไม่มีงานในระบบ")
    else:
        print("\nสรุปจำนวนงานในแต่ละประเภท:")
        for task_type, count in summary.items():
            print(f"- {task_type}: {count} งาน")

if __name__ == "__main__":
    main()