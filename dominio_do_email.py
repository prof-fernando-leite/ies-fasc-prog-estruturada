
def encontra_dominio(email) -> str:
    dominio = email.split('@')[1]
    return dominio

email = input("Email: ")
print(f"O domínio do seu e-mail é {encontra_dominio(email)}")