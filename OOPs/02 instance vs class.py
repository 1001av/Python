class employee:
    language = "python"
    salary = 1200000

Akhil = employee()
Akhil.language = "Javascript"  # this is an instance attribute
print(Akhil.salary, Akhil.language)

# : Instance attributes, take preference over class attributes during assignment & retrieval.