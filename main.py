from chain import get_chain

file_name = "./pdf/game-manual.pdf"
chain = get_chain(file_name)

if __name__=="__main__":
    while(True):
        print("MATTGPT :)\n")
        i: str = input("Your query (type exit to exit): ")
        if i.lower()=="exit": break

        res = chain.run(i)

        print(f"\n\nresponse: {res}")

        