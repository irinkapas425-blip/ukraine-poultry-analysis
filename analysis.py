import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(
    "animals_ukraine.xls",
    sheet_name="К-сть сг тварин за кат госп"
)

df = df.iloc[1:].copy()
cols = ["all agricultural holdings 1",
    "all agricultural holdings 2",
    "all agricultural holdings 3"]
df["attributes"] = df["attributes"].str.strip()

for col in cols:
    df[col] = pd.to_numeric(df[col], errors = "coerce") 

    #print(repr(val))

birds = df[df["attributes"].str.contains("Птиця", na=False)]    
birds_sorted = birds.sort_values("all agricultural holdings 1")
#print(birds_sorted)
#print("\nСереднє поголів'я птиці:")
#print(birds["all agricultural holdings 1"].mean())
#print("\nМаксимальное значение:")
#print(birds["all agricultural holdings 1"].max())
#print("\nМинимальное значение:")
#print(birds["all agricultural holdings 1"].min())
birds = birds[birds["period"] != 2022]
pigs = df[df["attributes"].str.contains("Свині", case = False, na = False)]
#pigs_sorted = pigs.sort_values("all agricultural holdings 1")
#print(pigs_sorted)
#print("\nСереднє поголів'я свині:")
#print(pigs["all agricultural holdings 1"].mean())
#print("\nМаксимальне поголів'я свині:")
#print(pigs["all agricultural holdings 1"].max())
#print("\nМінімальне поголів'я свині:")
#print(pigs["all agricultural holdings 1"].min())

cattle = df[df["attributes"].str.contains("Велика рогата худоба",case=False, na=False)]
#cattle_sorted = cattle.sort_values("all agricultural holdings 1")
#print(cattle_sorted)
#print("\nСереднє поголів'я ВРХ:")
#print(cattle["all agricultural holdings 1"].mean())
#print("\nМаксимальне поголів'я ВРХ:")
#print(cattle["all agricultural holdings 1"].max())
#print("\nМінімальне поголів'я ВРХ:")
#print(cattle["all agricultural holdings 1"].min())

xl = pd.ExcelFile("animals_ukraine.xls")
#print(xl.sheet_names)

#print(df.columns.tolist())
#print(df.head(20))
#print(cattle)
#print(pigs)
#print(df["attributes"]. unique())
#print(birds)
#print(df.head)
#print()
#print(df.types)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

ax1.bar(birds["period"], birds["all agricultural holdings 1"], color="blue")
ax1.set_title("Птиці")
ax1.set_xlabel("Рік")   # підпис осі X
ax1.set_ylabel("Кількість (тис. голів)")

ax2.bar(pigs["period"], pigs["all agricultural holdings 1"], color="red")
ax2.set_title("Свині")
ax2.set_xlabel("Рік")   # підпис осі X
ax2.set_ylabel("Кількість (тис. голів)")

ax3.bar(cattle["period"], cattle["all agricultural holdings 1"], color="green")
ax3.set_title("ВРХ")
ax3.set_xlabel("Рік")   # підпис осі X
ax3.set_ylabel("Кількість (тис. голів)")


plt.tight_layout()
plt.savefig("animals.png")
plt.savefig("animals.png")
print("Зберігаю графік")
plt.savefig("animals.png")
print("Збережено")
plt.show()

