failed_logins = {}

with open("sample-log.txt", "r") as file:
    for line in file:
        if "LOGIN FAILED" in line:
            user = line.split("user=")[1].split()[0]
            ip = line.split("ip=")[1].strip()

            key = (user, ip)
            failed_logins[key] = failed_logins.get(key, 0) + 1

print("Tentativas de login com falha:")
for (user, ip), count in failed_logins.items():
    print(f"Usuário: {user} | IP: {ip} | Falhas: {count}")

    if count >= 3:
        print("⚠️ Risco elevado: possível força bruta\n")
