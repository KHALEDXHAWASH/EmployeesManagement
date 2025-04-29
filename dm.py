def boxString(title):
    print("-" * (len(title) + 4))
    print(f"| {title} |")
    print("-" * (len(title) + 4))


def get_sales_distribution(sales_list):
    total=sum(sales_list)
    average=total/len(sales_list)
    above = sum(1 for sale in sales_list
                if sale > average)
    below = sum(1 for sale in sales_list
                if sale < average)
    return above,below


def classify_rating(rating):
    if (10>rating>=8):
        return "Excellent"
    elif (rating>=5):
        return "Good"
    else:
        return "Needs Improvement"


def main():
    try:
        with open("performance","r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error:'performance'not found.")
        return

    employees=[]
    total_sales=0

    for line in lines:
        parts=line.strip().split(",")
        if len(parts) !=3:
            continue
        name,sales,rating=parts[0],int(parts[1]),int(parts[2])
        employees.append({"name":name,"sales":sales,"rating":rating})
        total_sales+=sales

    avg_sales=total_sales/len(employees)
    sales_only=[e["sales"] for e in employees]

    top_performer = max(employees,key=lambda e: e["sales"])
    lowest_performer = min(employees,key=lambda e: e["rating"])

    boxString("Employee Performance Report")
    print(f"{'Emp No.':<8} {'Name':<10} {'Sales':<12} {'Rating':<6}")
    print("-" * 40)

    for idx,i in enumerate(employees,start=1):
        note =""
        if i==top_performer:
            note = "<=== Top Performer"
        elif i==lowest_performer:
            note = "<=== Lowest Performer"
        print(f"{idx:<8} {i['name']:<10} ${i['sales']:<11,} {i['rating']:<6} {note}")

    print("-" * 40)
    print(f"Total Sales: ${total_sales:,}")
    print(f"\nAverage Sales per Employee: ${avg_sales:,.2f}")

    above, below = get_sales_distribution(sales_only)
    print(f"Employees above average sales: {above}")
    print(f"Employees below average sales: {below}")

    ratings={"Excellent": 0, "Good": 0, "Needs Improvement": 0}
    for i in employees:
        category=classify_rating(i["rating"])
        ratings[category] += 1

    print("\nRating Categories:")
    for cat in ratings:
        print(f"{cat}: {ratings[cat]} employees")


if __name__ =="__main__":
    main()
