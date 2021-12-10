from flask import Flask, request

app = Flask("myFirstAPI")


@app.route("/compute/<n>", methods=["GET","POST"])
def compute(n):
    if request.method == "GET":
        try:
            n = int(n)
            s = getSum(n)
            response = {
                "data": s
            }
            return response, 200
        except Exception as e:
            response = {
                "error": f"Failed to compute. {e}"
            }
            return response, 500
    if request.method == "POST":
        body = request.json
        if body["mode"] == "sum":
            try:
                n = int(n)
                s = getSum(n)
                response = {
                    "data": s
                }
                return response, 200
            except Exception as e:
                response = {
                    "error": f"Failed to compute. {e}"
                }
                return response, 500
        if body["mode"] == "product":
            try:
                n = int(n)
                p = getProduct(n)
                response = {
                    "data": p
                }
                return response, 200
            except Exception as e:
                response = {
                    "error": f"Failed to compute. {e}"
                }
                return response, 500


def getSum(n):
    s = 0 
    for i in range(n+1):
        s += i
    return s


def getProduct(n):
    p = 1 
    for i in range(1, n+1):
        p = p * i
    return p


if __name__ == "__main__":
    print(f"INFO: Fisierul: {__name__}")
    s = getSum(10)
    print(f"INFO: Suma numerelor pana la 10: {s}")

    app.run(port=5688, debug=False)
    # while True:
    #     option = input("Ce vrei sa rulezi? ")
    #     if option == "sum":
    #         nInput = input("Introdu un numar: ")
    #         nInput = int(nInput)
    #         s = getSum(nInput)
    #         print(f"INFO: Suma numerelor pana la {nInput}: {s}")
    #     elif option == "product":
    #         nInput = input("Introdu un numar: ")
    #         nInput = int(nInput)
    #         p = getProduct(nInput)
    #         print(f"INFO: Produsul numerelor pana la {nInput}: {p}")
    #     else:
    #         print("ERROR: Nu am putut sa calculez. Incearca din nou folosing 'product' sau 'sum'")
    
