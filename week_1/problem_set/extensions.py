x = input("File name: ").lower().strip().split(".")[-1]

if x == "jpg" or x == "jpeg":
    print("image/jpeg")
elif x == "gif":
    print("image/gif")
elif x == "png":
    print("image/png")
elif x == "pdf":
    print("application/pdf")
elif x == "txt":
    print("text/plain")
elif x == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
